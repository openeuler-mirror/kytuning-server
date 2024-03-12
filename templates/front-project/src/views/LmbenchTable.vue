<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Lmbench" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Lmbench#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="tableDatas" :span-method="objectSpanMethod" border style="width: 100%">
      <!--    <el-table :data="tableDatas" show-header="false"> //隐藏了表头，但只是让这样行的内容变空，但位置还在-->
      <el-table-column prop="first" label="一级字段" align="center" min-width="30%" center></el-table-column>
      <el-table-column prop="second" label="二级字段" align="center" min-width="50%"></el-table-column>
      <el-table-column prop="third"></el-table-column>
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
      other_list: [{first: '执行命令', second: './lmbench-except-base.sh; make see'}, {first: '修改参数：', second: 'xxx'}],
      lmbench_datas: {
        basic_Mhz: '',
        basic_tlb_pages: '',
        basic_cache_line_bytes: '',
        basic_mem_par: '',
        basic_scal_load: '',
        processor_null_call: '',
        processor_null_I_O: '',
        processor_stat: '',
        processor_open_clo: '',
        processor_slct_TCP: '',
        processor_sig_inst: '',
        processor_sig_hndl: '',
        processor_fork_proc: '',
        processor_exec_proc: '',
        processor_sh_proc: '',
        processor_Mhz: '',
        basic_intgr_bit: '',
        basic_intgr_add: '',
        basic_intgr_mul: '',
        basic_intgr_div: '',
        basic_intgr_mod: '',
        basic_int64_bit: '',
        basic_int64_add: '',
        basic_int64_mul: '',
        basic_int64_div: '',
        basic_int64_mod: '',
        basic_float_add: '',
        basic_float_mul: '',
        basic_float_div: '',
        basic_float_bogo: '',
        basic_double_add: '',
        basic_double_mul: '',
        basic_double_div: '',
        basic_double_bogo: '',
        context_2p_0K: '',
        context_2p_16K: '',
        context_2p_64K: '',
        context_8p_16K: '',
        context_8p_64K: '',
        context_16p_16K: '',
        context_16p_64K: '',
        local_2p_0K: '',
        local_Pipe: '',
        local_AF_UNIX: '',
        local_UDP: '',
        local_TCP: '',
        local_TCP_conn: '',
        local_RPC_TCP: '',
        local_RPC_UDP: '',
        local_bigger_Mmap_Latency: '',
        local_bigger_Prot_Fault: '',
        local_bigger_Page_Fault: '',
        local_bigger_100fd_selct: '',
        local_bigger_0K_File_create: '',
        local_bigger_0K_File_delete: '',
        local_bigger_10K_File_create: '',
        local_bigger_10K_File_delete: '',
        local_bigger_Pipe: '',
        local_bigger_AF_UNIX: '',
        local_bigger_TCP: '',
        local_bigger_File_reread: '',
        local_bigger_Mmap_reread: '',
        local_bigger_Bcopy_libc: '',
        local_bigger_Bcopy_hand: '',
        local_bigger_Mem_read: '',
        local_bigger_Mem_write: '',
        memory_Mhz: '',
        memory_L1: '',
        memory_L2: '',
        memory_Main_mem: '',
        memory_Rand_mem: '',
      },
      getLmbenchDatas: [],
    }
  },
  computed: {
    tableDatas() {
    return [
        {first:'Basic system parameters',second:'Mhz',third:this.lmbench_datas.basic_Mhz},
        {first:'Basic system parameters',second:'tlb pages',third:this.lmbench_datas.basic_tlb_pages},
      {first:'Basic system parameters',second:'cache line bytes',third:this.lmbench_datas.basic_cache_line_bytes},
      {first:'Basic system parameters',second:'mem par',third:this.lmbench_datas.basic_mem_par},
      {first:'Basic system parameters',second:'scal load',third:this.lmbench_datas.basic_scal_load},
        {first:'Processor',second:'Mhz',third:this.lmbench_datas.processor_null_call},
        {first:'Processor',second:'null call',third:this.lmbench_datas.processor_null_I_O},
        {first:'Processor',second:'null I/O',third:this.lmbench_datas.processor_stat},
        {first:'Processor',second:'stat',third:this.lmbench_datas.processor_open_clo},
        {first:'Processor',second:'open close',third:this.lmbench_datas.processor_slct_TCP},
        {first:'Processor',second:'slct TCP',third:this.lmbench_datas.processor_sig_inst},
        {first:'Processor',second:'sig inst',third:this.lmbench_datas.processor_sig_hndl},
        {first:'Processor',second:'sig hndl',third:this.lmbench_datas.processor_fork_proc},
        {first:'Processor',second:'fork proc',third:this.lmbench_datas.processor_exec_proc},
        {first:'Processor',second:'exec proc',third:this.lmbench_datas.processor_sh_proc},
        {first:'Processor',second:'sh proc',third:this.lmbench_datas.processor_Mhz},
        {first:'Basic integer operations',second:'intgr bit',third:this.lmbench_datas.basic_intgr_bit},
        {first:'Basic integer operations',second:'intgr add',third:this.lmbench_datas.basic_intgr_add},
        {first:'Basic integer operations',second:'intgr mul',third:this.lmbench_datas.basic_intgr_mul},
        {first:'Basic integer operations',second:'intgr div',third:this.lmbench_datas.basic_intgr_div},
        {first:'Basic integer operations',second:'intgr mod',third:this.lmbench_datas.basic_intgr_mod},
        {first:'Basic uint64 operations',second:'int64 bit',third:this.lmbench_datas.basic_int64_bit},
        {first:'Basic uint64 operations',second:'int64 add',third:this.lmbench_datas.basic_int64_add},
        {first:'Basic uint64 operations',second:'int64 mul',third:this.lmbench_datas.basic_int64_mul},
        {first:'Basic uint64 operations',second:'int64 div',third:this.lmbench_datas.basic_int64_div},
        {first:'Basic uint64 operations',second:'int64 mod',third:this.lmbench_datas.basic_int64_mod},
        {first:'Basic float operations',second:'float add',third:this.lmbench_datas.basic_float_add},
        {first:'Basic float operations',second:'float mul',third:this.lmbench_datas.basic_float_mul},
        {first:'Basic float operations',second:'float div',third:this.lmbench_datas.basic_float_div},
        {first:'Basic float operations',second:'float bogo',third:this.lmbench_datas.basic_float_bogo},
        {first:'Basic double operations',second:'double add',third:this.lmbench_datas.basic_double_add},
        {first:'Basic double operations',second:'double mul',third:this.lmbench_datas.basic_double_mul},
        {first:'Basic double operations',second:'double div',third:this.lmbench_datas.basic_double_div},
        {first:'Basic double operations',second:'double bogo',third:this.lmbench_datas.basic_double_bogo},
        {first:'Context switching',second:'2p/0K',third:this.lmbench_datas.context_2p_0K},
        {first:'Context switching',second:'2p/16K',third:this.lmbench_datas.context_2p_16K},
        {first:'Context switching',second:'2p/64K',third:this.lmbench_datas.context_2p_64K},
        {first:'Context switching',second:'8p/16K',third:this.lmbench_datas.context_8p_16K},
        {first:'Context switching',second:'8p/64K',third:this.lmbench_datas.context_8p_64K},
        {first:'Context switching',second:'16p/16K',third:this.lmbench_datas.context_16p_16K},
        {first:'Context switching',second:'16p/64K',third:this.lmbench_datas.context_16p_64K},
        {first:'*Local* Communication latencies',second:'2p/0K',third:this.lmbench_datas.local_2p_0K},
        {first:'*Local* Communication latencies',second:'Pipe',third:this.lmbench_datas.local_Pipe},
        {first:'*Local* Communication latencies',second:'AF UNIX',third:this.lmbench_datas.local_AF_UNIX},
        {first:'*Local* Communication latencies',second:'UDP',third:this.lmbench_datas.local_UDP},
        {first:'*Local* Communication latencies',second:'TCP',third:this.lmbench_datas.local_TCP},
        {first:'*Local* Communication latencies',second:'TCP conn',third:this.lmbench_datas.local_TCP_conn},
        {first:'*Local* Communication latencies',second:'RPC/TCP',third:this.lmbench_datas.local_RPC_TCP},
        {first:'*Local* Communication latencies',second:'RPC/UDP',third:this.lmbench_datas.local_RPC_UDP},
        {first:'File & VM system latencies in microseconds',second:'0K File create',third:this.lmbench_datas.local_bigger_Mmap_Latency},
        {first:'File & VM system latencies in microseconds',second:'0K File delete',third:this.lmbench_datas.local_bigger_Prot_Fault},
        {first:'File & VM system latencies in microseconds',second:'10K File create',third:this.lmbench_datas.local_bigger_Page_Fault},
        {first:'File & VM system latencies in microseconds',second:'10K File delete',third:this.lmbench_datas.local_bigger_100fd_selct},
        {first:'File & VM system latencies in microseconds',second:'Mmap Latency',third:this.lmbench_datas.local_bigger_0K_File_create},
        {first:'File & VM system latencies in microseconds',second:'Prot Fault',third:this.lmbench_datas.local_bigger_0K_File_delete},
        {first:'File & VM system latencies in microseconds',second:'Page Fault',third:this.lmbench_datas.local_bigger_10K_File_create},
        {first:'File & VM system latencies in microseconds',second:'100fd selct',third:this.lmbench_datas.local_bigger_10K_File_delete},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Pipe',third:this.lmbench_datas.local_bigger_Pipe},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'AF UNIX',third:this.lmbench_datas.local_bigger_AF_UNIX},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'TCP',third:this.lmbench_datas.local_bigger_TCP},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'File reread',third:this.lmbench_datas.local_bigger_File_reread},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Mmap reread',third:this.lmbench_datas.local_bigger_Mmap_reread},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Bcopy(libc)',third:this.lmbench_datas.local_bigger_Bcopy_libc},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Bcopy(hand)',third:this.lmbench_datas.local_bigger_Bcopy_hand},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Mem read',third:this.lmbench_datas.local_bigger_Mem_read},
        {first:'*Local* Communication bandwidths in MB/s - bigger is better',second:'Mem write',third:this.lmbench_datas.local_bigger_Mem_write},
        {first:'Memory latencies in nanoseconds',second:'Mhz',third:this.lmbench_datas.memory_Mhz},
        {first:'Memory latencies in nanoseconds',second:'L1 $',third:this.lmbench_datas.memory_L1},
        {first:'Memory latencies in nanoseconds',second:'L2 $',third:this.lmbench_datas.memory_L2},
        {first:'Memory latencies in nanoseconds',second:'Main mem',third:this.lmbench_datas.memory_Main_mem},
        {first:'Memory latencies in nanoseconds',second:'Rand mem',third:this.lmbench_datas.memory_Rand_mem},
      ]
    }
  },
  created() {
    axios.get('/api/lmbench/?env_id=' + this.$route.params.baseId).then((response) => {
      this.getLmbenchDatas = response.data.data
      this.other_list[0].second=this.getLmbenchDatas[0].execute_cmd
      this.other_list[1].second=this.getLmbenchDatas[0].modify_parameters
      this.lmbench_datas.basic_Mhz = this.getLmbenchDatas[0].basic_Mhz
      this.lmbench_datas.basic_tlb_pages = this.getLmbenchDatas[0].basic_tlb_pages
      this.lmbench_datas.basic_cache_line_bytes = this.getLmbenchDatas[0].basic_cache_line_bytes
      this.lmbench_datas.basic_mem_par = this.getLmbenchDatas[0].basic_mem_par
      this.lmbench_datas.basic_scal_load = this.getLmbenchDatas[0].basic_scal_load
      this.lmbench_datas.processor_null_call = this.getLmbenchDatas[0].processor_null_call
      this.lmbench_datas.processor_null_I_O = this.getLmbenchDatas[0].processor_null_I_O
      this.lmbench_datas.processor_stat = this.getLmbenchDatas[0].processor_stat
      this.lmbench_datas.processor_open_clo = this.getLmbenchDatas[0].processor_open_clo
      this.lmbench_datas.processor_slct_TCP = this.getLmbenchDatas[0].processor_slct_TCP
      this.lmbench_datas.processor_sig_inst = this.getLmbenchDatas[0].processor_sig_inst
      this.lmbench_datas.processor_sig_hndl = this.getLmbenchDatas[0].processor_sig_hndl
      this.lmbench_datas.processor_fork_proc = this.getLmbenchDatas[0].processor_fork_proc
      this.lmbench_datas.processor_exec_proc = this.getLmbenchDatas[0].processor_exec_proc
      this.lmbench_datas.processor_sh_proc = this.getLmbenchDatas[0].processor_sh_proc
      this.lmbench_datas.processor_Mhz = this.getLmbenchDatas[0].processor_Mhz
      this.lmbench_datas.basic_intgr_bit = this.getLmbenchDatas[0].basic_intgr_bit
      this.lmbench_datas.basic_intgr_add = this.getLmbenchDatas[0].basic_intgr_add
      this.lmbench_datas.basic_intgr_mul = this.getLmbenchDatas[0].basic_intgr_mul
      this.lmbench_datas.basic_intgr_div = this.getLmbenchDatas[0].basic_intgr_div
      this.lmbench_datas.basic_intgr_mod = this.getLmbenchDatas[0].basic_intgr_mod
      this.lmbench_datas.basic_int64_bit = this.getLmbenchDatas[0].basic_int64_bit
      this.lmbench_datas.basic_int64_add = this.getLmbenchDatas[0].basic_int64_add
      this.lmbench_datas.basic_int64_mul = this.getLmbenchDatas[0].basic_int64_mul
      this.lmbench_datas.basic_int64_div = this.getLmbenchDatas[0].basic_int64_div
      this.lmbench_datas.basic_int64_mod = this.getLmbenchDatas[0].basic_int64_mod
      this.lmbench_datas.basic_float_add = this.getLmbenchDatas[0].basic_float_add
      this.lmbench_datas.basic_float_mul = this.getLmbenchDatas[0].basic_float_mul
      this.lmbench_datas.basic_float_div = this.getLmbenchDatas[0].basic_float_div
      this.lmbench_datas.basic_float_bogo = this.getLmbenchDatas[0].basic_float_bogo
      this.lmbench_datas.basic_double_add = this.getLmbenchDatas[0].basic_double_add
      this.lmbench_datas.basic_double_mul = this.getLmbenchDatas[0].basic_double_mul
      this.lmbench_datas.basic_double_div = this.getLmbenchDatas[0].basic_double_div
      this.lmbench_datas.basic_double_bogo = this.getLmbenchDatas[0].basic_double_bogo
      this.lmbench_datas.context_2p_0K = this.getLmbenchDatas[0].context_2p_0K
      this.lmbench_datas.context_2p_16K = this.getLmbenchDatas[0].context_2p_16K
      this.lmbench_datas.context_2p_64K = this.getLmbenchDatas[0].context_2p_64K
      this.lmbench_datas.context_8p_16K = this.getLmbenchDatas[0].context_8p_16K
      this.lmbench_datas.context_8p_64K = this.getLmbenchDatas[0].context_8p_64K
      this.lmbench_datas.context_16p_16K = this.getLmbenchDatas[0].context_16p_16K
      this.lmbench_datas.context_16p_64K = this.getLmbenchDatas[0].context_16p_64K
      this.lmbench_datas.local_2p_0K = this.getLmbenchDatas[0].local_2p_0K
      this.lmbench_datas.local_Pipe = this.getLmbenchDatas[0].local_Pipe
      this.lmbench_datas.local_AF_UNIX = this.getLmbenchDatas[0].local_AF_UNIX
      this.lmbench_datas.local_UDP = this.getLmbenchDatas[0].local_UDP
      this.lmbench_datas.local_TCP = this.getLmbenchDatas[0].local_TCP
      this.lmbench_datas.local_TCP_conn = this.getLmbenchDatas[0].local_TCP_conn
      this.lmbench_datas.local_RPC_TCP = this.getLmbenchDatas[0].local_RPC_TCP
      this.lmbench_datas.local_RPC_UDP = this.getLmbenchDatas[0].local_RPC_UDP
      this.lmbench_datas.local_bigger_Mmap_Latency = this.getLmbenchDatas[0].local_bigger_Mmap_Latency
      this.lmbench_datas.local_bigger_Prot_Fault = this.getLmbenchDatas[0].local_bigger_Prot_Fault
      this.lmbench_datas.local_bigger_Page_Fault = this.getLmbenchDatas[0].local_bigger_Page_Fault
      this.lmbench_datas.local_bigger_100fd_selct = this.getLmbenchDatas[0].local_bigger_100fd_selct
      this.lmbench_datas.local_bigger_0K_File_create = this.getLmbenchDatas[0].local_bigger_0K_File_create
      this.lmbench_datas.local_bigger_0K_File_delete = this.getLmbenchDatas[0].local_bigger_0K_File_delete
      this.lmbench_datas.local_bigger_10K_File_create = this.getLmbenchDatas[0].local_bigger_10K_File_create
      this.lmbench_datas.local_bigger_10K_File_delete = this.getLmbenchDatas[0].local_bigger_10K_File_delete
      this.lmbench_datas.local_bigger_Pipe = this.getLmbenchDatas[0].local_bigger_Pipe
      this.lmbench_datas.local_bigger_AF_UNIX = this.getLmbenchDatas[0].local_bigger_AF_UNIX
      this.lmbench_datas.local_bigger_TCP = this.getLmbenchDatas[0].local_bigger_TCP
      this.lmbench_datas.local_bigger_File_reread = this.getLmbenchDatas[0].local_bigger_File_reread
      this.lmbench_datas.local_bigger_Mmap_reread = this.getLmbenchDatas[0].local_bigger_Mmap_reread
      this.lmbench_datas.local_bigger_Bcopy_libc = this.getLmbenchDatas[0].local_bigger_Bcopy_libc
      this.lmbench_datas.local_bigger_Bcopy_hand = this.getLmbenchDatas[0].local_bigger_Bcopy_hand
      this.lmbench_datas.local_bigger_Mem_read = this.getLmbenchDatas[0].local_bigger_Mem_read
      this.lmbench_datas.local_bigger_Mem_write = this.getLmbenchDatas[0].local_bigger_Mem_write
      this.lmbench_datas.memory_Mhz = this.getLmbenchDatas[0].memory_Mhz
      this.lmbench_datas.memory_L1 = this.getLmbenchDatas[0].memory_L1
      this.lmbench_datas.memory_L2 = this.getLmbenchDatas[0].memory_L2
      this.lmbench_datas.memory_Main_mem = this.getLmbenchDatas[0].memory_Main_mem
      this.lmbench_datas.memory_Rand_mem = this.getLmbenchDatas[0].memory_Rand_mem
    })
  },
  methods: {
    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0) {
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
