# Create your views here.
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

    # pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        """
        返回列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        env_id = request.GET.get('env_id')
        queryset = Unixbench.objects.filter(env_id=env_id).all()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '列表')

    def get_data(self, serializer):
        # 初始化数据为空 否则如果下面只获取的单线程或者多线程另外一组获取不到可能会报错
        single_Dhrystone = ''
        single_Double_Precision = ''
        single_execl_throughput = ''
        single_file_copy_1024 = ''
        single_file_copy_256 = ''
        single_file_copy_4096 = ''
        single_pipe_throughput = ''
        single_pipe_based = ''
        single_process_creation = ''
        single_shell_scripts_1 = ''
        single_shell_scripts_8 = ''
        single_system_call_overhead = ''
        single_index_score = ''
        multi_Dhrystone = ''
        multi_Double_Precision = ''
        multi_execl_throughput = ''
        multi_file_copy_1024 = ''
        multi_file_copy_256 = ''
        multi_file_copy_4096 = ''
        multi_pipe_throughput = ''
        multi_pipe_based = ''
        multi_process_creation = ''
        multi_shell_scripts_1 = ''
        multi_shell_scripts_8 = ''
        multi_system_call_overhead = ''
        multi_index_score = ''
        execute_cmd = serializer.data[0]['execute_cmd']
        modify_parameters = serializer.data[0]['modify_parameters']
        for data in serializer.data:
            if data['thread'] == '单线程':
                # 查询基准数据的单线程数据]
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
                # 查询基准数据的多线程数据
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
        new_data = {'single_Dhrystone': single_Dhrystone,
                'single_Double_Precision': single_Double_Precision,
                'single_execl_throughput': single_execl_throughput,
                'single_file_copy_1024': single_file_copy_1024,
                'single_file_copy_256': single_file_copy_256,
                'single_file_copy_4096': single_file_copy_4096,
                'single_pipe_throughput': single_pipe_throughput,
                'single_pipe_based': single_pipe_based,
                'single_process_creation': single_process_creation,
                'single_shell_scripts_1': single_shell_scripts_1,
                'single_shell_scripts_8': single_shell_scripts_8,
                'single_system_call_overhead': single_system_call_overhead,
                'single_index_score': single_index_score,
                'multi_Dhrystone': multi_Dhrystone,
                'multi_Double_Precision': multi_Double_Precision,
                'multi_execl_throughput': multi_execl_throughput,
                'multi_file_copy_1024': multi_file_copy_1024,
                'multi_file_copy_256': multi_file_copy_256,
                'multi_file_copy_4096': multi_file_copy_4096,
                'multi_pipe_throughput': multi_pipe_throughput,
                'multi_pipe_based': multi_pipe_based,
                'multi_process_creation': multi_process_creation,
                'multi_shell_scripts_1': multi_shell_scripts_1,
                'multi_shell_scripts_8': multi_shell_scripts_8,
                'multi_system_call_overhead': multi_system_call_overhead,
                'multi_index_score': multi_index_score,
                'execute_cmd': execute_cmd,
                'modify_parameters': modify_parameters}
        return new_data


    def create(self, request, *args, **kwargs):
        serializer_unixbench_errors = []
        error_message = []
        data_unixbench = {}
        for k, unixbench_json in request.__dict__['data_unixbench'].items():
            if k.lower().startswith('unixbench'):
                constants.UNIXBENCH_BOOL = True
                data_unixbench['env_id'] = request.__dict__['data_unixbench']['env_id']
                thread = "多线程"
                if k.split('-')[-3] == 'single':
                    thread = "单线程"
                # todo 所有的参数 、 cmd 是在哪里保存的
                data_unixbench['thread'] = thread
                data_unixbench['execute_cmd'] = 'xx'
                data_unixbench['modify_parameters'] = '参数'
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
                    # self.perform_create(serializer_unixbench)
                    pass
                serializer_unixbench_errors.append(serializer_unixbench.errors)
                error_message.append(get_error_message(serializer_unixbench))
        return json_response(serializer_unixbench_errors, status.HTTP_400_BAD_REQUEST, error_message)
