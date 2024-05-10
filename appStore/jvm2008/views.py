import numpy as np

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


    def get_data(self, serializer_):
        serializer = self.get_serializer(serializer_, many=True)
        execute_cmd = serializer.data[0]['execute_cmd']
        modify_parameters = serializer.data[0]['modify_parameters']
        base_compiler = ''
        base_compress = ''
        base_crypto = ''
        base_derby = ''
        base_mpegaudio = ''
        base_scimark_large = ''
        base_scimark_small = ''
        base_serial = ''
        base_startup = ''
        base_sunflow = ''
        base_xml = ''
        base_Noncompliant_pomposite_result = ''
        peak_compiler = ''
        peak_compress = ''
        peak_crypto = ''
        peak_derby = ''
        peak_mpegaudio = ''
        peak_scimark_large = ''
        peak_scimark_small = ''
        peak_serial = ''
        peak_startup = ''
        peak_sunflow = ''
        peak_xml = ''
        peak_Noncompliant_pomposite_result = ''

        # 0-0 或者0-1这样的数据有几组，以此来判断需不需要计算平均值
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            for data in serializer.data:
                if data['tune_type'] == 'base':
                    base_compiler = data['compiler']
                    base_compress = data['compress']
                    base_crypto = data['crypto']
                    base_derby = data['derby']
                    base_mpegaudio = data['mpegaudio']
                    base_scimark_large = data['scimark_large']
                    base_scimark_small = data['scimark_small']
                    base_serial = data['serial']
                    base_startup = data['startup']
                    base_sunflow = data['sunflow']
                    base_xml = data['xml']
                    base_Noncompliant_pomposite_result = data['Noncompliant_pomposite_result']
                elif data['tune_type'] == 'peak':
                    peak_compiler = data['compiler']
                    peak_compress = data['compress']
                    peak_crypto = data['crypto']
                    peak_derby = data['derby']
                    peak_mpegaudio = data['mpegaudio']
                    peak_scimark_large = data['scimark_large']
                    peak_scimark_small = data['scimark_small']
                    peak_serial = data['serial']
                    peak_startup = data['startup']
                    peak_sunflow = data['sunflow']
                    peak_xml = data['xml']
                    peak_Noncompliant_pomposite_result = data['Noncompliant_pomposite_result']
        else:
            # 数据分组
            base_data_ = serializer_.filter(tune_type='base')
            peak_data_ = serializer_.filter(tune_type='peak')
            # base数据，将每个字典转换为NumPy数组
            base_compiler_list = [d.compiler for d in base_data_]
            base_compress_list = [d.compress for d in base_data_]
            base_crypto_list = [d.crypto for d in base_data_]
            base_derby_list = [d.derby for d in base_data_]
            base_mpegaudio_list = [d.mpegaudio for d in base_data_]
            base_scimark_large_list = [d.scimark_large for d in base_data_]
            base_scimark_small_list = [d.scimark_small for d in base_data_]
            base_serial_list = [d.serial for d in base_data_]
            base_startup_list = [d.startup for d in base_data_]
            base_sunflow_list = [d.sunflow for d in base_data_]
            base_xml_list = [d.xml for d in base_data_]
            base_Noncompliant_pomposite_result_list = [d.Noncompliant_pomposite_result for d in base_data_]
            # 计算每个数组的平均值
            base_compiler = np.mean(base_compiler_list).round(2)
            base_compress = np.mean(base_compress_list).round(2)
            base_crypto = np.mean(base_crypto_list).round(2)
            base_derby = np.mean(base_derby_list).round(2)
            base_mpegaudio = np.mean(base_mpegaudio_list).round(2)
            base_scimark_large = np.mean(base_scimark_large_list).round(2)
            base_scimark_small = np.mean(base_scimark_small_list).round(2)
            base_serial = np.mean(base_serial_list).round(2)
            base_startup = np.mean(base_startup_list).round(2)
            base_sunflow = np.mean(base_sunflow_list).round(2)
            base_xml = np.mean(base_xml_list).round(2)
            base_Noncompliant_pomposite_result = np.mean(base_Noncompliant_pomposite_result_list).round(2)
            # peak数据，将每个字典转换为NumPy数组
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
            peak_Noncompliant_pomposite_result_list = [d.Noncompliant_pomposite_result for d in peak_data_ if
                                                       d.Noncompliant_pomposite_result is not None]

            # 计算每个数组的平均值
            peak_compiler = np.mean(peak_compiler_list).round(2)
            peak_compress = np.mean(peak_compress_list).round(2)
            peak_crypto = np.mean(peak_crypto_list).round(2)
            peak_derby = np.mean(peak_derby_list).round(2)
            peak_mpegaudio = np.mean(peak_mpegaudio_list).round(2)
            peak_scimark_large = np.mean(peak_scimark_large_list).round(2)
            peak_scimark_small = np.mean(peak_scimark_small_list).round(2)
            peak_serial = np.mean(peak_serial_list).round(2)
            peak_startup = np.mean(peak_startup_list).round(2)
            peak_sunflow = np.mean(peak_sunflow_list).round(2)
            peak_xml = np.mean(peak_xml_list).round(2)
            peak_Noncompliant_pomposite_result = np.mean(peak_Noncompliant_pomposite_result_list).round(2)

        new_data = {
            'execute_cmd': execute_cmd,
            'modify_parameters': modify_parameters,
            'base_compiler': base_compiler,
            'base_compress': base_compress,
            'base_crypto': base_crypto,
            'base_derby': base_derby,
            'base_mpegaudio': base_mpegaudio,
            'base_scimark_large': base_scimark_large,
            'base_scimark_small': base_scimark_small,
            'base_serial': base_serial,
            'base_startup': base_startup,
            'base_sunflow': base_sunflow,
            'base_xml': base_xml,
            'base_Noncompliant_pomposite_result': base_Noncompliant_pomposite_result,
            'peak_compiler': peak_compiler,
            'peak_compress': peak_compress,
            'peak_crypto': peak_crypto,
            'peak_derby': peak_derby,
            'peak_mpegaudio': peak_mpegaudio,
            'peak_scimark_large': peak_scimark_large,
            'peak_scimark_small': peak_scimark_small,
            'peak_serial': peak_serial,
            'peak_startup': peak_startup,
            'peak_sunflow': peak_sunflow,
            'peak_xml': peak_xml,
            'peak_Noncompliant_pomposite_result': peak_Noncompliant_pomposite_result,
        }
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
        base_queryset = Jvm2008.objects.filter(env_id=env_id).all()
        data = self.get_data(base_queryset)
        others = [{'column1': 'Jvm2008', 'column2': '', 'column3': 'Jvm2008m#1 (基准数据)'},
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
                comparsion_datas = self.get_data(comparsion_queryset)
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

                datas[0]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[0]['column' + str(new_index)] - datas[0]['column3']) / datas[0]['column3'] * 100)
                datas[1]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[1]['column' + str(new_index)] - datas[1]['column3']) / datas[1]['column3'] * 100)
                datas[2]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[2]['column' + str(new_index)] - datas[2]['column3']) / datas[2]['column3'] * 100)
                datas[3]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[3]['column' + str(new_index)] - datas[3]['column3']) / datas[3]['column3'] * 100)
                datas[4]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[4]['column' + str(new_index)] - datas[4]['column3']) / datas[4]['column3'] * 100)
                datas[5]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[5]['column' + str(new_index)] - datas[5]['column3']) / datas[5]['column3'] * 100)
                datas[6]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[6]['column' + str(new_index)] - datas[6]['column3']) / datas[6]['column3'] * 100)
                datas[7]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[7]['column' + str(new_index)] - datas[7]['column3']) / datas[7]['column3'] * 100)
                datas[8]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (datas[8]['column' + str(new_index)] - datas[8]['column3']) / datas[8]['column3'] * 100)
                datas[9]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[9]['column' + str(new_index)] - datas[9]['column3']) / datas[9]['column3'] * 100)
                datas[10]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[10]['column' + str(new_index)] - datas[10]['column3']) / datas[10]['column3'] * 100)
                datas[11]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[11]['column' + str(new_index)] - datas[11]['column3']) / datas[11]['column3'] * 100)
                datas[12]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[12]['column' + str(new_index)] - datas[12]['column3']) / datas[12]['column3'] * 100)
                datas[13]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[13]['column' + str(new_index)] - datas[13]['column3']) / datas[13]['column3'] * 100)
                datas[14]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[14]['column' + str(new_index)] - datas[14]['column3']) / datas[14]['column3'] * 100)
                datas[15]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[15]['column' + str(new_index)] - datas[15]['column3']) / datas[15]['column3'] * 100)
                datas[16]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[16]['column' + str(new_index)] - datas[16]['column3']) / datas[16]['column3'] * 100)
                datas[17]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[17]['column' + str(new_index)] - datas[17]['column3']) / datas[17]['column3'] * 100)
                datas[18]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[18]['column' + str(new_index)] - datas[18]['column3']) / datas[18]['column3'] * 100)
                datas[19]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[19]['column' + str(new_index)] - datas[19]['column3']) / datas[19]['column3'] * 100)
                datas[20]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[20]['column' + str(new_index)] - datas[20]['column3']) / datas[20]['column3'] * 100)
                datas[21]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[21]['column' + str(new_index)] - datas[21]['column3']) / datas[21]['column3'] * 100)
                datas[22]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[22]['column' + str(new_index)] - datas[22]['column3']) / datas[22]['column3'] * 100)
                datas[23]['column' + str(new_index + 1)] = "%.2f%%" % (
                            (datas[23]['column' + str(new_index)] - datas[23]['column3']) / datas[23]['column3'] * 100)
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
                data_jvm2008['modify_parameters'] = '参数'
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
                data_jvm2008['Noncompliant_pomposite_result'] = jvm2008_json['items'][tune_type][
                    'Noncompliant composite result:']
                data_jvm2008['test_time'] = return_time(jvm2008_json['time'])
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
