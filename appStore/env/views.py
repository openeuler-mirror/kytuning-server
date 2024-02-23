from base64 import b64decode
from django.http import JsonResponse, request, HttpRequest
# Create your views here.
from rest_framework import status
from appStore.env.serializers import EnvSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet

class EnvViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    # queryset = Stream.objects.all().order_by('id')
    serializer_class = EnvSerializer
    # pagination_class = LimsPageSet

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
        serializer_env = self.get_serializer(data=data_env)
        # env_id = ''
        request.data['env_id'] = ''
        if serializer_env.is_valid():
            # todo 放开
            # self.perform_create(serializer_env)
            # todo 查到当前数据的id供后面使用
            request.data['env_id'] = 2
        if serializer_env.errors:
            return json_response(serializer_env.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_env))
        if not request.data['env_id']:
            return json_response({}, status.HTTP_400_BAD_REQUEST, '没有env_id')

        return json_response({}, status.HTTP_200_OK, '创建成功！')
