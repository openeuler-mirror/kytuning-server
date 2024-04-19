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

    # def list(self, request, *args, **kwargs):
    #     """
    #     返回列表
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     env_id = request.GET.get('env_id')
    #     queryset = Unixbench.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return json_response(serializer.data, status.HTTP_200_OK, '列表')

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
        data = self.get_data(base_queryset)
        others = [{'column1':'Unxibench','column2':'', 'column3':'Unixbench#1'},{'column1': '执行命令','column2':'', 'column3': data['execute_cmd']}, {'column1': '修改参数：', 'column2':'', 'column3':data['modify_parameters']}]
        datas = [
            {'column1': '单线程', 'column2': 'Dhrystone 2 using register variables(lps)', 'column3': data['single_Dhrystone']},
            {'column1': '单线程', 'column2': 'Double-Precision Whetstone(MWIPS)', 'column3': data['single_Double_Precision']},
            {'column1': '单线程', 'column2': 'Execl Throughput(lps)', 'column3': data['single_execl_throughput']},
            {'column1': '单线程', 'column2': 'File Copy 1024 bufsize 2000 maxblocks(KBps)', 'column3': data['single_file_copy_1024']},
            {'column1': '单线程', 'column2': 'File Copy 256 bufsize 500 maxblocks(KBps)', 'column3': data['single_file_copy_256']},
            {'column1': '单线程', 'column2': 'File Copy 4096 bufsize 8000 maxblocks(KBps)', 'column3': data['single_file_copy_4096']},
            {'column1': '单线程', 'column2': 'Pipe Throughput(lps)', 'column3': data['single_pipe_throughput']},
            {'column1': '单线程', 'column2': 'Pipe-based Context Switching(lps)', 'column3': data['single_pipe_based']},
            {'column1': '单线程', 'column2': 'Process Creation(lps)', 'column3': data['single_process_creation']},
            {'column1': '单线程', 'column2': 'Shell Scripts (1 concurrent)(lpm)', 'column3': data['single_shell_scripts_1']},
            {'column1': '单线程', 'column2': 'Shell Scripts (8 concurrent)(lpm)', 'column3': data['single_shell_scripts_8']},
            {'column1': '单线程', 'column2': 'System Call Overhead(lps)', 'column3': data['single_system_call_overhead']},
            {'column1': '单线程', 'column2': 'Index Score(sum)', 'column3': data['single_index_score']},
            {'column1': '多线程', 'column2': 'Dhrystone 2 using register variables(lps)', 'column3': data['multi_Dhrystone']},
            {'column1': '多线程', 'column2': 'Double-Precision Whetstone(MWIPS)', 'column3': data['multi_Double_Precision']},
            {'column1': '多线程', 'column2': 'Execl Throughput(lps)', 'column3': data['multi_execl_throughput']},
            {'column1': '多线程', 'column2': 'File Copy 1024 bufsize 2000 maxblocks(KBps)', 'column3': data['multi_file_copy_1024']},
            {'column1': '多线程', 'column2': 'File Copy 256 bufsize 500 maxblocks(KBps)', 'column3': data['multi_file_copy_256']},
            {'column1': '多线程', 'column2': 'File Copy 4096 bufsize 8000 maxblocks(KBps)', 'column3': data['multi_file_copy_4096']},
            {'column1': '多线程', 'column2': 'Pipe Throughput(lps)', 'column3': data['multi_pipe_throughput']},
            {'column1': '多线程', 'column2': 'Pipe-based Context Switching(lps)', 'column3': data['multi_pipe_based']},
            {'column1': '多线程', 'column2': 'Process Creation(lps)', 'column3': data['multi_process_creation']},
            {'column1': '多线程', 'column2': 'Shell Scripts (1 concurrent)(lpm)', 'column3': data['multi_shell_scripts_1']},
            {'column1': '多线程', 'column2': 'Shell Scripts (8 concurrent)(lpm)', 'column3': data['multi_shell_scripts_8']},
            {'column1': '多线程', 'column2': 'System Call Overhead(lps)', 'column3': data['multi_system_call_overhead']},
            {'column1': '多线程', 'column2': 'Index Score(sum)', 'column3': data['multi_index_score']},
        ]

        if comparsionIds != ['']:
            # 处理对比数据
            for index ,comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Unixbench.objects.filter(env_id=comparativeId).all()
                comparsion_data = self.get_data(comparsion_queryset)
                others[0]['column'+str(new_index)] = 'Unixbench#'+str(index + 2)
                others[1]['column'+str(new_index)] = comparsion_data['execute_cmd']
                others[2]['column'+str(new_index)] = comparsion_data['modify_parameters']
                others[0]['column'+str(new_index+1)] = ''
                others[1]['column'+str(new_index+1)] = ''
                others[2]['column'+str(new_index+1)] = ''

                datas[0]['column'+str(new_index)] = comparsion_data['single_Dhrystone']
                datas[1]['column'+str(new_index)] = comparsion_data['single_Double_Precision']
                datas[2]['column'+str(new_index)] = comparsion_data['single_execl_throughput']
                datas[3]['column'+str(new_index)] = comparsion_data['single_file_copy_1024']
                datas[4]['column'+str(new_index)] = comparsion_data['single_file_copy_256']
                datas[5]['column'+str(new_index)] = comparsion_data['single_file_copy_4096']
                datas[6]['column'+str(new_index)] = comparsion_data['single_pipe_throughput']
                datas[7]['column'+str(new_index)] = comparsion_data['single_pipe_based']
                datas[8]['column'+str(new_index)] = comparsion_data['single_process_creation']
                datas[9]['column'+str(new_index)] = comparsion_data['single_shell_scripts_1']
                datas[10]['column'+str(new_index)] = comparsion_data['single_shell_scripts_8']
                datas[11]['column'+str(new_index)] = comparsion_data['single_system_call_overhead']
                datas[12]['column'+str(new_index)] = comparsion_data['single_index_score']
                datas[13]['column'+str(new_index)] = comparsion_data['multi_Dhrystone']
                datas[14]['column'+str(new_index)] = comparsion_data['multi_Double_Precision']
                datas[15]['column'+str(new_index)] = comparsion_data['multi_execl_throughput']
                datas[16]['column'+str(new_index)] = comparsion_data['multi_file_copy_1024']
                datas[17]['column'+str(new_index)] = comparsion_data['multi_file_copy_256']
                datas[18]['column'+str(new_index)] = comparsion_data['multi_file_copy_4096']
                datas[19]['column'+str(new_index)] = comparsion_data['multi_pipe_throughput']
                datas[20]['column'+str(new_index)] = comparsion_data['multi_pipe_based']
                datas[21]['column'+str(new_index)] = comparsion_data['multi_process_creation']
                datas[22]['column'+str(new_index)] = comparsion_data['multi_shell_scripts_1']
                datas[23]['column'+str(new_index)] = comparsion_data['multi_shell_scripts_8']
                datas[24]['column'+str(new_index)] = comparsion_data['multi_system_call_overhead']
                datas[25]['column'+str(new_index)] = comparsion_data['multi_index_score']

                datas[0]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[0]['column'+str(new_index)] - datas[0]['column3'])/datas[0]['column3'] * 100)
                datas[1]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[1]['column'+str(new_index)] - datas[1]['column3'])/datas[1]['column3'] * 100)
                datas[2]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[2]['column'+str(new_index)] - datas[2]['column3'])/datas[2]['column3'] * 100)
                datas[3]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[3]['column'+str(new_index)] - datas[3]['column3'])/datas[3]['column3'] * 100)
                datas[4]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[4]['column'+str(new_index)] - datas[4]['column3'])/datas[4]['column3'] * 100)
                datas[5]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[5]['column'+str(new_index)] - datas[5]['column3'])/datas[5]['column3'] * 100)
                datas[6]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[6]['column'+str(new_index)] - datas[6]['column3'])/datas[6]['column3'] * 100)
                datas[7]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[7]['column'+str(new_index)] - datas[7]['column3'])/datas[7]['column3'] * 100)
                datas[8]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[8]['column'+str(new_index)] - datas[8]['column3'])/datas[8]['column3'] * 100)
                datas[9]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[9]['column'+str(new_index)] - datas[9]['column3'])/datas[9]['column3'] * 100)
                datas[10]['column'+str(new_index+1)] = "%.2f%%" % ((datas[10]['column'+str(new_index)] - datas[10]['column3'])/datas[10]['column3'] * 100)
                datas[11]['column'+str(new_index+1)] = "%.2f%%" % ((datas[11]['column'+str(new_index)] - datas[11]['column3'])/datas[11]['column3'] * 100)
                datas[12]['column'+str(new_index+1)] = "%.2f%%" % ((datas[12]['column'+str(new_index)] - datas[12]['column3'])/datas[12]['column3'] * 100)
                datas[13]['column'+str(new_index+1)] = "%.2f%%" % ((datas[13]['column'+str(new_index)] - datas[13]['column3'])/datas[13]['column3'] * 100)
                datas[14]['column'+str(new_index+1)] = "%.2f%%" % ((datas[14]['column'+str(new_index)] - datas[14]['column3'])/datas[14]['column3'] * 100)
                datas[15]['column'+str(new_index+1)] = "%.2f%%" % ((datas[15]['column'+str(new_index)] - datas[15]['column3'])/datas[15]['column3'] * 100)
                datas[16]['column'+str(new_index+1)] = "%.2f%%" % ((datas[16]['column'+str(new_index)] - datas[16]['column3'])/datas[16]['column3'] * 100)
                datas[17]['column'+str(new_index+1)] = "%.2f%%" % ((datas[17]['column'+str(new_index)] - datas[17]['column3'])/datas[17]['column3'] * 100)
                datas[18]['column'+str(new_index+1)] = "%.2f%%" % ((datas[18]['column'+str(new_index)] - datas[18]['column3'])/datas[18]['column3'] * 100)
                datas[19]['column'+str(new_index+1)] = "%.2f%%" % ((datas[19]['column'+str(new_index)] - datas[19]['column3'])/datas[19]['column3'] * 100)
                datas[20]['column'+str(new_index+1)] = "%.2f%%" % ((datas[20]['column'+str(new_index)] - datas[20]['column3'])/datas[20]['column3'] * 100)
                datas[21]['column'+str(new_index+1)] = "%.2f%%" % ((datas[21]['column'+str(new_index)] - datas[21]['column3'])/datas[21]['column3'] * 100)
                datas[22]['column'+str(new_index+1)] = "%.2f%%" % ((datas[22]['column'+str(new_index)] - datas[22]['column3'])/datas[22]['column3'] * 100)
                datas[23]['column'+str(new_index+1)] = "%.2f%%" % ((datas[23]['column'+str(new_index)] - datas[23]['column3'])/datas[23]['column3'] * 100)
                datas[24]['column'+str(new_index+1)] = "%.2f%%" % ((datas[24]['column'+str(new_index)] - datas[24]['column3'])/datas[24]['column3'] * 100)
                datas[25]['column'+str(new_index+1)] = "%.2f%%" % ((datas[25]['column'+str(new_index)] - datas[25]['column3'])/datas[25]['column3'] * 100)

        unixbench_data = {'others': others, 'data': datas}
        return json_response(unixbench_data, status.HTTP_200_OK, '列表')

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
                data_unixbench['mark_name'] = '-'.join(k.split('-')[-2:])
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
                    self.perform_create(serializer_unixbench)
                serializer_unixbench_errors.append(serializer_unixbench.errors)
                error_message.append(get_error_message(serializer_unixbench))
        return json_response(serializer_unixbench_errors, status.HTTP_400_BAD_REQUEST, error_message)
