"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Feb 29 16:18:43 2024 +0800
"""
import numpy as np

# Create your views here.
from rest_framework import status

from appStore.jvm2008.models import Jvm2008
from appStore.jvm2008.serializers import Jvm2008Serializer
from appStore.project.models import Project
from appStore.utils.common import json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet


class Jvm2008ViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Jvm2008.objects.all().order_by('id')
    serializer_class = Jvm2008Serializer

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        # 0-0 或者0-1这样的数据有几组，以此来判断需不需要计算平均值
        groups = set([d.mark_name for d in serializer_])
        if not groups or len(groups) == 1:
            if not groups:
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'Jvm2008#' + str(title_index)
                datas[1]['column' + str(column_index)] = None
                datas[2]['column' + str(column_index)] = None
                datas[3]['column' + str(column_index)] = None
                # 初始化所有数据为None
                for i in range(4, 28):
                    datas[i]['column' + str(column_index)] = None
                column_index += 1
                title_index += 1
            elif len(groups) == 1:
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'Jvm2008#' + str(title_index)
                datas[1]['column' + str(column_index)] = Project.objects.filter(env_id=serializer.data[0]['env_id']).first().project_name
                datas[2]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
                datas[3]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
                # 初始化所有数据为None
                for i in range(4, 28):
                    datas[i]['column' + str(column_index)] = None
                for data in serializer.data:
                    if data['tune_type'] == 'base':
                        datas[4]['column' + str(column_index)] = data['compiler']
                        datas[5]['column' + str(column_index)] = data['compress']
                        datas[6]['column' + str(column_index)] = data['crypto']
                        datas[7]['column' + str(column_index)] = data['derby']
                        datas[8]['column' + str(column_index)] = data['mpegaudio']
                        datas[9]['column' + str(column_index)] = data['scimark_large']
                        datas[10]['column' + str(column_index)] = data['scimark_small']
                        datas[11]['column' + str(column_index)] = data['serial']
                        datas[12]['column' + str(column_index)] = data['startup']
                        datas[13]['column' + str(column_index)] = data['sunflow']
                        datas[14]['column' + str(column_index)] = data['xml']
                        datas[15]['column' + str(column_index)] = data['Noncompliant_pomposite_result']
                    elif data['tune_type'] == 'peak':
                        datas[16]['column' + str(column_index)] = data['compiler']
                        datas[17]['column' + str(column_index)] = data['compress']
                        datas[18]['column' + str(column_index)] = data['crypto']
                        datas[19]['column' + str(column_index)] = data['derby']
                        datas[20]['column' + str(column_index)] = data['mpegaudio']
                        datas[21]['column' + str(column_index)] = data['scimark_large']
                        datas[22]['column' + str(column_index)] = data['scimark_small']
                        datas[23]['column' + str(column_index)] = data['serial']
                        datas[24]['column' + str(column_index)] = data['startup']
                        datas[25]['column' + str(column_index)] = data['sunflow']
                        datas[26]['column' + str(column_index)] = data['xml']
                        datas[27]['column' + str(column_index)] = data['Noncompliant_pomposite_result']
                column_index += 1
                title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = ''
            for i in range(4, 28):
                datas[i]['column' + str(column_index)] = datas[i]['column' + str(column_index - 1)]
            column_index += 1
        else:
            # 计算平均值
            base_data_ = serializer_.filter(tune_type='base')
            peak_data_ = serializer_.filter(tune_type='peak')
            # base数据，将每个字典转换为NumPy数组
            base_compiler_list = [d.compiler for d in base_data_ if d.compiler is not None]
            base_compress_list = [d.compress for d in base_data_ if d.compress is not None]
            base_crypto_list = [d.crypto for d in base_data_ if d.crypto is not None]
            base_derby_list = [d.derby for d in base_data_ if d.derby is not None]
            base_mpegaudio_list = [d.mpegaudio for d in base_data_ if d.mpegaudio is not None]
            base_scimark_large_list = [d.scimark_large for d in base_data_ if d.scimark_large is not None]
            base_scimark_small_list = [d.scimark_small for d in base_data_ if d.scimark_small is not None]
            base_serial_list = [d.serial for d in base_data_ if d.serial is not None]
            base_startup_list = [d.startup for d in base_data_ if d.startup is not None]
            base_sunflow_list = [d.sunflow for d in base_data_ if d.sunflow is not None]
            base_xml_list = [d.xml for d in base_data_ if d.xml is not None]
            base_Noncompliant_pomposite_result_list = [d.Noncompliant_pomposite_result for d in base_data_ if d.Noncompliant_pomposite_result is not None]
            # 计算每个数组的平均值
            average_base_compiler = np.mean(base_compiler_list).round(2) if not np.isnan(np.mean(base_compiler_list)) else None
            average_base_compress = np.mean(base_compress_list).round(2) if not np.isnan(np.mean(base_compress_list)) else None
            average_base_crypto = np.mean(base_crypto_list).round(2) if not np.isnan(np.mean(base_crypto_list)) else None
            average_base_derby = np.mean(base_derby_list).round(2) if not np.isnan(np.mean(base_derby_list)) else None
            average_base_mpegaudio = np.mean(base_mpegaudio_list).round(2) if not np.isnan(np.mean(base_mpegaudio_list)) else None
            average_base_scimark_large = np.mean(base_scimark_large_list).round(2) if not np.isnan(np.mean(base_scimark_large_list)) else None
            average_base_scimark_small = np.mean(base_scimark_small_list).round(2) if not np.isnan(np.mean(base_scimark_small_list)) else None
            average_base_serial = np.mean(base_serial_list).round(2) if not np.isnan(np.mean(base_serial_list)) else None
            average_base_startup = np.mean(base_startup_list).round(2) if not np.isnan(np.mean(base_startup_list)) else None
            average_base_sunflow = np.mean(base_sunflow_list).round(2) if not np.isnan(np.mean(base_sunflow_list)) else None
            average_base_xml = np.mean(base_xml_list).round(2) if not np.isnan(np.mean(base_xml_list)) else None
            average_base_Noncompliant_pomposite_result = np.mean(base_Noncompliant_pomposite_result_list).round(2) if not np.isnan(np.mean(base_Noncompliant_pomposite_result_list)) else None

            peak_compiler_list = [d.compiler for d in peak_data_ if d.compiler is not None]
            peak_compress_list = [d.compress for d in peak_data_ if d.compress is not None]
            peak_crypto_list = [d.crypto for d in peak_data_ if d.crypto is not None]
            peak_derby_list = [d.derby for d in peak_data_ if d.derby is not None]
            peak_mpegaudio_list = [d.mpegaudio for d in peak_data_ if d.mpegaudio is not None]
            peak_scimark_large_list = [d.scimark_large for d in peak_data_ if d.scimark_large is not None]
            peak_scimark_small_list = [d.scimark_small for d in peak_data_ if d.scimark_small is not None]
            peak_serial_list = [d.serial for d in peak_data_ if d.serial is not None]
            peak_startup_list = [d.startup for d in peak_data_ if d.startup is not None]
            peak_sunflow_list = [d.sunflow for d in peak_data_ if d.sunflow is not None]
            peak_xml_list = [d.xml for d in peak_data_ if d.xml is not None]
            peak_Noncompliant_pomposite_result_list = [d.Noncompliant_pomposite_result for d in peak_data_ if d.Noncompliant_pomposite_result is not None]
            # 计算每个数组的平均值
            average_peak_compiler = np.mean(peak_compiler_list).round(2) if not np.isnan(np.mean(peak_compiler_list)) else None
            average_peak_compress = np.mean(peak_compress_list).round(2) if not np.isnan(np.mean(peak_compress_list)) else None
            average_peak_crypto = np.mean(peak_crypto_list).round(2) if not np.isnan(np.mean(peak_crypto_list)) else None
            average_peak_derby = np.mean(peak_derby_list).round(2) if not np.isnan(np.mean(peak_derby_list)) else None
            average_peak_mpegaudio = np.mean(peak_mpegaudio_list).round(2) if not np.isnan(np.mean(peak_mpegaudio_list)) else None
            average_peak_scimark_large = np.mean(peak_scimark_large_list).round(2) if not np.isnan(np.mean(peak_scimark_large_list)) else None
            average_peak_scimark_small = np.mean(peak_scimark_small_list).round(2) if not np.isnan(np.mean(peak_scimark_small_list)) else None
            average_peak_serial = np.mean(peak_serial_list).round(2) if not np.isnan(np.mean(peak_serial_list)) else None
            average_peak_startup = np.mean(peak_startup_list).round(2) if not np.isnan(np.mean(peak_startup_list)) else None
            average_peak_sunflow = np.mean(peak_sunflow_list).round(2) if not np.isnan(np.mean(peak_sunflow_list)) else None
            average_peak_xml = np.mean(peak_xml_list).round(2) if not np.isnan(np.mean(peak_xml_list)) else None
            average_peak_Noncompliant_pomposite_result = np.mean(peak_Noncompliant_pomposite_result_list).round(2) if not np.isnan(np.mean(peak_Noncompliant_pomposite_result_list)) else None

            # 查到mark-name相同的数据拼接为一组：serializer.data
            for mark_name in groups:
                temp_datas = serializer_.filter(mark_name=mark_name)
                datas[0]['column' + str(column_index)] = 'Jvm2008#' + str(title_index)
                datas[1]['column' + str(column_index)] = Project.objects.filter(env_id=temp_datas[0].env_id).first().project_name
                datas[2]['column' + str(column_index)] = temp_datas[0].execute_cmd
                datas[3]['column' + str(column_index)] = temp_datas[0].modify_parameters
                # 基准数据和对比数据的全部数据
                # 初始化所有数据为None
                for i in range(4, 28):
                    datas[i]['column' + str(column_index)] = None
                for data in temp_datas:
                    if data.tune_type == 'base':
                        datas[4]['column' + str(column_index)] = data.compiler
                        datas[5]['column' + str(column_index)] = data.compress
                        datas[6]['column' + str(column_index)] = data.crypto
                        datas[7]['column' + str(column_index)] = data.derby
                        datas[8]['column' + str(column_index)] = data.mpegaudio
                        datas[9]['column' + str(column_index)] = data.scimark_large
                        datas[10]['column' + str(column_index)] = data.scimark_small
                        datas[11]['column' + str(column_index)] = data.serial
                        datas[12]['column' + str(column_index)] = data.startup
                        datas[13]['column' + str(column_index)] = data.sunflow
                        datas[14]['column' + str(column_index)] = data.xml
                        datas[15]['column' + str(column_index)] = data.Noncompliant_pomposite_result
                    elif data.tune_type == 'peak':
                        datas[16]['column' + str(column_index)] = data.compiler
                        datas[17]['column' + str(column_index)] = data.compress
                        datas[18]['column' + str(column_index)] = data.crypto
                        datas[19]['column' + str(column_index)] = data.derby
                        datas[20]['column' + str(column_index)] = data.mpegaudio
                        datas[21]['column' + str(column_index)] = data.scimark_large
                        datas[22]['column' + str(column_index)] = data.scimark_small
                        datas[23]['column' + str(column_index)] = data.serial
                        datas[24]['column' + str(column_index)] = data.startup
                        datas[25]['column' + str(column_index)] = data.sunflow
                        datas[26]['column' + str(column_index)] = data.xml
                        datas[27]['column' + str(column_index)] = data.Noncompliant_pomposite_result
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = ''
            datas[4]['column' + str(column_index)] = average_base_compiler
            datas[5]['column' + str(column_index)] = average_base_compress
            datas[6]['column' + str(column_index)] = average_base_crypto
            datas[7]['column' + str(column_index)] = average_base_derby
            datas[8]['column' + str(column_index)] = average_base_mpegaudio
            datas[9]['column' + str(column_index)] = average_base_scimark_large
            datas[10]['column' + str(column_index)] = average_base_scimark_small
            datas[11]['column' + str(column_index)] = average_base_serial
            datas[12]['column' + str(column_index)] = average_base_startup
            datas[13]['column' + str(column_index)] = average_base_sunflow
            datas[14]['column' + str(column_index)] = average_base_xml
            datas[15]['column' + str(column_index)] = average_base_Noncompliant_pomposite_result
            datas[16]['column' + str(column_index)] = average_peak_compiler
            datas[17]['column' + str(column_index)] = average_peak_compress
            datas[18]['column' + str(column_index)] = average_peak_crypto
            datas[19]['column' + str(column_index)] = average_peak_derby
            datas[20]['column' + str(column_index)] = average_peak_mpegaudio
            datas[21]['column' + str(column_index)] = average_peak_scimark_large
            datas[22]['column' + str(column_index)] = average_peak_scimark_small
            datas[23]['column' + str(column_index)] = average_peak_serial
            datas[24]['column' + str(column_index)] = average_peak_startup
            datas[25]['column' + str(column_index)] = average_peak_sunflow
            datas[26]['column' + str(column_index)] = average_peak_xml
            datas[27]['column' + str(column_index)] = average_peak_Noncompliant_pomposite_result
            column_index += 1

        if not base_column_index:
            # 记录基准数据
            base_column_index = column_index - 1
        else:
            # 对比数据的对比值
            datas[0]['column' + str(column_index)] = '对比值'
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = ''
            for i in range(4, 28):
                datas[i]['column' + str(column_index)] = \
                    "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i][
                        'column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if \
                    datas[i]['column' + str(column_index - 1)] is not None and datas[i][
                        'column' + str(base_column_index)] is not None else None
            column_index += 1
        return datas, title_index, column_index, base_column_index

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
        datas = [
            {'column1': 'Jvm2008', 'column2': ''},
            {'column1': '项目名称', 'column2': ''},
            {'column1': '执行命令', 'column2': ''},
            {'column1': '修改参数', 'column2': ''},
            {'column1': 'base', 'column2': 'compiler size'},
            {'column1': 'base', 'column2': 'compress'},
            {'column1': 'base', 'column2': 'crypto'},
            {'column1': 'base', 'column2': 'derby'},
            {'column1': 'base', 'column2': 'mpegaudio'},
            {'column1': 'base', 'column2': 'scimark.large size'},
            {'column1': 'base', 'column2': 'scimark.small'},
            {'column1': 'base', 'column2': 'serial'},
            {'column1': 'base', 'column2': 'startup'},
            {'column1': 'base', 'column2': 'sunflow'},
            {'column1': 'base', 'column2': 'xml'},
            {'column1': 'base', 'column2': 'Noncompliant composite result:'},
            {'column1': 'peak', 'column2': 'compiler'},
            {'column1': 'peak', 'column2': 'compress'},
            {'column1': 'peak', 'column2': 'crypto'},
            {'column1': 'peak', 'column2': 'derby'},
            {'column1': 'peak', 'column2': 'mpegaudio'},
            {'column1': 'peak', 'column2': 'scimark.large'},
            {'column1': 'peak', 'column2': 'scimark.small'},
            {'column1': 'peak', 'column2': 'serial'},
            {'column1': 'peak', 'column2': 'startup'},
            {'column1': 'peak', 'column2': 'sunflow'},
            {'column1': 'peak', 'column2': 'xml'},
            {'column1': 'peak', 'column2': 'Noncompliant composite result:'},
        ]
        title_index = 1
        column_index = 3
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)
        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Jvm2008.objects.filter(env_id=comparativeId).all()
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas,
                                                                                    title_index, column_index,
                                                                                    base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_jvm2008_errors = []
        errors_message = []
        for k, jvm2008_json in request.__dict__['data_jvm2008'].items():
            if k.lower().startswith('specjvm'):
                data_jvm2008 = {}
                tune_type = k.split('-')[-3]
                data_jvm2008['env_id'] = request.__dict__['data_jvm2008']['env_id']
                data_jvm2008['tune_type'] = tune_type
                data_jvm2008['execute_cmd'] = jvm2008_json.get('execute_cmd')
                data_jvm2008['modify_parameters'] = str(jvm2008_json.get('modify_parameters'))[1:-2] if jvm2008_json.get('modify_parameters') else None
                data_jvm2008['mark_name'] = k[-3:]
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
                data_jvm2008['Noncompliant_pomposite_result'] = jvm2008_json['items'][tune_type].get(
                    'Noncompliant composite result:')
                data_jvm2008 = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                                data_jvm2008.items()}
                serializer_jvm2008 = Jvm2008Serializer(data=data_jvm2008)
                if serializer_jvm2008.is_valid():
                    self.perform_create(serializer_jvm2008)
                else:
                    serializer_jvm2008_errors.append(serializer_jvm2008.errors)
                    errors_message.append(get_error_message(serializer_jvm2008))
        if serializer_jvm2008_errors:
            print(serializer_jvm2008_errors, "jvm2008")
            return json_response(serializer_jvm2008_errors, status.HTTP_400_BAD_REQUEST, errors_message)
        else:
            return
