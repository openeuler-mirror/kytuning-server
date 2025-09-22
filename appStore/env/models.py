"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 14:07:53 2024 +0800
"""
from django.db import models


# Create your models here.

class Env(models.Model):
    """环境信息表"""
    hwinfo_machineinfo_manufacturer = models.CharField(max_length=50, verbose_name='manufacturer',null=True,blank=True)
    hwinfo_machineinfo_product = models.CharField(max_length=50, verbose_name='product',null=True,blank=True)
    hwinfo_machineinfo_serialnumber = models.CharField(max_length=255, verbose_name='serialnumber')
    hwinfo_bios_vendor = models.CharField(max_length=50, verbose_name='vendor',null=True,blank=True)
    hwinfo_bios_version = models.CharField(max_length=50, verbose_name='version',null=True,blank=True)
    hwinfo_cpu_Vendor_ID = models.CharField(max_length=50, verbose_name='Vendor ID',null=True,blank=True)
    hwinfo_cpu_CPU_family = models.CharField(max_length=50, verbose_name='CPU family',null=True,blank=True)
    hwinfo_cpu_model_name = models.CharField(max_length=50, verbose_name='model_name',null=True,blank=True)
    hwinfo_cpu_CPU_MHz = models.TextField(verbose_name='CPU MHz',null=True,blank=True)
    hwinfo_cpu_CPUs = models.CharField(max_length=50, verbose_name='CPU(s)',null=True,blank=True)
    hwinfo_cpu_Threads_per_core = models.CharField(max_length=50, verbose_name='Thread(s) per core',null=True,blank=True)
    hwinfo_cpu_CPU_Arch = models.CharField(max_length=50, verbose_name='CPU Arch',null=True,blank=True)
    hwinfo_cpu_CPU_op_mode = models.CharField(max_length=50, verbose_name='CPU op-mode',null=True,blank=True)
    hwinfo_cpu_Byte_Order = models.CharField(max_length=50, verbose_name='Byte Order',null=True,blank=True)
    hwinfo_cpu_On_line_CPUs_list = models.CharField(max_length=50, verbose_name='On-line CPU(s) list',null=True,blank=True)
    hwinfo_cpu_Virtualization = models.CharField(max_length=50, verbose_name='Virtualization',null=True,blank=True)
    hwinfo_cpu_Virtualization_type = models.CharField(max_length=50, verbose_name='Virtualization type',null=True,blank=True)
    hwinfo_cpu_L1d_cache = models.CharField(max_length=50, verbose_name='L1d cache:',null=True,blank=True)
    hwinfo_cpu_L1i_cache = models.CharField(max_length=50, verbose_name='L1i cache',null=True,blank=True)
    hwinfo_cpu_L2_cache = models.CharField(max_length=50, verbose_name='L2 cache',null=True,blank=True)
    hwinfo_cpu_L3_cache = models.CharField(max_length=50, verbose_name='L3 cache',null=True,blank=True)
    hwinfo_memory_Flags = models.TextField(verbose_name='Flags',null=True,blank=True)
    hwinfo_memory_vendor = models.TextField(verbose_name='vendor',null=True,blank=True)
    hwinfo_memory_mem_type = models.CharField(max_length=50, verbose_name='mem_type',null=True,blank=True)
    hwinfo_memory_total_size = models.CharField(max_length=50, verbose_name='total_size',null=True,blank=True)
    hwinfo_memory_mem_used = models.CharField(max_length=50, verbose_name='mem_used',null=True,blank=True)
    hwinfo_memory_mem_count = models.CharField(max_length=50, verbose_name='mem_count',null=True,blank=True)
    hwinfo_memory_mem_free = models.CharField(max_length=50, verbose_name='mem_free',null=True,blank=True)
    hwinfo_memory_mem_freq = models.TextField(verbose_name='mem_freq',null=True,blank=True)
    hwinfo_memory_swap = models.CharField(max_length=50, verbose_name='swap',null=True,blank=True)
    hwinfo_disk = models.TextField(verbose_name='disk', default="",null=True,blank=True)
    hwinfo_nicinfo = models.TextField(verbose_name='nicinfo', default="",null=True,blank=True)
    swinfo_os_curr_UTC_time = models.CharField(max_length=50, verbose_name='curr UTC time',null=True,blank=True)
    swinfo_os_os_id = models.CharField(max_length=50, verbose_name='os_id',null=True,blank=True)
    swinfo_os_os_arch = models.CharField(max_length=50, verbose_name='os_arch',null=True,blank=True)
    swinfo_os_osversion = models.CharField(max_length=100, verbose_name='osversion',null=True,blank=True)
    swinfo_os_kernel = models.TextField(verbose_name='kernel',null=True,blank=True)
    swinfo_os_grub = models.TextField(verbose_name='grub',null=True,blank=True)
    swinfo_runtime_sysconf = models.TextField(verbose_name='sysconf',null=True,blank=True)
    swinfo_runtime_sysctl = models.TextField(verbose_name='sysctl',null=True,blank=True)
    swinfo_runtime_systemctlinfo = models.TextField(verbose_name='systemctlinfo',null=True,blank=True)
    swinfo_runtime_driverinfo = models.TextField(verbose_name='driverinfo',null=True,blank=True)
    swinfo_runtime_rpmlist = models.TextField(verbose_name='rpmlist',null=True,blank=True)
    swinfo_runtime_ipclist = models.TextField(verbose_name='ipclist',null=True,blank=True)
    swinfo_runtime_selinux_status = models.CharField(max_length=50, verbose_name='selinux_status',null=True,blank=True)
    swinfo_runtime_power_status = models.CharField(max_length=50, verbose_name='power_status',null=True,blank=True)
    swinfo_runtime_cpu_sched = models.CharField(max_length=50, verbose_name='cpu_sched',null=True,blank=True)
    swinfo_runtime_loadavg = models.CharField(max_length=50, verbose_name='loadavg',null=True,blank=True)
    swinfo_runtime_uptime = models.CharField(max_length=50, verbose_name='uptime',null=True,blank=True)
    swinfo_software_ver_gccversion = models.CharField(max_length=50, verbose_name='gccversion',null=True,blank=True)
    swinfo_software_ver_glibcversion = models.CharField(max_length=50, verbose_name='glibcversion',null=True,blank=True)
    swinfo_software_ver_javaversion = models.TextField(verbose_name='javaversion',null=True,blank=True)
    swinfo_software_ver_g_version = models.CharField(max_length=50, verbose_name='g++version',null=True,blank=True)
    swinfo_software_ver_gfortranversion = models.CharField(max_length=300, verbose_name='gfortranversion',null=True,blank=True)
    swinfo_software_ver_pythonversion = models.CharField(max_length=50, verbose_name='pythonversion',null=True,blank=True)
    nwinfo_nic = models.TextField(verbose_name='nic', default="")
    time= models.CharField(max_length=50, verbose_name='时间戳')

    class Meta:
        db_table = 'env'
