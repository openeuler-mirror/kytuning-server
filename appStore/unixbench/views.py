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
        serializer_unixbench_errors = []
        error_message = []
        data_unixbench = {}
        for k, unixbench_json in request.__dict__['data_unixbench'].items():
            if k.lower().startswith('unixbench'):
                data_unixbench['env_id'] = request.__dict__['data_unixbench']['env_id']
                thread = "多线程"
                if k.split('-')[-3] == 'single':
                    thread = "单线程"
                # todo 所有的参数 、 cmd 是在哪里保存的
                data_unixbench['thread'] = thread
                data_unixbench['execute_cmd'] = 'xx'
                data_unixbench['modify_parameters'] = '参数'
                print(unixbench_json,111)
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
                data_unixbench['test_time'] = return_time(unixbench_json['time'])
                serializer_unixbench = UnixbenchSerializer(data=data_unixbench)
                if serializer_unixbench.is_valid():
                    pass
                    # todo 放开
                    # self.perform_create(serializer_unixbench)
                serializer_unixbench_errors.append(serializer_unixbench.errors)
                error_message.append(get_error_message(serializer_unixbench))
        return json_response(serializer_unixbench_errors, status.HTTP_400_BAD_REQUEST, error_message)
