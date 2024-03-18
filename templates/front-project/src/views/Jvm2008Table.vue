<template>
  <div>
    <el-table :data="other_list" border style="width:100%;margin-top: 20px">
      <el-table-column prop="first" label="Jvm2008" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Jvm2008#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="tableDatas" :span-method="objectSpanMethod"  border style="width: 100%" :show-header="false">
      <el-table-column prop="first" align="center" min-width="30%"></el-table-column>
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
      jvmData: {
        base_compiler: '',
        base_compress: '',
        base_crypto: '',
        base_derby: '',
        base_mpegaudio: '',
        base_scimark_large: '',
        base_scimark_small: '',
        base_serial: '',
        base_startup: '',
        base_sunflow: '',
        base_xml: '',
        base_Noncompliant_pomposite_result: '',
        peak_compiler: '',
        peak_compress: '',
        peak_crypto: '',
        peak_derby: '',
        peak_mpegaudio: '',
        peak_scimark_large: '',
        peak_scimark_small: '',
        peak_serial: '',
        peak_startup: '',
        peak_sunflow: '',
        peak_xml: '',
        peak_Noncompliant_pomposite_result: '',
      },
      getJvmData: [],
      baseData: [],
      peakData: [],
    }
  },
  computed: {
    tableDatas() {
      return [
        {first: 'base', second: 'compiler', third: this.baseData.compiler},
        {first: 'base', second: 'compress', third: this.baseData.compress},
        {first: 'base', second: 'crypto', third: this.baseData.crypto},
        {first: 'base', second: 'derby', third: this.baseData.derby},
        {first: 'base', second: 'mpegaudio', third: this.baseData.mpegaudio},
        {first: 'base', second: 'scimark.large', third: this.baseData.scimark_large},
        {first: 'base', second: 'scimark.small', third: this.baseData.scimark_small},
        {first: 'base', second: 'serial', third: this.baseData.serial},
        {first: 'base', second: 'startup', third: this.baseData.startup},
        {first: 'base', second: 'sunflow', third: this.baseData.sunflow},
        {first: 'base', second: 'xml', third: this.baseData.xml},
        {first: 'base', second: 'Noncompliant composite result:', third: this.baseData.Noncompliant_pomposite_result},
        {first: 'peak', second: 'compiler', third: this.peakData.compiler},
        {first: 'peak', second: 'compress', third: this.peakData.compress},
        {first: 'peak', second: 'crypto', third: this.peakData.crypto},
        {first: 'peak', second: 'derby', third: this.peakData.derby},
        {first: 'peak', second: 'mpegaudio', third: this.peakData.mpegaudio},
        {first: 'peak', second: 'scimark.large', third: this.peakData.scimark_large},
        {first: 'peak', second: 'scimark.small', third: this.peakData.scimark_small},
        {first: 'peak', second: 'serial', third: this.peakData.serial},
        {first: 'peak', second: 'startup', third: this.peakData.startup},
        {first: 'peak', second: 'sunflow', third: this.peakData.sunflow},
        {first: 'peak', second: 'xml', third: this.peakData.xml},
        {first: 'peak', second: 'Noncompliant composite result:', third: this.peakData.Noncompliant_pomposite_result},
      ]
    }
  },
  created() {
    axios.get('/api/jvm2008/?env_id=' + this.$route.params.baseId).then((response) => {
      this.getJvmData = response.data.data
      if (this.getJvmData[0].tune_type === 'base') {
        this.baseData = this.getJvmData[0]
        this.peakData = this.getJvmData[1]
      }else if(this.getJvmData[0].tune_type === 'peak'){
        this.baseData = this.getJvmData[1]
        this.peakData = this.getJvmData[0]
      }
      this.other_list[0].second=this.baseData.execute_cmd
      this.other_list[1].second=this.baseData.modify_parameters

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
            if (item['first'] === arr[index - 1]['first']) {
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
