<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Stream" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Stream#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="tableDatas" :span-method="objectSpanMethod" border style="width: 100%">
      <!--    <el-table :data="tableDatas" show-header="false"> //隐藏了表头，但只是让这样行的内容变空，但位置还在-->
      <el-table-column prop="ThreadType" align="center" min-width="30%" center></el-table-column>
      <el-table-column prop="second" align="center" min-width="50%"></el-table-column>
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
      other_list: [{first: '执行命令', second: './Run -c {FUNC_THREAD_NUM}'}, {first: '修改参数：', second: 'xxx'}],

      stream_datas: {
        Dhrystone: '',
        Double_Precision: '',
        execl_throughput: '',
        file_copy_1024: '',
        file_copy_256: '',
        file_copy_4096: '',
        pipe_throughput: '',
        pipe_based: '',
        process_creation: '',
        shell_scripts_1: '',
        shell_scripts_8: '',
        system_call_overhead: '',
        index_score: '',
        Dhrystone_2: '',
        Double_Precision_2: '',
        execl_throughput_2: '',
        file_copy_1024_2: '',
        file_copy_256_2: '',
        file_copy_4096_2: '',
        pipe_throughput_2: '',
        pipe_based_2: '',
        process_creation_2: '',
        shell_scripts_1_2: '',
        shell_scripts_8_2: '',
        system_call_overhead_2: '',
        index_score_2: '',

      },
      getUnixbenchDatas: [],
      MultiThreaddata:[],
      singleThreaddata:[],

    }
  },
  computed: {
    tableDatas() {
      return [
          {ThreadType: '单线程', second: 'Dhrystone 2 using register variables(lps)', third: this.stream_datas.Dhrystone},
          {ThreadType: '单线程', second: 'Double-Precision Whetstone(MWIPS)', third: this.stream_datas.Double_Precision},
          {ThreadType: '单线程', second: 'Execl Throughput(lps)', third: this.stream_datas.execl_throughput},
          {ThreadType: '单线程', second: 'File Copy 1024 bufsize 2000 maxblocks(KBps)', third: this.stream_datas.file_copy_1024},
          {ThreadType: '单线程', second: 'File Copy 256 bufsize 500 maxblocks(KBps)', third: this.stream_datas.file_copy_256},
          {ThreadType: '单线程', second: 'File Copy 4096 bufsize 8000 maxblocks(KBps)', third: this.stream_datas.file_copy_4096},
          {ThreadType: '单线程', second: 'Pipe Throughput(lps)', third: this.stream_datas.pipe_throughput},
          {ThreadType: '单线程', second: 'Pipe-based Context Switching(lps)', third: this.stream_datas.pipe_based},
          {ThreadType: '单线程', second: 'Process Creation(lps)', third: this.stream_datas.process_creation},
          {ThreadType: '单线程', second: 'Shell Scripts (1 concurrent)(lpm)', third: this.stream_datas.shell_scripts_1},
          {ThreadType: '单线程', second: 'Shell Scripts (8 concurrent)(lpm)', third: this.stream_datas.shell_scripts_8},
          {ThreadType: '单线程', second: 'System Call Overhead(lps)', third: this.stream_datas.system_call_overhead},
          {ThreadType: '单线程', second: 'Index Score(sum)', third: this.stream_datas.index_score},

          {ThreadType: '多线程', second: 'Dhrystone 2 using register variables(lps)', third: this.stream_datas.Dhrystone_2},
          {ThreadType: '多线程', second: 'Double-Precision Whetstone(MWIPS)', third: this.stream_datas.Double_Precision_2},
          {ThreadType: '多线程', second: 'Execl Throughput(lps)', third: this.stream_datas.execl_throughput_2},
          {ThreadType: '多线程', second: 'File Copy 1024 bufsize 2000 maxblocks(KBps)', third: this.stream_datas.file_copy_1024_2},
          {ThreadType: '多线程', second: 'File Copy 256 bufsize 500 maxblocks(KBps)', third: this.stream_datas.file_copy_256_2},
          {ThreadType: '多线程', second: 'File Copy 4096 bufsize 8000 maxblocks(KBps)', third: this.stream_datas.file_copy_4096_2},
          {ThreadType: '多线程', second: 'Pipe Throughput(lps)', third: this.stream_datas.pipe_throughput_2},
          {ThreadType: '多线程', second: 'Pipe-based Context Switching(lps)', third: this.stream_datas.pipe_based_2},
          {ThreadType: '多线程', second: 'Process Creation(lps)', third: this.stream_datas.process_creation_2},
          {ThreadType: '多线程', second: 'Shell Scripts (1 concurrent)(lpm)', third: this.stream_datas.shell_scripts_1_2},
          {ThreadType: '多线程', second: 'Shell Scripts (8 concurrent)(lpm)', third: this.stream_datas.shell_scripts_8_2},
          {ThreadType: '多线程', second: 'System Call Overhead(lps)', third: this.stream_datas.system_call_overhead_2},
          {ThreadType: '多线程', second: 'Index Score(sum)', third: this.stream_datas.index_score_2},
      ]
    }
  },
  created() {
    axios.get('/api/unixbench/?env_id=' + this.$route.params.envId).then((response) => {
      this.getUnixbenchDatas = response.data.data
      //判断getUnixbenchDatas是否有两组数据
      if (this.getUnixbenchDatas[0].thread === '单线程'){
        this.singleThreaddata = this.getUnixbenchDatas[0]
        this.MultiThreaddata = this.getUnixbenchDatas[1]
      }else if(this.getUnixbenchDatas[0].thread === '多线程'){
        this.MultiThreaddata = this.getUnixbenchDatas[0]
        this.singleThreaddata = this.getUnixbenchDatas[1]
      }
      this.stream_datas.Dhrystone = this.singleThreaddata.Dhrystone
      this.stream_datas.Double_Precision = this.singleThreaddata.Double_Precision
      this.stream_datas.execl_throughput = this.singleThreaddata.execl_throughput
      this.stream_datas.file_copy_1024 = this.singleThreaddata.file_copy_1024
      this.stream_datas.file_copy_256 = this.singleThreaddata.file_copy_256
      this.stream_datas.file_copy_4096 = this.singleThreaddata.file_copy_4096
      this.stream_datas.pipe_throughput = this.singleThreaddata.pipe_throughput
      this.stream_datas.pipe_based = this.singleThreaddata.pipe_based
      this.stream_datas.process_creation = this.singleThreaddata.process_creation
      this.stream_datas.shell_scripts_1 = this.singleThreaddata.shell_scripts_1
      this.stream_datas.shell_scripts_8 = this.singleThreaddata.shell_scripts_8
      this.stream_datas.system_call_overhead = this.singleThreaddata.system_call_overhead
      this.stream_datas.index_score = this.singleThreaddata.index_score

      this.stream_datas.Dhrystone_2 = this.MultiThreaddata.Dhrystone
      this.stream_datas.Double_Precision_2 = this.MultiThreaddata.Double_Precision
      this.stream_datas.execl_throughput_2 = this.MultiThreaddata.execl_throughput
      this.stream_datas.file_copy_1024_2 = this.MultiThreaddata.file_copy_1024
      this.stream_datas.file_copy_256_2 = this.MultiThreaddata.file_copy_256
      this.stream_datas.file_copy_4096_2 = this.MultiThreaddata.file_copy_4096
      this.stream_datas.pipe_throughput_2 = this.MultiThreaddata.pipe_throughput
      this.stream_datas.pipe_based_2 = this.MultiThreaddata.pipe_based
      this.stream_datas.process_creation_2 = this.MultiThreaddata.process_creation
      this.stream_datas.shell_scripts_1_2 = this.MultiThreaddata.shell_scripts_1
      this.stream_datas.shell_scripts_8_2 = this.MultiThreaddata.shell_scripts_8
      this.stream_datas.system_call_overhead_2 = this.MultiThreaddata.system_call_overhead
      this.stream_datas.index_score_2 = this.MultiThreaddata.index_score
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
            if (item['ThreadType'] === arr[index - 1]['ThreadType']) {
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
