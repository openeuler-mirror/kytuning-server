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
        data_jvm2008 = {}
        for k, jvm2008_json in request.__dict__['data_jvm2008'].items():
            if k.lower().startswith('specjvm'):
                data_jvm2008['env_id'] = request.__dict__['data_jvm2008']['env_id']
                if k.split('-')[-3] == "base":
                    data_jvm2008['base'] = 'base'
                    data_jvm2008['base_execute_cmd'] = 'xxx'
                    data_jvm2008['base_modify_parameters'] = 'xxx'
                    data_jvm2008['base_compiler'] = jvm2008_json['items']['base']['compiler']
                    data_jvm2008['base_compress'] = jvm2008_json['items']['base']['compress']
                    data_jvm2008['base_crypto'] = jvm2008_json['items']['base']['crypto']
                    data_jvm2008['base_derby'] = jvm2008_json['items']['base']['derby']
                    data_jvm2008['base_mpegaudio'] = jvm2008_json['items']['base']['mpegaudio']
                    data_jvm2008['base_scimark_large'] = jvm2008_json['items']['base']['scimark.large']
                    data_jvm2008['base_scimark_small'] = jvm2008_json['items']['base']['scimark.small']
                    data_jvm2008['base_serial'] = jvm2008_json['items']['base']['serial']
                    data_jvm2008['base_startup'] = jvm2008_json['items']['base']['startup']
                    data_jvm2008['base_sunflow'] = jvm2008_json['items']['base']['sunflow']
                    data_jvm2008['base_xml'] = jvm2008_json['items']['base']['xml']
                    data_jvm2008['base_Noncompliant_pomposite_result'] = jvm2008_json['items']['base']['Noncompliant composite result:']
                    data_jvm2008['base_test_time'] = return_time(jvm2008_json['time'])
                elif k.split('-')[-3] == "peak":
                    data_jvm2008['peak'] = 'peak'
                    data_jvm2008['peak_execute_cmd'] = 'xxx'
                    data_jvm2008['peak_modify_parameters'] = 'xxx'
                    data_jvm2008['peak_compiler'] = jvm2008_json['items']['peak']['compiler']
                    data_jvm2008['peak_compress'] = jvm2008_json['items']['peak']['compress']
                    data_jvm2008['peak_crypto'] = jvm2008_json['items']['peak']['crypto']
                    data_jvm2008['peak_derby'] = jvm2008_json['items']['peak']['derby']
                    data_jvm2008['peak_mpegaudio'] = jvm2008_json['items']['peak']['mpegaudio']
                    data_jvm2008['peak_scimark_large'] = jvm2008_json['items']['peak']['scimark.large']
                    data_jvm2008['peak_scimark_small'] = jvm2008_json['items']['peak']['scimark.small']
                    data_jvm2008['peak_serial'] = jvm2008_json['items']['peak']['serial']
                    data_jvm2008['peak_startup'] = jvm2008_json['items']['peak']['startup']
                    data_jvm2008['peak_sunflow'] = jvm2008_json['items']['peak']['sunflow']
                    data_jvm2008['peak_xml'] = jvm2008_json['items']['peak']['xml']
                    data_jvm2008['peak_Noncompliant_pomposite_result'] = jvm2008_json['items']['peak']['Noncompliant composite result:']
                    data_jvm2008['peak_test_time'] = return_time(jvm2008_json['time'])
        serializer_jvm2008 = Jvm2008Serializer(data=data_jvm2008)
        if serializer_jvm2008.is_valid():
            # todo 放开
            pass
            # self.perform_create(serializer_jvm2008)
        else:
            print(serializer_jvm2008.errors,"jvm2008")
            return json_response(serializer_jvm2008.errors, status.HTTP_400_BAD_REQUEST,
                                 get_error_message(serializer_jvm2008))
