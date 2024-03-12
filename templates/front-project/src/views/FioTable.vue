<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Fio" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Fio#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column
          prop="rw"
          align="center" min-width="30%"
      ></el-table-column>
      <el-table-column  align="center" min-width="50%">
        <template #default="{ row }">
          <div v-for="(property, index) in displayProperties(row)" :key="index">
            <div>{{ property }}</div>
          </div>
        </template>
      </el-table-column>
      <el-table-column>
        <template #default="{ row }" >
          <div v-for="(property, index) in displayProperties(row)" :key="index">
            <div>{{ row[property] }}</div>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
import {ElTable, ElTableColumn} from 'element-plus';

export default ({
  components: {
    ElTable,
    ElTableColumn
  },
  data() {
    return {
      other_list: [{first: '执行命令', second: './Run -c {FUNC_THREAD_NUM}'}, {first: '修改参数：', second: 'xxx'}],
      tableData: []
    };
  },
  created() {
    axios.get('/api/fio/?env_id=' + this.$route.params.baseId).then((response) => {
      this.tableData = response.data.data
      this.other_list[0].second = this.tableData[0].execute_cmd
      this.other_list[1].second = this.tableData[0].modify_parameters
    })
  },
  methods: {
// 返回要显示的属性，排除 'rw' 属性
    displayProperties(row) {
      return Object.keys(row).filter(key => key !== 'rw' && key !== 'id' && key !== 'env_id' && key !== 'execute_cmd' && key !== 'modify_parameters' && key !== 'test_time');
    }
  }
});
</script>
<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
