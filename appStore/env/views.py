"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 14:07:53 2024 +0800
"""
import os
import json
from base64 import b64decode

from django.http import HttpRequest

# Create your views here.
from rest_framework import status

from appStore.env.models import Env
from appStore.env.serializers import EnvSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet

class EnvViewSet(CusModelViewSet):
    """
    env数据管理
    """
    queryset = Env.objects.all().order_by('id')
    serializer_class = EnvSerializer
    pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        """
        返回列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        env_id = request.GET.get('env_id')
        # comparsionIds = request.GET.get('comparsionIds')
        # comparsionIds = comparsionIds.split(',')
        queryset = Env.objects.filter(id=env_id).all()
        serializer = self.get_serializer(queryset, many=True)
        data_ = serializer.data[0]

        # 处理disk、nicinfo数据
        disk_and_nicinfo_datas = []
        for value in eval(data_['hwinfo_disk']):
            disk = [{'column1': 'hwinfo', 'column2': 'disk', 'column3': 'name','column4': value['name']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'part_type', 'column4': value['part_type']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'vendor', 'column4': value['vendor']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'model', 'column4': value['model']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'size', 'column4': value['size']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'rota', 'column4': value['rota']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'sched', 'column4': value['sched']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'rq_size', 'column4': value['rq_size']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'tran', 'column4': value['tran']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'mntpoint=/', 'column4': value['mntpoint=/']},
                    {'column1': 'hwinfo', 'column2': 'disk', 'column3': 'mntpoint=/home', 'column4': value['mntpoint=/home']},
                    ]
            disk_and_nicinfo_datas.extend(disk)

        for value in eval(data_['hwinfo_nicinfo']):
            nicinfo = [{'column1': 'hwinfo', 'column2': 'nicinfo', 'column3': 'logicalname','column4': value['logicalname']},
                    {'column1': 'hwinfo', 'column2': 'nicinfo', 'column3': 'product', 'column4': value['product']},
                    {'column1': 'hwinfo', 'column2': 'nicinfo', 'column3': 'speed', 'column4': value['speed']},]
            disk_and_nicinfo_datas.extend(nicinfo)

        # 处理多组nic数据
        nic_datas = []
        for value in eval(data_['nwinfo_nic']):
            nic = [
                {'column1': 'nwinfo', 'column2': 'nic', 'column3': 'nicname', 'column4': value['nicname']},
                {'column1': 'nwinfo', 'column2': 'nic', 'column3': 'ip', 'column4': value['ip']},
                {'column1': 'nwinfo', 'column2': 'nic', 'column3': 'hwaddr', 'column4': value['hwaddr']},
                {'column1': 'nwinfo', 'column2': 'nic', 'column3': 'gateway', 'column4': value['gateway']},
                {'column1': 'nwinfo', 'column2': 'nic', 'column3': 'mtu', 'column4': value['mtu']},
            ]
            nic_datas.extend(nic)

        datas = [{'column1': 'hwinfo','column2': 'machineinfo','column3': 'manufacturer','column4': data_['hwinfo_machineinfo_manufacturer']},
            {'column1': 'hwinfo', 'column2': 'machineinfo', 'column3': 'product','column4': data_['hwinfo_machineinfo_product']},
            {'column1': 'hwinfo','column2': 'machineinfo','column3': 'serialnumber','column4': data_['hwinfo_machineinfo_serialnumber']},
            {'column1': 'hwinfo', 'column2': 'bios', 'column3': 'vendor', 'column4': data_['hwinfo_bios_vendor']},
            {'column1': 'hwinfo', 'column2': 'bios', 'column3': 'version', 'column4': data_['hwinfo_bios_version']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'Vendor ID', 'column4': data_['hwinfo_cpu_Vendor_ID']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'CPU family', 'column4': data_['hwinfo_cpu_CPU_family']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'model_name', 'column4': data_['hwinfo_cpu_model_name']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'CPU MHz', 'column4': data_['hwinfo_cpu_CPU_MHz']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'CPU(s)', 'column4': data_['hwinfo_cpu_CPUs']},
            {'column1': 'hwinfo','column2': 'cpu','column3': 'Thread(s) per core','column4': data_['hwinfo_cpu_Threads_per_core']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'CPU Arch', 'column4': data_['hwinfo_cpu_CPU_Arch']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'CPU op-mode', 'column4': data_['hwinfo_cpu_CPU_op_mode']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'Byte Order', 'column4': data_['hwinfo_cpu_Byte_Order']},
            {'column1': 'hwinfo','column2': 'cpu','column3': 'On-line CPU(s) list','column4': data_['hwinfo_cpu_On_line_CPUs_list']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'Virtualization', 'column4': data_['hwinfo_cpu_Virtualization']},
            {'column1': 'hwinfo','column2': 'cpu','column3': 'Virtualization type','column4': data_['hwinfo_cpu_Virtualization_type']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'L1d cache:', 'column4': data_['hwinfo_cpu_L1d_cache']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'L1i cache', 'column4': data_['hwinfo_cpu_L1i_cache']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'L2 cache', 'column4': data_['hwinfo_cpu_L2_cache']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'L3 cache', 'column4': data_['hwinfo_cpu_L3_cache']},
            {'column1': 'hwinfo', 'column2': 'cpu', 'column3': 'Flags', 'column4': data_['hwinfo_memory_Flags']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'vendor', 'column4': data_['hwinfo_memory_vendor']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'mem_type', 'column4': data_['hwinfo_memory_mem_type']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'total_size', 'column4': data_['hwinfo_memory_total_size']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'mem_used', 'column4': data_['hwinfo_memory_mem_used']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'mem_count', 'column4': data_['hwinfo_memory_mem_count']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'mem_free', 'column4': data_['hwinfo_memory_mem_free']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'mem_freq', 'column4': data_['hwinfo_memory_mem_freq']},
            {'column1': 'hwinfo', 'column2': 'memory', 'column3': 'swap', 'column4': data_['hwinfo_memory_swap']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'curr UTC time', 'column4': data_['swinfo_os_curr_UTC_time']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'os_id', 'column4': data_['swinfo_os_os_id']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'os_arch', 'column4': data_['swinfo_os_os_arch']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'osversion', 'column4': data_['swinfo_os_osversion']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'kernel', 'column4': data_['swinfo_os_kernel']},
            {'column1': 'swinfo', 'column2': 'os', 'column3': 'grub', 'column4': data_['swinfo_os_grub']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'sysconf', 'column4': data_['swinfo_runtime_sysconf']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'sysctl', 'column4': data_['swinfo_runtime_sysctl']},
            {'column1': 'swinfo','column2': 'runtime','column3': 'systemctlinfo','column4': data_['swinfo_runtime_systemctlinfo']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'driverinfo', 'column4': data_['swinfo_runtime_driverinfo']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'rpmlist', 'column4': data_['swinfo_runtime_rpmlist']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'ipclist', 'column4': data_['swinfo_runtime_ipclist']},
            {'column1': 'swinfo','column2': 'runtime','column3': 'selinux_status','column4': data_['swinfo_runtime_selinux_status']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'power_status','column4': data_['swinfo_runtime_power_status']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'cpu_sched', 'column4': data_['swinfo_runtime_cpu_sched']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'loadavg', 'column4': data_['swinfo_runtime_loadavg']},
            {'column1': 'swinfo', 'column2': 'runtime', 'column3': 'uptime', 'column4': data_['swinfo_runtime_uptime']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'gccversion','column4': data_['swinfo_software_ver_gccversion']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'glibcversion','column4': data_['swinfo_software_ver_glibcversion']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'javaversion','column4': data_['swinfo_software_ver_javaversion']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'g++version','column4': data_['swinfo_software_ver_g_version']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'gfortranversion','column4': data_['swinfo_software_ver_gfortranversion']},
            {'column1': 'swinfo','column2': 'software_ver','column3': 'pythonversion','column4': data_['swinfo_software_ver_pythonversion']},
           ]
        datas[30:30] = disk_and_nicinfo_datas
        datas.extend(nic_datas)
        env_data = {'data': datas}
        return json_response(env_data, status.HTTP_200_OK, '列表')


    def create(self, request, *args, **kwargs):
        """
            接收json文件，创建所有数据
            :param request:
            :param args:
            :param kwargs:
            :return:
        """
        """环境数据处理"""
        data_env = {}
        data_env['time'] = request.data['time']
        #查数据库中是否有这条数据，如果有返回对应数据对应的时间戳
        filter_env = Env.objects.filter(time=data_env['time'])
        # if filter_env:
        #     return json_response({'env_id':filter_env[0].id}, status.HTTP_400_BAD_REQUEST, '该数据在环境信息表中已存入')

        data_env['hwinfo_machineinfo_manufacturer'] = request.data['envinfo']['hwinfo']['machineinfo']['manufacturer']
        data_env['hwinfo_machineinfo_product'] = request.data['envinfo']['hwinfo']['machineinfo']['product']
        data_env['hwinfo_machineinfo_serialnumber'] = request.data['envinfo']['hwinfo']['machineinfo']['serialnumber']
        data_env['hwinfo_bios_vendor'] = request.data['envinfo']['hwinfo']['bios']['vendor']
        data_env['hwinfo_bios_version'] = request.data['envinfo']['hwinfo']['bios']['version']
        data_env['hwinfo_cpu_Vendor_ID'] = request.data['envinfo']['hwinfo']['cpu']['Vendor ID']
        data_env['hwinfo_cpu_CPU_family'] = request.data['envinfo']['hwinfo']['cpu']['CPU family']
        data_env['hwinfo_cpu_model_name'] = request.data['envinfo']['hwinfo']['cpu']['model_name']
        data_env['hwinfo_cpu_CPU_MHz'] = request.data['envinfo']['hwinfo']['cpu']['CPU MHz']
        data_env['hwinfo_cpu_CPUs'] = request.data['envinfo']['hwinfo']['cpu']['CPU(s)']
        data_env['hwinfo_cpu_Threads_per_core'] = request.data['envinfo']['hwinfo']['cpu']['Thread(s) per core']
        data_env['hwinfo_cpu_CPU_Arch'] = request.data['envinfo']['hwinfo']['cpu']['CPU Arch']
        data_env['hwinfo_cpu_CPU_op_mode'] = request.data['envinfo']['hwinfo']['cpu']['CPU op-mode']
        data_env['hwinfo_cpu_Byte_Order'] = request.data['envinfo']['hwinfo']['cpu']['Byte Order']
        data_env['hwinfo_cpu_On_line_CPUs_list'] = request.data['envinfo']['hwinfo']['cpu']['On-line CPU(s) list']
        data_env['hwinfo_cpu_Virtualization'] = request.data['envinfo']['hwinfo']['cpu']['Virtualization']
        data_env['hwinfo_cpu_Virtualization_type'] = request.data['envinfo']['hwinfo']['cpu']['Virtualization type']
        data_env['hwinfo_cpu_L1d_cache'] = request.data['envinfo']['hwinfo']['cpu']['L1d cache:']
        data_env['hwinfo_cpu_L1i_cache'] = request.data['envinfo']['hwinfo']['cpu']['L1i cache']
        data_env['hwinfo_cpu_L2_cache'] = request.data['envinfo']['hwinfo']['cpu']['L2 cache']
        data_env['hwinfo_cpu_L3_cache'] = request.data['envinfo']['hwinfo']['cpu']['L3 cache']
        data_env['hwinfo_memory_Flags'] = request.data['envinfo']['hwinfo']['cpu']['Flags']
        data_env['hwinfo_memory_vendor'] = request.data['envinfo']['hwinfo']['memory']['vendor']
        data_env['hwinfo_memory_mem_type'] = request.data['envinfo']['hwinfo']['memory']['mem_type']
        data_env['hwinfo_memory_total_size'] = request.data['envinfo']['hwinfo']['memory']['total_size']
        data_env['hwinfo_memory_mem_used'] = request.data['envinfo']['hwinfo']['memory']['mem_used']
        data_env['hwinfo_memory_mem_count'] = request.data['envinfo']['hwinfo']['memory']['mem_count']
        data_env['hwinfo_memory_mem_free'] = request.data['envinfo']['hwinfo']['memory']['mem_free']
        data_env['hwinfo_memory_mem_freq'] = request.data['envinfo']['hwinfo']['memory']['mem_freq']
        data_env['hwinfo_memory_swap'] = request.data['envinfo']['hwinfo']['memory']['swap']
        data_env['hwinfo_disk'] = str(request.data['envinfo']['hwinfo']['disk'])
        data_env['hwinfo_nicinfo'] = str(request.data['envinfo']['hwinfo']['nicinfo'])
        data_env['swinfo_os_curr_UTC_time'] = request.data['envinfo']['swinfo']['os']['curr UTC time']
        data_env['swinfo_os_os_id'] = request.data['envinfo']['swinfo']['os']['os_id']
        data_env['swinfo_os_os_arch'] = request.data['envinfo']['swinfo']['os']['os_arch']
        data_env['swinfo_os_osversion'] = request.data['envinfo']['swinfo']['os']['osversion']
        data_env['swinfo_os_kernel'] = request.data['envinfo']['swinfo']['os']['kernel']
        data_env['swinfo_os_grub'] = request.data['envinfo']['swinfo']['os']['grub']
        data_env['swinfo_runtime_sysconf'] = b64decode(request.data['envinfo']['swinfo']['runtime']['sysctl']).decode(
            "ascii")
        data_env['swinfo_runtime_sysctl'] = b64decode(request.data['envinfo']['swinfo']['runtime']['sysconf']).decode(
            "ascii")
        data_env['swinfo_runtime_systemctlinfo'] = b64decode(
            request.data['envinfo']['swinfo']['runtime']['systemctlinfo']).decode("ascii")
        data_env['swinfo_runtime_driverinfo'] = b64decode(
            request.data['envinfo']['swinfo']['runtime']['driverinfo']).decode("ascii")
        data_env['swinfo_runtime_rpmlist'] = b64decode(request.data['envinfo']['swinfo']['runtime']['rpmlist']).decode(
            "ascii")
        data_env['swinfo_runtime_ipclist'] = b64decode(request.data['envinfo']['swinfo']['runtime']['ipclist']).decode(
            "ascii")
        data_env['swinfo_runtime_selinux_status'] = request.data['envinfo']['swinfo']['runtime']['selinux_status']
        data_env['swinfo_runtime_power_status'] = request.data['envinfo']['swinfo']['runtime']['power_status']
        data_env['swinfo_runtime_cpu_sched'] = request.data['envinfo']['swinfo']['runtime']['cpu_sched']
        data_env['swinfo_runtime_loadavg'] = request.data['envinfo']['swinfo']['runtime']['loadavg']
        data_env['swinfo_runtime_uptime'] = request.data['envinfo']['swinfo']['runtime']['uptime']
        data_env['swinfo_software_ver_gccversion'] = request.data['envinfo']['swinfo']['software_ver']['gccversion']
        data_env['swinfo_software_ver_glibcversion'] = request.data['envinfo']['swinfo']['software_ver']['glibcversion']
        data_env['swinfo_software_ver_javaversion'] = request.data['envinfo']['swinfo']['software_ver']['javaversion']
        data_env['swinfo_software_ver_g_version'] = request.data['envinfo']['swinfo']['software_ver']['g++version']
        data_env['swinfo_software_ver_gfortranversion'] = request.data['envinfo']['swinfo']['software_ver'][
            'gfortranversion']
        data_env['swinfo_software_ver_pythonversion'] = request.data['envinfo']['swinfo']['software_ver'][
            'pythonversion']
        data_env['nwinfo_nic'] = str(request.data['envinfo']['nwinfo']['nic'])
        serializer_env = self.get_serializer(data=data_env)
        request.data['env_id'] = '1'
        if serializer_env.is_valid():
            self.perform_create(serializer_env)
            request.data['env_id'] = serializer_env.data['id']
            # wqz
            # request.data['env_id'] = 1
        if serializer_env.errors:
            return json_response(serializer_env.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_env))
        if not request.data['env_id']:
            return json_response({}, status.HTTP_400_BAD_REQUEST, '没有env_id')

        """保存all_json文件"""
        json_file_path = '/var/www/html/all_json_data_file/'
        folder_path = os.path.dirname(json_file_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = '%s.json' % (data_env['time'])
        with open(json_file_path + file_name, 'w') as file:
            json.dump(request.data, file)

        project_message = []

        """stream数据处理"""
        from appStore.stream.views import StreamViewSet
        request_stream = HttpRequest()
        request_stream.method = 'POST'
        request_stream.data_stream = request.data
        StreamViewSet = StreamViewSet()
        stream_message = StreamViewSet.create(request=request_stream, *args, **kwargs)
        if stream_message:
            project_message.append({"stream": json.loads(stream_message.content.decode('utf-8'))['data']})

        """lmbench数据处理"""
        from appStore.lmbench.views import LmbenchViewSet
        request_unixbench = HttpRequest()
        request_unixbench.method = 'POST'
        request_unixbench.data_lmbench = request.data
        LmbenchViewSet = LmbenchViewSet()
        lmbench_message = LmbenchViewSet.create(request=request_unixbench, *args, **kwargs)
        if lmbench_message:
            project_message.append({"lmbench": json.loads(lmbench_message.content.decode('utf-8'))['data']})

        """unixbench数据处理"""
        from appStore.unixbench.views import UnixbenchViewSet
        request_unixbench = HttpRequest()
        request_unixbench.method = 'POST'
        request_unixbench.data_unixbench = request.data
        UnixbenchViewSet = UnixbenchViewSet()
        unixbench_message = UnixbenchViewSet.create(request=request_unixbench, *args, **kwargs)
        if unixbench_message:
            project_message.append({"unixbench": json.loads(unixbench_message.content.decode('utf-8'))['data']})

        """fio数据处理"""
        from appStore.fio.views import FioViewSet
        request_fio = HttpRequest()
        request_fio.method = 'POST'
        request_fio.data_fio = request.data
        FioViewSet = FioViewSet()
        fio_message = FioViewSet.create(request=request_fio, *args, **kwargs)
        if fio_message:
            project_message.append({"fio": json.loads(fio_message.content.decode('utf-8'))['data']})

        """iozone数据处理"""
        from appStore.iozone.views import IozoneViewSet
        request_iozone = HttpRequest()
        request_iozone.method = 'POST'
        request_iozone.data_iozone = request.data
        IozoneViewSet = IozoneViewSet()
        iozone_message = IozoneViewSet.create(request=request_iozone, *args, **kwargs)
        if iozone_message:
            project_message.append({"iozone": json.loads(iozone_message.content.decode('utf-8'))['data']})

        """jvm2008数据处理"""
        from appStore.jvm2008.views import Jvm2008ViewSet
        request_jvm2008 = HttpRequest()
        request_jvm2008.method = 'POST'
        request_jvm2008.data_jvm2008 = request.data
        Jvm2008ViewSet = Jvm2008ViewSet()
        jvm_message = Jvm2008ViewSet.create(request=request_jvm2008, *args, **kwargs)
        if jvm_message:
            project_message.append({"jvm2008": json.loads(jvm_message.content.decode('utf-8'))['data']})

        """speccpu2006数据处理"""
        from appStore.cpu2006.views import Cpu2006ViewSet
        request_cpu2006 = HttpRequest()
        request_cpu2006.method = 'POST'
        request_cpu2006.data_cpu2006 = request.data
        Cpu2006ViewSet = Cpu2006ViewSet()
        cpu2006_message = Cpu2006ViewSet.create(request=request_cpu2006, *args, **kwargs)
        if cpu2006_message:
            project_message.append({"cpu2006": json.loads(cpu2006_message.content.decode('utf-8'))['data']})

        """speccpu2017数据处理"""
        from appStore.cpu2017.views import Cpu2017ViewSet
        request_cpu2017 = HttpRequest()
        request_cpu2017.method = 'POST'
        request_cpu2017.data_cpu2017= request.data
        Cpu2017ViewSet = Cpu2017ViewSet()
        cpu2017_message =  Cpu2017ViewSet.create(request=request_cpu2017, *args, **kwargs)
        if cpu2017_message:
            project_message.append({"cpu2017": json.loads(cpu2017_message.content.decode('utf-8'))['data']})

        """project数据处理"""
        from appStore.project.views import ProjectViewSet
        request_project = HttpRequest()
        request_project.method = 'POST'
        request_project.data_project = request.data
        request_project.project_message = project_message
        ProjectViewSet = ProjectViewSet()
        ProjectViewSet.create(request=request_project, *args, **kwargs)

        return json_response({}, status.HTTP_200_OK, '创建成功！')

