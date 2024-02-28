import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from appStore.iozone.serializers import IozoneSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class IozoneViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    serializer_class = IozoneSerializer
    # pagination_class = LimsPageSet

    def create(self, request, *args, **kwargs):
        for k, iozone_json in request.__dict__['data_iozone'].items():
            if k.lower().startswith('iozone'):
                data_iozone = {}
                data_iozone['env_id'] = request.__dict__['data_iozone']['env_id']
                data_iozone['execute_cmd'] = "xxx"
                data_iozone['modify_parameters'] = "xxx"
                data_iozone['testcase_name'] = k.split('-')[-3]
                # todo 存在多组数据的情况吗？
                data_iozone['file_size'] = iozone_json['测试记录'][0]['文件大小']
                data_iozone['block_size'] = iozone_json['测试记录'][0]['块大小']
                data_iozone['Write_test'] = iozone_json['测试记录'][0]['写测试（KB/s）']
                data_iozone['Rewrite_test'] = iozone_json['测试记录'][0]['重写测试（KB/s）']
                data_iozone['read_test'] = iozone_json['测试记录'][0]['读测试（KB/s）']
                data_iozone['reread_test'] = iozone_json['测试记录'][0]['重读测试（KB/s）']
                data_iozone['random_read_test'] = iozone_json['测试记录'][0]['随机读测试（KB/s）']
                data_iozone['random_write_test'] = iozone_json['测试记录'][0]['随机写测试（KB/s）']
                data_iozone['test_time'] = return_time(iozone_json['time'])
                serializer_iozone = IozoneSerializer(data=data_iozone)
                if serializer_iozone.is_valid():
                    pass
                    # todo 放开
                    # self.perform_create(serializer_iozone)
                    return
                print(serializer_iozone.errors,"iozone")
                return json_response(serializer_iozone.errors, status.HTTP_400_BAD_REQUEST,
                                     get_error_message(serializer_iozone))
