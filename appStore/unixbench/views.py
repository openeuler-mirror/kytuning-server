# Create your views here.
from rest_framework import status
from appStore.unixbench.serializers import UnixbenchSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class UnixbenchViewSet(CusModelViewSet):
    """
    Unixbench数据管理
    """

    # queryset = Stream.objects.all().order_by('id')
    serializer_class = UnixbenchSerializer

    # pagination_class = LimsPageSet

    def create(self, request, *args, **kwargs):
        data_unixbench = {}
        for k, unixbench_json in request.__dict__['data_unixbench'].items():
            if k.lower().startswith('unixbench'):
                data_unixbench['env_id'] = request.__dict__['data_unixbench']['env_id']
                if k.split('-')[-3] == 'single':
                    # todo 所有的参数 、 cmd 是在哪里保存的
                    data_unixbench['single_thread'] = '单线程'
                    data_unixbench['single_execute_cmd'] = 'xx'
                    data_unixbench['single_modify_parameters'] = '参数'
                    data_unixbench['single_Dhrystone'] = unixbench_json['单线程']['Dhrystone 2 using register variables(lps)']
                    data_unixbench['single_Double_Precision'] = unixbench_json['单线程']['Double-Precision Whetstone(MWIPS)']
                    data_unixbench['single_execl_throughput'] = unixbench_json['单线程']['Execl Throughput(lps)']
                    data_unixbench['single_file_copy_1024'] = unixbench_json['单线程']['File Copy 1024 bufsize 2000 maxblocks(KBps)']
                    data_unixbench['single_file_copy_256'] = unixbench_json['单线程']['File Copy 256 bufsize 500 maxblocks(KBps)']
                    data_unixbench['single_file_copy_4096'] = unixbench_json['单线程']['File Copy 4096 bufsize 8000 maxblocks(KBps)']
                    data_unixbench['single_pipe_throughput'] = unixbench_json['单线程']['Pipe Throughput(lps)']
                    data_unixbench['single_pipe_based'] = unixbench_json['单线程']['Pipe-based Context Switching(lps)']
                    data_unixbench['single_process_creation'] = unixbench_json['单线程']['Process Creation(lps)']
                    data_unixbench['single_shell_scripts_1'] = unixbench_json['单线程']['Shell Scripts (1 concurrent)(lpm)']
                    data_unixbench['single_shell_scripts_8'] = unixbench_json['单线程']['Shell Scripts (8 concurrent)(lpm)']
                    data_unixbench['single_system_call_overhead'] = unixbench_json['单线程']['System Call Overhead(lps)']
                    data_unixbench['single_index_score'] = unixbench_json['单线程']['Index Score(sum)']
                    data_unixbench['single_test_time'] = return_time(unixbench_json['time'])
                elif  k.split('-')[-3] == 'multi':
                    data_unixbench['multi_thread'] = '多线程'
                    data_unixbench['multi_execute_cmd'] = 'xx'
                    data_unixbench['multi_modify_parameters'] = '参数'
                    data_unixbench['multi_Dhrystone'] = unixbench_json['多线程']['Dhrystone 2 using register variables(lps)']
                    data_unixbench['multi_Double_Precision'] = unixbench_json['多线程']['Double-Precision Whetstone(MWIPS)']
                    data_unixbench['multi_execl_throughput'] = unixbench_json['多线程']['Execl Throughput(lps)']
                    data_unixbench['multi_file_copy_1024'] = unixbench_json['多线程']['File Copy 1024 bufsize 2000 maxblocks(KBps)']
                    data_unixbench['multi_file_copy_256'] = unixbench_json['多线程']['File Copy 256 bufsize 500 maxblocks(KBps)']
                    data_unixbench['multi_file_copy_4096'] = unixbench_json['多线程']['File Copy 4096 bufsize 8000 maxblocks(KBps)']
                    data_unixbench['multi_pipe_throughput'] = unixbench_json['多线程']['Pipe Throughput(lps)']
                    data_unixbench['multi_pipe_based'] = unixbench_json['多线程']['Pipe-based Context Switching(lps)']
                    data_unixbench['multi_process_creation'] = unixbench_json['多线程']['Process Creation(lps)']
                    data_unixbench['multi_shell_scripts_1'] = unixbench_json['多线程']['Shell Scripts (1 concurrent)(lpm)']
                    data_unixbench['multi_shell_scripts_8'] = unixbench_json['多线程']['Shell Scripts (8 concurrent)(lpm)']
                    data_unixbench['multi_system_call_overhead'] = unixbench_json['多线程']['System Call Overhead(lps)']
                    data_unixbench['multi_index_score'] = unixbench_json['多线程']['Index Score(sum)']
                    data_unixbench['multi_test_time'] = return_time(unixbench_json['time'])
        serializer_unixbench = UnixbenchSerializer(data=data_unixbench)
        if serializer_unixbench.is_valid():
            pass
            # todo 放开
            # self.perform_create(serializer_unixbench)
        return json_response(serializer_unixbench.errors, status.HTTP_400_BAD_REQUEST,
                             get_error_message(serializer_unixbench))
