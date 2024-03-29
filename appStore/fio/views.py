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

    # def list(self, request, *args, **kwargs):
    #     """
    #     返回列表
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     env_id = request.GET.get('env_id')
    #     queryset = Fio.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return json_response(serializer.data, status.HTTP_200_OK, '列表')


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
        base_datas = self.get_data(base_serializer)
        datas = self.do_base_data(base_datas)
        others = [{'column1': 'Fio', 'column2': '', 'column3': 'Fio#1'},
                  {'column1': '执行命令', 'column2': '', 'column3': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Fio.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)
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
                            datas[index2]['column' + str(new_index + 1)] = value['bs']
                            datas[index2 + 1]['column' + str(new_index + 1)] = value['io']
                            datas[index2 + 2]['column' + str(new_index + 1)] = value['iops']
                            datas[index2 + 3]['column' + str(new_index + 1)] = value['bw']
                            value0 = int(
                                "".join(filter(lambda s: s in '0123456789.', datas[0]['column' + str(new_index)])))
                            value0_colum3 = int("".join(filter(lambda s: s in '0123456789.', datas[0]['column3'])))
                            value1 = int(
                                "".join(filter(lambda s: s in '0123456789.', datas[1]['column' + str(new_index)])))
                            value1_colum3 = int("".join(filter(lambda s: s in '0123456789.', datas[1]['column3'])))
                            value2 = int(
                                "".join(filter(lambda s: s in '0123456789.', datas[2]['column' + str(new_index)])))
                            value2_colum3 = int("".join(filter(lambda s: s in '0123456789.', datas[2]['column3'])))
                            value3 = int("".join(filter(lambda s: s in '0123456789.',
                                                        datas[3]['column' + str(new_index)].split('(')[-1])))
                            value3_colum3 = int("".join(
                                filter(lambda s: s in '0123456789.', datas[3]['column3'].split('(')[-1])))
                            # bs数据
                            datas[index2]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value0 - value0_colum3) / value0_colum3 * 100)
                            # io数据
                            datas[index2 + 1]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value1 - value1_colum3) / value1_colum3 * 100)
                            # iops数据
                            datas[index2 + 2]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value2 - value2_colum3) / value2_colum3 * 100)
                            # bw数据
                            datas[index2 + 3]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (value3 - value3_colum3) / value3_colum3 * 100)
                            break
        unixbench_data = {'others': others, 'data': datas}
        return json_response(unixbench_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        for k, fio_json in request.__dict__['data_fio'].items():
            data_fio = {}
            if k.lower().startswith('fio'):
                constants.FIO_BOOL = True
                data_fio['env_id'] = request.__dict__['data_fio']['env_id']
                data_fio['execute_cmd'] = 'xx'
                data_fio['modify_parameters'] = 'xx'
                data_fio['rw'] = fio_json['rw']
                data_fio['bs'] = fio_json['items']['bs']
                data_fio['io'] = fio_json['items']['io']
                data_fio['iops'] = fio_json['items']['iops']
                data_fio['bw'] = fio_json['items']['bw']
                data_fio['test_time'] = return_time(fio_json['time'])
                serializer_fio = FioSerializer(data=data_fio)
                if serializer_fio.is_valid():
                    pass
                    # self.perform_create(serializer_fio)
                    continue
                print(serializer_fio.errors, "fio")
                return json_response(serializer_fio.errors, status.HTTP_400_BAD_REQUEST,
                                     get_error_message(serializer_fio))
