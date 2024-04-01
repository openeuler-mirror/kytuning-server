import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.iozone.models import Iozone
from appStore.iozone.serializers import IozoneSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class IozoneViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Iozone.objects.all().order_by('id')
    serializer_class = IozoneSerializer

    # pagination_class = LimsPageSet

    # def list(self, request, *args, **kwargs):
    #     """
    #     返回列表
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     env_id = request.GET.get('env_id')
    #     queryset = Iozone.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     datas=[]
    #     for data in serializer.data:
    #         data = [{'first': '写测试（KB/s）', 'second': data['file_size'], 'third': data['write_test']},
    #                 {'first': '重写测试（KB/s）', 'second': data['file_size'], 'third': data['rewrite_test']},
    #                 {'first': '读测试（KB/s）', 'second': data['file_size'], 'third': data['read_test']},
    #                 {'first': '重读测试（KB/s）', 'second': data['file_size'], 'third': data['reread_test']},
    #                 {'first': '随机读测试（KB/s）', 'second': data['file_size'], 'third': data['random_read_test']},
    #                 {'first': '随机写测试（KB/s）', 'second': data['file_size'], 'third': data['random_write_test']}]
    #         datas.append(data)
    #     # return json_response(serializer.data, status.HTTP_200_OK, '列表')
    #     return json_response(datas, status.HTTP_200_OK, '列表')

    def get_data(self, serializer):
        datas = []
        for data in serializer.data:
            data_ = [
                {'column1': data['testcase_name'] + '-' + '写测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['write_test']},
                {'column1': data['testcase_name'] + '-' + '重写测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['rewrite_test']},
                {'column1': data['testcase_name'] + '-' + '读测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['read_test']},
                {'column1': data['testcase_name'] + '-' + '重读测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['reread_test']},
                {'column1': data['testcase_name'] + '-' + '随机读测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['random_read_test']},
                {'column1': data['testcase_name'] + '-' + '随机写测试（KB/s）', 'column2': data['file_size'],
                 'column3': data['random_write_test']}]
            datas.extend(data_)
        return datas

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
        base_queryset = Iozone.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        datas = self.get_data(base_serializer)
        others = [{'column1': 'Iozone', 'column2': '', 'column3': 'Iozone#1'},
                  {'column1': '执行命令', 'column2': '', 'column3': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Iozone.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)
                others[0]['column' + str(new_index)] = 'Iozone#'+str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_serializer.data[0]['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_serializer.data[0]['modify_parameters']
                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                for value in comparsion_datas:
                    # 判断comparsion_datas数据中的column1字段和datas中的column1字段相同，则在datas中增加值对应值
                    for index2, data_ in enumerate(datas):
                        if data_['column1'] == value['column1']:
                            # 在datas中增加对比数据
                            datas[index2]['column' + str(new_index)] = value['column3']
                            # 在datas中增加计算数据
                            datas[index2]['column' + str(new_index + 1)] = "%.2f%%" % (
                                        (datas[index2]['column' + str(new_index)] - datas[index2]['column3']) /
                                        datas[index2]['column3'] * 100)
                            break
        iozone_data = {'others': others, 'data': datas}
        return json_response(iozone_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        for k, iozone_json in request.__dict__['data_iozone'].items():
            if k.lower().startswith('iozone'):
                constants.IOZONE_BOOL = True
                data_iozone = {}
                data_iozone['env_id'] = request.__dict__['data_iozone']['env_id']
                data_iozone['execute_cmd'] = "xxx"
                data_iozone['modify_parameters'] = "xxx"
                data_iozone['testcase_name'] = k.split('-')[-3]
                data_iozone['file_size'] = iozone_json['测试记录'][0]['文件大小']
                data_iozone['block_size'] = iozone_json['测试记录'][0]['块大小']
                data_iozone['write_test'] = iozone_json['测试记录'][0]['写测试（KB/s）']
                data_iozone['rewrite_test'] = iozone_json['测试记录'][0]['重写测试（KB/s）']
                data_iozone['read_test'] = iozone_json['测试记录'][0]['读测试（KB/s）']
                data_iozone['reread_test'] = iozone_json['测试记录'][0]['重读测试（KB/s）']
                data_iozone['random_read_test'] = iozone_json['测试记录'][0]['随机读测试（KB/s）']
                data_iozone['random_write_test'] = iozone_json['测试记录'][0]['随机写测试（KB/s）']
                data_iozone['test_time'] = return_time(iozone_json['time'])
                serializer_iozone = IozoneSerializer(data=data_iozone)
                if serializer_iozone.is_valid():
                    # self.perform_create(serializer_iozone)
                    pass
                else:
                    print(serializer_iozone.errors, "iozone")
                    return json_response(serializer_iozone.errors, status.HTTP_400_BAD_REQUEST,
                                         get_error_message(serializer_iozone))
