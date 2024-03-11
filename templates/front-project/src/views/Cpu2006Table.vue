<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Unixbench" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Unixbench#1"></el-table-column>
    </el-table>
  </div>
  <div class="element-main">
    <div> Element-ui 官方提供 table Demo</div>
    <el-table
        style="width: 100%"
        :data="tableData"
    >
      <el-table-column
          prop="date"
          label="日期"
          width="180">
      </el-table-column>
      <el-table-column
          prop="name"
          label="姓名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="address"
          label="地址">
      </el-table-column>
    </el-table>
    <div>===================================== 分割线 =====================================</div>
    <div>行列转换后的 Demo</div>
    <el-table
        style="width: 100%"
        :data="getValues"
        :show-header="false"
    >
      <el-table-column
          v-for="(item, index) in getHeaders"
          :key="index"
          :prop="item"
      >
      </el-table-column>
    </el-table>
  </div>
</template>


<script>
// import axios from 'axios'
import {ElTable, ElTableColumn} from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
  },
  data() {
    return {
      headers: [
        {
          prop: 'date',
          label: '日期',
        },
        {
          prop: 'name',
          label: '姓名',
        },
        {
          prop: 'address',
          label: '地址',
        },
      ],
      tableData: [
        {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },
        {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        },
        {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        },
        {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }
      ]
    }
  },
  computed: {
    getHeaders() {
      console.log(this.tableData.reduce((pre, cur, index) => pre.concat(`value${index}`), ['title']),1111)
      return this.tableData.reduce((pre, cur, index) => pre.concat(`value${index}`), ['title'])
    },
    getValues() {
      return this.headers.map(item => {
        console.log(this.tableData.reduce((pre, cur, index) => Object.assign(pre, {['value' + index]: cur[item.prop]}), {'title': item.label,}),222)
        return this.tableData.reduce((pre, cur, index) => Object.assign(pre, {['value' + index]: cur[item.prop]}), {'title': item.label,});
      });
    }
  },
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
