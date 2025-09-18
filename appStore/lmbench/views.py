"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Feb 29 16:18:43 2024 +0800
"""
import math
import numpy as np
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

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        if len(serializer_) <= 1:
            if len(serializer_) == 0:
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'Lmbench#' + str(title_index)
                datas[1]['column' + str(column_index)] = None
                datas[2]['column' + str(column_index)] = None
                # 初始化所有数据为None
                for i in range(3, 74):
                    datas[i]['column' + str(column_index)] = None
                title_index += 1
                column_index += 1

            else:
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'Lmbench#' + str(title_index)
                datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
                datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
                datas[3]['column' + str(column_index)] = serializer.data[0]['basic_Mhz']
                datas[4]['column' + str(column_index)] = serializer.data[0]['basic_tlb_pages']
                datas[5]['column' + str(column_index)] = serializer.data[0]['basic_cache_line_bytes']
                datas[6]['column' + str(column_index)] = serializer.data[0]['basic_mem_par']
                datas[7]['column' + str(column_index)] = serializer.data[0]['basic_scal_load']
                datas[8]['column' + str(column_index)] = serializer.data[0]['processor_null_call']
                datas[9]['column' + str(column_index)] = serializer.data[0]['processor_null_I_O']
                datas[10]['column' + str(column_index)] = serializer.data[0]['processor_stat']
                datas[11]['column' + str(column_index)] = serializer.data[0]['processor_open_clo']
                datas[12]['column' + str(column_index)] = serializer.data[0]['processor_slct_TCP']
                datas[13]['column' + str(column_index)] = serializer.data[0]['processor_sig_inst']
                datas[14]['column' + str(column_index)] = serializer.data[0]['processor_sig_hndl']
                datas[15]['column' + str(column_index)] = serializer.data[0]['processor_fork_proc']
                datas[16]['column' + str(column_index)] = serializer.data[0]['processor_exec_proc']
                datas[17]['column' + str(column_index)] = serializer.data[0]['processor_sh_proc']
                datas[18]['column' + str(column_index)] = serializer.data[0]['processor_Mhz']
                datas[19]['column' + str(column_index)] = serializer.data[0]['basic_intgr_bit']
                datas[20]['column' + str(column_index)] = serializer.data[0]['basic_intgr_add']
                datas[21]['column' + str(column_index)] = serializer.data[0]['basic_intgr_mul']
                datas[22]['column' + str(column_index)] = serializer.data[0]['basic_intgr_div']
                datas[23]['column' + str(column_index)] = serializer.data[0]['basic_intgr_mod']
                datas[24]['column' + str(column_index)] = serializer.data[0]['basic_int64_bit']
                datas[25]['column' + str(column_index)] = serializer.data[0]['basic_int64_add']
                datas[26]['column' + str(column_index)] = serializer.data[0]['basic_int64_mul']
                datas[27]['column' + str(column_index)] = serializer.data[0]['basic_int64_div']
                datas[28]['column' + str(column_index)] = serializer.data[0]['basic_int64_mod']
                datas[29]['column' + str(column_index)] = serializer.data[0]['basic_float_add']
                datas[30]['column' + str(column_index)] = serializer.data[0]['basic_float_mul']
                datas[31]['column' + str(column_index)] = serializer.data[0]['basic_float_div']
                datas[32]['column' + str(column_index)] = serializer.data[0]['basic_float_bogo']
                datas[33]['column' + str(column_index)] = serializer.data[0]['basic_double_add']
                datas[34]['column' + str(column_index)] = serializer.data[0]['basic_double_mul']
                datas[35]['column' + str(column_index)] = serializer.data[0]['basic_double_div']
                datas[36]['column' + str(column_index)] = serializer.data[0]['basic_double_bogo']
                datas[37]['column' + str(column_index)] = serializer.data[0]['context_2p_0K']
                datas[38]['column' + str(column_index)] = serializer.data[0]['context_2p_16K']
                datas[39]['column' + str(column_index)] = serializer.data[0]['context_2p_64K']
                datas[40]['column' + str(column_index)] = serializer.data[0]['context_8p_16K']
                datas[41]['column' + str(column_index)] = serializer.data[0]['context_8p_64K']
                datas[42]['column' + str(column_index)] = serializer.data[0]['context_16p_16K']
                datas[43]['column' + str(column_index)] = serializer.data[0]['context_16p_64K']
                datas[44]['column' + str(column_index)] = serializer.data[0]['local_2p_0K']
                datas[45]['column' + str(column_index)] = serializer.data[0]['local_Pipe']
                datas[46]['column' + str(column_index)] = serializer.data[0]['local_AF_UNIX']
                datas[47]['column' + str(column_index)] = serializer.data[0]['local_UDP']
                datas[48]['column' + str(column_index)] = serializer.data[0]['local_TCP']
                datas[49]['column' + str(column_index)] = serializer.data[0]['local_TCP_conn']
                datas[50]['column' + str(column_index)] = serializer.data[0]['local_RPC_TCP']
                datas[51]['column' + str(column_index)] = serializer.data[0]['local_RPC_UDP']
                datas[52]['column' + str(column_index)] = serializer.data[0]['local_bigger_Mmap_Latency']
                datas[53]['column' + str(column_index)] = serializer.data[0]['local_bigger_Prot_Fault']
                datas[54]['column' + str(column_index)] = serializer.data[0]['local_bigger_Page_Fault']
                datas[55]['column' + str(column_index)] = serializer.data[0]['local_bigger_100fd_selct']
                datas[56]['column' + str(column_index)] = serializer.data[0]['local_bigger_0K_File_create']
                datas[57]['column' + str(column_index)] = serializer.data[0]['local_bigger_0K_File_delete']
                datas[58]['column' + str(column_index)] = serializer.data[0]['local_bigger_10K_File_create']
                datas[59]['column' + str(column_index)] = serializer.data[0]['local_bigger_10K_File_delete']
                datas[60]['column' + str(column_index)] = serializer.data[0]['local_bigger_Pipe']
                datas[61]['column' + str(column_index)] = serializer.data[0]['local_bigger_AF_UNIX']
                datas[62]['column' + str(column_index)] = serializer.data[0]['local_bigger_TCP']
                datas[63]['column' + str(column_index)] = serializer.data[0]['local_bigger_File_reread']
                datas[64]['column' + str(column_index)] = serializer.data[0]['local_bigger_Mmap_reread']
                datas[65]['column' + str(column_index)] = serializer.data[0]['local_bigger_Bcopy_libc']
                datas[66]['column' + str(column_index)] = serializer.data[0]['local_bigger_Bcopy_hand']
                datas[67]['column' + str(column_index)] = serializer.data[0]['local_bigger_Mem_read']
                datas[68]['column' + str(column_index)] = serializer.data[0]['local_bigger_Mem_write']
                datas[69]['column' + str(column_index)] = serializer.data[0]['memory_Mhz']
                datas[70]['column' + str(column_index)] = serializer.data[0]['memory_L1']
                datas[71]['column' + str(column_index)] = serializer.data[0]['memory_L2']
                datas[72]['column' + str(column_index)] = serializer.data[0]['memory_Main_mem']
                datas[73]['column' + str(column_index)] = serializer.data[0]['memory_Rand_mem']
                title_index += 1
                column_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(3, 74):
                datas[i]['column' + str(column_index)] = datas[i]['column' + str(column_index - 1)]
            column_index += 1
        else:
            # 计算平均值
            basic_Mhz_list = [d.basic_Mhz for d in serializer_ if d.basic_Mhz is not None]
            basic_tlb_pages_list = [d.basic_tlb_pages for d in serializer_ if d.basic_tlb_pages is not None]
            basic_cache_line_bytes_list = [d.basic_cache_line_bytes for d in serializer_ if d.basic_cache_line_bytes is not None]
            basic_mem_par_list = [d.basic_mem_par for d in serializer_ if d.basic_mem_par is not None]
            basic_scal_load_list = [d.basic_scal_load for d in serializer_ if d.basic_scal_load is not None]
            processor_null_call_list = [d.processor_null_call for d in serializer_ if d.processor_null_call is not None]
            processor_null_I_O_list = [d.processor_null_I_O for d in serializer_ if d.processor_null_I_O is not None]
            processor_stat_list = [d.processor_stat for d in serializer_ if d.processor_stat is not None]
            processor_open_clo_list = [d.processor_open_clo for d in serializer_ if d.processor_open_clo is not None]
            processor_slct_TCP_list = [d.processor_slct_TCP for d in serializer_ if d.processor_slct_TCP is not None]
            processor_sig_inst_list = [d.processor_sig_inst for d in serializer_ if d.processor_sig_inst is not None]
            processor_sig_hndl_list = [d.processor_sig_hndl for d in serializer_ if d.processor_sig_hndl is not None]
            processor_fork_proc_list = [d.processor_fork_proc for d in serializer_ if d.processor_fork_proc is not None]
            processor_exec_proc_list = [d.processor_exec_proc for d in serializer_ if d.processor_exec_proc is not None]
            processor_sh_proc_list = [d.processor_sh_proc for d in serializer_ if d.processor_sh_proc is not None]
            processor_Mhz_list = [d.processor_Mhz for d in serializer_ if d.processor_Mhz is not None]
            basic_intgr_bit_list = [d.basic_intgr_bit for d in serializer_ if d.basic_intgr_bit is not None]
            basic_intgr_add_list = [d.basic_intgr_add for d in serializer_ if d.basic_intgr_add is not None]
            basic_intgr_mul_list = [d.basic_intgr_mul for d in serializer_ if d.basic_intgr_mul is not None]
            basic_intgr_div_list = [d.basic_intgr_div for d in serializer_ if d.basic_intgr_div is not None]
            basic_intgr_mod_list = [d.basic_intgr_mod for d in serializer_ if d.basic_intgr_mod is not None]
            basic_int64_bit_list = [d.basic_int64_bit for d in serializer_ if d.basic_int64_bit is not None]
            basic_int64_add_list = [d.basic_int64_add for d in serializer_ if d.basic_int64_add is not None]
            basic_int64_mul_list = [d.basic_int64_mul for d in serializer_ if d.basic_int64_mul is not None]
            basic_int64_div_list = [d.basic_int64_div for d in serializer_ if d.basic_int64_div is not None]
            basic_int64_mod_list = [d.basic_int64_mod for d in serializer_ if d.basic_int64_mod is not None]
            basic_float_add_list = [d.basic_float_add for d in serializer_ if d.basic_float_add is not None]
            basic_float_mul_list = [d.basic_float_mul for d in serializer_ if d.basic_float_mul is not None]
            basic_float_div_list = [d.basic_float_div for d in serializer_ if d.basic_float_div is not None]
            basic_float_bogo_list = [d.basic_float_bogo for d in serializer_ if d.basic_float_bogo is not None]
            basic_double_add_list = [d.basic_double_add for d in serializer_ if d.basic_double_add is not None]
            basic_double_mul_list = [d.basic_double_mul for d in serializer_ if d.basic_double_mul is not None]
            basic_double_div_list = [d.basic_double_div for d in serializer_ if d.basic_double_div is not None]
            basic_double_bogo_list = [d.basic_double_bogo for d in serializer_ if d.basic_double_bogo is not None]
            context_2p_0K_list = [d.context_2p_0K for d in serializer_ if d.context_2p_0K is not None]
            context_2p_16K_list = [d.context_2p_16K for d in serializer_ if d.context_2p_16K is not None]
            context_2p_64K_list = [d.context_2p_64K for d in serializer_ if d.context_2p_64K is not None]
            context_8p_16K_list = [d.context_8p_16K for d in serializer_ if d.context_8p_16K is not None]
            context_8p_64K_list = [d.context_8p_64K for d in serializer_ if d.context_8p_64K is not None]
            context_16p_16K_list = [d.context_16p_16K for d in serializer_ if d.context_16p_16K is not None]
            context_16p_64K_list = [d.context_16p_64K for d in serializer_ if d.context_16p_64K is not None]
            local_2p_0K_list = [d.local_2p_0K for d in serializer_ if d.local_2p_0K is not None]
            local_Pipe_list = [d.local_Pipe for d in serializer_ if d.local_Pipe is not None]
            local_AF_UNIX_list = [d.local_AF_UNIX for d in serializer_ if d.local_AF_UNIX is not None]
            local_UDP_list = [d.local_UDP for d in serializer_ if d.local_UDP is not None]
            local_TCP_list = [d.local_TCP for d in serializer_ if d.local_TCP is not None]
            local_TCP_conn_list = [d.local_TCP_conn for d in serializer_ if d.local_TCP_conn is not None]
            local_RPC_TCP_list = [d.local_RPC_TCP for d in serializer_ if d.local_RPC_TCP is not None]
            local_RPC_UDP_list = [d.local_RPC_UDP for d in serializer_ if d.local_RPC_UDP is not None]
            local_bigger_Mmap_Latency_list = [d.local_bigger_Mmap_Latency for d in serializer_ if d.local_bigger_Mmap_Latency is not None]
            local_bigger_Prot_Fault_list = [d.local_bigger_Prot_Fault for d in serializer_ if d.local_bigger_Prot_Fault is not None]
            local_bigger_Page_Fault_list = [d.local_bigger_Page_Fault for d in serializer_ if d.local_bigger_Page_Fault is not None]
            local_bigger_100fd_selct_list = [d.local_bigger_100fd_selct for d in serializer_ if d.local_bigger_100fd_selct is not None]
            local_bigger_0K_File_create_list = [d.local_bigger_0K_File_create for d in serializer_ if d.local_bigger_0K_File_create is not None]
            local_bigger_0K_File_delete_list = [d.local_bigger_0K_File_delete for d in serializer_ if d.local_bigger_0K_File_delete is not None]
            local_bigger_10K_File_create_list = [d.local_bigger_10K_File_create for d in serializer_ if d.local_bigger_10K_File_create is not None]
            local_bigger_10K_File_delete_list = [d.local_bigger_10K_File_delete for d in serializer_ if d.local_bigger_10K_File_delete is not None]
            local_bigger_Pipe_list = [d.local_bigger_Pipe for d in serializer_ if d.local_bigger_Pipe is not None]
            local_bigger_AF_UNIX_list = [d.local_bigger_AF_UNIX for d in serializer_ if d.local_bigger_AF_UNIX is not None]
            local_bigger_TCP_list = [d.local_bigger_TCP for d in serializer_ if d.local_bigger_TCP is not None]
            local_bigger_File_reread_list = [d.local_bigger_File_reread for d in serializer_ if d.local_bigger_File_reread is not None]
            local_bigger_Mmap_reread_list = [d.local_bigger_Mmap_reread for d in serializer_ if d.local_bigger_Mmap_reread is not None]
            local_bigger_Bcopy_libc_list = [d.local_bigger_Bcopy_libc for d in serializer_ if d.local_bigger_Bcopy_libc is not None]
            local_bigger_Bcopy_hand_list = [d.local_bigger_Bcopy_hand for d in serializer_ if d.local_bigger_Bcopy_hand is not None]
            local_bigger_Mem_read_list = [d.local_bigger_Mem_read for d in serializer_ if d.local_bigger_Mem_read is not None]
            local_bigger_Mem_write_list = [d.local_bigger_Mem_write for d in serializer_ if d.local_bigger_Mem_write is not None]
            memory_Mhz_list = [d.memory_Mhz for d in serializer_ if d.memory_Mhz is not None]
            memory_L1_list = [d.memory_L1 for d in serializer_ if d.memory_L1 is not None]
            memory_L2_list = [d.memory_L2 for d in serializer_ if d.memory_L2 is not None]
            memory_Main_mem_list = [d.memory_Main_mem for d in serializer_ if d.memory_Main_mem is not None]
            memory_Rand_mem_list = [d.memory_Rand_mem for d in serializer_ if d.memory_Rand_mem is not None]
            # 计算每个数组的平均值
            average_basic_Mhz = np.mean(basic_Mhz_list).round(2) if not np.isnan(np.mean(basic_Mhz_list)) else None
            average_basic_tlb_pages = np.mean(basic_tlb_pages_list).round(2) if not np.isnan(np.mean(basic_tlb_pages_list)) else None
            average_basic_cache_line_bytes = np.mean(basic_cache_line_bytes_list).round(2) if not np.isnan(np.mean(basic_cache_line_bytes_list)) else None
            average_basic_mem_par = np.mean(basic_mem_par_list).round(2) if not np.isnan(np.mean(basic_mem_par_list)) else None
            average_basic_scal_load = np.mean(basic_scal_load_list).round(2) if not np.isnan(np.mean(basic_scal_load_list)) else None
            average_processor_null_call = np.mean(processor_null_call_list).round(2) if not np.isnan(np.mean(processor_null_call_list)) else None
            average_processor_null_I_O = np.mean(processor_null_I_O_list).round(2) if not np.isnan(np.mean(processor_null_I_O_list)) else None
            average_processor_stat = np.mean(processor_stat_list).round(2) if not np.isnan(np.mean(processor_stat_list)) else None
            average_processor_open_clo = np.mean(processor_open_clo_list).round(2) if not np.isnan(np.mean(processor_open_clo_list)) else None
            average_processor_slct_TCP = np.mean(processor_slct_TCP_list).round(2) if not np.isnan(np.mean(processor_slct_TCP_list)) else None
            average_processor_sig_inst = np.mean(processor_sig_inst_list).round(2) if not np.isnan(np.mean(processor_sig_inst_list)) else None
            average_processor_sig_hndl = np.mean(processor_sig_hndl_list).round(2) if not np.isnan(np.mean(processor_sig_hndl_list)) else None
            average_processor_fork_proc = np.mean(processor_fork_proc_list).round(2) if not np.isnan(np.mean(processor_fork_proc_list)) else None
            average_processor_exec_proc = np.mean(processor_exec_proc_list).round(2) if not np.isnan(np.mean(processor_exec_proc_list)) else None
            average_processor_sh_proc = np.mean(processor_sh_proc_list).round(2) if not np.isnan(np.mean(processor_sh_proc_list)) else None
            average_processor_Mhz = np.mean(processor_Mhz_list).round(2) if not np.isnan(np.mean(processor_Mhz_list)) else None
            average_basic_intgr_bit = np.mean(basic_intgr_bit_list).round(2) if not np.isnan(np.mean(basic_intgr_bit_list)) else None
            average_basic_intgr_add = np.mean(basic_intgr_add_list).round(2) if not np.isnan(np.mean(basic_intgr_add_list)) else None
            average_basic_intgr_mul = np.mean(basic_intgr_mul_list).round(2) if not np.isnan(np.mean(basic_intgr_mul_list)) else None
            average_basic_intgr_div = np.mean(basic_intgr_div_list).round(2) if not np.isnan(np.mean(basic_intgr_div_list)) else None
            average_basic_intgr_mod = np.mean(basic_intgr_mod_list).round(2) if not np.isnan(np.mean(basic_intgr_mod_list)) else None
            average_basic_int64_bit = np.mean(basic_int64_bit_list).round(2) if not np.isnan(np.mean(basic_int64_bit_list)) else None
            average_basic_int64_add = np.mean(basic_int64_add_list).round(2) if not np.isnan(np.mean(basic_int64_add_list)) else None
            average_basic_int64_mul = np.mean(basic_int64_mul_list).round(2) if not np.isnan(np.mean(basic_int64_mul_list)) else None
            average_basic_int64_div = np.mean(basic_int64_div_list).round(2) if not np.isnan(np.mean(basic_int64_div_list)) else None
            average_basic_int64_mod = np.mean(basic_int64_mod_list).round(2) if not np.isnan(np.mean(basic_int64_mod_list)) else None
            average_basic_float_add = np.mean(basic_float_add_list).round(2) if not np.isnan(np.mean(basic_float_add_list)) else None
            average_basic_float_mul = np.mean(basic_float_mul_list).round(2) if not np.isnan(np.mean(basic_float_mul_list)) else None
            average_basic_float_div = np.mean(basic_float_div_list).round(2) if not np.isnan(np.mean(basic_float_div_list)) else None
            average_basic_float_bogo = np.mean(basic_float_bogo_list).round(2) if not np.isnan(np.mean(basic_float_bogo_list)) else None
            average_basic_double_add = np.mean(basic_double_add_list).round(2) if not np.isnan(np.mean(basic_double_add_list)) else None
            average_basic_double_mul = np.mean(basic_double_mul_list).round(2) if not np.isnan(np.mean(basic_double_mul_list)) else None
            average_basic_double_div = np.mean(basic_double_div_list).round(2) if not np.isnan(np.mean(basic_double_div_list)) else None
            average_basic_double_bogo = np.mean(basic_double_bogo_list).round(2) if not np.isnan(np.mean(basic_double_bogo_list)) else None
            average_context_2p_0K = np.mean(context_2p_0K_list).round(2) if not np.isnan(np.mean(context_2p_0K_list)) else None
            average_context_2p_16K = np.mean(context_2p_16K_list).round(2) if not np.isnan(np.mean(context_2p_16K_list)) else None
            average_context_2p_64K = np.mean(context_2p_64K_list).round(2) if not np.isnan(np.mean(context_2p_64K_list)) else None
            average_context_8p_16K = np.mean(context_8p_16K_list).round(2) if not np.isnan(np.mean(context_8p_16K_list)) else None
            average_context_8p_64K = np.mean(context_8p_64K_list).round(2) if not np.isnan(np.mean(context_8p_64K_list)) else None
            average_context_16p_16K = np.mean(context_16p_16K_list).round(2) if not np.isnan(np.mean(context_16p_16K_list)) else None
            average_context_16p_64K = np.mean(context_16p_64K_list).round(2) if not np.isnan(np.mean(context_16p_64K_list)) else None
            average_local_2p_0K = np.mean(local_2p_0K_list).round(2) if not np.isnan(np.mean(local_2p_0K_list)) else None
            average_local_Pipe = np.mean(local_Pipe_list).round(2) if not np.isnan(np.mean(local_Pipe_list)) else None
            average_local_AF_UNIX = np.mean(local_AF_UNIX_list).round(2) if not np.isnan(np.mean(local_AF_UNIX_list)) else None
            average_local_UDP = np.mean(local_UDP_list).round(2) if not np.isnan(np.mean(local_UDP_list)) else None
            average_local_TCP = np.mean(local_TCP_list).round(2) if not np.isnan(np.mean(local_TCP_list)) else None
            average_local_TCP_conn = np.mean(local_TCP_conn_list).round(2) if not np.isnan(np.mean(local_TCP_conn_list)) else None
            average_local_RPC_TCP = np.mean(local_RPC_TCP_list).round(2) if not np.isnan(np.mean(local_RPC_TCP_list)) else None
            average_local_RPC_UDP = np.mean(local_RPC_UDP_list).round(2) if not np.isnan(np.mean(local_RPC_UDP_list)) else None
            average_local_bigger_Mmap_Latency = np.mean(local_bigger_Mmap_Latency_list).round(2) if not np.isnan(np.mean(local_bigger_Mmap_Latency_list)) else None
            average_local_bigger_Prot_Fault = np.mean(local_bigger_Prot_Fault_list).round(2) if not np.isnan(np.mean(local_bigger_Prot_Fault_list)) else None
            average_local_bigger_Page_Fault = np.mean(local_bigger_Page_Fault_list).round(2) if not np.isnan(np.mean(local_bigger_Page_Fault_list)) else None
            average_local_bigger_100fd_selct = np.mean(local_bigger_100fd_selct_list).round(2) if not np.isnan(np.mean(local_bigger_100fd_selct_list)) else None
            average_local_bigger_0K_File_create = np.mean(local_bigger_0K_File_create_list).round(2) if not np.isnan(np.mean(local_bigger_0K_File_create_list)) else None
            average_local_bigger_0K_File_delete = np.mean(local_bigger_0K_File_delete_list).round(2) if not np.isnan(np.mean(local_bigger_0K_File_delete_list)) else None
            average_local_bigger_10K_File_create = np.mean(local_bigger_10K_File_create_list).round(2) if not np.isnan(np.mean(local_bigger_10K_File_create_list)) else None
            average_local_bigger_10K_File_delete = np.mean(local_bigger_10K_File_delete_list).round(2) if not np.isnan(np.mean(local_bigger_10K_File_delete_list)) else None
            average_local_bigger_Pipe = np.mean(local_bigger_Pipe_list).round(2) if not np.isnan(np.mean(local_bigger_Pipe_list)) else None
            average_local_bigger_AF_UNIX = np.mean(local_bigger_AF_UNIX_list).round(2) if not np.isnan(np.mean(local_bigger_AF_UNIX_list)) else None
            average_local_bigger_TCP = np.mean(local_bigger_TCP_list).round(2) if not np.isnan(np.mean(local_bigger_TCP_list)) else None
            average_local_bigger_File_reread = np.mean(local_bigger_File_reread_list).round(2) if not np.isnan(np.mean(local_bigger_File_reread_list)) else None
            average_local_bigger_Mmap_reread = np.mean(local_bigger_Mmap_reread_list).round(2) if not np.isnan(np.mean(local_bigger_Mmap_reread_list)) else None
            average_local_bigger_Bcopy_libc = np.mean(local_bigger_Bcopy_libc_list).round(2) if not np.isnan(np.mean(local_bigger_Bcopy_libc_list)) else None
            average_local_bigger_Bcopy_hand = np.mean(local_bigger_Bcopy_hand_list).round(2) if not np.isnan(np.mean(local_bigger_Bcopy_hand_list)) else None
            average_local_bigger_Mem_read = np.mean(local_bigger_Mem_read_list).round(2) if not np.isnan(np.mean(local_bigger_Mem_read_list)) else None
            average_local_bigger_Mem_write = np.mean(local_bigger_Mem_write_list).round(2) if not np.isnan(np.mean(local_bigger_Mem_write_list)) else None
            average_memory_Mhz = np.mean(memory_Mhz_list).round(2) if not np.isnan(np.mean(memory_Mhz_list)) else None
            average_memory_L1 = np.mean(memory_L1_list).round(2) if not np.isnan(np.mean(memory_L1_list)) else None
            average_memory_L2 = np.mean(memory_L2_list).round(2) if not np.isnan(np.mean(memory_L2_list)) else None
            average_memory_Main_mem = np.mean(memory_Main_mem_list).round(2) if not np.isnan(np.mean(memory_Main_mem_list)) else None
            average_memory_Rand_mem = np.mean(memory_Rand_mem_list).round(2) if not np.isnan(np.mean(memory_Rand_mem_list)) else None
            # 基准数据和对比数据的全部数据
            for data in serializer_:
                datas[0]['column' + str(column_index)] = 'Lmbench#' + str(title_index)
                datas[1]['column' + str(column_index)] = data.execute_cmd
                datas[2]['column' + str(column_index)] = data.modify_parameters
                datas[3]['column' + str(column_index)] = data.basic_Mhz
                datas[4]['column' + str(column_index)] = data.basic_tlb_pages
                datas[5]['column' + str(column_index)] = data.basic_cache_line_bytes
                datas[6]['column' + str(column_index)] = data.basic_mem_par
                datas[7]['column' + str(column_index)] = data.basic_scal_load
                datas[8]['column' + str(column_index)] = data.processor_null_call
                datas[9]['column' + str(column_index)] = data.processor_null_I_O
                datas[10]['column' + str(column_index)] = data.processor_stat
                datas[11]['column' + str(column_index)] = data.processor_open_clo
                datas[12]['column' + str(column_index)] = data.processor_slct_TCP
                datas[13]['column' + str(column_index)] = data.processor_sig_inst
                datas[14]['column' + str(column_index)] = data.processor_sig_hndl
                datas[15]['column' + str(column_index)] = data.processor_fork_proc
                datas[16]['column' + str(column_index)] = data.processor_exec_proc
                datas[17]['column' + str(column_index)] = data.processor_sh_proc
                datas[18]['column' + str(column_index)] = data.processor_Mhz
                datas[19]['column' + str(column_index)] = data.basic_intgr_bit
                datas[20]['column' + str(column_index)] = data.basic_intgr_add
                datas[21]['column' + str(column_index)] = data.basic_intgr_mul
                datas[22]['column' + str(column_index)] = data.basic_intgr_div
                datas[23]['column' + str(column_index)] = data.basic_intgr_mod
                datas[24]['column' + str(column_index)] = data.basic_int64_bit
                datas[25]['column' + str(column_index)] = data.basic_int64_add
                datas[26]['column' + str(column_index)] = data.basic_int64_mul
                datas[27]['column' + str(column_index)] = data.basic_int64_div
                datas[28]['column' + str(column_index)] = data.basic_int64_mod
                datas[29]['column' + str(column_index)] = data.basic_float_add
                datas[30]['column' + str(column_index)] = data.basic_float_mul
                datas[31]['column' + str(column_index)] = data.basic_float_div
                datas[32]['column' + str(column_index)] = data.basic_float_bogo
                datas[33]['column' + str(column_index)] = data.basic_double_add
                datas[34]['column' + str(column_index)] = data.basic_double_mul
                datas[35]['column' + str(column_index)] = data.basic_double_div
                datas[36]['column' + str(column_index)] = data.basic_double_bogo
                datas[37]['column' + str(column_index)] = data.context_2p_0K
                datas[38]['column' + str(column_index)] = data.context_2p_16K
                datas[39]['column' + str(column_index)] = data.context_2p_64K
                datas[40]['column' + str(column_index)] = data.context_8p_16K
                datas[41]['column' + str(column_index)] = data.context_8p_64K
                datas[42]['column' + str(column_index)] = data.context_16p_16K
                datas[43]['column' + str(column_index)] = data.context_16p_64K
                datas[44]['column' + str(column_index)] = data.local_2p_0K
                datas[45]['column' + str(column_index)] = data.local_Pipe
                datas[46]['column' + str(column_index)] = data.local_AF_UNIX
                datas[47]['column' + str(column_index)] = data.local_UDP
                datas[48]['column' + str(column_index)] = data.local_TCP
                datas[49]['column' + str(column_index)] = data.local_TCP_conn
                datas[50]['column' + str(column_index)] = data.local_RPC_TCP
                datas[51]['column' + str(column_index)] = data.local_RPC_UDP
                datas[52]['column' + str(column_index)] = data.local_bigger_Mmap_Latency
                datas[53]['column' + str(column_index)] = data.local_bigger_Prot_Fault
                datas[54]['column' + str(column_index)] = data.local_bigger_Page_Fault
                datas[55]['column' + str(column_index)] = data.local_bigger_100fd_selct
                datas[56]['column' + str(column_index)] = data.local_bigger_0K_File_create
                datas[57]['column' + str(column_index)] = data.local_bigger_0K_File_delete
                datas[58]['column' + str(column_index)] = data.local_bigger_10K_File_create
                datas[59]['column' + str(column_index)] = data.local_bigger_10K_File_delete
                datas[60]['column' + str(column_index)] = data.local_bigger_Pipe
                datas[61]['column' + str(column_index)] = data.local_bigger_AF_UNIX
                datas[62]['column' + str(column_index)] = data.local_bigger_TCP
                datas[63]['column' + str(column_index)] = data.local_bigger_File_reread
                datas[64]['column' + str(column_index)] = data.local_bigger_Mmap_reread
                datas[65]['column' + str(column_index)] = data.local_bigger_Bcopy_libc
                datas[66]['column' + str(column_index)] = data.local_bigger_Bcopy_hand
                datas[67]['column' + str(column_index)] = data.local_bigger_Mem_read
                datas[68]['column' + str(column_index)] = data.local_bigger_Mem_write
                datas[69]['column' + str(column_index)] = data.memory_Mhz
                datas[70]['column' + str(column_index)] = data.memory_L1
                datas[71]['column' + str(column_index)] = data.memory_L2
                datas[72]['column' + str(column_index)] = data.memory_Main_mem
                datas[73]['column' + str(column_index)] = data.memory_Rand_mem
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = average_basic_Mhz
            datas[4]['column' + str(column_index)] = average_basic_tlb_pages
            datas[5]['column' + str(column_index)] = average_basic_cache_line_bytes
            datas[6]['column' + str(column_index)] = average_basic_mem_par
            datas[7]['column' + str(column_index)] = average_basic_scal_load
            datas[8]['column' + str(column_index)] = average_processor_null_call
            datas[9]['column' + str(column_index)] = average_processor_null_I_O
            datas[10]['column' + str(column_index)] = average_processor_stat
            datas[11]['column' + str(column_index)] = average_processor_open_clo
            datas[12]['column' + str(column_index)] = average_processor_slct_TCP
            datas[13]['column' + str(column_index)] = average_processor_sig_inst
            datas[14]['column' + str(column_index)] = average_processor_sig_hndl
            datas[15]['column' + str(column_index)] = average_processor_fork_proc
            datas[16]['column' + str(column_index)] = average_processor_exec_proc
            datas[17]['column' + str(column_index)] = average_processor_sh_proc
            datas[18]['column' + str(column_index)] = average_processor_Mhz
            datas[19]['column' + str(column_index)] = average_basic_intgr_bit
            datas[20]['column' + str(column_index)] = average_basic_intgr_add
            datas[21]['column' + str(column_index)] = average_basic_intgr_mul
            datas[22]['column' + str(column_index)] = average_basic_intgr_div
            datas[23]['column' + str(column_index)] = average_basic_intgr_mod
            datas[24]['column' + str(column_index)] = average_basic_int64_bit
            datas[25]['column' + str(column_index)] = average_basic_int64_add
            datas[26]['column' + str(column_index)] = average_basic_int64_mul
            datas[27]['column' + str(column_index)] = average_basic_int64_div
            datas[28]['column' + str(column_index)] = average_basic_int64_mod
            datas[29]['column' + str(column_index)] = average_basic_float_add
            datas[30]['column' + str(column_index)] = average_basic_float_mul
            datas[31]['column' + str(column_index)] = average_basic_float_div
            datas[32]['column' + str(column_index)] = average_basic_float_bogo
            datas[33]['column' + str(column_index)] = average_basic_double_add
            datas[34]['column' + str(column_index)] = average_basic_double_mul
            datas[35]['column' + str(column_index)] = average_basic_double_div
            datas[36]['column' + str(column_index)] = average_basic_double_bogo
            datas[37]['column' + str(column_index)] = average_context_2p_0K
            datas[38]['column' + str(column_index)] = average_context_2p_16K
            datas[39]['column' + str(column_index)] = average_context_2p_64K
            datas[40]['column' + str(column_index)] = average_context_8p_16K
            datas[41]['column' + str(column_index)] = average_context_8p_64K
            datas[42]['column' + str(column_index)] = average_context_16p_16K
            datas[43]['column' + str(column_index)] = average_context_16p_64K
            datas[44]['column' + str(column_index)] = average_local_2p_0K
            datas[45]['column' + str(column_index)] = average_local_Pipe
            datas[46]['column' + str(column_index)] = average_local_AF_UNIX
            datas[47]['column' + str(column_index)] = average_local_UDP
            datas[48]['column' + str(column_index)] = average_local_TCP
            datas[49]['column' + str(column_index)] = average_local_TCP_conn
            datas[50]['column' + str(column_index)] = average_local_RPC_TCP
            datas[51]['column' + str(column_index)] = average_local_RPC_UDP
            datas[52]['column' + str(column_index)] = average_local_bigger_Mmap_Latency
            datas[53]['column' + str(column_index)] = average_local_bigger_Prot_Fault
            datas[54]['column' + str(column_index)] = average_local_bigger_Page_Fault
            datas[55]['column' + str(column_index)] = average_local_bigger_100fd_selct
            datas[56]['column' + str(column_index)] = average_local_bigger_0K_File_create
            datas[57]['column' + str(column_index)] = average_local_bigger_0K_File_delete
            datas[58]['column' + str(column_index)] = average_local_bigger_10K_File_create
            datas[59]['column' + str(column_index)] = average_local_bigger_10K_File_delete
            datas[60]['column' + str(column_index)] = average_local_bigger_Pipe
            datas[61]['column' + str(column_index)] = average_local_bigger_AF_UNIX
            datas[62]['column' + str(column_index)] = average_local_bigger_TCP
            datas[63]['column' + str(column_index)] = average_local_bigger_File_reread
            datas[64]['column' + str(column_index)] = average_local_bigger_Mmap_reread
            datas[65]['column' + str(column_index)] = average_local_bigger_Bcopy_libc
            datas[66]['column' + str(column_index)] = average_local_bigger_Bcopy_hand
            datas[67]['column' + str(column_index)] = average_local_bigger_Mem_read
            datas[68]['column' + str(column_index)] = average_local_bigger_Mem_write
            datas[69]['column' + str(column_index)] = average_memory_Mhz
            datas[70]['column' + str(column_index)] = average_memory_L1
            datas[71]['column' + str(column_index)] = average_memory_L2
            datas[72]['column' + str(column_index)] = average_memory_Main_mem
            datas[73]['column' + str(column_index)] = average_memory_Rand_mem
            column_index += 1

        if not base_column_index:
            # 记录基准数据
            base_column_index = column_index - 1
        else:
            # 对比数据的对比值
            datas[0]['column' + str(column_index)] = '对比值'
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(3, 74):
                if 59 < i < 69:
                    datas[i]['column' + str(column_index)] = \
                        "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i][
                            'column' + str(base_column_index)]) / datas[i][
                                        'column' + str(base_column_index)] * 100) if datas[i]['column' + str(
                            column_index - 1)] is not None and datas[i]['column' + str(
                            base_column_index)] is not None else None
                else:
                    datas[i]['column' + str(column_index)] = \
                        "%.2f%%" % ((datas[i]['column' + str(base_column_index)] - datas[i][
                            'column' + str(column_index - 1)]) / datas[i]['column' + str(base_column_index)] * 100) if \
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
        base_queryset = Lmbench.objects.filter(env_id=env_id).all()
        if not base_queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        datas = [
        {'column1':'Lmbench','column2':''},
        {'column1': '执行命令','column2':''},
        {'column1': '修改参数', 'column2':''},
        {'column1':'Basic system parameters','column2':'Mhz'},
        {'column1':'Basic system parameters','column2':'tlb pages'},
        {'column1':'Basic system parameters','column2':'cache line bytes'},
        {'column1':'Basic system parameters','column2':'mem par'},
        {'column1':'Basic system parameters','column2':'scal load'},
        {'column1':'Processor','column2':'Mhz'},
        {'column1':'Processor','column2':'null call'},
        {'column1':'Processor','column2':'null I/O'},
        {'column1':'Processor','column2':'stat'},
        {'column1':'Processor','column2':'open close'},
        {'column1':'Processor','column2':'slct TCP'},
        {'column1':'Processor','column2':'sig inst'},
        {'column1':'Processor','column2':'sig hndl'},
        {'column1':'Processor','column2':'fork proc'},
        {'column1':'Processor','column2':'exec proc'},
        {'column1':'Processor','column2':'sh proc'},
        {'column1':'Basic integer operations','column2':'intgr bit'},
        {'column1':'Basic integer operations','column2':'intgr add'},
        {'column1':'Basic integer operations','column2':'intgr mul'},
        {'column1':'Basic integer operations','column2':'intgr div'},
        {'column1':'Basic integer operations','column2':'intgr mod'},
        {'column1':'Basic uint64 operations','column2':'int64 bit'},
        {'column1':'Basic uint64 operations','column2':'int64 add'},
        {'column1':'Basic uint64 operations','column2':'int64 mul'},
        {'column1':'Basic uint64 operations','column2':'int64 div'},
        {'column1':'Basic uint64 operations','column2':'int64 mod'},
        {'column1':'Basic float operations','column2':'float add'},
        {'column1':'Basic float operations','column2':'float mul'},
        {'column1':'Basic float operations','column2':'float div'},
        {'column1':'Basic float operations','column2':'float bogo'},
        {'column1':'Basic double operations','column2':'double add'},
        {'column1':'Basic double operations','column2':'double mul'},
        {'column1':'Basic double operations','column2':'double div'},
        {'column1':'Basic double operations','column2':'double bogo'},
        {'column1':'Context switching','column2':'2p/0K'},
        {'column1':'Context switching','column2':'2p/16K'},
        {'column1':'Context switching','column2':'2p/64K'},
        {'column1':'Context switching','column2':'8p/16K'},
        {'column1':'Context switching','column2':'8p/64K'},
        {'column1':'Context switching','column2':'16p/16K'},
        {'column1':'Context switching','column2':'16p/64K'},
        {'column1':'*Local* Communication latencies','column2':'2p/0K'},
        {'column1':'*Local* Communication latencies','column2':'Pipe'},
        {'column1':'*Local* Communication latencies','column2':'AF UNIX'},
        {'column1':'*Local* Communication latencies','column2':'UDP'},
        {'column1':'*Local* Communication latencies','column2':'TCP'},
        {'column1':'*Local* Communication latencies','column2':'TCP conn'},
        {'column1':'*Local* Communication latencies','column2':'RPC/TCP'},
        {'column1':'*Local* Communication latencies','column2':'RPC/UDP'},
        {'column1':'File & VM system latencies in microseconds','column2':'0K File create'},
        {'column1':'File & VM system latencies in microseconds','column2':'0K File delete'},
        {'column1':'File & VM system latencies in microseconds','column2':'10K File create'},
        {'column1':'File & VM system latencies in microseconds','column2':'10K File delete'},
        {'column1':'File & VM system latencies in microseconds','column2':'Mmap Latency'},
        {'column1':'File & VM system latencies in microseconds','column2':'Prot Fault'},
        {'column1':'File & VM system latencies in microseconds','column2':'Page Fault'},
        {'column1':'File & VM system latencies in microseconds','column2':'100fd selct'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Pipe'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'AF UNIX'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'TCP'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'File reread'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mmap reread'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Bcopy(libc)'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Bcopy(hand)'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mem read'},
        {'column1':'*Local* Communication bandwidths in MB/s - bigger is better','column2':'Mem write'},
        {'column1':'Memory latencies in nanoseconds','column2':'Mhz'},
        {'column1':'Memory latencies in nanoseconds','column2':'L1 $'},
        {'column1':'Memory latencies in nanoseconds','column2':'L2 $'},
        {'column1':'Memory latencies in nanoseconds','column2':'Main mem'},
        {'column1':'Memory latencies in nanoseconds','column2':'Rand mem'},
        ]
        title_index = 1
        column_index = 3
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)
        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Lmbench.objects.filter(env_id=comparativeId).all()
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index,
                                                                                    column_index, base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')


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
                    lmbench = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                               lmbench.items()}
                    serializer_lmbench = LmbenchSerializer(data=lmbench)
                    if serializer_lmbench.is_valid():
                        self.perform_create(serializer_lmbench)
                    else:
                        serializer_lmbench_error.append(serializer_lmbench.errors)
                        error_message.append(get_error_message(serializer_lmbench))
        if serializer_lmbench_error:
            print(serializer_lmbench_error,"lmbench")
            return json_response(serializer_lmbench_error, status.HTTP_400_BAD_REQUEST, error_message)
        else:
            return
