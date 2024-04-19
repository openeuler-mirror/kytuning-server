import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.lmbench.models import Lmbench
from appStore.lmbench.serializers import LmbenchSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class LmbenchViewSet(CusModelViewSet):
    """
    Lmbench数据管理
    """
    queryset = Lmbench.objects.all().order_by('id')
    serializer_class = LmbenchSerializer

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
    #     queryset = Lmbench.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return json_response(serializer.data, status.HTTP_200_OK, '列表')

    def get_data(self, serializer):
        data = {'execute_cmd': serializer.data[0]['execute_cmd'],
                'modify_parameters': serializer.data[0]['modify_parameters'],
                'basic_Mhz': serializer.data[0]['basic_Mhz'],
                'basic_tlb_pages': serializer.data[0]['basic_tlb_pages'],
                'basic_cache_line_bytes': serializer.data[0]['basic_cache_line_bytes'],
                'basic_mem_par': serializer.data[0]['basic_mem_par'],
                'basic_scal_load': serializer.data[0]['basic_scal_load'],
                'processor_null_call': serializer.data[0]['processor_null_call'],
                'processor_null_I_O': serializer.data[0]['processor_null_I_O'],
                'processor_stat': serializer.data[0]['processor_stat'],
                'processor_open_clo': serializer.data[0]['processor_open_clo'],
                'processor_slct_TCP': serializer.data[0]['processor_slct_TCP'],
                'processor_sig_inst': serializer.data[0]['processor_sig_inst'],
                'processor_sig_hndl': serializer.data[0]['processor_sig_hndl'],
                'processor_fork_proc': serializer.data[0]['processor_fork_proc'],
                'processor_exec_proc': serializer.data[0]['processor_exec_proc'],
                'processor_sh_proc': serializer.data[0]['processor_sh_proc'],
                'processor_Mhz': serializer.data[0]['processor_Mhz'],
                'basic_intgr_bit': serializer.data[0]['basic_intgr_bit'],
                'basic_intgr_add': serializer.data[0]['basic_intgr_add'],
                'basic_intgr_mul': serializer.data[0]['basic_intgr_mul'],
                'basic_intgr_div': serializer.data[0]['basic_intgr_div'],
                'basic_intgr_mod': serializer.data[0]['basic_intgr_mod'],
                'basic_int64_bit': serializer.data[0]['basic_int64_bit'],
                'basic_int64_add': serializer.data[0]['basic_int64_add'],
                'basic_int64_mul': serializer.data[0]['basic_int64_mul'],
                'basic_int64_div': serializer.data[0]['basic_int64_div'],
                'basic_int64_mod': serializer.data[0]['basic_int64_mod'],
                'basic_float_add': serializer.data[0]['basic_float_add'],
                'basic_float_mul': serializer.data[0]['basic_float_mul'],
                'basic_float_div': serializer.data[0]['basic_float_div'],
                'basic_float_bogo': serializer.data[0]['basic_float_bogo'],
                'basic_double_add': serializer.data[0]['basic_double_add'],
                'basic_double_mul': serializer.data[0]['basic_double_mul'],
                'basic_double_div': serializer.data[0]['basic_double_div'],
                'basic_double_bogo': serializer.data[0]['basic_double_bogo'],
                'context_2p_0K': serializer.data[0]['context_2p_0K'],
                'context_2p_16K': serializer.data[0]['context_2p_16K'],
                'context_2p_64K': serializer.data[0]['context_2p_64K'],
                'context_8p_16K': serializer.data[0]['context_8p_16K'],
                'context_8p_64K': serializer.data[0]['context_8p_64K'],
                'context_16p_16K': serializer.data[0]['context_16p_16K'],
                'context_16p_64K': serializer.data[0]['context_16p_64K'],
                'local_2p_0K': serializer.data[0]['local_2p_0K'],
                'local_Pipe': serializer.data[0]['local_Pipe'],
                'local_AF_UNIX': serializer.data[0]['local_AF_UNIX'],
                'local_UDP': serializer.data[0]['local_UDP'],
                'local_TCP': serializer.data[0]['local_TCP'],
                'local_TCP_conn': serializer.data[0]['local_TCP_conn'],
                'local_RPC_TCP': serializer.data[0]['local_RPC_TCP'],
                'local_RPC_UDP': serializer.data[0]['local_RPC_UDP'],
                'local_bigger_Mmap_Latency': serializer.data[0]['local_bigger_Mmap_Latency'],
                'local_bigger_Prot_Fault': serializer.data[0]['local_bigger_Prot_Fault'],
                'local_bigger_Page_Fault': serializer.data[0]['local_bigger_Page_Fault'],
                'local_bigger_100fd_selct': serializer.data[0]['local_bigger_100fd_selct'],
                'local_bigger_0K_File_create': serializer.data[0]['local_bigger_0K_File_create'],
                'local_bigger_0K_File_delete': serializer.data[0]['local_bigger_0K_File_delete'],
                'local_bigger_10K_File_create': serializer.data[0]['local_bigger_10K_File_create'],
                'local_bigger_10K_File_delete': serializer.data[0]['local_bigger_10K_File_delete'],
                'local_bigger_Pipe': serializer.data[0]['local_bigger_Pipe'],
                'local_bigger_AF_UNIX': serializer.data[0]['local_bigger_AF_UNIX'],
                'local_bigger_TCP': serializer.data[0]['local_bigger_TCP'],
                'local_bigger_File_reread': serializer.data[0]['local_bigger_File_reread'],
                'local_bigger_Mmap_reread': serializer.data[0]['local_bigger_Mmap_reread'],
                'local_bigger_Bcopy_libc': serializer.data[0]['local_bigger_Bcopy_libc'],
                'local_bigger_Bcopy_hand': serializer.data[0]['local_bigger_Bcopy_hand'],
                'local_bigger_Mem_read': serializer.data[0]['local_bigger_Mem_read'],
                'local_bigger_Mem_write': serializer.data[0]['local_bigger_Mem_write'],
                'memory_Mhz': serializer.data[0]['memory_Mhz'],
                'memory_L1': serializer.data[0]['memory_L1'],
                'memory_L2': serializer.data[0]['memory_L2'],
                'memory_Main_mem': serializer.data[0]['memory_Main_mem'],
                'memory_Rand_mem': serializer.data[0]['memory_Rand_mem'],
                }
        return data

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
        base_queryset = Lmbench.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        # 判断数据超过两条，不显示
        if len(base_queryset) > 1:
            return json_response({}, status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, '数据存储有问题，存一条以上的数据了')
        data = self.get_data(base_serializer)
        others = [{'column1':'Lmbench','column2':'', 'column3':'Lmbench#1'},{'column1': '执行命令','column2':'', 'column3': data['execute_cmd']}, {'column1': '修改参数：', 'column2':'', 'column3':data['modify_parameters']}]
        datas = [
        {'column1':'Basic system parameters','column2':'Mhz','column3':data['basic_Mhz']},
        {'column1':'Basic system parameters','column2':'tlb pages','column3':data['basic_tlb_pages']},
        {'column1':'Basic system parameters','column2':'cache line bytes','column3':data['basic_cache_line_bytes']},
        {'column1':'Basic system parameters','column2':'mem par','column3':data['basic_mem_par']},
        {'column1':'Basic system parameters','column2':'scal load','column3':data['basic_scal_load']},
        {'column1':'Processor','column2':'Mhz','column3':data['processor_null_call']},
        {'column1':'Processor','column2':'null call','column3':data['processor_null_I_O']},
        {'column1':'Processor','column2':'null I/O','column3':data['processor_stat']},
        {'column1':'Processor','column2':'stat','column3':data['processor_open_clo']},
        {'column1':'Processor','column2':'open close','column3':data['processor_slct_TCP']},
        {'column1':'Processor','column2':'slct TCP','column3':data['processor_sig_inst']},
        {'column1':'Processor','column2':'sig inst','column3':data['processor_sig_hndl']},
        {'column1':'Processor','column2':'sig hndl','column3':data['processor_fork_proc']},
        {'column1':'Processor','column2':'fork proc','column3':data['processor_exec_proc']},
        {'column1':'Processor','column2':'exec proc','column3':data['processor_sh_proc']},
        {'column1':'Processor','column2':'sh proc','column3':data['processor_Mhz']},
        {'column1':'Basic integer operations','column2':'intgr bit','column3':data['basic_intgr_bit']},
        {'column1':'Basic integer operations','column2':'intgr add','column3':data['basic_intgr_add']},
        {'column1':'Basic integer operations','column2':'intgr mul','column3':data['basic_intgr_mul']},
        {'column1':'Basic integer operations','column2':'intgr div','column3':data['basic_intgr_div']},
        {'column1':'Basic integer operations','column2':'intgr mod','column3':data['basic_intgr_mod']},
        {'column1':'Basic uint64 operations','column2':'int64 bit','column3':data['basic_int64_bit']},
        {'column1':'Basic uint64 operations','column2':'int64 add','column3':data['basic_int64_add']},
        {'column1':'Basic uint64 operations','column2':'int64 mul','column3':data['basic_int64_mul']},
        {'column1':'Basic uint64 operations','column2':'int64 div','column3':data['basic_int64_div']},
        {'column1':'Basic uint64 operations','column2':'int64 mod','column3':data['basic_int64_mod']},
        {'column1':'Basic float operations','column2':'float add','column3':data['basic_float_add']},
        {'column1':'Basic float operations','column2':'float mul','column3':data['basic_float_mul']},
        {'column1':'Basic float operations','column2':'float div','column3':data['basic_float_div']},
        {'column1':'Basic float operations','column2':'float bogo','column3':data['basic_float_bogo']},
        {'column1':'Basic double operations','column2':'double add','column3':data['basic_double_add']},
        {'column1':'Basic double operations','column2':'double mul','column3':data['basic_double_mul']},
        {'column1':'Basic double operations','column2':'double div','column3':data['basic_double_div']},
        {'column1':'Basic double operations','column2':'double bogo','column3':data['basic_double_bogo']},
        {'column1':'Context switching','column2':'2p/0K','column3':data['context_2p_0K']},
        {'column1':'Context switching','column2':'2p/16K','column3':data['context_2p_16K']},
        {'column1':'Context switching','column2':'2p/64K','column3':data['context_2p_64K']},
        {'column1':'Context switching','column2':'8p/16K','column3':data['context_8p_16K']},
        {'column1':'Context switching','column2':'8p/64K','column3':data['context_8p_64K']},
        {'column1':'Context switching','column2':'16p/16K','column3':data['context_16p_16K']},
        {'column1':'Context switching','column2':'16p/64K','column3':data['context_16p_64K']},
        {'column1':'*Local* Communication latencies','column2':'2p/0K','column3':data['local_2p_0K']},
        {'column1':'*Local* Communication latencies','column2':'Pipe','column3':data['local_Pipe']},
        {'column1':'*Local* Communication latencies','column2':'AF UNIX','column3':data['local_AF_UNIX']},
        {'column1':'*Local* Communication latencies','column2':'UDP','column3':data['local_UDP']},
        {'column1':'*Local* Communication latencies','column2':'TCP','column3':data['local_TCP']},
        {'column1':'*Local* Communication latencies','column2':'TCP conn','column3':data['local_TCP_conn']},
        {'column1':'*Local* Communication latencies','column2':'RPC/TCP','column3':data['local_RPC_TCP']},
        {'column1':'*Local* Communication latencies','column2':'RPC/UDP','column3':data['local_RPC_UDP']},
        {'column1':'File & VM system latencies in microseconds','column2':'0K File create','column3':data['local_bigger_Mmap_Latency']},
        {'column1':'File & VM system latencies in microseconds','column2':'0K File delete','column3':data['local_bigger_Prot_Fault']},
        {'column1':'File & VM system latencies in microseconds','column2':'10K File create','column3':data['local_bigger_Page_Fault']},
        {'column1':'File & VM system latencies in microseconds','column2':'10K File delete','column3':data['local_bigger_100fd_selct']},
        {'column1':'File & VM system latencies in microseconds','column2':'Mmap Latency','column3':data['local_bigger_0K_File_create']},
        {'column1':'File & VM system latencies in microseconds','column2':'Prot Fault','column3':data['local_bigger_0K_File_delete']},
        {'column1':'File & VM system latencies in microseconds','column2':'Page Fault','column3':data['local_bigger_10K_File_create']},
        {'column1':'File & VM system latencies in microseconds','column2':'100fd selct','column3':data['local_bigger_10K_File_delete']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Pipe','column3':data['local_bigger_Pipe']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'AF UNIX','column3':data['local_bigger_AF_UNIX']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'TCP','column3':data['local_bigger_TCP']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'File reread','column3':data['local_bigger_File_reread']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mmap reread','column3':data['local_bigger_Mmap_reread']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Bcopy(libc)','column3':data['local_bigger_Bcopy_libc']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Bcopy(hand)','column3':data['local_bigger_Bcopy_hand']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mem read','column3':data['local_bigger_Mem_read']},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mem write','column3':data['local_bigger_Mem_write']},
        {'column1':'Memory latencies in nanoseconds','column2':'Mhz','column3':data['memory_Mhz']},
        {'column1':'Memory latencies in nanoseconds','column2':'L1 $','column3':data['memory_L1']},
        {'column1':'Memory latencies in nanoseconds','column2':'L2 $','column3':data['memory_L2']},
        {'column1':'Memory latencies in nanoseconds','column2':'Main mem','column3':data['memory_Main_mem']},
        {'column1':'Memory latencies in nanoseconds','column2':'Rand mem','column3':data['memory_Rand_mem']},
        ]
        if comparsionIds != ['']:
            # 处理对比数据
            for index ,comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Lmbench.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)
                others[0]['column'+str(new_index)] = 'Lmbench#'+str(index + 2)
                others[1]['column'+str(new_index)] = comparsion_datas['execute_cmd']
                others[2]['column'+str(new_index)] = comparsion_datas['modify_parameters']
                others[0]['column'+str(new_index+1)] = ''
                others[1]['column'+str(new_index+1)] = ''
                others[2]['column'+str(new_index+1)] = ''

                datas[0]['column'+str(new_index)] = comparsion_datas['basic_Mhz']
                datas[1]['column'+str(new_index)] = comparsion_datas['basic_tlb_pages']
                datas[2]['column'+str(new_index)] = comparsion_datas['basic_cache_line_bytes']
                datas[3]['column'+str(new_index)] = comparsion_datas['basic_mem_par']
                datas[4]['column'+str(new_index)] = comparsion_datas['basic_scal_load']
                datas[5]['column'+str(new_index)] = comparsion_datas['processor_null_call']
                datas[6]['column'+str(new_index)] = comparsion_datas['processor_null_I_O']
                datas[7]['column'+str(new_index)] = comparsion_datas['processor_stat']
                datas[8]['column'+str(new_index)] = comparsion_datas['processor_open_clo']
                datas[9]['column'+str(new_index)] = comparsion_datas['processor_slct_TCP']
                datas[10]['column'+str(new_index)] = comparsion_datas['processor_sig_inst']
                datas[11]['column'+str(new_index)] = comparsion_datas['processor_sig_hndl']
                datas[12]['column'+str(new_index)] = comparsion_datas['processor_fork_proc']
                datas[13]['column'+str(new_index)] = comparsion_datas['processor_exec_proc']
                datas[14]['column'+str(new_index)] = comparsion_datas['processor_sh_proc']
                datas[15]['column'+str(new_index)] = comparsion_datas['processor_Mhz']
                datas[16]['column'+str(new_index)] = comparsion_datas['basic_intgr_bit']
                datas[17]['column'+str(new_index)] = comparsion_datas['basic_intgr_add']
                datas[18]['column'+str(new_index)] = comparsion_datas['basic_intgr_mul']
                datas[19]['column'+str(new_index)] = comparsion_datas['basic_intgr_div']
                datas[20]['column'+str(new_index)] = comparsion_datas['basic_intgr_mod']
                datas[21]['column'+str(new_index)] = comparsion_datas['basic_int64_bit']
                datas[22]['column'+str(new_index)] = comparsion_datas['basic_int64_add']
                datas[23]['column'+str(new_index)] = comparsion_datas['basic_int64_mul']
                datas[24]['column'+str(new_index)] = comparsion_datas['basic_int64_div']
                datas[25]['column'+str(new_index)] = comparsion_datas['basic_int64_mod']
                datas[26]['column'+str(new_index)] = comparsion_datas['basic_float_add']
                datas[27]['column'+str(new_index)] = comparsion_datas['basic_float_mul']
                datas[28]['column'+str(new_index)] = comparsion_datas['basic_float_div']
                datas[29]['column'+str(new_index)] = comparsion_datas['basic_float_bogo']
                datas[20]['column'+str(new_index)] = comparsion_datas['basic_double_add']
                datas[31]['column'+str(new_index)] = comparsion_datas['basic_double_mul']
                datas[32]['column'+str(new_index)] = comparsion_datas['basic_double_div']
                datas[33]['column'+str(new_index)] = comparsion_datas['basic_double_bogo']
                datas[34]['column'+str(new_index)] = comparsion_datas['context_2p_0K']
                datas[35]['column'+str(new_index)] = comparsion_datas['context_2p_16K']
                datas[36]['column'+str(new_index)] = comparsion_datas['context_2p_64K']
                datas[37]['column'+str(new_index)] = comparsion_datas['context_8p_16K']
                datas[38]['column'+str(new_index)] = comparsion_datas['context_8p_64K']
                datas[39]['column'+str(new_index)] = comparsion_datas['context_16p_16K']
                datas[40]['column'+str(new_index)] = comparsion_datas['context_16p_64K']
                datas[41]['column'+str(new_index)] = comparsion_datas['local_2p_0K']
                datas[42]['column'+str(new_index)] = comparsion_datas['local_Pipe']
                datas[43]['column'+str(new_index)] = comparsion_datas['local_AF_UNIX']
                datas[44]['column'+str(new_index)] = comparsion_datas['local_UDP']
                datas[45]['column'+str(new_index)] = comparsion_datas['local_TCP']
                datas[46]['column'+str(new_index)] = comparsion_datas['local_TCP_conn']
                datas[47]['column'+str(new_index)] = comparsion_datas['local_RPC_TCP']
                datas[48]['column'+str(new_index)] = comparsion_datas['local_RPC_UDP']
                datas[49]['column'+str(new_index)] = comparsion_datas['local_bigger_Mmap_Latency']
                datas[50]['column'+str(new_index)] = comparsion_datas['local_bigger_Prot_Fault']
                datas[51]['column'+str(new_index)] = comparsion_datas['local_bigger_Page_Fault']
                datas[52]['column'+str(new_index)] = comparsion_datas['local_bigger_100fd_selct']
                datas[53]['column'+str(new_index)] = comparsion_datas['local_bigger_0K_File_create']
                datas[54]['column'+str(new_index)] = comparsion_datas['local_bigger_0K_File_delete']
                datas[55]['column'+str(new_index)] = comparsion_datas['local_bigger_10K_File_create']
                datas[56]['column'+str(new_index)] = comparsion_datas['local_bigger_10K_File_delete']
                datas[57]['column'+str(new_index)] = comparsion_datas['local_bigger_Pipe']
                datas[58]['column'+str(new_index)] = comparsion_datas['local_bigger_AF_UNIX']
                datas[59]['column'+str(new_index)] = comparsion_datas['local_bigger_TCP']
                datas[60]['column'+str(new_index)] = comparsion_datas['local_bigger_File_reread']
                datas[61]['column'+str(new_index)] = comparsion_datas['local_bigger_Mmap_reread']
                datas[62]['column'+str(new_index)] = comparsion_datas['local_bigger_Bcopy_libc']
                datas[63]['column'+str(new_index)] = comparsion_datas['local_bigger_Bcopy_hand']
                datas[64]['column'+str(new_index)] = comparsion_datas['local_bigger_Mem_read']
                datas[65]['column'+str(new_index)] = comparsion_datas['local_bigger_Mem_write']
                datas[66]['column'+str(new_index)] = comparsion_datas['memory_Mhz']
                datas[67]['column'+str(new_index)] = comparsion_datas['memory_L1']
                datas[68]['column'+str(new_index)] = comparsion_datas['memory_L2']
                datas[69]['column'+str(new_index)] = comparsion_datas['memory_Main_mem']
                datas[70]['column'+str(new_index)] = comparsion_datas['memory_Rand_mem']

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
                datas[10]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[10]['column'+str(new_index)] - datas[10]['column3'])/datas[10]['column3'] * 100)
                datas[11]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[11]['column'+str(new_index)] - datas[11]['column3'])/datas[11]['column3'] * 100)
                datas[12]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[12]['column'+str(new_index)] - datas[12]['column3'])/datas[12]['column3'] * 100)
                datas[13]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[13]['column'+str(new_index)] - datas[13]['column3'])/datas[13]['column3'] * 100)
                datas[14]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[14]['column'+str(new_index)] - datas[14]['column3'])/datas[14]['column3'] * 100)
                datas[15]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[15]['column'+str(new_index)] - datas[15]['column3'])/datas[15]['column3'] * 100)
                datas[16]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[16]['column'+str(new_index)] - datas[16]['column3'])/datas[16]['column3'] * 100)
                datas[17]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[17]['column'+str(new_index)] - datas[17]['column3'])/datas[17]['column3'] * 100)
                datas[18]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[18]['column'+str(new_index)] - datas[18]['column3'])/datas[18]['column3'] * 100)
                datas[19]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[19]['column'+str(new_index)] - datas[19]['column3'])/datas[19]['column3'] * 100)
                datas[20]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[20]['column'+str(new_index)] - datas[20]['column3'])/datas[20]['column3'] * 100)
                datas[21]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[21]['column'+str(new_index)] - datas[21]['column3'])/datas[21]['column3'] * 100)
                datas[22]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[22]['column'+str(new_index)] - datas[22]['column3'])/datas[22]['column3'] * 100)
                datas[23]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[23]['column'+str(new_index)] - datas[23]['column3'])/datas[23]['column3'] * 100)
                datas[24]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[24]['column'+str(new_index)] - datas[24]['column3'])/datas[24]['column3'] * 100)
                datas[25]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[25]['column'+str(new_index)] - datas[25]['column3'])/datas[25]['column3'] * 100)
                datas[26]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[26]['column'+str(new_index)] - datas[26]['column3'])/datas[26]['column3'] * 100)
                datas[27]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[27]['column'+str(new_index)] - datas[27]['column3'])/datas[27]['column3'] * 100)
                datas[28]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[28]['column'+str(new_index)] - datas[28]['column3'])/datas[28]['column3'] * 100)
                datas[29]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[29]['column'+str(new_index)] - datas[29]['column3'])/datas[29]['column3'] * 100)
                datas[20]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[20]['column'+str(new_index)] - datas[20]['column3'])/datas[20]['column3'] * 100)
                datas[31]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[31]['column'+str(new_index)] - datas[31]['column3'])/datas[31]['column3'] * 100)
                datas[32]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[32]['column'+str(new_index)] - datas[32]['column3'])/datas[32]['column3'] * 100)
                datas[33]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[33]['column'+str(new_index)] - datas[33]['column3'])/datas[33]['column3'] * 100)
                datas[34]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[34]['column'+str(new_index)] - datas[34]['column3'])/datas[34]['column3'] * 100)
                datas[35]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[35]['column'+str(new_index)] - datas[35]['column3'])/datas[35]['column3'] * 100)
                datas[36]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[36]['column'+str(new_index)] - datas[36]['column3'])/datas[36]['column3'] * 100)
                datas[37]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[37]['column'+str(new_index)] - datas[37]['column3'])/datas[37]['column3'] * 100)
                datas[38]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[38]['column'+str(new_index)] - datas[38]['column3'])/datas[38]['column3'] * 100)
                datas[39]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[39]['column'+str(new_index)] - datas[39]['column3'])/datas[39]['column3'] * 100)
                datas[40]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[40]['column'+str(new_index)] - datas[40]['column3'])/datas[40]['column3'] * 100)
                datas[41]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[41]['column'+str(new_index)] - datas[41]['column3'])/datas[41]['column3'] * 100)
                datas[42]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[42]['column'+str(new_index)] - datas[42]['column3'])/datas[42]['column3'] * 100)
                datas[43]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[43]['column'+str(new_index)] - datas[43]['column3'])/datas[43]['column3'] * 100)
                datas[44]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[44]['column'+str(new_index)] - datas[44]['column3'])/datas[44]['column3'] * 100)
                datas[45]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[45]['column'+str(new_index)] - datas[45]['column3'])/datas[45]['column3'] * 100)
                datas[46]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[46]['column'+str(new_index)] - datas[46]['column3'])/datas[46]['column3'] * 100)
                datas[47]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[47]['column'+str(new_index)] - datas[47]['column3'])/datas[47]['column3'] * 100)
                datas[48]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[48]['column'+str(new_index)] - datas[48]['column3'])/datas[48]['column3'] * 100)
                datas[49]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[49]['column'+str(new_index)] - datas[49]['column3'])/datas[49]['column3'] * 100)
                datas[50]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[50]['column'+str(new_index)] - datas[50]['column3'])/datas[50]['column3'] * 100)
                datas[51]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[51]['column'+str(new_index)] - datas[51]['column3'])/datas[51]['column3'] * 100)
                datas[52]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[52]['column'+str(new_index)] - datas[52]['column3'])/datas[52]['column3'] * 100)
                datas[53]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[53]['column'+str(new_index)] - datas[53]['column3'])/datas[53]['column3'] * 100)
                datas[54]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[54]['column'+str(new_index)] - datas[54]['column3'])/datas[54]['column3'] * 100)
                datas[55]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[55]['column'+str(new_index)] - datas[55]['column3'])/datas[55]['column3'] * 100)
                datas[56]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[56]['column'+str(new_index)] - datas[56]['column3'])/datas[56]['column3'] * 100)
                datas[57]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[57]['column'+str(new_index)] - datas[57]['column3'])/datas[57]['column3'] * 100)
                datas[58]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[58]['column'+str(new_index)] - datas[58]['column3'])/datas[58]['column3'] * 100)
                datas[59]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[59]['column'+str(new_index)] - datas[59]['column3'])/datas[59]['column3'] * 100)
                datas[60]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[60]['column'+str(new_index)] - datas[60]['column3'])/datas[60]['column3'] * 100)
                datas[61]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[61]['column'+str(new_index)] - datas[61]['column3'])/datas[61]['column3'] * 100)
                datas[62]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[62]['column'+str(new_index)] - datas[62]['column3'])/datas[62]['column3'] * 100)
                datas[63]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[63]['column'+str(new_index)] - datas[63]['column3'])/datas[63]['column3'] * 100)
                datas[64]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[64]['column'+str(new_index)] - datas[64]['column3'])/datas[64]['column3'] * 100)
                datas[65]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[65]['column'+str(new_index)] - datas[65]['column3'])/datas[65]['column3'] * 100)
                datas[66]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[66]['column'+str(new_index)] - datas[66]['column3'])/datas[66]['column3'] * 100)
                datas[67]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[67]['column'+str(new_index)] - datas[67]['column3'])/datas[67]['column3'] * 100)
                datas[68]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[68]['column'+str(new_index)] - datas[68]['column3'])/datas[68]['column3'] * 100)
                datas[69]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[69]['column'+str(new_index)] - datas[69]['column3'])/datas[69]['column3'] * 100)
                datas[70]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[70]['column'+str(new_index)] - datas[70]['column3'])/datas[70]['column3'] * 100)

        lmbench_data = {'others': others, 'data': datas}
        return json_response(lmbench_data, status.HTTP_200_OK, '列表')


    def create(self, request, *args, **kwargs):
        serializer_lmbench_error = []
        error_message = []
        for k, all_json in request.__dict__['data_lmbench'].items():
            if k.lower().startswith('lmbench'):
                constants.LMBENCH_BOOL = True
                for lmbench_json in all_json['items']:
                    # 每一条lmbench数据
                    lmbench = {}
                    lmbench['env_id'] = request.__dict__['data_lmbench']['env_id']
                    lmbench['test_time'] = return_time(all_json['time'])
                    lmbench['execute_cmd'] = 'xxx'
                    lmbench['modify_parameters'] = 'xxx'
                    # 处理数据，原始数据每个一级标就是一个json，把所有以及字段放到一个json中
                    new_lmbench = {}
                    for i in lmbench_json:
                        new_lmbench.update(i)
                    for key, value in new_lmbench.items():
                        if key == "Basic system parameters":
                            lmbench['basic_Mhz'] = value['Mhz']
                            lmbench['basic_tlb_pages'] = value['tlb pages']
                            lmbench['basic_cache_line_bytes'] = value['cache line bytes']
                            lmbench['basic_mem_par'] = value['mem par']
                            lmbench['basic_scal_load'] = value['scal load']
                        elif key == "Processor":
                            lmbench['processor_null_call'] = value['Mhz']
                            lmbench['processor_null_I_O'] = value['null call']
                            lmbench['processor_stat'] = value['null I/O']
                            lmbench['processor_open_clo'] = value['stat']
                            lmbench['processor_slct_TCP'] = value['open close']
                            lmbench['processor_sig_inst'] = value['slct TCP']
                            lmbench['processor_sig_hndl'] = value['sig inst']
                            lmbench['processor_fork_proc'] = value['sig hndl']
                            lmbench['processor_exec_proc'] = value['fork proc']
                            lmbench['processor_sh_proc'] = value['exec proc']
                            lmbench['processor_Mhz'] = value['sh proc']
                        elif key == "Basic integer operations":
                            lmbench['basic_intgr_bit'] = value['intgr bit']
                            lmbench['basic_intgr_add'] = value['intgr add']
                            lmbench['basic_intgr_mul'] = value['intgr mul']
                            lmbench['basic_intgr_div'] = value['intgr div']
                            lmbench['basic_intgr_mod'] = value['intgr mod']
                        elif key == "Basic uint64 operations":
                            lmbench['basic_int64_bit'] = value['int64 bit']
                            lmbench['basic_int64_add'] = value['int64 add']
                            lmbench['basic_int64_mul'] = value['int64 mul']
                            lmbench['basic_int64_div'] = value['int64 div']
                            lmbench['basic_int64_mod'] = value['int64 mod']
                        elif key == "Basic float operations":
                            lmbench['basic_float_add'] = value['float add']
                            lmbench['basic_float_mul'] = value['float mul']
                            lmbench['basic_float_div'] = value['float div']
                            lmbench['basic_float_bogo'] = value['float bogo']
                        elif key == "Basic double operations":
                            lmbench['basic_double_add'] = value['double add']
                            lmbench['basic_double_mul'] = value['double mul']
                            lmbench['basic_double_div'] = value['double div']
                            lmbench['basic_double_bogo'] = value['double bogo']
                        elif key == "Context switching":
                            lmbench['context_2p_0K'] = value['2p/0K']
                            lmbench['context_2p_16K'] = value['2p/16K']
                            lmbench['context_2p_64K'] = value['2p/64K']
                            lmbench['context_8p_16K'] = value['8p/16K']
                            lmbench['context_8p_64K'] = value['8p/64K']
                            lmbench['context_16p_16K'] = value['16p/16K']
                            lmbench['context_16p_64K'] = value['16p/64K']
                        elif key == "*Local* Communication latencies":
                            lmbench['local_2p_0K'] = value['2p/0K']
                            lmbench['local_Pipe'] = value['Pipe']
                            lmbench['local_AF_UNIX'] = value['AF UNIX']
                            lmbench['local_UDP'] = value['UDP']
                            lmbench['local_TCP'] = value['TCP']
                            lmbench['local_TCP_conn'] = value['TCP conn']
                            lmbench['local_RPC_TCP'] = value['RPC/TCP']
                            lmbench['local_RPC_UDP'] = value['RPC/UDP']
                        elif key == "File & VM system latencies in microseconds":
                            lmbench['local_bigger_0K_File_create'] = value['0K File create']
                            lmbench['local_bigger_0K_File_delete'] = value['0K File delete']
                            lmbench['local_bigger_10K_File_create'] = value['10K File create']
                            lmbench['local_bigger_10K_File_delete'] = value['10K File delete']
                            lmbench['local_bigger_Mmap_Latency'] = value['Mmap Latency']
                            lmbench['local_bigger_Prot_Fault'] = value['Prot Fault']
                            lmbench['local_bigger_Page_Fault'] = value['Page Fault']
                            lmbench['local_bigger_100fd_selct'] = value['100fd selct']
                        elif key == "*Local* Communication bandwidths in MB/s - bigger is better":
                            lmbench['local_bigger_Pipe'] = value['Pipe']
                            lmbench['local_bigger_AF_UNIX'] = value['AF UNIX']
                            lmbench['local_bigger_TCP'] = value['TCP']
                            lmbench['local_bigger_File_reread'] = value['File reread']
                            lmbench['local_bigger_Mmap_reread'] = value['Mmap reread']
                            lmbench['local_bigger_Bcopy_libc'] = value['Bcopy(libc)']
                            lmbench['local_bigger_Bcopy_hand'] = value['Bcopy(hand)']
                            lmbench['local_bigger_Mem_read'] = value['Mem read']
                            lmbench['local_bigger_Mem_write'] = value['Mem write']
                        elif key == "Memory latencies in nanoseconds":
                            lmbench['memory_Mhz'] = value['Mhz']
                            lmbench['memory_L1'] = value['L1 $']
                            lmbench['memory_L2'] = value['L2 $']
                            lmbench['memory_Main_mem'] = value['Main mem']
                            lmbench['memory_Rand_mem'] = value['Rand mem']
                    serializer_lmbench = LmbenchSerializer(data=lmbench)
                    if serializer_lmbench.is_valid():
                        self.perform_create(serializer_lmbench)
                    serializer_lmbench_error.append(serializer_lmbench.errors)
                    error_message.append(get_error_message(serializer_lmbench))
        if serializer_lmbench_error:
            print(serializer_lmbench_error,"lmbench")
            return json_response(serializer_lmbench_error, status.HTTP_400_BAD_REQUEST, error_message)
