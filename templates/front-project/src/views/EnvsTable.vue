<template>
  <div>
    <el-table
        :data="tableDatas"
        :span-method="objectSpanMethod"
        border
        style="width: 100%; margin-top: 20px">
      <el-table-column
          prop="first"
          label="一级字段"
          width="100">
      </el-table-column>
      <el-table-column
          prop="second"
          label="二级字段"
      width="150">
      </el-table-column>
      <el-table-column
          prop="third"
          label="三级字段"
      width="180">
      </el-table-column>
      <el-table-column
          prop="fourth"
          label="值"
      >
        <!--          showOverflowTooltip="true">-->
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
import {ElTable, ElTableColumn} from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
  },
  data() {
    return {
      disk_datas: [],      //后期把disk、nic等都放到这里面，下面在遍历  disk目前写两个
      nicinfo_datas: [],      //后期把disk、nic等都放到这里面，下面在遍历  1个
      nwinfo_nic_datas: [],      //后期把disk、nic等都放到这里面，下面在遍历  1个
      env_datas: {
        hwinfo_machineinfo_manufacturer: '',
        hwinfo_machineinfo_product: '',
        hwinfo_machineinfo_serialnumber: '',
        hwinfo_bios_vendor: '',
        hwinfo_bios_version: '',
        hwinfo_cpu_Vendor_ID: '',
        hwinfo_cpu_CPU_family: '',
        hwinfo_cpu_model_name: '',
        hwinfo_cpu_CPU_MHz: '',
        hwinfo_cpu_CPUs: '',
        hwinfo_cpu_Threads_per_core: '',
        hwinfo_cpu_CPU_Arch: '',
        hwinfo_cpu_CPU_op_mode: '',
        hwinfo_cpu_Byte_Order: '',
        hwinfo_cpu_On_line_CPUs_list: '',
        hwinfo_cpu_Virtualization: '',
        hwinfo_cpu_Virtualization_type: '',
        hwinfo_cpu_L1d_cache: '',
        hwinfo_cpu_L1i_cache: '',
        hwinfo_cpu_L2_cache: '',
        hwinfo_cpu_L3_cache: '',
        hwinfo_memory_Flags: '',
        hwinfo_memory_vendor: '',
        hwinfo_memory_mem_type: '',
        hwinfo_memory_total_size: '',
        hwinfo_memory_mem_used: '',
        hwinfo_memory_mem_count: '',
        hwinfo_memory_mem_free: '',
        hwinfo_memory_mem_freq: '',
        hwinfo_memory_swap: '',
        hwinfo_disk_name: '',
        hwinfo_disk_part_type: '',
        hwinfo_disk_vendor: '',
        hwinfo_disk_model: '',
        hwinfo_disk_size: '',
        hwinfo_disk_rota: '',
        hwinfo_disk_sched: '',
        hwinfo_disk_rq_size: '',
        hwinfo_disk_tran: '',
        hwinfo_disk_mntpoint: '',
        hwinfo_disk_mntpoint_home: '',
        hwinfo_disk_name_2: '',
        hwinfo_disk_part_type_2: '',
        hwinfo_disk_vendor_2: '',
        hwinfo_disk_model_2: '',
        hwinfo_disk_size_2: '',
        hwinfo_disk_rota_2: '',
        hwinfo_disk_sched_2: '',
        hwinfo_disk_rq_size_2: '',
        hwinfo_disk_tran_2: '',
        hwinfo_disk_mntpoint_2: '',
        hwinfo_disk_mntpoint_home_2: '',
        hwinfo_nicinfo_logicalname: '',
        hwinfo_nicinfo_product: '',
        hwinfo_nicinfo_speed: '',
        swinfo_os_curr_UTC_time: '',
        swinfo_os_os_id: '',
        swinfo_os_os_arch: '',
        swinfo_os_osversion: '',
        swinfo_os_kernel: '',
        swinfo_os_grub: '',
        swinfo_runtime_sysconf: '',
        swinfo_runtime_sysctl: '',
        swinfo_runtime_systemctlinfo: '',
        swinfo_runtime_driverinfo: '',
        swinfo_runtime_rpmlist: '',
        swinfo_runtime_ipclist: '',
        swinfo_runtime_selinux_status: '',
        swinfo_runtime_power_status: '',
        swinfo_runtime_cpu_sched: '',
        swinfo_runtime_loadavg: '',
        swinfo_runtime_uptime: '',
        swinfo_software_ver_gccversion: '',
        swinfo_software_ver_glibcversion: '',
        swinfo_software_ver_javaversion: '',
        swinfo_software_ver_g_version: '',
        swinfo_software_ver_gfortranversion: '',
        swinfo_software_ver_pythonversion: '',
        nwinfo_nic: '',
        nwinfo_nic_nicname: '',
        nwinfo_nic_ip: '',
        nwinfo_nic_hwaddr: '',
        nwinfo_nic_gateway: '',
        nwinfo_nic_mtu: '',
      },
      getEnvDatas: [],
    };
  },
  computed: {
    tableDatas() {
      return [
        {
          first: 'hwinfo',
          second: 'machineinfo',
          third: 'manufacturer',
          fourth: this.env_datas.hwinfo_machineinfo_manufacturer
        },
        {first: 'hwinfo', second: 'machineinfo', third: 'product', fourth: this.env_datas.hwinfo_machineinfo_product},
        {
          first: 'hwinfo',
          second: 'machineinfo',
          third: 'serialnumber',
          fourth: this.env_datas.hwinfo_machineinfo_serialnumber
        },
        {first: 'hwinfo', second: 'bios', third: 'vendor', fourth: this.env_datas.hwinfo_bios_vendor},
        {first: 'hwinfo', second: 'bios', third: 'version', fourth: this.env_datas.hwinfo_bios_version},
        {first: 'hwinfo', second: 'cpu', third: 'Vendor ID', fourth: this.env_datas.hwinfo_cpu_Vendor_ID},
        {first: 'hwinfo', second: 'cpu', third: 'CPU family', fourth: this.env_datas.hwinfo_cpu_CPU_family},
        {first: 'hwinfo', second: 'cpu', third: 'model_name', fourth: this.env_datas.hwinfo_cpu_model_name},
        {first: 'hwinfo', second: 'cpu', third: 'CPU MHz', fourth: this.env_datas.hwinfo_cpu_CPU_MHz},
        {first: 'hwinfo', second: 'cpu', third: 'CPU(s)', fourth: this.env_datas.hwinfo_cpu_CPUs},
        {
          first: 'hwinfo',
          second: 'cpu',
          third: 'Thread(s) per core',
          fourth: this.env_datas.hwinfo_cpu_Threads_per_core
        },
        {first: 'hwinfo', second: 'cpu', third: 'CPU Arch', fourth: this.env_datas.hwinfo_cpu_CPU_Arch},
        {first: 'hwinfo', second: 'cpu', third: 'CPU op-mode', fourth: this.env_datas.hwinfo_cpu_CPU_op_mode},
        {first: 'hwinfo', second: 'cpu', third: 'Byte Order', fourth: this.env_datas.hwinfo_cpu_Byte_Order},
        {
          first: 'hwinfo',
          second: 'cpu',
          third: 'On-line CPU(s) list',
          fourth: this.env_datas.hwinfo_cpu_On_line_CPUs_list
        },
        {first: 'hwinfo', second: 'cpu', third: 'Virtualization', fourth: this.env_datas.hwinfo_cpu_Virtualization},
        {
          first: 'hwinfo',
          second: 'cpu',
          third: 'Virtualization type',
          fourth: this.env_datas.hwinfo_cpu_Virtualization_type
        },
        {first: 'hwinfo', second: 'cpu', third: 'L1d cache:', fourth: this.env_datas.hwinfo_cpu_L1d_cache},
        {first: 'hwinfo', second: 'cpu', third: 'L1i cache', fourth: this.env_datas.hwinfo_cpu_L1i_cache},
        {first: 'hwinfo', second: 'cpu', third: 'L2 cache', fourth: this.env_datas.hwinfo_cpu_L2_cache},
        {first: 'hwinfo', second: 'cpu', third: 'L3 cache', fourth: this.env_datas.hwinfo_cpu_L3_cache},
        {first: 'hwinfo', second: 'cpu', third: 'Flags', fourth: this.env_datas.hwinfo_memory_Flags},
        {first: 'hwinfo', second: 'memory', third: 'vendor', fourth: this.env_datas.hwinfo_memory_vendor},
        {first: 'hwinfo', second: 'memory', third: 'mem_type', fourth: this.env_datas.hwinfo_memory_mem_type},
        {first: 'hwinfo', second: 'memory', third: 'total_size', fourth: this.env_datas.hwinfo_memory_total_size},
        {first: 'hwinfo', second: 'memory', third: 'mem_used', fourth: this.env_datas.hwinfo_memory_mem_used},
        {first: 'hwinfo', second: 'memory', third: 'mem_count', fourth: this.env_datas.hwinfo_memory_mem_count},
        {first: 'hwinfo', second: 'memory', third: 'mem_free', fourth: this.env_datas.hwinfo_memory_mem_free},
        {first: 'hwinfo', second: 'memory', third: 'mem_freq', fourth: this.env_datas.hwinfo_memory_mem_freq},
        {first: 'hwinfo', second: 'memory', third: 'swap', fourth: this.env_datas.hwinfo_memory_swap},

                // {first: 'hwinfo', second: 'disk', third: 'part_type', fourth: this.disk_datas[0].part_type},     hwinfo_disk_part_type
        {first: 'hwinfo', second: 'disk', third: 'name', fourth: this.env_datas.hwinfo_disk_name},
        {first: 'hwinfo', second: 'disk', third: 'part_type', fourth: this.env_datas.hwinfo_disk_part_type},
        {first: 'hwinfo', second: 'disk', third: 'vendor', fourth: this.env_datas.hwinfo_disk_vendor},
        {first: 'hwinfo', second: 'disk', third: 'model', fourth: this.env_datas.hwinfo_disk_model},
        {first: 'hwinfo', second: 'disk', third: 'size', fourth: this.env_datas.hwinfo_disk_size},
        {first: 'hwinfo', second: 'disk', third: 'rota', fourth: this.env_datas.hwinfo_disk_rota},
        {first: 'hwinfo', second: 'disk', third: 'sched', fourth: this.env_datas.hwinfo_disk_sched},
        {first: 'hwinfo', second: 'disk', third: 'rq_size', fourth: this.env_datas.hwinfo_disk_rq_size},
        {first: 'hwinfo', second: 'disk', third: 'tran', fourth: this.env_datas.hwinfo_disk_tran},
        {first: 'hwinfo', second: 'disk', third: 'mntpoint=/', fourth: this.env_datas.hwinfo_disk_mntpoint},
        {first: 'hwinfo', second: 'disk', third: 'mntpoint=/home', fourth: this.env_datas.hwinfo_disk_mntpoint_home},
        {first: 'hwinfo', second: 'disk', third: 'name', fourth: this.env_datas.hwinfo_disk_name_2},
        {first: 'hwinfo', second: 'disk', third: 'part_type', fourth: this.env_datas.hwinfo_disk_part_type_2},
        {first: 'hwinfo', second: 'disk', third: 'vendor', fourth: this.env_datas.hwinfo_disk_name_2},
        {first: 'hwinfo', second: 'disk', third: 'model', fourth: this.env_datas.hwinfo_disk_part_type_2},
        {first: 'hwinfo', second: 'disk', third: 'size', fourth: this.env_datas.hwinfo_disk_vendor_2},
        {first: 'hwinfo', second: 'disk', third: 'rota', fourth: this.env_datas.hwinfo_disk_model_2},
        {first: 'hwinfo', second: 'disk', third: 'sched', fourth: this.env_datas.hwinfo_disk_size_2},
        {first: 'hwinfo', second: 'disk', third: 'rq_size', fourth: this.env_datas.hwinfo_disk_rota_2},
        {first: 'hwinfo', second: 'disk', third: 'tran', fourth: this.env_datas.hwinfo_disk_sched_2},
        {first: 'hwinfo', second: 'disk', third: 'mntpoint=/', fourth: this.env_datas.hwinfo_disk_rq_size_2},
        {first: 'hwinfo', second: 'disk', third: 'mntpoint=/home', fourth: this.env_datas.hwinfo_disk_tran_2},

        // {first: 'hwinfo', second: 'disk', third: 'name', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'part_type', fourth: this.disk_datas[0].part_type},
        // {first: 'hwinfo', second: 'disk', third: 'vendor', fourth: this.disk_datas[0].vendor},
        // {first: 'hwinfo', second: 'disk', third: 'model', fourth: this.disk_datas[0].model},
        // {first: 'hwinfo', second: 'disk', third: 'size', fourth: this.disk_datas[0].size},
        // {first: 'hwinfo', second: 'disk', third: 'rota', fourth: this.disk_datas[0].rota},
        // {first: 'hwinfo', second: 'disk', third: 'sched', fourth: this.disk_datas[0].sched},
        // {first: 'hwinfo', second: 'disk', third: 'rq_size', fourth: this.disk_datas[0].rq_size},
        // {first: 'hwinfo', second: 'disk', third: 'tran', fourth: this.disk_datas[0].tran},
        // {first: 'hwinfo', second: 'disk', third: 'mntpoint=/', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'mntpoint=/home', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'name', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'part_type', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'vendor', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'model', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'size', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'rota', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'sched', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'rq_size', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'tran', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'mntpoint=/', fourth: this.disk_datas[0].name},
        // {first: 'hwinfo', second: 'disk', third: 'mntpoint=/home', fourth: this.disk_datas[0].name},

        {first: 'hwinfo', second: 'nicinfo', third: 'logicalname', fourth: this.env_datas.hwinfo_nicinfo_logicalname},
        {first: 'hwinfo', second: 'nicinfo', third: 'product', fourth: this.env_datas.hwinfo_nicinfo_product},
        {first: 'hwinfo', second: 'nicinfo', third: 'speed', fourth: this.env_datas.hwinfo_nicinfo_speed},
        {first: 'swinfo', second: 'os', third: 'curr UTC time', fourth: this.env_datas.swinfo_os_curr_UTC_time},
        {first: 'swinfo', second: 'os', third: 'os_id', fourth: this.env_datas.swinfo_os_os_id},
        {first: 'swinfo', second: 'os', third: 'os_arch', fourth: this.env_datas.swinfo_os_os_arch},
        {first: 'swinfo', second: 'os', third: 'osversion', fourth: this.env_datas.swinfo_os_osversion},
        {first: 'swinfo', second: 'os', third: 'kernel', fourth: this.env_datas.swinfo_os_kernel},
        {first: 'swinfo', second: 'os', third: 'grub', fourth: this.env_datas.swinfo_os_grub},
        {first: 'swinfo', second: 'runtime', third: 'sysconf', fourth: this.env_datas.swinfo_runtime_sysconf},
        {first: 'swinfo', second: 'runtime', third: 'sysctl', fourth: this.env_datas.swinfo_runtime_sysctl},
        {
          first: 'swinfo',
          second: 'runtime',
          third: 'systemctlinfo',
          fourth: this.env_datas.swinfo_runtime_systemctlinfo
        },
        {first: 'swinfo', second: 'runtime', third: 'driverinfo', fourth: this.env_datas.swinfo_runtime_driverinfo},
        {first: 'swinfo', second: 'runtime', third: 'rpmlist', fourth: this.env_datas.swinfo_runtime_rpmlist},
        {first: 'swinfo', second: 'runtime', third: 'ipclist', fourth: this.env_datas.swinfo_runtime_ipclist},
        {
          first: 'swinfo',
          second: 'runtime',
          third: 'selinux_status',
          fourth: this.env_datas.swinfo_runtime_selinux_status
        },
        {first: 'swinfo', second: 'runtime', third: 'power_status', fourth: this.env_datas.swinfo_runtime_power_status},
        {first: 'swinfo', second: 'runtime', third: 'cpu_sched', fourth: this.env_datas.swinfo_runtime_cpu_sched},
        {first: 'swinfo', second: 'runtime', third: 'loadavg', fourth: this.env_datas.swinfo_runtime_loadavg},
        {first: 'swinfo', second: 'runtime', third: 'uptime', fourth: this.env_datas.swinfo_runtime_uptime},
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'gccversion',
          fourth: this.env_datas.swinfo_software_ver_gccversion
        },
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'glibcversion',
          fourth: this.env_datas.swinfo_software_ver_glibcversion
        },
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'javaversion',
          fourth: this.env_datas.swinfo_software_ver_javaversion
        },
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'g++version',
          fourth: this.env_datas.swinfo_software_ver_g_version
        },
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'gfortranversion',
          fourth: this.env_datas.swinfo_software_ver_gfortranversion
        },
        {
          first: 'swinfo',
          second: 'software_ver',
          third: 'pythonversion',
          fourth: this.env_datas.swinfo_software_ver_pythonversion
        },
        {first: 'nwinfo', second: 'nic', third: 'nicname', fourth: this.env_datas.nwinfo_nic_nicname},
        {first: 'nwinfo', second: 'nic', third: 'ip', fourth: this.env_datas.nwinfo_nic_ip},
        {first: 'nwinfo', second: 'nic', third: 'hwaddr', fourth: this.env_datas.nwinfo_nic_hwaddr},
        {first: 'nwinfo', second: 'nic', third: 'gateway', fourth: this.env_datas.nwinfo_nic_gateway},
        {first: 'nwinfo', second: 'nic', third: 'mtu', fourth: this.env_datas.nwinfo_nic_mtu},
      ]
    }
  },
  created() {
    axios.get('/api/env/' + this.$route.params.envId + '/').then((response) => {
      this.getEnvDatas = response.data.data
      this.env_datas.hwinfo_machineinfo_manufacturer = this.getEnvDatas.hwinfo_machineinfo_manufacturer
      this.env_datas.hwinfo_machineinfo_product = this.getEnvDatas.hwinfo_machineinfo_product
      this.env_datas.hwinfo_machineinfo_serialnumber = this.getEnvDatas.hwinfo_machineinfo_serialnumber
      this.env_datas.hwinfo_bios_vendor = this.getEnvDatas.hwinfo_bios_vendor
      this.env_datas.hwinfo_bios_version = this.getEnvDatas.hwinfo_bios_version
      this.env_datas.hwinfo_cpu_Vendor_ID = this.getEnvDatas.hwinfo_cpu_Vendor_ID
      this.env_datas.hwinfo_cpu_CPU_family = this.getEnvDatas.hwinfo_cpu_CPU_family
      this.env_datas.hwinfo_cpu_model_name = this.getEnvDatas.hwinfo_cpu_model_name
      this.env_datas.hwinfo_cpu_CPU_MHz = this.getEnvDatas.hwinfo_cpu_CPU_MHz
      this.env_datas.hwinfo_cpu_CPUs = this.getEnvDatas.hwinfo_cpu_CPUs
      this.env_datas.hwinfo_cpu_Threads_per_core = this.getEnvDatas.hwinfo_cpu_Threads_per_core
      this.env_datas.hwinfo_cpu_CPU_Arch = this.getEnvDatas.hwinfo_cpu_CPU_Arch
      this.env_datas.hwinfo_cpu_CPU_op_mode = this.getEnvDatas.hwinfo_cpu_CPU_op_mode
      this.env_datas.hwinfo_cpu_Byte_Order = this.getEnvDatas.hwinfo_cpu_Byte_Order
      this.env_datas.hwinfo_cpu_On_line_CPUs_list = this.getEnvDatas.hwinfo_cpu_On_line_CPUs_list
      this.env_datas.hwinfo_cpu_Virtualization = this.getEnvDatas.hwinfo_cpu_Virtualization
      this.env_datas.hwinfo_cpu_Virtualization_type = this.getEnvDatas.hwinfo_cpu_Virtualization_type
      this.env_datas.hwinfo_cpu_L1d_cache = this.getEnvDatas.hwinfo_cpu_L1d_cache
      this.env_datas.hwinfo_cpu_L1i_cache = this.getEnvDatas.hwinfo_cpu_L1i_cache
      this.env_datas.hwinfo_cpu_L2_cache = this.getEnvDatas.hwinfo_cpu_L2_cache
      this.env_datas.hwinfo_cpu_L3_cache = this.getEnvDatas.hwinfo_cpu_L3_cache
      this.env_datas.hwinfo_memory_Flags = this.getEnvDatas.hwinfo_memory_Flags
      this.env_datas.hwinfo_memory_vendor = this.getEnvDatas.hwinfo_memory_vendor
      this.env_datas.hwinfo_memory_mem_type = this.getEnvDatas.hwinfo_memory_mem_type
      this.env_datas.hwinfo_memory_total_size = this.getEnvDatas.hwinfo_memory_total_size
      this.env_datas.hwinfo_memory_mem_used = this.getEnvDatas.hwinfo_memory_mem_used
      this.env_datas.hwinfo_memory_mem_count = this.getEnvDatas.hwinfo_memory_mem_count
      this.env_datas.hwinfo_memory_mem_free = this.getEnvDatas.hwinfo_memory_mem_free
      this.env_datas.hwinfo_memory_mem_freq = this.getEnvDatas.hwinfo_memory_mem_freq
      this.env_datas.hwinfo_memory_swap = this.getEnvDatas.hwinfo_memory_swap
      // 处理disk数据，目前写死的两组数据，后期在实现自动化遍历
      const disk_json_str = this.getEnvDatas.hwinfo_disk.replace(/'/g, '"').replace(/True/g, 'true').replace(/None/g, 'null');
      this.disk_datas = JSON.parse(disk_json_str);
      console.log("disk list = ",this.disk_datas[0]);
      this.env_datas.hwinfo_disk_name = this.disk_datas[0].name
      this.env_datas.hwinfo_disk_part_type = this.disk_datas[0].part_type
      this.env_datas.hwinfo_disk_vendor = this.disk_datas[0].vendor
      this.env_datas.hwinfo_disk_model = this.disk_datas[0].model
      this.env_datas.hwinfo_disk_size = this.disk_datas[0].size
      this.env_datas.hwinfo_disk_rota = this.disk_datas[0].rota
      this.env_datas.hwinfo_disk_sched = this.disk_datas[0].sched
      this.env_datas.hwinfo_disk_rq_size = this.disk_datas[0].rq_size
      this.env_datas.hwinfo_disk_tran = this.disk_datas[0].tran
      this.env_datas.hwinfo_disk_mntpoint = this.disk_datas[0]["mntpoint=/"];
      this.env_datas.hwinfo_disk_mntpoint_home = this.disk_datas[0]["mntpoint=/home"]
      this.env_datas.hwinfo_disk_name_2 = this.disk_datas[0].name
      this.env_datas.hwinfo_disk_part_type_2 = this.disk_datas[0].part_type
      this.env_datas.hwinfo_disk_vendor_2 = this.disk_datas[0].vendor
      this.env_datas.hwinfo_disk_model_2 = this.disk_datas[0].model
      this.env_datas.hwinfo_disk_size_2 = this.disk_datas[0].size
      this.env_datas.hwinfo_disk_rota_2 = this.disk_datas[0].rota
      this.env_datas.hwinfo_disk_sched_2 = this.disk_datas[0].sched
      this.env_datas.hwinfo_disk_rq_size_2 = this.disk_datas[0].rq_size
      this.env_datas.hwinfo_disk_tran_2 = this.disk_datas[0].tran
      this.env_datas.hwinfo_disk_mntpoint_2 = this.disk_datas[0]["mntpoint=/"];
      this.env_datas.hwinfo_disk_mntpoint_home_2 = this.disk_datas[0]["mntpoint=/home"]
      // 处理nicinfo数据，目前写死的1组数据，后期在实现自动化遍历,并且使用方法和disk的还不一样后期在看使用哪一种.
      const nicinfo_json_str = this.getEnvDatas.hwinfo_nicinfo.replace(/'/g, '"').replace(/True/g, 'true').replace(/None/g, 'null');
      this.nicinfo_datas = JSON.parse(nicinfo_json_str);
      this.env_datas.hwinfo_nicinfo_logicalname = this.nicinfo_datas[0].logicalname
      this.env_datas.hwinfo_nicinfo_product =this.nicinfo_datas[0].product
      this.env_datas.hwinfo_nicinfo_speed =this.nicinfo_datas[0].speed

      this.env_datas.swinfo_os_curr_UTC_time = this.getEnvDatas.swinfo_os_curr_UTC_time
      this.env_datas.swinfo_os_os_id = this.getEnvDatas.swinfo_os_os_id
      this.env_datas.swinfo_os_os_arch = this.getEnvDatas.swinfo_os_os_arch
      this.env_datas.swinfo_os_osversion = this.getEnvDatas.swinfo_os_osversion
      this.env_datas.swinfo_os_kernel = this.getEnvDatas.swinfo_os_kernel
      this.env_datas.swinfo_os_grub = this.getEnvDatas.swinfo_os_grub
      this.env_datas.swinfo_runtime_sysconf = this.getEnvDatas.swinfo_runtime_sysconf
      this.env_datas.swinfo_runtime_sysctl = this.getEnvDatas.swinfo_runtime_sysctl
      this.env_datas.swinfo_runtime_systemctlinfo = this.getEnvDatas.swinfo_runtime_systemctlinfo
      this.env_datas.swinfo_runtime_driverinfo = this.getEnvDatas.swinfo_runtime_driverinfo
      this.env_datas.swinfo_runtime_rpmlist = this.getEnvDatas.swinfo_runtime_rpmlist
      this.env_datas.swinfo_runtime_ipclist = this.getEnvDatas.swinfo_runtime_ipclist
      this.env_datas.swinfo_runtime_selinux_status = this.getEnvDatas.swinfo_runtime_selinux_status
      this.env_datas.swinfo_runtime_power_status = this.getEnvDatas.swinfo_runtime_power_status
      this.env_datas.swinfo_runtime_cpu_sched = this.getEnvDatas.swinfo_runtime_cpu_sched
      this.env_datas.swinfo_runtime_loadavg = this.getEnvDatas.swinfo_runtime_loadavg
      this.env_datas.swinfo_runtime_uptime = this.getEnvDatas.swinfo_runtime_uptime
      this.env_datas.swinfo_software_ver_gccversion = this.getEnvDatas.swinfo_software_ver_gccversion
      this.env_datas.swinfo_software_ver_glibcversion = this.getEnvDatas.swinfo_software_ver_glibcversion
      this.env_datas.swinfo_software_ver_javaversion = this.getEnvDatas.swinfo_software_ver_javaversion
      this.env_datas.swinfo_software_ver_g_version = this.getEnvDatas.swinfo_software_ver_g_version
      this.env_datas.swinfo_software_ver_gfortranversion = this.getEnvDatas.swinfo_software_ver_gfortranversion
      this.env_datas.swinfo_software_ver_pythonversion = this.getEnvDatas.swinfo_software_ver_pythonversion

      // 处理nwinfo_nic数据，目前写死的1组数据，后期在实现自动化遍历,并且使用方法和disk的还不一样后期在看使用哪一种.
      const nwinfo_nic_json_str = this.getEnvDatas.nwinfo_nic.replace(/'/g, '"').replace(/True/g, 'true').replace(/None/g, 'null');
      this.nwinfo_nic_datas = JSON.parse(nwinfo_nic_json_str);
      this.env_datas.nwinfo_nic_nicname = this.nwinfo_nic_datas[0].nicname
      this.env_datas.nwinfo_nic_ip = this.nwinfo_nic_datas[0].ip
      this.env_datas.nwinfo_nic_hwaddr = this.nwinfo_nic_datas[0].hwaddr
      this.env_datas.nwinfo_nic_gateway = this.nwinfo_nic_datas[0].gateway
      this.env_datas.nwinfo_nic_mtu = this.nwinfo_nic_datas[0].mtu
      // tableDatas

      // this.env_datas.nwinfo_nic = this.getEnvDatas.nwinfo_nic
      // this.env_datas.nwinfo_nic_nicname = this.getEnvDatas.nwinfo_nic_nicname
      // this.env_datas.nwinfo_nic_ip = this.getEnvDatas.nwinfo_nic_ip
      // this.env_datas.nwinfo_nic_hwaddr = this.getEnvDatas.nwinfo_nic_hwaddr
      // this.env_datas.nwinfo_nic_gateway = this.getEnvDatas.nwinfo_nic_gateway
      // this.env_datas.nwinfo_nic_mtu = this.getEnvDatas.nwinfo_nic_mtu
    });
  },
  methods: {
    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0 || columnIndex === 1) {
        const _row = this.filterData(this.tableDatas, columnIndex).one[rowIndex];
        const _col = _row > 0 ? 1 : 0;  // 为0是不执行合并。 为1是从当前单元格开始，执行合并1列
        return {
          rowspan: _row,
          colspan: _col,
        }
      }
    },
    filterData(arr, colIndex) {
      let spanOneArr = [];
      let concatOne = 0;
      arr.forEach((item, index) => {
        if (index === 0) {
          spanOneArr.push(1);
        } else {
          //first second 分别表示表格数据第一列和第二列对应的参数字段，根据实际参数修改
          if (colIndex === 0) {
            if (item.first === arr[index - 1].first) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          } else {
            if (item.second === arr[index - 1].second) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          }
        }
      });
      return {
        one: spanOneArr,
      };
    }
  }
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
