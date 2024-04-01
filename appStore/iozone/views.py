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
