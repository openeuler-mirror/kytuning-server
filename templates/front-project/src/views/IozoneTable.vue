<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Iozone" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Iozone#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="getIozoneDatas" border style="width: 100%" :show-header="false">
      <el-table-column prop="first" label="一级字段" align="center" min-width="30%" center></el-table-column>
      <el-table-column prop="second" label="二级字段" align="center" min-width="50%"></el-table-column>
      <el-table-column prop="third" label="san级字段" ></el-table-column>
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
      getIozoneDatas:  [
            {
                "first": "写测试（KB/s）",
                "second": 1048576.0,
                "third": 2814553.0
            },
            {
                "first": "重写测试（KB/s)",
                "second": 1048576.0,
                "third": 4204919.0
            },
            {
                "first": "读测试（KB/s）",
                "second": 1048576.0,
                "third": 5474048.0
            },
            {
                "first": "重读测试（KB/s)",
                "second": 1048576.0,
                "third": 4684993.0
            },
            {
                "first": "随机读测试（KB/s）",
                "second": 1048576.0,
                "third": 5497958.0
            },
            {
                "first": "随机写测试（KB/s）",
                "second": 1048576.0,
                "third": 4139888.0
            }
        ],
    }
  },
  computed: {
    tableDatas() {
    return [
        {first:'Memory latencies in nanoseconds',second:'Rand mem',third:'this.lmbench_datas.memory_Rand_mem'},
      ]
    }
  },
  created() {
    axios.get('/api/iozone/?env_id=' + this.$route.params.baseId).then((response) => {
      this.getIozoneDatas = response.data.data[0]
    })
  },
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
