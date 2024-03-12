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
      other_list: [{first: '执行命令', second: './Run.sh'}, {first: '修改参数：', second: 'xxx'}],

      stream_datas: {
        single_array_size: '',
        single_copy: '',
        single_scale: '',
        single_add: '',
        single_triad: '',
        multi_array_size: '',
        multi_copy: '',
        multi_scale: '',
        multi_add: '',
        multi_triad: '',
      },
      getStreamDatas: []
    }
  },
  computed: {
    tableDatas() {
      return [
        {ThreadType: '单线程', second: 'Array size', third: this.stream_datas.single_array_size,},
        {ThreadType: '单线程', second: 'Copy', third: this.stream_datas.single_copy,},
        {ThreadType: '单线程', second: 'Scale', third: this.stream_datas.single_scale,},
        {ThreadType: '单线程', second: 'Add', third: this.stream_datas.single_add,},
        {ThreadType: '单线程', second: 'Triad', third: this.stream_datas.single_triad,},
        {ThreadType: '多线程', second: 'Array size', third: this.stream_datas.multi_array_size,},
        {ThreadType: '多线程', second: 'Copy', third: this.stream_datas.multi_copy,},
        {ThreadType: '多线程', second: 'Scale', third: this.stream_datas.multi_scale,},
        {ThreadType: '多线程', second: 'Add', third: this.stream_datas.multi_add,},
        {ThreadType: '多线程', second: 'Triad', third: this.stream_datas.multi_triad}]
    }
  },
  created() {
    axios.get('/api/stream/?env_id=' + this.$route.params.baseId).then((response) => {
      this.getStreamDatas = response.data.data[0]
      this.other_list[0].second = this.getStreamDatas.execute_cmd
      this.other_list[1].second = this.getStreamDatas.modify_parameters
      this.stream_datas.single_array_size = this.getStreamDatas.single_array_size
      this.stream_datas.single_copy = this.getStreamDatas.single_copy
      this.stream_datas.single_scale = this.getStreamDatas.single_scale
      this.stream_datas.single_add = this.getStreamDatas.single_add
      this.stream_datas.single_triad = this.getStreamDatas.single_triad
      this.stream_datas.multi_array_size = this.getStreamDatas.multi_array_size
      this.stream_datas.multi_copy = this.getStreamDatas.multi_copy
      this.stream_datas.multi_scale = this.getStreamDatas.multi_scale
      this.stream_datas.multi_add = this.getStreamDatas.multi_add
      this.stream_datas.multi_triad = this.getStreamDatas.multi_triad
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
