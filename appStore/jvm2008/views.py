import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from appStore.jvm2008.serializers import Jvm2008Serializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class Jvm2008ViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    # queryset = Stream.objects.all().order_by('id')
    serializer_class = Jvm2008Serializer

    # pagination_class = LimsPageSet

    def create(self, request, *args, **kwargs):
        serializer_jvm2008_errors = []
        errors_message = []
        for k, jvm2008_json in request.__dict__['data_jvm2008'].items():
            if k.lower().startswith('specjvm'):
                data_jvm2008 = {}
                tune_type = k.split('-')[-3]
                data_jvm2008['env_id'] = request.__dict__['data_jvm2008']['env_id']
                data_jvm2008['tune_type'] = tune_type
                data_jvm2008['execute_cmd'] = 'xxx'
                data_jvm2008['modify_parameters'] = 'xxx'
                data_jvm2008['compiler'] = jvm2008_json['items'][tune_type]['compiler']
                data_jvm2008['compress'] = jvm2008_json['items'][tune_type]['compress']
                data_jvm2008['crypto'] = jvm2008_json['items'][tune_type]['crypto']
                data_jvm2008['derby'] = jvm2008_json['items'][tune_type]['derby']
                data_jvm2008['mpegaudio'] = jvm2008_json['items'][tune_type]['mpegaudio']
                data_jvm2008['scimark_large'] = jvm2008_json['items'][tune_type]['scimark.large']
                data_jvm2008['scimark_small'] = jvm2008_json['items'][tune_type]['scimark.small']
                data_jvm2008['serial'] = jvm2008_json['items'][tune_type]['serial']
                data_jvm2008['startup'] = jvm2008_json['items'][tune_type]['startup']
                data_jvm2008['sunflow'] = jvm2008_json['items'][tune_type]['sunflow']
                data_jvm2008['xml'] = jvm2008_json['items'][tune_type]['xml']
                data_jvm2008['Noncompliant_pomposite_result'] = jvm2008_json['items'][tune_type][
                    'Noncompliant composite result:']
                data_jvm2008['test_time'] = return_time(jvm2008_json['time'])
                serializer_jvm2008 = Jvm2008Serializer(data=data_jvm2008)
                if serializer_jvm2008.is_valid():
                    # todo 放开
                    pass
                    # self.perform_create(serializer_jvm2008)
                else:
                    print(serializer_jvm2008.errors, "jvm2008")
                    serializer_jvm2008_errors.append(serializer_jvm2008.errors)
                    errors_message.append(get_error_message(serializer_jvm2008))
        return json_response(serializer_jvm2008_errors, status.HTTP_400_BAD_REQUEST, errors_message)
