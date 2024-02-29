import json
from itertools import groupby

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from appStore.fio.serializers import FioSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class FioViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    # queryset = Stream.objects.all().order_by('id')
    serializer_class = FioSerializer

    def create(self, request, *args, **kwargs):
        for k, fio_json in request.__dict__['data_fio'].items():
            data_fio = {}
            if k.lower().startswith('fio'):
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
                    self.perform_create(serializer_fio)
                    continue
                print(serializer_fio.errors,"fio")
                return json_response(serializer_fio.errors, status.HTTP_400_BAD_REQUEST,
                                     get_error_message(serializer_fio))
