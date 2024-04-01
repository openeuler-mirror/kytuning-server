import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.jvm2008.models import Jvm2008
from appStore.jvm2008.serializers import Jvm2008Serializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class Jvm2008ViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Jvm2008.objects.all().order_by('id')
    serializer_class = Jvm2008Serializer

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
    #     queryset = Jvm2008.objects.filter(env_id=env_id).all()
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
        base_queryset = Jvm2008.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        # 判断数据超过两条，不显示
        if len(base_queryset) > 2:
            return json_response({}, status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, '数据存储有问题，存两条以上的数据了')
        data = self.get_data(base_serializer)
        others = [{'column1': 'Jvm2008', 'column2': '', 'column3': 'Jvm2008m#1'},
                  {'column1': '执行命令', 'column2': '', 'column3': data['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': data['modify_parameters']}]
        datas = [
            {'column1': 'base', 'column2': 'compiler size', 'column3': data['base_compiler']},
            {'column1': 'base', 'column2': 'compress', 'column3': data['base_compress']},
            {'column1': 'base', 'column2': 'crypto', 'column3': data['base_crypto']},
            {'column1': 'base', 'column2': 'derby', 'column3': data['base_derby']},
            {'column1': 'base', 'column2': 'mpegaudio', 'column3': data['base_mpegaudio']},
            {'column1': 'base', 'column2': 'scimark.large size', 'column3': data['base_scimark_large']},
            {'column1': 'base', 'column2': 'scimark.small', 'column3': data['base_scimark_small']},
            {'column1': 'base', 'column2': 'serial', 'column3': data['base_serial']},
            {'column1': 'base', 'column2': 'startup', 'column3': data['base_startup']},
            {'column1': 'base', 'column2': 'sunflow', 'column3': data['base_sunflow']},
            {'column1': 'base', 'column2': 'xml', 'column3': data['base_xml']},
            {'column1': 'base', 'column2': 'Noncompliant composite result:',
             'column3': data['base_Noncompliant_pomposite_result']},
            {'column1': 'peak', 'column2': 'compiler', 'column3': data['peak_compiler']},
            {'column1': 'peak', 'column2': 'compress', 'column3': data['peak_compress']},
            {'column1': 'peak', 'column2': 'crypto', 'column3': data['peak_crypto']},
            {'column1': 'peak', 'column2': 'derby', 'column3': data['peak_derby']},
            {'column1': 'peak', 'column2': 'mpegaudio', 'column3': data['peak_mpegaudio']},
            {'column1': 'peak', 'column2': 'scimark.large', 'column3': data['peak_scimark_large']},
            {'column1': 'peak', 'column2': 'scimark.small', 'column3': data['peak_scimark_small']},
            {'column1': 'peak', 'column2': 'serial', 'column3': data['peak_serial']},
            {'column1': 'peak', 'column2': 'startup', 'column3': data['peak_startup']},
            {'column1': 'peak', 'column2': 'sunflow', 'column3': data['peak_sunflow']},
            {'column1': 'peak', 'column2': 'xml', 'column3': data['peak_xml']},
            {'column1': 'peak', 'column2': 'Noncompliant composite result:',
             'column3': data['peak_Noncompliant_pomposite_result']},
        ]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Jvm2008.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)
                others[0]['column' + str(new_index)] = 'Jvm2008#' + str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_datas['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_datas['modify_parameters']
                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                datas[0]['column' + str(new_index)] = comparsion_datas['base_compiler']
                datas[1]['column' + str(new_index)] = comparsion_datas['base_compress']
                datas[2]['column' + str(new_index)] = comparsion_datas['base_crypto']
                datas[3]['column' + str(new_index)] = comparsion_datas['base_derby']
                datas[4]['column' + str(new_index)] = comparsion_datas['base_mpegaudio']
                datas[5]['column' + str(new_index)] = comparsion_datas['base_scimark_large']
                datas[6]['column' + str(new_index)] = comparsion_datas['base_scimark_small']
                datas[7]['column' + str(new_index)] = comparsion_datas['base_serial']
                datas[8]['column' + str(new_index)] = comparsion_datas['base_startup']
                datas[9]['column' + str(new_index)] = comparsion_datas['base_sunflow']
                datas[10]['column' + str(new_index)] = comparsion_datas['base_xml']
                datas[11]['column' + str(new_index)] = comparsion_datas['base_Noncompliant_pomposite_result']
                datas[12]['column' + str(new_index)] = comparsion_datas['peak_compiler']
                datas[13]['column' + str(new_index)] = comparsion_datas['peak_compress']
                datas[14]['column' + str(new_index)] = comparsion_datas['peak_crypto']
                datas[15]['column' + str(new_index)] = comparsion_datas['peak_derby']
                datas[16]['column' + str(new_index)] = comparsion_datas['peak_mpegaudio']
                datas[17]['column' + str(new_index)] = comparsion_datas['peak_scimark_large']
                datas[18]['column' + str(new_index)] = comparsion_datas['peak_scimark_small']
                datas[19]['column' + str(new_index)] = comparsion_datas['peak_serial']
                datas[20]['column' + str(new_index)] = comparsion_datas['peak_startup']
                datas[21]['column' + str(new_index)] = comparsion_datas['peak_sunflow']
                datas[22]['column' + str(new_index)] = comparsion_datas['peak_xml']
                datas[23]['column' + str(new_index)] = comparsion_datas['peak_Noncompliant_pomposite_result']


        jvm2008_data = {'others': others, 'data': datas}
        return json_response(jvm2008_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_jvm2008_errors = []
        errors_message = []
        for k, jvm2008_json in request.__dict__['data_jvm2008'].items():
            if k.lower().startswith('specjvm'):
                constants.JVM2008_BOOL = True
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
                    # self.perform_create(serializer_jvm2008)
                    pass
                else:
                    print(serializer_jvm2008.errors, "jvm2008")
                    serializer_jvm2008_errors.append(serializer_jvm2008.errors)
                    errors_message.append(get_error_message(serializer_jvm2008))
        return json_response(serializer_jvm2008_errors, status.HTTP_400_BAD_REQUEST, errors_message)
