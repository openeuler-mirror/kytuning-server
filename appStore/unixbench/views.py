"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 4 10:06:06 2024 +0800
"""
# Create your views here.
import math
import numpy as np
from rest_framework import status

from appStore.unixbench.models import Unixbench
from appStore.unixbench.serializers import UnixbenchSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time, list_response
from appStore.utils.customer_view import CusModelViewSet


class UnixbenchViewSet(CusModelViewSet):
    """
    Unixbench数据管理
    """

    queryset = Unixbench.objects.all().order_by('id')
    serializer_class = UnixbenchSerializer

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        # 0-0 或者0-1这样的数据有几组，以此来判断需不需要计算平均值
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            # 基准数据和对比数据的全部数据
            datas[0]['column' + str(column_index)] = 'Unixbench#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            # 初始化所有数据为None
            for i in range(3, 29):
                datas[i]['column' + str(column_index)] = None
            for data in serializer.data:
                if data['thread'] == '单线程':
                    # 单线程数据
                    single_Dhrystone = data['Dhrystone']
                    single_Double_Precision = data['Double_Precision']
                    single_execl_throughput = data['execl_throughput']
                    single_file_copy_1024 = data['file_copy_1024']
                    single_file_copy_256 = data['file_copy_256']
                    single_file_copy_4096 = data['file_copy_4096']
                    single_pipe_throughput = data['pipe_throughput']
                    single_pipe_based = data['pipe_based']
                    single_process_creation = data['process_creation']
                    single_shell_scripts_1 = data['shell_scripts_1']
                    single_shell_scripts_8 = data['shell_scripts_8']
                    single_system_call_overhead = data['system_call_overhead']
                    single_index_score = data['index_score']
                if data['thread'] == '多线程':
                    # 多线程数据
                    multi_Dhrystone = data['Dhrystone']
                    multi_Double_Precision = data['Double_Precision']
                    multi_execl_throughput = data['execl_throughput']
                    multi_file_copy_1024 = data['file_copy_1024']
                    multi_file_copy_256 = data['file_copy_256']
                    multi_file_copy_4096 = data['file_copy_4096']
                    multi_pipe_throughput = data['pipe_throughput']
                    multi_pipe_based = data['pipe_based']
                    multi_process_creation = data['process_creation']
                    multi_shell_scripts_1 = data['shell_scripts_1']
                    multi_shell_scripts_8 = data['shell_scripts_8']
                    multi_system_call_overhead = data['system_call_overhead']
                    multi_index_score = data['index_score']
            datas[3]['column' + str(column_index)] = single_Dhrystone
            datas[4]['column' + str(column_index)] = single_Double_Precision
            datas[5]['column' + str(column_index)] = single_execl_throughput
            datas[6]['column' + str(column_index)] = single_file_copy_1024
            datas[7]['column' + str(column_index)] = single_file_copy_256
            datas[8]['column' + str(column_index)] = single_file_copy_4096
            datas[9]['column' + str(column_index)] = single_pipe_throughput
            datas[10]['column' + str(column_index)] = single_pipe_based
            datas[11]['column' + str(column_index)] = single_process_creation
            datas[12]['column' + str(column_index)] = single_shell_scripts_1
            datas[13]['column' + str(column_index)] = single_shell_scripts_8
            datas[14]['column' + str(column_index)] = single_system_call_overhead
            datas[15]['column' + str(column_index)] = single_index_score
            datas[16]['column' + str(column_index)] = multi_Dhrystone
            datas[17]['column' + str(column_index)] = multi_Double_Precision
            datas[18]['column' + str(column_index)] = multi_execl_throughput
            datas[19]['column' + str(column_index)] = multi_file_copy_1024
            datas[20]['column' + str(column_index)] = multi_file_copy_256
            datas[21]['column' + str(column_index)] = multi_file_copy_4096
            datas[22]['column' + str(column_index)] = multi_pipe_throughput
            datas[23]['column' + str(column_index)] = multi_pipe_based
            datas[24]['column' + str(column_index)] = multi_process_creation
            datas[25]['column' + str(column_index)] = multi_shell_scripts_1
            datas[26]['column' + str(column_index)] = multi_shell_scripts_8
            datas[27]['column' + str(column_index)] = multi_system_call_overhead
            datas[28]['column' + str(column_index)] = multi_index_score
            column_index += 1
            title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = single_Dhrystone
            datas[4]['column' + str(column_index)] = single_Double_Precision
            datas[5]['column' + str(column_index)] = single_execl_throughput
            datas[6]['column' + str(column_index)] = single_file_copy_1024
            datas[7]['column' + str(column_index)] = single_file_copy_256
            datas[8]['column' + str(column_index)] = single_file_copy_4096
            datas[9]['column' + str(column_index)] = single_pipe_throughput
            datas[10]['column' + str(column_index)] = single_pipe_based
            datas[11]['column' + str(column_index)] = single_process_creation
            datas[12]['column' + str(column_index)] = single_shell_scripts_1
            datas[13]['column' + str(column_index)] = single_shell_scripts_8
            datas[14]['column' + str(column_index)] = single_system_call_overhead
            datas[15]['column' + str(column_index)] = single_index_score
            datas[16]['column' + str(column_index)] = multi_Dhrystone
            datas[17]['column' + str(column_index)] = multi_Double_Precision
            datas[18]['column' + str(column_index)] = multi_execl_throughput
            datas[19]['column' + str(column_index)] = multi_file_copy_1024
            datas[20]['column' + str(column_index)] = multi_file_copy_256
            datas[21]['column' + str(column_index)] = multi_file_copy_4096
            datas[22]['column' + str(column_index)] = multi_pipe_throughput
            datas[23]['column' + str(column_index)] = multi_pipe_based
            datas[24]['column' + str(column_index)] = multi_process_creation
            datas[25]['column' + str(column_index)] = multi_shell_scripts_1
            datas[26]['column' + str(column_index)] = multi_shell_scripts_8
            datas[27]['column' + str(column_index)] = multi_system_call_overhead
            datas[28]['column' + str(column_index)] = multi_index_score
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(29):
                    if i > 2:
                        datas[i]['column' + str(column_index)] = \
                            "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i]['column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if datas[i]['column' + str(column_index - 1)] is not None and datas[i]['column' + str(base_column_index)] is not None else None
                column_index += 1
        else:
            # 数据分组
            single_data_ = serializer_.filter(thread='单线程')
            multi_data_ = serializer_.filter(thread='多线程')
            # 计算平均值
            single_Dhrystone_list = [d.Dhrystone for d in single_data_ if d.Dhrystone is not None]
            single_Double_Precision_list = [d.Double_Precision for d in single_data_ if d.Double_Precision is not None]
            single_execl_throughput_list = [d.execl_throughput for d in single_data_ if d.execl_throughput is not None]
            single_file_copy_1024_list = [d.file_copy_1024 for d in single_data_ if d.file_copy_1024 is not None]
            single_file_copy_256_list = [d.file_copy_256 for d in single_data_ if d.file_copy_256 is not None]
            single_file_copy_4096_list = [d.file_copy_4096 for d in single_data_ if d.file_copy_4096 is not None]
            single_pipe_throughput_list = [d.pipe_throughput for d in single_data_ if d.pipe_throughput is not None]
            single_pipe_based_list = [d.pipe_based for d in single_data_ if d.pipe_based is not None]
            single_process_creation_list = [d.process_creation for d in single_data_ if d.process_creation is not None]
            single_shell_scripts_1_list = [d.shell_scripts_1 for d in single_data_ if d.shell_scripts_1 is not None]
            single_shell_scripts_8_list = [d.shell_scripts_8 for d in single_data_ if d.shell_scripts_8 is not None]
            single_system_call_overhead_list = [d.system_call_overhead for d in single_data_ if d.system_call_overhead is not None]
            single_index_score_list = [d.index_score for d in single_data_ if d.index_score is not None]
            # 计算每个数组的平均值
            average_single_Dhrystone = np.mean(single_Dhrystone_list).round(2) if not np.isnan(np.mean(single_Dhrystone_list)) else None
            average_single_Double_Precision = np.mean(single_Double_Precision_list).round(2) if not np.isnan(np.mean(single_Double_Precision_list)) else None
            average_single_execl_throughput = np.mean(single_execl_throughput_list).round(2) if not np.isnan(np.mean(single_execl_throughput_list)) else None
            average_single_file_copy_1024 = np.mean(single_file_copy_1024_list).round(2) if not np.isnan(np.mean(single_file_copy_1024_list)) else None
            average_single_file_copy_256 = np.mean(single_file_copy_256_list).round(2) if not np.isnan(np.mean(single_file_copy_256_list)) else None
            average_single_file_copy_4096 = np.mean(single_file_copy_4096_list).round(2) if not np.isnan(np.mean(single_file_copy_4096_list)) else None
            average_single_pipe_throughput = np.mean(single_pipe_throughput_list).round(2) if not np.isnan(np.mean(single_pipe_throughput_list)) else None
            average_single_pipe_based = np.mean(single_pipe_based_list).round(2) if not np.isnan(np.mean(single_pipe_based_list)) else None
            average_single_process_creation = np.mean(single_process_creation_list).round(2) if not np.isnan(np.mean(single_process_creation_list)) else None
            average_single_shell_scripts_1 = np.mean(single_shell_scripts_1_list).round(2) if not np.isnan(np.mean(single_shell_scripts_1_list)) else None
            average_single_shell_scripts_8 = np.mean(single_shell_scripts_8_list).round(2) if not np.isnan(np.mean(single_shell_scripts_8_list)) else None
            average_single_system_call_overhead = np.mean(single_system_call_overhead_list).round(2) if not np.isnan(np.mean(single_system_call_overhead_list)) else None
            average_single_index_score = np.mean(single_index_score_list).round(2) if not np.isnan(np.mean(single_index_score_list)) else None

            # 多线程数据
            multi_Dhrystone_list = [d.Dhrystone for d in multi_data_ if d.Dhrystone is not None]
            multi_Double_Precision_list = [d.Double_Precision for d in multi_data_ if d.Double_Precision is not None]
            multi_execl_throughput_list = [d.execl_throughput for d in multi_data_ if d.execl_throughput is not None]
            multi_file_copy_1024_list = [d.file_copy_1024 for d in multi_data_ if d.file_copy_1024 is not None]
            multi_file_copy_256_list = [d.file_copy_256 for d in multi_data_ if d.file_copy_256 is not None]
            multi_file_copy_4096_list = [d.file_copy_4096 for d in multi_data_ if d.file_copy_4096 is not None]
            multi_pipe_throughput_list = [d.pipe_throughput for d in multi_data_ if d.pipe_throughput is not None]
            multi_pipe_based_list = [d.pipe_based for d in multi_data_ if d.pipe_based is not None]
            multi_process_creation_list = [d.process_creation for d in multi_data_ if d.process_creation is not None]
            multi_shell_scripts_1_list = [d.shell_scripts_1 for d in multi_data_ if d.shell_scripts_1 is not None]
            multi_shell_scripts_8_list = [d.shell_scripts_8 for d in multi_data_ if d.shell_scripts_8 is not None]
            multi_system_call_overhead_list = [d.system_call_overhead for d in multi_data_ if d.system_call_overhead is not None]
            multi_index_score_list = [d.index_score for d in multi_data_ if d.index_score is not None]
            # 计算每个数组的平均值
            average_multi_Dhrystone = np.mean(multi_Dhrystone_list).round(2) if not np.isnan(np.mean(multi_Dhrystone_list)) else None
            average_multi_Double_Precision = np.mean(multi_Double_Precision_list).round(2) if not np.isnan(np.mean(multi_Double_Precision_list)) else None
            average_multi_execl_throughput = np.mean(multi_execl_throughput_list).round(2) if not np.isnan(np.mean(multi_execl_throughput_list)) else None
            average_multi_file_copy_1024 = np.mean(multi_file_copy_1024_list).round(2) if not np.isnan(np.mean(multi_file_copy_1024_list)) else None
            average_multi_file_copy_256 = np.mean(multi_file_copy_256_list).round(2) if not np.isnan(np.mean(multi_file_copy_256_list)) else None
            average_multi_file_copy_4096 = np.mean(multi_file_copy_4096_list).round(2) if not np.isnan(np.mean(multi_file_copy_4096_list)) else None
            average_multi_pipe_throughput = np.mean(multi_pipe_throughput_list).round(2) if not np.isnan(np.mean(multi_pipe_throughput_list)) else None
            average_multi_pipe_based = np.mean(multi_pipe_based_list).round(2) if not np.isnan(np.mean(multi_pipe_based_list)) else None
            average_multi_process_creation = np.mean(multi_process_creation_list).round(2) if not np.isnan(np.mean(multi_process_creation_list)) else None
            average_multi_shell_scripts_1 = np.mean(multi_shell_scripts_1_list).round(2) if not np.isnan(np.mean(multi_shell_scripts_1_list)) else None
            average_multi_shell_scripts_8 = np.mean(multi_shell_scripts_8_list).round(2) if not np.isnan(np.mean(multi_shell_scripts_8_list)) else None
            average_multi_system_call_overhead = np.mean(multi_system_call_overhead_list).round(2) if not np.isnan(np.mean(multi_system_call_overhead_list)) else None
            average_multi_index_score = np.mean(multi_index_score_list).round(2) if not np.isnan(np.mean(multi_index_score_list)) else None

            # 查到mark-name相同的数据拼接为一组：serializer.data
            for mark_name in groups:
                temp_datas = serializer_.filter(mark_name=mark_name)
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'Unixbench#' + str(title_index)
                datas[1]['column' + str(column_index)] = temp_datas[0].execute_cmd
                datas[2]['column' + str(column_index)] = temp_datas[0].modify_parameters
                # 初始化所有数据为None
                for i in range(3, 29):
                    datas[i]['column' + str(column_index)] = None
                for data in temp_datas:
                    if data.thread == '单线程':
                        # 单线程数据
                        single_Dhrystone = data.Dhrystone
                        single_Double_Precision = data.Double_Precision
                        single_execl_throughput = data.execl_throughput
                        single_file_copy_1024 = data.file_copy_1024
                        single_file_copy_256 = data.file_copy_256
                        single_file_copy_4096 = data.file_copy_4096
                        single_pipe_throughput = data.pipe_throughput
                        single_pipe_based = data.pipe_based
                        single_process_creation = data.process_creation
                        single_shell_scripts_1 = data.shell_scripts_1
                        single_shell_scripts_8 = data.shell_scripts_8
                        single_system_call_overhead = data.system_call_overhead
                        single_index_score = data.index_score
                    if data.thread == '多线程':
                        # 多线程数据
                        multi_Dhrystone = data.Dhrystone
                        multi_Double_Precision = data.Double_Precision
                        multi_execl_throughput = data.execl_throughput
                        multi_file_copy_1024 = data.file_copy_1024
                        multi_file_copy_256 = data.file_copy_256
                        multi_file_copy_4096 = data.file_copy_4096
                        multi_pipe_throughput = data.pipe_throughput
                        multi_pipe_based = data.pipe_based
                        multi_process_creation = data.process_creation
                        multi_shell_scripts_1 = data.shell_scripts_1
                        multi_shell_scripts_8 = data.shell_scripts_8
                        multi_system_call_overhead = data.system_call_overhead
                        multi_index_score = data.index_score
                datas[3]['column' + str(column_index)] = single_Dhrystone
                datas[4]['column' + str(column_index)] = single_Double_Precision
                datas[5]['column' + str(column_index)] = single_execl_throughput
                datas[6]['column' + str(column_index)] = single_file_copy_1024
                datas[7]['column' + str(column_index)] = single_file_copy_256
                datas[8]['column' + str(column_index)] = single_file_copy_4096
                datas[9]['column' + str(column_index)] = single_pipe_throughput
                datas[10]['column' + str(column_index)] = single_pipe_based
                datas[11]['column' + str(column_index)] = single_process_creation
                datas[12]['column' + str(column_index)] = single_shell_scripts_1
                datas[13]['column' + str(column_index)] = single_shell_scripts_8
                datas[14]['column' + str(column_index)] = single_system_call_overhead
                datas[15]['column' + str(column_index)] = single_index_score
                datas[16]['column' + str(column_index)] = multi_Dhrystone
                datas[17]['column' + str(column_index)] = multi_Double_Precision
                datas[18]['column' + str(column_index)] = multi_execl_throughput
                datas[19]['column' + str(column_index)] = multi_file_copy_1024
                datas[20]['column' + str(column_index)] = multi_file_copy_256
                datas[21]['column' + str(column_index)] = multi_file_copy_4096
                datas[22]['column' + str(column_index)] = multi_pipe_throughput
                datas[23]['column' + str(column_index)] = multi_pipe_based
                datas[24]['column' + str(column_index)] = multi_process_creation
                datas[25]['column' + str(column_index)] = multi_shell_scripts_1
                datas[26]['column' + str(column_index)] = multi_shell_scripts_8
                datas[27]['column' + str(column_index)] = multi_system_call_overhead
                datas[28]['column' + str(column_index)] = multi_index_score
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = average_single_Dhrystone
            datas[4]['column' + str(column_index)] = average_single_Double_Precision
            datas[5]['column' + str(column_index)] = average_single_execl_throughput
            datas[6]['column' + str(column_index)] = average_single_file_copy_1024
            datas[7]['column' + str(column_index)] = average_single_file_copy_256
            datas[8]['column' + str(column_index)] = average_single_file_copy_4096
            datas[9]['column' + str(column_index)] = average_single_pipe_throughput
            datas[10]['column' + str(column_index)] = average_single_pipe_based
            datas[11]['column' + str(column_index)] = average_single_process_creation
            datas[12]['column' + str(column_index)] = average_single_shell_scripts_1
            datas[13]['column' + str(column_index)] = average_single_shell_scripts_8
            datas[14]['column' + str(column_index)] = average_single_system_call_overhead
            datas[15]['column' + str(column_index)] = average_single_index_score
            datas[16]['column' + str(column_index)] = average_multi_Dhrystone
            datas[17]['column' + str(column_index)] = average_multi_Double_Precision
            datas[18]['column' + str(column_index)] = average_multi_execl_throughput
            datas[19]['column' + str(column_index)] = average_multi_file_copy_1024
            datas[20]['column' + str(column_index)] = average_multi_file_copy_256
            datas[21]['column' + str(column_index)] = average_multi_file_copy_4096
            datas[22]['column' + str(column_index)] = average_multi_pipe_throughput
            datas[23]['column' + str(column_index)] = average_multi_pipe_based
            datas[24]['column' + str(column_index)] = average_multi_process_creation
            datas[25]['column' + str(column_index)] = average_multi_shell_scripts_1
            datas[26]['column' + str(column_index)] = average_multi_shell_scripts_8
            datas[27]['column' + str(column_index)] = average_multi_system_call_overhead
            datas[28]['column' + str(column_index)] = average_multi_index_score
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(29):
                    if i > 2:
                        datas[i]['column' + str(column_index)] = \
                            "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i]['column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if datas[i]['column' + str(column_index - 1)] is not None and datas[i]['column' + str(base_column_index)] is not None else None
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
        base_queryset = Unixbench.objects.filter(env_id=env_id).all()
        if not base_queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        datas = [
            {'column1': 'Unxibench', 'column2': ''},
            {'column1': '执行命令', 'column2': ''},
            {'column1': '修改参数', 'column2': ''},
            {'column1': '单线程', 'column2': 'Dhrystone 2 using register variables(lps)'},
            {'column1': '单线程', 'column2': 'Double-Precision Whetstone(MWIPS)'},
            {'column1': '单线程', 'column2': 'Execl Throughput(lps)'},
            {'column1': '单线程', 'column2': 'File Copy 1024 bufsize 2000 maxblocks(KBps)'},
            {'column1': '单线程', 'column2': 'File Copy 256 bufsize 500 maxblocks(KBps)'},
            {'column1': '单线程', 'column2': 'File Copy 4096 bufsize 8000 maxblocks(KBps)'},
            {'column1': '单线程', 'column2': 'Pipe Throughput(lps)'},
            {'column1': '单线程', 'column2': 'Pipe-based Context Switching(lps)'},
            {'column1': '单线程', 'column2': 'Process Creation(lps)'},
            {'column1': '单线程', 'column2': 'Shell Scripts (1 concurrent)(lpm)'},
            {'column1': '单线程', 'column2': 'Shell Scripts (8 concurrent)(lpm)'},
            {'column1': '单线程', 'column2': 'System Call Overhead(lps)'},
            {'column1': '单线程', 'column2': 'Index Score(sum)'},
            {'column1': '多线程', 'column2': 'Dhrystone 2 using register variables(lps)'},
            {'column1': '多线程', 'column2': 'Double-Precision Whetstone(MWIPS)'},
            {'column1': '多线程', 'column2': 'Execl Throughput(lps)'},
            {'column1': '多线程', 'column2': 'File Copy 1024 bufsize 2000 maxblocks(KBps)'},
            {'column1': '多线程', 'column2': 'File Copy 256 bufsize 500 maxblocks(KBps)'},
            {'column1': '多线程', 'column2': 'File Copy 4096 bufsize 8000 maxblocks(KBps)'},
            {'column1': '多线程', 'column2': 'Pipe Throughput(lps)'},
            {'column1': '多线程', 'column2': 'Pipe-based Context Switching(lps)'},
            {'column1': '多线程', 'column2': 'Process Creation(lps)'},
            {'column1': '多线程', 'column2': 'Shell Scripts (1 concurrent)(lpm)'},
            {'column1': '多线程', 'column2': 'Shell Scripts (8 concurrent)(lpm)'},
            {'column1': '多线程', 'column2': 'System Call Overhead(lps)'},
            {'column1': '多线程', 'column2': 'Index Score(sum)'},
        ]
        title_index = 1
        column_index = 3
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)

        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Unixbench.objects.filter(env_id=comparativeId).all()
                if not comparsion_queryset:
                    return json_response({}, status.HTTP_200_OK, '列表')
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index,
                                                                                    column_index, base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_unixbench_errors = []
        error_message = []
        data_unixbench = {}
        for k, unixbench_json in request.__dict__['data_unixbench'].items():
            if k.lower().startswith('unixbench'):
                constants.UNIXBENCH_BOOL = True
                data_unixbench['env_id'] = request.__dict__['data_unixbench']['env_id']
                thread = ""
                if k.split('-')[-3] == 'single':
                    thread = "单线程"
                elif k.split('-')[-3] == 'multi':
                    thread = "多线程"
                # todo 所有的参数 、 cmd 是在哪里保存的
                data_unixbench['thread'] = thread
                data_unixbench['execute_cmd'] = 'xx'
                data_unixbench['modify_parameters'] = '参数'
                data_unixbench['mark_name'] = k[-3:]
                data_unixbench['Dhrystone'] = unixbench_json[thread]['Dhrystone 2 using register variables(lps)']
                data_unixbench['Double_Precision'] = unixbench_json[thread]['Double-Precision Whetstone(MWIPS)']
                data_unixbench['execl_throughput'] = unixbench_json[thread]['Execl Throughput(lps)']
                data_unixbench['file_copy_1024'] = unixbench_json[thread]['File Copy 1024 bufsize 2000 maxblocks(KBps)']
                data_unixbench['file_copy_256'] = unixbench_json[thread]['File Copy 256 bufsize 500 maxblocks(KBps)']
                data_unixbench['file_copy_4096'] = unixbench_json[thread]['File Copy 4096 bufsize 8000 maxblocks(KBps)']
                data_unixbench['pipe_throughput'] = unixbench_json[thread]['Pipe Throughput(lps)']
                data_unixbench['pipe_based'] = unixbench_json[thread]['Pipe-based Context Switching(lps)']
                data_unixbench['process_creation'] = unixbench_json[thread]['Process Creation(lps)']
                data_unixbench['shell_scripts_1'] = unixbench_json[thread]['Shell Scripts (1 concurrent)(lpm)']
                data_unixbench['shell_scripts_8'] = unixbench_json[thread]['Shell Scripts (8 concurrent)(lpm)']
                data_unixbench['system_call_overhead'] = unixbench_json[thread]['System Call Overhead(lps)']
                data_unixbench['index_score'] = unixbench_json[thread]['Index Score(sum)']
                data_unixbench = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                                  data_unixbench.items()}
                serializer_unixbench = UnixbenchSerializer(data=data_unixbench)
                if serializer_unixbench.is_valid():
                    self.perform_create(serializer_unixbench)
                else:
                    serializer_unixbench_errors.append(serializer_unixbench.errors)
                    error_message.append(get_error_message(serializer_unixbench))
        if serializer_unixbench_errors:
            print(serializer_unixbench_errors, "unixbench")
            return json_response(serializer_unixbench_errors, status.HTTP_400_BAD_REQUEST, error_message)
        else:
            return
