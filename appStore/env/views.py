import json
from base64 import b64decode

from django.http import JsonResponse, request, HttpRequest
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from appStore.env.models import Env
from appStore.env.serializers import EnvSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet

class EnvViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Env.objects.all().order_by('id')
    serializer_class = EnvSerializer
    pagination_class = LimsPageSet

    def create(self, request, *args, **kwargs):
        """
            接收json文件，创建所有数据
            :param request:
            :param args:
            :param kwargs:
            :return:
        """
        """项目表处理"""
        """环境数据处理"""
        data_env = {}
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
        data_env['nwinfo_nic_nicname'] = str(request.data['envinfo']['nwinfo']['nic'])
        data_env['nwinfo_nic'] = str(request.data['envinfo']['nwinfo']['nic'])
        serializer_env = self.get_serializer(data=data_env)
        # env_id = ''
        request.data['env_id'] = ''
        if serializer_env.is_valid():
            # todo 放开
            self.perform_create(serializer_env)
            # todo 查到当前数据的id供后面使用
            request.data['env_id'] = 2
        if serializer_env.errors:
            return json_response(serializer_env.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_env))
        if not request.data['env_id']:
            return json_response({}, status.HTTP_400_BAD_REQUEST, '没有env_id')

        """project数据处理"""
        from appStore.project.views import ProjectViewSet
        request_project = HttpRequest()
        request_project.method = 'POST'
        request_project.data_project = request.data
        ProjectViewSet = ProjectViewSet()
        ProjectViewSet.create(request=request_project, *args, **kwargs)

        """fio数据处理"""
        from appStore.fio.views import FioViewSet
        request_fio = HttpRequest()
        request_fio.method = 'POST'
        request_fio.data_fio = request.data
        FioViewSet = FioViewSet()
        FioViewSet.create(request=request_fio, *args, **kwargs)

        """iozone数据处理"""
        from appStore.iozone.views import IozoneViewSet
        request_iozone = HttpRequest()
        request_iozone.method = 'POST'
        request_iozone.data_iozone = request.data
        IozoneViewSet = IozoneViewSet()
        IozoneViewSet.create(request=request_iozone, *args, **kwargs)


        """lmbench数据处理"""
        from appStore.lmbench.views import LmbenchViewSet
        request_unixbench = HttpRequest()
        request_unixbench.method = 'POST'
        request_unixbench.data_lmbench = request.data
        UnixbenchViewSet = LmbenchViewSet()
        UnixbenchViewSet.create(request=request_unixbench, *args, **kwargs)

        """speccpu2006数据处理"""
        from appStore.cpu2006.views import Cpu2006ViewSet
        request_cpu2006 = HttpRequest()
        request_cpu2006.method = 'POST'
        request_cpu2006.data_cpu2006 = request.data
        Cpu2006ViewSet = Cpu2006ViewSet()
        Cpu2006ViewSet.create(request=request_cpu2006, *args, **kwargs)

        """speccpu2017数据处理"""
        from appStore.cpu2017.views import Cpu2017ViewSet
        request_cpu2017 = HttpRequest()
        request_cpu2017.method = 'POST'
        request_cpu2017.data_cpu2017= request.data
        Cpu2017ViewSet = Cpu2017ViewSet()
        Cpu2017ViewSet.create(request=request_cpu2017, *args, **kwargs)

        """jvm2008数据处理"""
        from appStore.jvm2008.views import Jvm2008ViewSet
        request_jvm2008 = HttpRequest()
        request_jvm2008.method = 'POST'
        request_jvm2008.data_jvm2008 = request.data
        Jvm2008ViewSet = Jvm2008ViewSet()
        Jvm2008ViewSet.create(request=request_jvm2008, *args, **kwargs)

        """stream数据处理"""
        from appStore.stream.views import StreamViewSet
        request_stream = HttpRequest()
        request_stream.method = 'POST'
        request_stream.data_stream = request.data
        StreamViewSet = StreamViewSet()
        StreamViewSet.create(request=request_stream, *args, **kwargs)

        """unixbench数据处理"""
        from appStore.unixbench.views import UnixbenchViewSet
        request_unixbench = HttpRequest()
        request_unixbench.method = 'POST'
        request_unixbench.data_unixbench = request.data
        UnixbenchViewSet = UnixbenchViewSet()
        UnixbenchViewSet.create(request=request_unixbench, *args, **kwargs)

        return json_response({}, status.HTTP_200_OK, '创建成功！')

