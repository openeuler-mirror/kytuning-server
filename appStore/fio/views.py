import json
from itertools import groupby

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.fio.models import Fio
from appStore.fio.serializers import FioSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils import constants
from appStore.utils.customer_view import CusModelViewSet


class FioViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Fio.objects.all().order_by('id')
    serializer_class = FioSerializer

    def get_unit(self, data):
        # value是值，unit是单位
        unit = data.split("".join(filter(lambda s: s in '0123456789.', data)))[-1]
        if unit:
            value = data.split(unit)[0]
        else:
            value = data
        return value, unit

    def get_bw_unit(self,data):
        unit1 = data.split('(')[0].split(
            "".join(filter(lambda s: s in '0123456789.', data.split('(')[0])))[-1]
        # 这里是kB/s)，后面就不需要再次拼接了
        unit2 = data.split('(')[-1].split(
            "".join(filter(lambda s: s in '0123456789.', data.split('(')[-1])))[-1]
        value1 = float(data.split('(')[0].split(unit1)[0])
        value2 = float(data.split('(')[1].split(unit2)[0])
        return value1, value2, unit1, unit2

    def get_data(self, serializer_):
        serializer = self.get_serializer(serializer_, many=True)
        datas = []
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            for data in serializer.data:
                data = {'rw': data['rw'] + '(' + str(data['bs'] + ')'),
                        'bs': data['bs'],
                        'io': data['io'],
                        'iops': data['iops'],
                        'bw': data['bw'], }
                datas.append(data)
        else:
            # 当有多条数据时计算平均值
            # 判断bs的大小，方便按照bs的大小分组
            bs_size = set([d['bs'] for d in serializer.data])
            rw_types = set([d['rw'] for d in serializer.data])
            new_datas = []
            for test_type in bs_size:
                for rw_type in rw_types:
                    data_ = serializer_.filter(bs=test_type).filter(rw=rw_type)
                    if data_:
                        new_datas.append(data_)
            # new_datas是12组数据
            for data_ in new_datas:
                bs_list = [d.bs for d in data_]
                io_list = [d.io for d in data_]
                iops_list = [d.iops for d in data_]
                bw_list = [d.bw for d in data_]
                # 获取bs、io、iops的平均值

                bs = 0
                for bs_ in bs_list:
                    value, bs_unit = self.get_unit(bs_)
                    bs += float(value)
                bs = bs / len(bs_list)
                io = 0
                for io_ in io_list:
                    value, io_unit = self.get_unit(io_)
                    io += float(value)
                io = io / len(io_list)
                iops = 0
                for iops_ in iops_list:
                    value, iops_unit = self.get_unit(iops_)
                    iops += float(value)
                iops = iops / len(iops_list)
                # 获取bw的平均值
                value1 = 0
                value2 = 0
                for bw_ in bw_list:
                    value1_, value2_, bw_unit1, bw_unit2 = self.get_bw_unit(bw_)
                    value1 += float(value1_)
                    value2 += float(value2_)
                value1 = value1 / len(bw_list)
                value2 = value2 / len(bw_list)
                bw = str(value1) + bw_unit1 + '(' + str(value2) +bw_unit2

                data = {'rw': data_[0].rw + '(' + str(data_[0].bs + ')'),
                        'bs': str(bs) + bs_unit,
                        'io': str(io) + io_unit,
                        'iops': str(iops) + iops_unit,
                        'bw': bw, }
                datas.append(data)
        return datas

    def do_base_data(self, datas):
        new_data = []
        for value in datas:
            data = [{'column1': value['rw'], 'column2': 'bs', 'column3': value['bs']},
                    {'column1': value['rw'], 'column2': 'io', 'column3': value['io']},
                    {'column1': value['rw'], 'column2': 'iops', 'column3': value['iops']},
                    {'column1': value['rw'], 'column2': 'bw', 'column3': value['bw']}]
            new_data.extend(data)
        return new_data

    def list(self, request, *args, **kwargs):
        """
        返回列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        env_id = request.GET.get('env_id')
        comparsionIds = request.GET.get('comparsionIds')
        comparsionIds = comparsionIds.split(',')
        base_queryset = Fio.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        base_datas = self.get_data(base_queryset)
        datas = self.do_base_data(base_datas)
        others = [{'column1': 'Fio', 'column2': '', 'column3': 'Fio#1 (基准数据)'},
                  {'column1': '执行命令', 'column2': '', 'column3': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Fio.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_queryset)
                others[0]['column' + str(new_index)] = 'Fio#'+str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_serializer.data[0]['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_serializer.data[0]['modify_parameters']

                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                for value in comparsion_datas:
                    # 判断comparsion_datas数据中的rw字段和datas中的rw（column）字段相同，则在datas中增加值
                    for index2, data_ in enumerate(datas):
                        if data_['column1'] == value['rw']:
                            # 在datas中增加对比数据
                            datas[index2]['column' + str(new_index)] = value['bs']
                            datas[index2 + 1]['column' + str(new_index)] = value['io']
                            datas[index2 + 2]['column' + str(new_index)] = value['iops']
                            datas[index2 + 3]['column' + str(new_index)] = value['bw']
                            # 在datas中增加计算数据
                            value0 = float(
                                "".join(filter(lambda s: s in '0123456789.', datas[index2]['column' + str(new_index)])))
                            value0_colum3 = float("".join(filter(lambda s: s in '0123456789.', datas[index2]['column3'])))
                            value1 = float(
                                "".join(filter(lambda s: s in '0123456789.', datas[index2 + 1]['column' + str(new_index)])))
                            value1_colum3 = float("".join(filter(lambda s: s in '0123456789.', datas[index2 + 1]['column3'])))
                            value2 = float(
                                "".join(filter(lambda s: s in '0123456789.', datas[index2 + 2]['column' + str(new_index)])))
                            value2_colum3 = float("".join(filter(lambda s: s in '0123456789.', datas[index2 + 2]['column3'])))
                            value3 = float("".join(filter(lambda s: s in '0123456789.',
                                                        datas[index2 + 3]['column' + str(new_index)].split(' ')[-1])))
                            value3_colum3 = float("".join(
                                filter(lambda s: s in '0123456789.', datas[index2 + 3]['column3'].split(' ')[-1])))
                            # bs数据
                            datas[index2]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value0 - value0_colum3) / value0_colum3 )
                            # io数据
                            datas[index2 + 1]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value1 - value1_colum3) / value1_colum3 )
                            # iops数据
                            datas[index2 + 2]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value2 - value2_colum3) / value2_colum3)
                            # bw数据
                            datas[index2 + 3]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value3 - value3_colum3) / value3_colum3)
                            break
        unixbench_data = {'others': others, 'data': datas}
        return json_response(unixbench_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_fio_errors = []
        error_message = []
        for k, fio_json in request.__dict__['data_fio'].items():
            data_fio = {}
            if k.lower().startswith('fio'):
                constants.FIO_BOOL = True
                data_fio['env_id'] = request.__dict__['data_fio']['env_id']
                data_fio['execute_cmd'] = 'xx'
                data_fio['modify_parameters'] = 'xx'
                data_fio['mark_name'] = k[-3:]
                data_fio['rw'] = fio_json['rw']
                data_fio['bs'] = fio_json['items']['bs']
                data_fio['io'] = fio_json['items']['io']
                data_fio['iops'] = fio_json['items']['iops']
                data_fio['bw'] = fio_json['items']['bw']
                data_fio['test_time'] = return_time(fio_json['time'])
                data_fio = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                               data_fio.items()}
                serializer_fio = FioSerializer(data=data_fio)
                if serializer_fio.is_valid():
                    self.perform_create(serializer_fio)
                    continue
                return json_response(serializer_fio.errors, status.HTTP_400_BAD_REQUEST,
                                     get_error_message(serializer_fio))
        if serializer_fio_errors:
            print(serializer_fio_errors, "fio")
            return json_response(serializer_fio_errors, status.HTTP_400_BAD_REQUEST, error_message)
        else:
            return
