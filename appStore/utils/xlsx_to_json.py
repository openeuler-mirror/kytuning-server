"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:15:41 2024 +0800
"""
#!/usr/bin/env python
# encoding: utf-8
"""
xlsx表格转成json数据用于xlsx表格存储
@author: Wqz
@time: 26/7/23 4:33 PM
"""
import base64
import json
import math
import time
import numpy
import pandas as pd

user_data = {
    # 替换为实际的文件路径
    "file_path": "./kytuning-result.xlsx",
    # 替换为要读取的工作表名称列表
    "sheet_names": ["Stream", "Lmbench", "Unixbench", "Fio", "Specjvm2008", "Speccpu2006(base)", "Speccpu2017(base)"],
    # "sheet_names": ["Stream","Lmbench","Unixbench","Fio","Iozone","Specjvm2008","Speccpu2006(base)","Speccpu2017(base)"],
    # 保存数据的文件名
    "all_json_file": "./all_json_file.json",
    # 磁盘数量
    "disk_number": 2,
    # 网卡数量
    "nic_number": 1,
    # 每个项目中的每种测试项有几组数据，不支持多项目录入，因为表格中只有一组环境信息表，
    "stream_end_number": 1,
    "lmbench_end_number": 1,
    "unixbench_end_number": 1,
    "fio_end_number": 1,
    "iozone_end_number": 1,
    "jvm2008_end_number": 1,
    "cpu2006_end_number": 1,
    "cpu2017_end_number": 1,
}


def env_excel_to_json(file_path, sheet_name, disk_number, nic_number):
    """
    环境信息表转换成json数据
    :param file_path:
    :param sheet_name:
    :param disk_number:
    :param nic_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if index == 3:
            column_data = df[column].tolist()
            hwinfo_machineinfo_manufacturer = column_data[4]
            hwinfo_machineinfo_product = column_data[5]
            hwinfo_machineinfo_serialnumber = column_data[6]
            hwinfo_bios_vendor = column_data[7]
            hwinfo_bios_version = column_data[8]
            hwinfo_cpu_Vendor_ID = column_data[9]
            hwinfo_cpu_CPU_family = column_data[10]
            hwinfo_cpu_model_name = column_data[11]
            hwinfo_cpu_CPU_MHz = column_data[12]
            hwinfo_cpu_CPUs = column_data[13]
            hwinfo_cpu_Threads_per_core = column_data[14]
            hwinfo_cpu_CPU_Arch = column_data[15]
            hwinfo_cpu_CPU_op_mode = column_data[16]
            hwinfo_cpu_Byte_Order = column_data[17]
            hwinfo_cpu_On_line_CPUs_list = column_data[18]
            hwinfo_cpu_Virtualization = column_data[19]
            hwinfo_cpu_Virtualization_type = column_data[20]
            hwinfo_cpu_L1d_cache = column_data[21]
            hwinfo_cpu_L1i_cache = column_data[22]
            hwinfo_cpu_L2_cache = column_data[23]
            hwinfo_cpu_L3_cache = column_data[24]
            hwinfo_memory_Flags = column_data[25]
            hwinfo_memory_vendor = column_data[26]
            hwinfo_memory_mem_type = column_data[27]
            hwinfo_memory_total_size = column_data[28]
            hwinfo_memory_mem_used = column_data[29]
            hwinfo_memory_mem_count = column_data[30]
            hwinfo_memory_mem_free = column_data[31]
            hwinfo_memory_mem_freq = column_data[32]
            hwinfo_memory_swap = column_data[33]
            # 判断磁盘数量(disk) n*11
            # 判断网卡数据(nicinfo) n*3
            # 直接处理其它的，这两个特俗的后面处理
            try:
                new_number = 34 + disk_number * 11 + nic_number * 3
                swinfo_os_curr_UTC_time = column_data[new_number]
                swinfo_os_os_id = column_data[new_number + 1]
                swinfo_os_os_arch = column_data[new_number + 2]
                swinfo_os_osversion = column_data[new_number + 3]
                swinfo_os_kernel = column_data[new_number + 4]
                swinfo_os_grub = column_data[new_number + 5]
                if column_data[new_number + 6] == numpy.nan:
                    swinfo_runtime_sysconf = str(base64.b64encode(column_data[new_number + 6].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_sysconf = ''
                if column_data[new_number + 7] == numpy.nan:
                    swinfo_runtime_sysctl = str(base64.b64encode(column_data[new_number + 7].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_sysctl = ''
                if column_data[new_number + 8] == numpy.nan:
                    swinfo_runtime_systemctlinfo = str(base64.b64encode(column_data[new_number + 8].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_systemctlinfo = ''
                if column_data[new_number + 9] == numpy.nan:
                    swinfo_runtime_driverinfo = str(base64.b64encode(column_data[new_number + 9].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_driverinfo = ''
                if column_data[new_number + 10] == numpy.nan:
                    swinfo_runtime_rpmlist = str(base64.b64encode(column_data[new_number + 10].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_rpmlist = ''
                if column_data[new_number + 11] == numpy.nan:
                    swinfo_runtime_ipclist = str(base64.b64encode(column_data[new_number + 11].encode("ascii")))[2:-1]
                else:
                    swinfo_runtime_ipclist = ''
            except:
                print("请确认磁盘和网卡数量")

            swinfo_runtime_selinux_status = column_data[new_number + 12]
            swinfo_runtime_power_status = column_data[new_number + 13]
            swinfo_runtime_cpu_sched = column_data[new_number + 14]
            swinfo_runtime_loadavg = column_data[new_number + 15]
            swinfo_runtime_uptime = column_data[new_number + 16]
            swinfo_software_ver_gccversion = column_data[new_number + 17]
            swinfo_software_ver_glibcversion = column_data[new_number + 18]
            swinfo_software_ver_javaversion = column_data[new_number + 19]
            swinfo_software_ver_g_version = column_data[new_number + 20]
            swinfo_software_ver_gfortranversion = column_data[new_number + 21]
            swinfo_software_ver_pythonversion = column_data[new_number + 22]

            # 处理：disk_number
            disk = []
            start_number = 34
            for i in range(disk_number):
                disk.append({"name": column_data[start_number], "part_type": column_data[start_number + 1],
                             "vendor": column_data[start_number + 2], "model": column_data[start_number + 3],
                             "size": column_data[start_number + 4], "rota": column_data[start_number + 5],
                             "sched": column_data[start_number + 6], "rq_size": column_data[start_number + 7],
                             "tran": column_data[start_number + 8],
                             "mntpoint=/": column_data[start_number + 9],
                             "mntpoint=/home": column_data[start_number + 10]})
                start_number += 11
            # 处理：nic_number
            nicinfo = []
            for i in range(nic_number):
                nicinfo.append(
                    {"logicalname": column_data[start_number], "product": column_data[start_number + 1],
                     "speed": column_data[start_number + 2]})
                start_number += 3
            # 处理nwinfo_nic
            # 判断网卡数据(nic) n*5
            nic = []
            start_number_ = new_number + 23
            for i in range(nic_number):
                nic.append({"nicname": column_data[start_number_], "ip": column_data[start_number_ + 1],
                            "hwaddr": column_data[start_number_ + 2], "gateway": column_data[start_number_ + 3],
                            "mtu": column_data[start_number_ + 4]})
                start_number_ += 5

            data = {"envinfo": {"hwinfo": {
                "machineinfo": {"manufacturer": hwinfo_machineinfo_manufacturer, "product": hwinfo_machineinfo_product,
                                "serialnumber": hwinfo_machineinfo_serialnumber},
                "bios": {"vendor": hwinfo_bios_vendor, "version": hwinfo_bios_version},
                "cpu": {"Vendor ID": hwinfo_cpu_Vendor_ID, "CPU family": hwinfo_cpu_CPU_family,
                        "model_name": hwinfo_cpu_model_name, "CPU MHz": hwinfo_cpu_CPU_MHz, "CPU(s)": hwinfo_cpu_CPUs,
                        "Thread(s) per core": hwinfo_cpu_Threads_per_core, "CPU Arch": hwinfo_cpu_CPU_Arch,
                        "CPU op-mode": hwinfo_cpu_CPU_op_mode, "Byte Order": hwinfo_cpu_Byte_Order,
                        "On-line CPU(s) list": hwinfo_cpu_On_line_CPUs_list,
                        "Virtualization": hwinfo_cpu_Virtualization,
                        "Virtualization type": hwinfo_cpu_Virtualization_type, "L1d cache:": hwinfo_cpu_L1d_cache,
                        "L1i cache": hwinfo_cpu_L1i_cache, "L2 cache": hwinfo_cpu_L2_cache,
                        "L3 cache": hwinfo_cpu_L3_cache, "Flags": hwinfo_memory_Flags},
                "memory": {"vendor": hwinfo_memory_vendor, "mem_type": hwinfo_memory_mem_type,
                           "total_size": hwinfo_memory_total_size, "mem_used": hwinfo_memory_mem_used,
                           "mem_count": hwinfo_memory_mem_count, "mem_free": hwinfo_memory_mem_free,
                           "mem_freq": hwinfo_memory_mem_freq, "swap": hwinfo_memory_swap}, "disk": disk,
                "nicinfo": nicinfo}, "swinfo": {
                "os": {"curr UTC time": swinfo_os_curr_UTC_time, "os_id": swinfo_os_os_id, "os_arch": swinfo_os_os_arch,
                       "osversion": swinfo_os_osversion, "kernel": swinfo_os_kernel, "grub": swinfo_os_grub},
                "runtime": {"sysconf": swinfo_runtime_sysconf, "sysctl": swinfo_runtime_sysctl,
                            "systemctlinfo": swinfo_runtime_systemctlinfo, "driverinfo": swinfo_runtime_driverinfo,
                            "rpmlist": swinfo_runtime_rpmlist, "ipclist": swinfo_runtime_ipclist,
                            "selinux_status": swinfo_runtime_selinux_status,
                            "power_status": swinfo_runtime_power_status, "cpu_sched": swinfo_runtime_cpu_sched,
                            "loadavg": swinfo_runtime_loadavg, "uptime": swinfo_runtime_uptime},
                "software_ver": {"gccversion": swinfo_software_ver_gccversion,
                                 "glibcversion": swinfo_software_ver_glibcversion,
                                 "javaversion": swinfo_software_ver_javaversion,
                                 "g++version": swinfo_software_ver_g_version,
                                 "gfortranversion": swinfo_software_ver_gfortranversion,
                                 "pythonversion": swinfo_software_ver_pythonversion}}, "nwinfo": {"nic": nic}}}
    return data


def stream_excel_to_json(file_path, sheet_name, end_number):
    """
    stream表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 1 < index < end_number + 2:
            column_data = df[column].tolist()
            key_name = "stream-5.9-1-null-0-" + str(index - 2)
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            single_array_size = column_data[2]
            single_copy = column_data[3]
            single_scale = column_data[4]
            single_add = column_data[5]
            single_triad = column_data[6]
            multi_array_size = column_data[7]
            multi_copy = column_data[8]
            multi_scale = column_data[9]
            multi_add = column_data[10]
            multi_triad = column_data[11]
            data[key_name] = {
                "execute_cmd": execute_cmd, "modify_parameters": modify_parameters,
                "tool_name": "stream",
                "单线程": {"Array size": single_array_size, "Copy": single_copy, "Scale": single_scale, "Add": single_add,
                           "Triad": single_triad},
                "多线程": {"Array size": multi_array_size, "Copy": multi_copy, "Scale": multi_scale, "Add": multi_add,
                           "Triad": multi_triad}}
    return data


def lmbench_excel_to_json(file_path, sheet_name, end_number):
    """
    lmbench表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 1 < index < end_number + 2:
            column_data = df[column].tolist()
            key_name = "lmbench-3.0-a9-2-null-0-" + str(index - 2)
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            basic_Mhz = column_data[2]
            basic_tlb_pages = column_data[3]
            basic_cache_line_bytes = column_data[4]
            basic_mem_par = column_data[5]
            basic_scal_load = column_data[6]
            processor_Mhz = column_data[7]
            processor_null_call = column_data[8]
            processor_null_I_O = column_data[9]
            processor_stat = column_data[10]
            processor_open_close = column_data[11]
            processor_slct_TCP = column_data[12]
            processor_sig_inst = column_data[13]
            processor_sig_hndl = column_data[14]
            processor_fork_proc = column_data[15]
            processor_exec_proc = column_data[16]
            processor_sh_proc = column_data[17]
            basic_intgr_bit = column_data[18]
            basic_intgr_add = column_data[19]
            basic_intgr_mul = column_data[20]
            basic_intgr_div = column_data[21]
            basic_intgr_mod = column_data[22]
            basic_int64_bit = column_data[23]
            basic_int64_add = column_data[24]
            basic_int64_mul = column_data[25]
            basic_int64_div = column_data[26]
            basic_int64_mod = column_data[27]
            basic_float_add = column_data[28]
            basic_float_mul = column_data[29]
            basic_float_div = column_data[30]
            basic_float_bogo = column_data[31]
            basic_double_add = column_data[32]
            basic_double_mul = column_data[33]
            basic_double_div = column_data[34]
            basic_double_bogo = column_data[35]
            context_2p_0K = column_data[36]
            context_2p_16K = column_data[37]
            context_2p_64K = column_data[38]
            context_8p_16K = column_data[39]
            context_8p_64K = column_data[40]
            context_16p_16K = column_data[41]
            context_16p_64K = column_data[42]
            local_2p_0K = column_data[43]
            local_Pipe = column_data[44]
            local_AF_UNIX = column_data[45]
            local_UDP = column_data[46]
            local_RPC_UDP = column_data[47]
            local_TCP = column_data[48]
            local_RPC_TCP = column_data[49]
            local_TCP_conn = column_data[50]
            local_bigger_0K_File_create = column_data[51]
            local_bigger_0K_File_delete = column_data[52]
            local_bigger_10K_File_create = column_data[53]
            local_bigger_10K_File_delete = column_data[54]
            local_bigger_Mmap_Latency = column_data[55]
            local_bigger_Prot_Fault = column_data[56]
            local_bigger_Page_Fault = column_data[57]
            local_bigger_100fd_selct = column_data[58]
            local_bigger_Pipe = column_data[59]
            local_bigger_AF_UNIX = column_data[60]
            local_bigger_TCP = column_data[61]
            local_bigger_File_reread = column_data[62]
            local_bigger_Mmap_reread = column_data[63]
            local_bigger_Bcopy_libc = column_data[64]
            local_bigger_Bcopy_hand = column_data[65]
            local_bigger_Mem_read = column_data[66]
            local_bigger_Mem_write = column_data[67]
            memory_Mhz = column_data[68]
            memory_L1 = column_data[69]
            memory_L2 = column_data[70]
            memory_Main_mem = column_data[71]
            memory_Rand_mem = column_data[72]
            data[key_name] = {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters,
                              "tool_name": "lmbench", "items": [[
                    {"Basic system parameters": {"Mhz": basic_Mhz, "tlb pages": basic_tlb_pages,
                                                 "cache line bytes": basic_cache_line_bytes, "mem par": basic_mem_par,
                                                 "scal load": basic_scal_load}},
                    {"Processor": {"Mhz": processor_Mhz, "null call": processor_null_call,
                                   "null I/O": processor_null_I_O, "stat": processor_stat,
                                   "open close": processor_open_close, "slct TCP": processor_slct_TCP,
                                   "sig inst": processor_sig_inst, "sig hndl": processor_sig_hndl,
                                   "fork proc": processor_fork_proc, "exec proc": processor_exec_proc,
                                   "sh proc": processor_sh_proc}},
                    {"Basic integer operations": {"intgr bit": basic_intgr_bit, "intgr add": basic_intgr_add,
                                                  "intgr mul": basic_intgr_mul, "intgr div": basic_intgr_div,
                                                  "intgr mod": basic_intgr_mod}},
                    {"Basic uint64 operations": {"int64 bit": basic_int64_bit, "int64 add": basic_int64_add,
                                                 "int64 mul": basic_int64_mul, "int64 div": basic_int64_div,
                                                 "int64 mod": basic_int64_mod}},
                    {"Basic float operations": {"float add": basic_float_add, "float mul": basic_float_mul,
                                                "float div": basic_float_div, "float bogo": basic_float_bogo}},
                    {"Basic double operations": {"double add": basic_double_add, "double mul": basic_double_mul,
                                                 "double div": basic_double_div, "double bogo": basic_double_bogo}},
                    {"Context switching": {"2p/0K": context_2p_0K, "2p/16K": context_2p_16K, "2p/64K": context_2p_64K,
                                           "8p/16K": context_8p_16K, "8p/64K": context_8p_64K,
                                           "16p/16K": context_16p_16K, "16p/64K": context_16p_64K}},
                    {"*Local* Communication latencies": {"2p/0K": local_2p_0K, "Pipe": local_Pipe,
                                                         "AF UNIX": local_AF_UNIX, "UDP": local_UDP,
                                                         "RPC/UDP": local_RPC_UDP, "TCP": local_TCP,
                                                         "RPC/TCP": local_RPC_TCP, "TCP conn": local_TCP_conn}},
                    {"File & VM system latencies in microseconds": {"0K File create": local_bigger_0K_File_create,
                                                                    "0K File delete": local_bigger_0K_File_delete,
                                                                    "10K File create": local_bigger_10K_File_create,
                                                                    "10K File delete": local_bigger_10K_File_delete,
                                                                    "Mmap Latency": local_bigger_Mmap_Latency,
                                                                    "Prot Fault": local_bigger_Prot_Fault,
                                                                    "Page Fault": local_bigger_Page_Fault,
                                                                    "100fd selct": local_bigger_100fd_selct}},
                    {"*Local* Communication bandwidths in MB/s - bigger is better": {"Pipe": local_bigger_Pipe,
                                                                                     "AF UNIX": local_bigger_AF_UNIX,
                                                                                     "TCP": local_bigger_TCP,
                                                                                     "File reread": local_bigger_File_reread,
                                                                                     "Mmap reread": local_bigger_Mmap_reread,
                                                                                     "Bcopy(libc)": local_bigger_Bcopy_libc,
                                                                                     "Bcopy(hand)": local_bigger_Bcopy_hand,
                                                                                     "Mem read": local_bigger_Mem_read,
                                                                                     "Mem write": local_bigger_Mem_write}},
                    {"Memory latencies in nanoseconds": {"Mhz": memory_Mhz, "L1 $": memory_L1, "L2 $": memory_L2,
                                                         "Main mem": memory_Main_mem, "Rand mem": memory_Rand_mem}}]]}
    return data


def unixbench_excel_to_json(file_path, sheet_name, end_number):
    """
    unixbench表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 1 < index < end_number + 2:
            column_data = df[column].tolist()
            single_key_name = "Unixbench-5.9.1-single-0-" + str(index - 2)
            multi_key_name = "Unixbench-5.9.1-multi-0-" + str(index - 2)
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            single_Dhrystone = column_data[2]
            single_Double_Precision = column_data[3]
            single_execl_throughput = column_data[4]
            single_file_copy_1024 = column_data[5]
            single_file_copy_256 = column_data[6]
            single_file_copy_4096 = column_data[7]
            single_pipe_throughput = column_data[8]
            single_pipe_based = column_data[9]
            single_process_creation = column_data[10]
            single_shell_scripts_1 = column_data[11]
            single_shell_scripts_8 = column_data[12]
            single_system_call_overhead = column_data[13]
            single_index_score = column_data[14]
            multi_Dhrystone = column_data[15]
            multi_Double_Precision = column_data[16]
            multi_execl_throughput = column_data[17]
            multi_file_copy_1024 = column_data[18]
            multi_file_copy_256 = column_data[19]
            multi_file_copy_4096 = column_data[20]
            multi_pipe_throughput = column_data[21]
            multi_pipe_based = column_data[22]
            multi_process_creation = column_data[23]
            multi_shell_scripts_1 = column_data[24]
            multi_shell_scripts_8 = column_data[25]
            multi_system_call_overhead = column_data[26]
            multi_index_score = column_data[27]
            data[single_key_name] = {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters,
                                     "tool_name": "unixbench",
                                     "单线程": {"Dhrystone 2 using register variables(lps)": single_Dhrystone,
                                                "Double-Precision Whetstone(MWIPS)": single_Double_Precision,
                                                "Execl Throughput(lps)": single_execl_throughput,
                                                "File Copy 1024 bufsize 2000 maxblocks(KBps)": single_file_copy_1024,
                                                "File Copy 256 bufsize 500 maxblocks(KBps)": single_file_copy_256,
                                                "File Copy 4096 bufsize 8000 maxblocks(KBps)": single_file_copy_4096,
                                                "Pipe Throughput(lps)": single_pipe_throughput,
                                                "Pipe-based Context Switching(lps)": single_pipe_based,
                                                "Process Creation(lps)": single_process_creation,
                                                "Shell Scripts (1 concurrent)(lpm)": single_shell_scripts_1,
                                                "Shell Scripts (8 concurrent)(lpm)": single_shell_scripts_8,
                                                "System Call Overhead(lps)": single_system_call_overhead,
                                                "Index Score(sum)": single_index_score}}
            data[multi_key_name] = {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters,
                                    "tool_name": "unixbench",
                                    "多线程": {"Dhrystone 2 using register variables(lps)": multi_Dhrystone,
                                               "Double-Precision Whetstone(MWIPS)": multi_Double_Precision,
                                               "Execl Throughput(lps)": multi_execl_throughput,
                                               "File Copy 1024 bufsize 2000 maxblocks(KBps)": multi_file_copy_1024,
                                               "File Copy 256 bufsize 500 maxblocks(KBps)": multi_file_copy_256,
                                               "File Copy 4096 bufsize 8000 maxblocks(KBps)": multi_file_copy_4096,
                                               "Pipe Throughput(lps)": multi_pipe_throughput,
                                               "Pipe-based Context Switching(lps)": multi_pipe_based,
                                               "Process Creation(lps)": multi_process_creation,
                                               "Shell Scripts (1 concurrent)(lpm)": multi_shell_scripts_1,
                                               "Shell Scripts (8 concurrent)(lpm)": multi_shell_scripts_8,
                                               "System Call Overhead(lps)": multi_system_call_overhead,
                                               "Index Score(sum)": multi_index_score}}
    return data


def fio_excel_to_json(file_path, sheet_name, end_number):
    """
    fio表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    # for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    name_list_ = []
    for index, column in enumerate(columns):
        if index == 0:
            column_data = df[column].tolist()
            key1_ = [x for x in column_data if isinstance(x, str) and x not in ["执行命令:", "修改参数:", "执行命令", "修改参数"]]
            key1 = [item.split('(')[0] for item in key1_]
            key2 = df.iloc[:, 2].tolist()[2:][::4]
            name_list_ = ["fio-3.20-" + str(y) + "-" + str(x) + "-0-" for x, y in zip(key1, key2)]

        # 不需要处理index = 1 的情况全是"bs", "io", "iops", "bw",
        if 1 < index < end_number + 2:
            column_data = df[column].tolist()
            name_list = [value + str(int(index) - 2) for value in name_list_]
            for i in range(len(name_list)):
                iops_data = float(column_data[2:][i * 4 + 2][:-1]) * 1000 if str(column_data[2:][i * 4 + 2]).endswith("k") else float(
                    column_data[2:][i * 4 + 2])
                data[name_list[i]] = {"tool_name": "fio", "rw": name_list[i].split("-")[-3],
                                      "items": {"bs": column_data[2:][i * 4],
                                                "io": column_data[2:][i * 4 + 1],
                                                "iops": iops_data,
                                                "bw": column_data[2:][i * 4 + 3]}}
    return data


def iozone_excel_to_json(file_path, sheet_name, end_number):
    """
    iozone表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    double_or_half = []
    first_key = []
    file_size_list = []

    for index, column in enumerate(columns):
        if index == 0:
            first_key = df[column].tolist()[2:]
        if index == 1:
            file_size_list = [value for value in df[column].tolist() if
                              not isinstance(value, float) or not math.isnan(value)]

        if 1 < index < end_number + 1:
            column_data = df[column].tolist()
            half_file_size = sorted(file_size_list)[0]
            first_name = "half"
            range_number = (len(column_data) - 2) / len(file_size_list)
            for i in range(len(file_size_list)):
                if file_size_list[i] == half_file_size:
                    first_name = "half"
                elif file_size_list[i] == half_file_size * 2:
                    first_name = "full"
                elif file_size_list[i] == half_file_size * 4:
                    first_name = "double"
                double_or_half.append(first_name)
            key_list = [first_key[i:i + int(range_number)] for i in range(0, len(first_key) - 2, int(range_number))]
            value_list = [column_data[2:][i:i + int(range_number)] for i in
                          range(0, len(column_data) - 2, int(range_number))]
            merged = [dict(zip(key_list[i], value_list[i])) for i in range(len(key_list))]
            for i, d in enumerate(merged):
                key = "iozone3_430-%s-0-%d" % (double_or_half[i], index - 2)
                data[key] = {"tool_name": "iozone", "测试记录": {**{"文件大小": file_size_list[i], "块大小": 0}, **d}}
    return data


def jvm2008_excel_to_json(file_path, sheet_name, end_number):
    """
    jvm2008表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 1 < index < end_number + 2:
            column_data = df[column].tolist()
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            base_compiler = column_data[2]
            base_compress = column_data[3]
            base_crypto = column_data[4]
            base_derby = column_data[5]
            base_mpegaudio = column_data[6]
            base_scimark_large = column_data[7]
            base_scimark_small = column_data[8]
            base_serial = column_data[9]
            base_startup = column_data[10]
            base_sunflow = column_data[11]
            base_xml = column_data[12]
            base_Noncompliant_pomposite_result = column_data[13]
            peak_compiler = column_data[14]
            peak_compress = column_data[15]
            peak_crypto = column_data[16]
            peak_derby = column_data[17]
            peak_mpegaudio = column_data[18]
            peak_scimark_large = column_data[19]
            peak_scimark_small = column_data[20]
            peak_serial = column_data[21]
            peak_startup = column_data[22]
            peak_sunflow = column_data[23]
            peak_xml = column_data[24]
            peak_Noncompliant_pomposite_result = column_data[25]
            data["specjvm-demo-base-0-" + str(index - 2)] = {"execute_cmd": execute_cmd,
                                                             "modify_parameters": modify_parameters,
                                                             "tool_name": "specjvm2008", "items": {
                    "base": {"compiler": base_compiler, "compress": base_compress, "crypto": base_crypto,
                             "derby": base_derby,
                             "mpegaudio": base_mpegaudio, "scimark.large": base_scimark_large,
                             "scimark.small": base_scimark_small,
                             "serial": base_serial, "startup": base_startup, "sunflow": base_sunflow, "xml": base_xml,
                             "Noncompliant composite result:": base_Noncompliant_pomposite_result}}}

            data["specjvm-demo-peak-0-" + str(index - 2)] = {"execute_cmd": execute_cmd,
                                                             "modify_parameters": modify_parameters,
                                                             "tool_name": "specjvm2008", "items": {
                    "peak": {"compiler": peak_compiler, "compress": peak_compress, "crypto": peak_crypto,
                             "derby": peak_derby,
                             "mpegaudio": peak_mpegaudio, "scimark.large": peak_scimark_large,
                             "scimark.small": peak_scimark_small,
                             "serial": peak_serial, "startup": peak_startup, "sunflow": peak_sunflow, "xml": peak_xml,
                             "Noncompliant composite result:": peak_Noncompliant_pomposite_result}}}
    return data


def cpu2006_excel_to_json(file_path, sheet_name, end_number):
    """
    cpu2006表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 2 < index < end_number + 3:
            column_data = df[column].tolist()
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            single_int_400_perlbench = column_data[2]
            single_int_401_bzip2 = column_data[3]
            single_int_403_gcc = column_data[4]
            single_int_429_mcf = column_data[5]
            single_int_445_gobmk = column_data[6]
            single_int_456_hmmer = column_data[7]
            single_int_458_sjeng = column_data[8]
            single_int_462_libquantum = column_data[9]
            single_int_464_h264ref = column_data[10]
            single_int_471_omnetpp = column_data[11]
            single_int_473_astar = column_data[12]
            single_int_483_xalancbmk = column_data[13]
            single_int_SPECint_2006 = column_data[14]
            single_fp_410_bwaves = column_data[15]
            single_fp_416_gamess = column_data[16]
            single_fp_433_milc = column_data[17]
            single_fp_434_zeusmp = column_data[18]
            single_fp_435_gromacs = column_data[19]
            single_fp_436_cactusADM = column_data[20]
            single_fp_437_leslie3d = column_data[21]
            single_fp_444_namd = column_data[22]
            single_fp_447_dealII = column_data[23]
            single_fp_450_soplex = column_data[24]
            single_fp_453_povray = column_data[25]
            single_fp_454_calculix = column_data[26]
            single_fp_459_GemsFDTD = column_data[27]
            single_fp_465_tonto = column_data[28]
            single_fp_470_lbm = column_data[29]
            single_fp_481_wrf = column_data[30]
            single_fp_482_sphinx3 = column_data[31]
            single_fp_SPECfp_2006 = column_data[32]
            multi_int_400_perlbench = column_data[33]
            multi_int_401_bzip2 = column_data[34]
            multi_int_403_gcc = column_data[35]
            multi_int_429_mcf = column_data[36]
            multi_int_445_gobmk = column_data[37]
            multi_int_456_hmmer = column_data[38]
            multi_int_458_sjeng = column_data[39]
            multi_int_462_libquantum = column_data[40]
            multi_int_464_h264ref = column_data[41]
            multi_int_471_omnetpp = column_data[42]
            multi_int_473_astar = column_data[43]
            multi_int_483_xalancbmk = column_data[44]
            multi_int_SPECint_2006 = column_data[45]
            multi_fp_410_bwaves = column_data[46]
            multi_fp_416_gamess = column_data[47]
            multi_fp_433_milc = column_data[48]
            multi_fp_434_zeusmp = column_data[49]
            multi_fp_435_gromacs = column_data[50]
            multi_fp_436_cactusADM = column_data[51]
            multi_fp_437_leslie3d = column_data[52]
            multi_fp_444_namd = column_data[53]
            multi_fp_447_dealII = column_data[54]
            multi_fp_450_soplex = column_data[55]
            multi_fp_453_povray = column_data[56]
            multi_fp_454_calculix = column_data[57]
            multi_fp_459_GemsFDTD = column_data[58]
            multi_fp_465_tonto = column_data[59]
            multi_fp_470_lbm = column_data[60]
            multi_fp_481_wrf = column_data[61]
            multi_fp_482_sphinx3 = column_data[62]
            multi_fp_SPECfp_2006 = column_data[63]

            if sheet_name[12:16] == "base":
                data["cpu2006-1.2-%s-single-int-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_int": {
                         "base": {"400.perlbench": single_int_400_perlbench, "401.bzip2": single_int_401_bzip2,
                                  "403.gcc": single_int_403_gcc,
                                  "429.mcf": single_int_429_mcf, "445.gobmk": single_int_445_gobmk,
                                  "456.hmmer": single_int_456_hmmer,
                                  "458.sjeng": single_int_458_sjeng, "462.libquantum": single_int_462_libquantum,
                                  "464.h264ref": single_int_464_h264ref,
                                  "471.omnetpp": single_int_471_omnetpp, "473.astar": single_int_473_astar,
                                  "483.xalancbmk": single_int_483_xalancbmk,
                                  "SPECint_2006": single_int_SPECint_2006},
                         "peak": {"400.perlbench": "", "401.bzip2": "",
                                  "403.gcc": "", "429.mcf": "", "445.gobmk": "",
                                  "456.hmmer": "", "458.sjeng": "",
                                  "462.libquantum": "", "464.h264ref": "",
                                  "471.omnetpp": "", "473.astar": "",
                                  "483.xalancbmk": "", "SPECint_2006": ""}}}}

                data["cpu2006-1.2-%s-single-fp-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_fp": {
                         "base": {"410.bwaves": single_fp_410_bwaves, "416.gamess": single_fp_416_gamess,
                                  "433.milc": single_fp_433_milc,
                                  "434.zeusmp": single_fp_434_zeusmp, "435.gromacs": single_fp_435_gromacs,
                                  "436.cactusADM": single_fp_436_cactusADM, "437.leslie3d": single_fp_437_leslie3d,
                                  "444.namd": single_fp_444_namd, "447.dealII": single_fp_447_dealII,
                                  "450.soplex": single_fp_450_soplex,
                                  "453.povray": single_fp_453_povray, "454.calculix": single_fp_454_calculix,
                                  "459.GemsFDTD": single_fp_459_GemsFDTD, "465.tonto": single_fp_465_tonto,
                                  "470.lbm": single_fp_470_lbm,
                                  "481.wrf": single_fp_481_wrf, "482.sphinx3": single_fp_482_sphinx3,
                                  "SPECfp_2006": single_fp_SPECfp_2006},
                         "peak": {"410.bwaves": "", "416.gamess": "",
                                  "433.milc": "", "434.zeusmp": "",
                                  "435.gromacs": "", "436.cactusADM": "",
                                  "437.leslie3d": "",
                                  "444.namd": "", "447.dealII": "",
                                  "450.soplex": "", "453.povray": "",
                                  "454.calculix": "", "459.GemsFDTD": "",
                                  "465.tonto": "", "470.lbm": "",
                                  "481.wrf": "", "482.sphinx3": "",
                                  "SPECfp_2006": ""}}}}

                data["cpu2006-1.2-%s-multi-int-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_int": {
                         "base": {"400.perlbench": multi_int_400_perlbench, "401.bzip2": multi_int_401_bzip2,
                                  "403.gcc": multi_int_403_gcc,
                                  "429.mcf": multi_int_429_mcf, "445.gobmk": multi_int_445_gobmk,
                                  "456.hmmer": multi_int_456_hmmer,
                                  "458.sjeng": multi_int_458_sjeng, "462.libquantum": multi_int_462_libquantum,
                                  "464.h264ref": multi_int_464_h264ref,
                                  "471.omnetpp": multi_int_471_omnetpp, "473.astar": multi_int_473_astar,
                                  "483.xalancbmk": multi_int_483_xalancbmk,
                                  "SPECint_2006": multi_int_SPECint_2006},
                         "peak": {"400.perlbench": "", "401.bzip2": "",
                                  "403.gcc": "", "429.mcf": "",
                                  "445.gobmk": "",
                                  "456.hmmer": "", "458.sjeng": "",
                                  "462.libquantum": "", "464.h264ref": "",
                                  "471.omnetpp": "", "473.astar": "",
                                  "483.xalancbmk": "",
                                  "SPECint_2006": ""}}}}

                data["cpu2006-1.2-%s-multi-fp-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {
                         "多线程_fp": {"base": {"410.bwaves": multi_fp_410_bwaves, "416.gamess": multi_fp_416_gamess,
                                                "433.milc": multi_fp_433_milc,
                                                "434.zeusmp": multi_fp_434_zeusmp, "435.gromacs": multi_fp_435_gromacs,
                                                "436.cactusADM": multi_fp_436_cactusADM,
                                                "437.leslie3d": multi_fp_437_leslie3d,
                                                "444.namd": multi_fp_444_namd, "447.dealII": multi_fp_447_dealII,
                                                "450.soplex": multi_fp_450_soplex,
                                                "453.povray": multi_fp_453_povray, "454.calculix": multi_fp_454_calculix,
                                                "459.GemsFDTD": multi_fp_459_GemsFDTD, "465.tonto": multi_fp_465_tonto,
                                                "470.lbm": multi_fp_470_lbm,
                                                "481.wrf": multi_fp_481_wrf, "482.sphinx3": multi_fp_482_sphinx3,
                                                "SPECfp_2006": multi_fp_SPECfp_2006},
                                       "peak": {"410.bwaves": "", "416.gamess": "",
                                                "433.milc": "", "434.zeusmp": "",
                                                "435.gromacs": "",
                                                "436.cactusADM": "",
                                                "437.leslie3d": "",
                                                "444.namd": "", "447.dealII": "",
                                                "450.soplex": "", "453.povray": "",
                                                "454.calculix": "",
                                                "459.GemsFDTD": "", "465.tonto": "",
                                                "470.lbm": "",
                                                "481.wrf": "", "482.sphinx3": "",
                                                "SPECfp_2006": ""}}}}
            elif sheet_name[12:16] == "peak":
                data["cpu2006-1.2-%s-single-int-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_int": {
                         "base": {"400.perlbench": "", "401.bzip2": "",
                                  "403.gcc": "",
                                  "429.mcf": "", "445.gobmk": "",
                                  "456.hmmer": "",
                                  "458.sjeng": "", "462.libquantum": "",
                                  "464.h264ref": "",
                                  "471.omnetpp": "", "473.astar": "",
                                  "483.xalancbmk": "",
                                  "SPECint_2006": ""},
                         "peak": {"400.perlbench": single_int_400_perlbench, "401.bzip2": single_int_401_bzip2,
                                  "403.gcc": single_int_403_gcc, "429.mcf": single_int_429_mcf,
                                  "445.gobmk": single_int_445_gobmk,
                                  "456.hmmer": single_int_456_hmmer, "458.sjeng": single_int_458_sjeng,
                                  "462.libquantum": single_int_462_libquantum, "464.h264ref": single_int_464_h264ref,
                                  "471.omnetpp": single_int_471_omnetpp, "473.astar": single_int_473_astar,
                                  "483.xalancbmk": single_int_483_xalancbmk, "SPECint_2006": single_int_SPECint_2006}}}}

                data["cpu2006-1.2-%s-single-fp-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_fp": {
                         "base": {"410.bwaves": "", "416.gamess": "",
                                  "433.milc": "",
                                  "434.zeusmp": "", "435.gromacs": "",
                                  "436.cactusADM": "", "437.leslie3d": "",
                                  "444.namd": "", "447.dealII": "",
                                  "450.soplex": "",
                                  "453.povray": "", "454.calculix": "",
                                  "459.GemsFDTD": "", "465.tonto": "",
                                  "470.lbm": "",
                                  "481.wrf": "", "482.sphinx3": "",
                                  "SPECfp_2006": single_fp_SPECfp_2006},
                         "peak": {"410.bwaves": single_fp_410_bwaves, "416.gamess": single_fp_416_gamess,
                                  "433.milc": single_fp_433_milc, "434.zeusmp": single_fp_434_zeusmp,
                                  "435.gromacs": single_fp_435_gromacs, "436.cactusADM": single_fp_436_cactusADM,
                                  "437.leslie3d": single_fp_437_leslie3d,
                                  "444.namd": single_fp_444_namd, "447.dealII": single_fp_447_dealII,
                                  "450.soplex": single_fp_450_soplex, "453.povray": single_fp_453_povray,
                                  "454.calculix": single_fp_454_calculix, "459.GemsFDTD": single_fp_459_GemsFDTD,
                                  "465.tonto": single_fp_465_tonto, "470.lbm": single_fp_470_lbm,
                                  "481.wrf": single_fp_481_wrf, "482.sphinx3": single_fp_482_sphinx3,
                                  "SPECfp_2006": single_fp_SPECfp_2006}}}}

                data["cpu2006-1.2-%s-multi-int-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_int": {
                         "base": {"400.perlbench": "", "401.bzip2": "",
                                  "403.gcc": "",
                                  "429.mcf": "", "445.gobmk": "",
                                  "456.hmmer": "",
                                  "458.sjeng": "", "462.libquantum": "",
                                  "464.h264ref": "",
                                  "471.omnetpp": "", "473.astar": "",
                                  "483.xalancbmk": "",
                                  "SPECint_2006": ""},
                         "peak": {"400.perlbench": multi_int_400_perlbench, "401.bzip2": multi_int_401_bzip2,
                                  "403.gcc": multi_int_403_gcc, "429.mcf": multi_int_429_mcf,
                                  "445.gobmk": multi_int_445_gobmk,
                                  "456.hmmer": multi_int_456_hmmer, "458.sjeng": multi_int_458_sjeng,
                                  "462.libquantum": multi_int_462_libquantum, "464.h264ref": multi_int_464_h264ref,
                                  "471.omnetpp": multi_int_471_omnetpp, "473.astar": multi_int_473_astar,
                                  "483.xalancbmk": multi_int_483_xalancbmk,
                                  "SPECint_2006": multi_int_SPECint_2006}}}}

                data["cpu2006-1.2-%s-multi-fp-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_fp": {"base": {"410.bwaves": "", "416.gamess": "",
                                                      "433.milc": "",
                                                      "434.zeusmp": "", "435.gromacs": "",
                                                      "436.cactusADM": "",
                                                      "437.leslie3d": "",
                                                      "444.namd": "", "447.dealII": "",
                                                      "450.soplex": "",
                                                      "453.povray": "", "454.calculix": "",
                                                      "459.GemsFDTD": "", "465.tonto": "",
                                                      "470.lbm": "",
                                                      "481.wrf": "", "482.sphinx3": "",
                                                      "SPECfp_2006": single_fp_SPECfp_2006},
                                             "peak": {"410.bwaves": multi_fp_410_bwaves, "416.gamess": multi_fp_416_gamess,
                                                      "433.milc": multi_fp_433_milc, "434.zeusmp": multi_fp_434_zeusmp,
                                                      "435.gromacs": multi_fp_435_gromacs,
                                                      "436.cactusADM": multi_fp_436_cactusADM,
                                                      "437.leslie3d": multi_fp_437_leslie3d,
                                                      "444.namd": multi_fp_444_namd, "447.dealII": multi_fp_447_dealII,
                                                      "450.soplex": multi_fp_450_soplex, "453.povray": multi_fp_453_povray,
                                                      "454.calculix": multi_fp_454_calculix,
                                                      "459.GemsFDTD": multi_fp_459_GemsFDTD,
                                                      "465.tonto": multi_fp_465_tonto,
                                                      "470.lbm": multi_fp_470_lbm,
                                                      "481.wrf": multi_fp_481_wrf, "482.sphinx3": multi_fp_482_sphinx3,
                                                      "SPECfp_2006": multi_fp_SPECfp_2006}}}}
    return data


def cpu2017_excel_to_json(file_path, sheet_name, end_number):
    """
    cpu2017表格转json数据
    :param file_path:
    :param sheet_name:
    :param end_number:
    :return:
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    columns = df.columns
    data = {}
    for index, column in enumerate(columns):
        if 3 < index < end_number + 4:
            column_data = df[column].tolist()
            execute_cmd = column_data[0]
            modify_parameters = column_data[1]
            single_int_rate_500_perlbench_r = column_data[2]
            single_int_rate_502_gcc_r = column_data[3]
            single_int_rate_505_mcf_r = column_data[4]
            single_int_rate_520_omnetpp_r = column_data[5]
            single_int_rate_523_xalancbmk_r = column_data[6]
            single_int_rate_525_x264_r = column_data[7]
            single_int_rate_531_deepsjeng_r = column_data[8]
            single_int_rate_541_leela_r = column_data[9]
            single_int_rate_548_exchange2_r = column_data[10]
            single_int_rate_557_xz_r = column_data[11]
            single_int_rate_SPECrate2017_int = column_data[12]
            single_fp_rate_503_bwaves_r = column_data[13]
            single_fp_rate_507_cactuBSSN_r = column_data[14]
            single_fp_rate_508_namd_r = column_data[15]
            single_fp_rate_510_parest_r = column_data[16]
            single_fp_rate_511_povray_r = column_data[17]
            single_fp_rate_519_lbm_r = column_data[18]
            single_fp_rate_521_wrf_r = column_data[19]
            single_fp_rate_526_blender_r = column_data[20]
            single_fp_rate_527_cam4_r = column_data[21]
            single_fp_rate_538_imagick_r = column_data[22]
            single_fp_rate_544_nab_r = column_data[23]
            single_fp_rate_549_fotonik3d_r = column_data[24]
            single_fp_rate_554_roms_r = column_data[25]
            single_fp_rate_PECrate2017_fp = column_data[26]
            multi_int_rate_500_perlbench_r = column_data[27]
            multi_int_rate_502_gcc_r = column_data[28]
            multi_int_rate_505_mcf_r = column_data[29]
            multi_int_rate_520_omnetpp_r = column_data[30]
            multi_int_rate_523_xalancbmk_r = column_data[31]
            multi_int_rate_525_x264_r = column_data[32]
            multi_int_rate_531_deepsjeng_r = column_data[33]
            multi_int_rate_541_leela_r = column_data[34]
            multi_int_rate_548_exchange2_r = column_data[35]
            multi_int_rate_557_xz_r = column_data[36]
            multi_int_rate_SPECrate2017_int = column_data[37]
            multi_fp_rate_503_bwaves_r = column_data[38]
            multi_fp_rate_507_cactuBSSN_r = column_data[39]
            multi_fp_rate_508_namd_r = column_data[40]
            multi_fp_rate_510_parest_r = column_data[41]
            multi_fp_rate_511_povray_r = column_data[42]
            multi_fp_rate_519_lbm_r = column_data[43]
            multi_fp_rate_521_wrf_r = column_data[44]
            multi_fp_rate_526_blender_r = column_data[45]
            multi_fp_rate_527_cam4_r = column_data[46]
            multi_fp_rate_538_imagick_r = column_data[47]
            multi_fp_rate_544_nab_r = column_data[48]
            multi_fp_rate_549_fotonik3d_r = column_data[49]
            multi_fp_rate_554_roms_r = column_data[50]
            multi_fp_rate_PECrate2017_fp = column_data[51]

            if sheet_name[12:16] == "base":
                data["cpu2017-%s-single-intrate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_int_rate": {
                         "base": {"500.perlbench_r": single_int_rate_500_perlbench_r,
                                  "502.gcc_r": single_int_rate_502_gcc_r,
                                  "505.mcf_r": single_int_rate_505_mcf_r,
                                  "520.omnetpp_r": single_int_rate_520_omnetpp_r,
                                  "523.xalancbmk_r": single_int_rate_523_xalancbmk_r,
                                  "525.x264_r": single_int_rate_525_x264_r,
                                  "531.deepsjeng_r": single_int_rate_531_deepsjeng_r,
                                  "541.leela_r": single_int_rate_541_leela_r,
                                  "548.exchange2_r": single_int_rate_548_exchange2_r,
                                  "557.xz_r": single_int_rate_557_xz_r,
                                  "SPECrate2017_int": single_int_rate_SPECrate2017_int},
                         "peak": {"500.perlbench_r": "", "502.gcc_r": "",
                                  "505.mcf_r": "", "520.omnetpp_r": "",
                                  "523.xalancbmk_r": "", "525.x264_r": "",
                                  "531.deepsjeng_r": "", "541.leela_r": "",
                                  "548.exchange2_r": "", "557.xz_r": "",
                                  "SPECrate2017_int": ""}}}}

                data["cpu2017-%s-single-fprate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_fp_rate": {
                         "base": {"503.bwaves_r": single_fp_rate_503_bwaves_r,
                                  "507.cactuBSSN_r": single_fp_rate_507_cactuBSSN_r,
                                  "508.namd_r": single_fp_rate_508_namd_r,
                                  "510.parest_r": single_fp_rate_510_parest_r,
                                  "511.povray_r": single_fp_rate_511_povray_r,
                                  "519.lbm_r": single_fp_rate_519_lbm_r,
                                  "521.wrf_r": single_fp_rate_521_wrf_r,
                                  "526.blender_r": single_fp_rate_526_blender_r,
                                  "527.cam4_r": single_fp_rate_527_cam4_r,
                                  "538.imagick_r": single_fp_rate_538_imagick_r,
                                  "544.nab_r": single_fp_rate_544_nab_r,
                                  "549.fotonik3d_r": single_fp_rate_549_fotonik3d_r,
                                  "554.roms_r": single_fp_rate_554_roms_r,
                                  "SPECrate2017_fp": single_fp_rate_PECrate2017_fp},
                         "peak": {"503.bwaves_r": "", "507.cactuBSSN_r": "",
                                  "508.namd_r": "", "510.parest_r": "", "511.povray_r": "", "519.lbm_r": "",
                                  "521.wrf_r": "", "526.blender_r": "", "527.cam4_r": "", "538.imagick_r": "",
                                  "544.nab_r": "", "549.fotonik3d_r": "", "554.roms_r": "", "SPECrate2017_fp": ""}}}}
                data["cpu2017-%s-multi-intrate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_int_rate": {
                         "base": {"500.perlbench_r": multi_int_rate_500_perlbench_r,
                                  "502.gcc_r": multi_int_rate_502_gcc_r,
                                  "505.mcf_r": multi_int_rate_505_mcf_r,
                                  "520.omnetpp_r": multi_int_rate_520_omnetpp_r,
                                  "523.xalancbmk_r": multi_int_rate_523_xalancbmk_r,
                                  "525.x264_r": multi_int_rate_525_x264_r,
                                  "531.deepsjeng_r": multi_int_rate_531_deepsjeng_r,
                                  "541.leela_r": multi_int_rate_541_leela_r,
                                  "548.exchange2_r": multi_int_rate_548_exchange2_r,
                                  "557.xz_r": multi_int_rate_557_xz_r,
                                  "SPECrate2017_int": multi_int_rate_SPECrate2017_int},
                         "peak": {"500.perlbench_r": "", "502.gcc_r": "", "505.mcf_r": "", "520.omnetpp_r": "",
                                  "523.xalancbmk_r": "", "525.x264_r": "", "531.deepsjeng_r": "", "541.leela_r": "",
                                  "548.exchange2_r": "", "557.xz_r": "", "SPECrate2017_int": ""}}}}

                data["cpu2017-%s-multi-fprate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_fp_rate": {"base": {"503.bwaves_r": multi_fp_rate_503_bwaves_r,
                                                           "507.cactuBSSN_r": multi_fp_rate_507_cactuBSSN_r,
                                                           "508.namd_r": multi_fp_rate_508_namd_r,
                                                           "510.parest_r": multi_fp_rate_510_parest_r,
                                                           "511.povray_r": multi_fp_rate_511_povray_r,
                                                           "519.lbm_r": multi_fp_rate_519_lbm_r,
                                                           "521.wrf_r": multi_fp_rate_521_wrf_r,
                                                           "526.blender_r": multi_fp_rate_526_blender_r,
                                                           "527.cam4_r": multi_fp_rate_527_cam4_r,
                                                           "538.imagick_r": multi_fp_rate_538_imagick_r,
                                                           "544.nab_r": multi_fp_rate_544_nab_r,
                                                           "549.fotonik3d_r": multi_fp_rate_549_fotonik3d_r,
                                                           "554.roms_r": multi_fp_rate_554_roms_r,
                                                           "SPECrate2017_fp": multi_fp_rate_PECrate2017_fp},
                                                  "peak": {"503.bwaves_r": "", "507.cactuBSSN_r": "", "508.namd_r": "",
                                                           "510.parest_r": "", "511.povray_r": "", "519.lbm_r": "",
                                                           "521.wrf_r": "", "526.blender_r": "", "527.cam4_r": "",
                                                           "538.imagick_r": "", "544.nab_r": "", "549.fotonik3d_r": "",
                                                           "554.roms_r": "", "SPECrate2017_fp": ""}}}}
            elif sheet_name[12:16] == "peak":
                data["cpu2017-%s-single-intrate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_int_rate": {
                         "base": {"500.perlbench_r": "", "502.gcc_r": "", "505.mcf_r": "", "520.omnetpp_r": "",
                                  "523.xalancbmk_r": "", "525.x264_r": "", "531.deepsjeng_r": "", "541.leela_r": "",
                                  "548.exchange2_r": "", "557.xz_r": "", "SPECrate2017_int": ""},
                         "peak": {"500.perlbench_r": single_int_rate_500_perlbench_r,
                                  "502.gcc_r": single_int_rate_502_gcc_r,
                                  "505.mcf_r": single_int_rate_505_mcf_r,
                                  "520.omnetpp_r": single_int_rate_520_omnetpp_r,
                                  "523.xalancbmk_r": single_int_rate_523_xalancbmk_r,
                                  "525.x264_r": single_int_rate_525_x264_r,
                                  "531.deepsjeng_r": single_int_rate_531_deepsjeng_r,
                                  "541.leela_r": single_int_rate_541_leela_r,
                                  "548.exchange2_r": single_int_rate_548_exchange2_r,
                                  "557.xz_r": single_int_rate_557_xz_r,
                                  "SPECrate2017_int": single_int_rate_SPECrate2017_int}}}}

                data["cpu2017-%s-single-fprate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"单线程_fp_rate": {
                         "base": {"503.bwaves_r": "", "507.cactuBSSN_r": "", "508.namd_r": "", "510.parest_r": "",
                                  "511.povray_r": "", "519.lbm_r": "", "521.wrf_r": "", "526.blender_r": "",
                                  "527.cam4_r": "", "538.imagick_r": "", "544.nab_r": "", "549.fotonik3d_r": "",
                                  "554.roms_r": "", "SPECrate2017_fp": ""},
                         "peak": {"503.bwaves_r": single_fp_rate_503_bwaves_r,
                                  "507.cactuBSSN_r": single_fp_rate_507_cactuBSSN_r,
                                  "508.namd_r": single_fp_rate_508_namd_r,
                                  "510.parest_r": single_fp_rate_510_parest_r,
                                  "511.povray_r": single_fp_rate_511_povray_r,
                                  "519.lbm_r": single_fp_rate_519_lbm_r, "521.wrf_r": single_fp_rate_521_wrf_r,
                                  "526.blender_r": single_fp_rate_526_blender_r,
                                  "527.cam4_r": single_fp_rate_527_cam4_r,
                                  "538.imagick_r": single_fp_rate_538_imagick_r,
                                  "544.nab_r": single_fp_rate_544_nab_r,
                                  "549.fotonik3d_r": single_fp_rate_549_fotonik3d_r,
                                  "554.roms_r": single_fp_rate_554_roms_r,
                                  "SPECrate2017_fp": single_fp_rate_PECrate2017_fp}}}}

                data["cpu2017-%s-multi-intrate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_int_rate": {
                         "base": {"500.perlbench_r": "", "502.gcc_r": "", "505.mcf_r": "", "520.omnetpp_r": "",
                                  "523.xalancbmk_r": "", "525.x264_r": "", "531.deepsjeng_r": "", "541.leela_r": "",
                                  "548.exchange2_r": "", "557.xz_r": "", "SPECrate2017_int": ""},
                         "peak": {"500.perlbench_r": multi_int_rate_500_perlbench_r,
                                  "502.gcc_r": multi_int_rate_502_gcc_r,
                                  "505.mcf_r": multi_int_rate_505_mcf_r, "520.omnetpp_r": multi_int_rate_520_omnetpp_r,
                                  "523.xalancbmk_r": multi_int_rate_523_xalancbmk_r,
                                  "525.x264_r": multi_int_rate_525_x264_r,
                                  "531.deepsjeng_r": multi_int_rate_531_deepsjeng_r,
                                  "541.leela_r": multi_int_rate_541_leela_r,
                                  "548.exchange2_r": multi_int_rate_548_exchange2_r,
                                  "557.xz_r": multi_int_rate_557_xz_r,
                                  "SPECrate2017_int": multi_int_rate_SPECrate2017_int}}}}

                data["cpu2017-%s-multi-fprate-0-" % (sheet_name[12:16]) + str(index - 3)] = \
                    {"execute_cmd": execute_cmd, "modify_parameters": modify_parameters, "tool_name": "speccpu2006",
                     "items": {"多线程_fp_rate": {
                         "base": {"503.bwaves_r": "", "507.cactuBSSN_r": "", "508.namd_r": "", "510.parest_r": "",
                                  "511.povray_r": "", "519.lbm_r": "", "521.wrf_r": "", "526.blender_r": "",
                                  "527.cam4_r": "", "538.imagick_r": "", "544.nab_r": "", "549.fotonik3d_r": "",
                                  "554.roms_r": "", "SPECrate2017_fp": ""},
                         "peak": {"503.bwaves_r": multi_fp_rate_503_bwaves_r,
                                  "507.cactuBSSN_r": multi_fp_rate_507_cactuBSSN_r,
                                  "508.namd_r": multi_fp_rate_508_namd_r,
                                  "510.parest_r": multi_fp_rate_510_parest_r,
                                  "511.povray_r": multi_fp_rate_511_povray_r,
                                  "519.lbm_r": multi_fp_rate_519_lbm_r,
                                  "521.wrf_r": multi_fp_rate_521_wrf_r,
                                  "526.blender_r": multi_fp_rate_526_blender_r,
                                  "527.cam4_r": multi_fp_rate_527_cam4_r,
                                  "538.imagick_r": multi_fp_rate_538_imagick_r,
                                  "544.nab_r": multi_fp_rate_544_nab_r,
                                  "549.fotonik3d_r": multi_fp_rate_549_fotonik3d_r,
                                  "554.roms_r": multi_fp_rate_554_roms_r,
                                  "SPECrate2017_fp": multi_fp_rate_PECrate2017_fp}}}}
    return data


def replace_nan_with_empty_string(data):
    """
     递归函数，将字典中所有的 NaN 替换为一个空字符串
    :param data:
    :return:
    """
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace_nan_with_empty_string(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace_nan_with_empty_string(data[i])
    elif pd.isna(data):
        data = ""
    return data


env_data = env_excel_to_json(user_data['file_path'], "性能测试环境", user_data['disk_number'], user_data['nic_number'])
all_json_data = {**env_data, **{"time": time.time()}}

for sheet_name in user_data['sheet_names']:
    if sheet_name == "Stream":
        print('Stream 数据--------')
        stream_data = stream_excel_to_json(user_data['file_path'], sheet_name, user_data['stream_end_number'])
        all_json_data = {**all_json_data, **stream_data}
    elif sheet_name == "Lmbench":
        print('Lmbench 数据--------')
        lmbench_data = lmbench_excel_to_json(user_data['file_path'], sheet_name, user_data['lmbench_end_number'])
        all_json_data = {**all_json_data, **lmbench_data}
    elif sheet_name == "Unixbench":
        print('Unixbench 数据--------')
        unixbench_data = unixbench_excel_to_json(user_data['file_path'], sheet_name, user_data['unixbench_end_number'])
        all_json_data = {**all_json_data, **unixbench_data}
    elif sheet_name == "Fio":
        print('Fio 数据--------')
        fio_data = fio_excel_to_json(user_data['file_path'], sheet_name, user_data['fio_end_number'])
        all_json_data = {**all_json_data, **fio_data}
    elif sheet_name == "Iozone":
        print('Iozone 数据--------')
        iozone_data = iozone_excel_to_json(user_data['file_path'], sheet_name, user_data['iozone_end_number'])
        all_json_data = {**all_json_data, **iozone_data}
    elif sheet_name == "Specjvm2008":
        print('Specjvm2008 数据--------')
        jvm2008_data = jvm2008_excel_to_json(user_data['file_path'], sheet_name, user_data['jvm2008_end_number'])
        all_json_data = {**all_json_data, **jvm2008_data}
    elif sheet_name == "Speccpu2006(base)":
        print('Speccpu2006(base) 数据--------')
        cpu2006_base_data = cpu2006_excel_to_json(user_data['file_path'], sheet_name, user_data['cpu2006_end_number'])
        all_json_data = {**all_json_data, **cpu2006_base_data}
    elif sheet_name == "Speccpu2006(peak)":
        print('Speccpu2006(peak) 数据--------')
        cpu2006_peak_data = cpu2006_excel_to_json(user_data['file_path'], sheet_name, user_data['cpu2006_end_number'])
        all_json_data = {**all_json_data, **cpu2006_peak_data}
    elif sheet_name == "Speccpu2017(base)":
        print('Speccpu2017(base) 数据--------')
        cpu2017_base_data = cpu2017_excel_to_json(user_data['file_path'], sheet_name, user_data['cpu2017_end_number'])
        all_json_data = {**all_json_data, **cpu2017_base_data}
    elif sheet_name == "Speccpu2017(peak)":
        print('Speccpu2017(peak) 数据--------')
        cpu2017_peak_data = cpu2017_excel_to_json(user_data['file_path'], sheet_name, user_data['cpu2017_end_number'])
        all_json_data = {**all_json_data, **cpu2017_peak_data}

all_json_data = replace_nan_with_empty_string(all_json_data)

with open(user_data['all_json_file'], "w+", encoding="utf-8") as f_new:
    json.dump(all_json_data, f_new)

print('数据获取完成')
