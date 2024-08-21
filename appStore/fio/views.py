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
    fio数据管理
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

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        temp_datas = []
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            # 基准数据和对比数据的全部数据
            for data in serializer.data:
                data = {'rw': data['rw'] + '(' + str(data['bs'] + ')'),
                        'bs': data['bs'],
                        'io': data['io'],
                        'iops': data['iops'],
                        'bw': data['bw'], }
                temp_datas.append(data)
            # 先增加头部的内容
            datas[0]['column' + str(column_index)] = 'Fio#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            # 增加数据部分
            # 先初始化所有数据为空
            # todo 后期查看之前代码是如何实现的
            for i in range(3,len(datas)):
                datas[i]['column' + str(column_index)] = None
            for value in temp_datas:
                # 判断comparsion_datas数据中的rw字段和datas中的rw（column）字段相同，则在datas中增加值
                for index, data_ in enumerate(datas):
                    if data_['column1'] == value['rw']:
                        # 在datas中增加对比数据
                        datas[index]['column' + str(column_index)] = value['bs']
                        datas[index + 1]['column' + str(column_index)] = value['io']
                        datas[index + 2]['column' + str(column_index)] = value['iops']
                        datas[index + 3]['column' + str(column_index)] = value['bw']
                        break
            column_index += 1
            title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for index,data in enumerate(datas):
                if index > 2:
                    datas[index]['column' + str(column_index)] = datas[index]['column' + str(column_index - 1)]
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                # 获取到最后一组数据、处理数据
                for i in range(len(datas)):
                    if i > 2:
                        value  = datas[i]['column' + str(column_index-1)]           # 最后一组数据
                        base_value = datas[i]['column' + str(base_column_index)]    # base数据
                        if value is not None and base_value is not None:
                            value = float("".join(filter(lambda s: s in '0123456789.', value.split('(')[0])))
                            base_value = float("".join(filter(lambda s: s in '0123456789.', base_value.split('(')[0])))
                            datas[i]['column' + str(column_index)] = "%.2f%%" % ((value - base_value) /base_value * 100) if value is not None and base_value is not None else None
                        else:
                            datas[i]['column' + str(column_index)] = None
                column_index += 1
        else:
            # 计算平均值
            # 判断bs的大小，方便按照bs的大小分组
            bs_size = set([d['bs'] for d in serializer.data])
            rw_types = set([d['rw'] for d in serializer.data])
            new_datas = []
            average_datas = []
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
                bs = "%.2f" % (bs / len(bs_list))
                io = 0
                for io_ in io_list:
                    value, io_unit = self.get_unit(io_)
                    io += float(value)
                io = "%.2f" % (io / len(io_list))
                iops = 0
                for iops_ in iops_list:
                    value, iops_unit = self.get_unit(iops_)
                    iops += float(value)
                iops = "%.2f" % (iops / len(iops_list))
                # 获取bw的平均值
                value1 = 0
                value2 = 0
                for bw_ in bw_list:
                    value1_, value2_, bw_unit1, bw_unit2 = self.get_bw_unit(bw_)
                    value1 += float(value1_)
                    value2 += float(value2_)
                value1 = "%.2f" % (value1 / len(bw_list))
                value2 = "%.2f" % (value2 / len(bw_list))
                bw = str(value1) + bw_unit1 + '(' + str(value2) +bw_unit2

                data = {'rw': data_[0].rw + '(' + str(data_[0].bs + ')'),
                        'bs': str(bs) + bs_unit,
                        'io': str(io) + io_unit,
                        'iops': str(iops) + iops_unit,
                        'bw': bw, }
                average_datas.append(data)
            # 基准数据和对比数据的全部数据
            for mark_name in groups:
                group_data = []
                temp_mark_datas = serializer_.filter(mark_name=mark_name)
                # 先增加头部的内容
                datas[0]['column' + str(column_index)] = 'Fio#' + str(title_index)
                datas[1]['column' + str(column_index)] = temp_mark_datas[0].execute_cmd
                datas[2]['column' + str(column_index)] = temp_mark_datas[0].modify_parameters
                for data in temp_mark_datas:
                    data = {'rw': data.rw + '(' + str(data.bs + ')'),
                            'bs': data.bs,
                            'io': data.io,
                            'iops': data.iops,
                            'bw': data.bw, }
                    group_data.append(data)
                # 增加数据部分
                # 先初始化所有数据为空
                for i in range(3, len(datas)):
                    datas[i]['column' + str(column_index)] = None
                for value in group_data:
                    # 判断comparsion_datas数据中的rw字段和datas中的rw（column）字段相同，则在datas中增加值
                    for index, data_ in enumerate(datas):
                        if index > 2:
                            if data_['column1'] == value['rw']:
                                # 在datas中增加对比数据
                                datas[index]['column' + str(column_index)] = value['bs']
                                datas[index + 1]['column' + str(column_index)] = value['io']
                                datas[index + 2]['column' + str(column_index)] = value['iops']
                                datas[index + 3]['column' + str(column_index)] = value['bw']
                                break
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = serializer_[0].execute_cmd
            datas[2]['column' + str(column_index)] = serializer_[0].modify_parameters
            for i in range(3, len(datas)):
                datas[i]['column' + str(column_index)] = None
            for value in average_datas:
                for index, data_ in enumerate(datas):
                    if index > 2:
                        if data_['column1'] == value['rw']:
                            # 在datas中增加对比数据
                            datas[index]['column' + str(column_index)] = value['bs']
                            datas[index + 1]['column' + str(column_index)] = value['io']
                            datas[index + 2]['column' + str(column_index)] = value['iops']
                            datas[index + 3]['column' + str(column_index)] = value['bw']
                            break
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(3, len(datas)):
                    datas[i]['column' + str(column_index)] = None
                # 获取到最后一组数据、处理数据
                for i in range(len(datas)):
                    if i > 2:
                        value = datas[i]['column' + str(column_index - 1)]  # 最后一组数据
                        base_value = datas[i]['column' + str(base_column_index)]  # base数据
                        if value is not None and base_value is not None:
                            value = float("".join(filter(lambda s: s in '0123456789.', value.split('(')[0])))
                            base_value = float("".join(filter(lambda s: s in '0123456789.', base_value.split('(')[0])))
                            datas[i]['column' + str(column_index)] = "%.2f%%" % ((value - base_value) / base_value * 100)
                        else:
                            datas[i]['column' + str(column_index)] = None
                column_index += 1
                pass

        return datas, title_index, column_index, base_column_index


    def get_left_data(self, serializer_):
        serializer = self.get_serializer(serializer_, many=True)
        datas = []
        groups = set([d['mark_name'] for d in serializer.data])
        filter_datas = serializer_.filter(mark_name=list(groups)[0])
        for data in filter_datas:
            data_ = {'rw': data.rw + '(' + str(data.bs + ')'),
                    'bs': data.bs,
                    'io': data.io,
                    'iops': data.iops,
                    'bw': data.bw, }
            datas.append(data_)
        temp_data = []
        for value in datas:
            data = [{'column1': value['rw'], 'column2': 'bs'},
                    {'column1': value['rw'], 'column2': 'io'},
                    {'column1': value['rw'], 'column2': 'iops'},
                    {'column1': value['rw'], 'column2': 'bw'}]
            temp_data.extend(data)
        others = [{'column1': 'Fio', 'column2': '', },
                  {'column1': '执行命令', 'column2': ''},
                  {'column1': '修改参数', 'column2': ''}]
        new_data = others + temp_data
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
        datas = self.get_left_data(base_queryset)
        title_index = 1
        column_index = 3
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)
        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Fio.objects.filter(env_id=comparativeId).all()
                if not comparsion_queryset:
                    return json_response({}, status.HTTP_200_OK, '列表')
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index, column_index, base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')

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