<template>
  <div id="tatle-div">
    <el-row class="mb-4">
      <el-button @click="ShowSingleData" type="success" plain>基准数据</el-button>
      <el-button @click="getComparativeData()" type="primary" plain>数据对比</el-button>
      <el-button @click="restData()" type="danger" plain>取消选择</el-button>
    </el-row>
    <div>数据类型: {{ selected }}</div>
    <select v-model="selectedType">
      <option disabled value="">请在下列选项中选择一个</option>
      <option value="env">环境信息</option>
      <option value="stream">stream</option>
      <option value="lmbench">lmbench</option>
      <option value="unixbench">unixbench</option>
      <option value="fio">fio</option>
      <option value="iozone">iozone</option>
      <option value="cpu2006">cpu2006</option>
      <option value="cpu2017">cpu2017</option>
      <option value="jvm2008">jvm2008</option>
    </select>
  </div>
  <br>
  <el-table
      ref="multipleTable"
      :data="compData"
      tooltip-effect="dark"
      border
      style="width: 100%"
  >
    <el-table-column label="基准数据" width="55">
      <template #default="{ row }">
        <el-checkbox v-model="base[row.id]" :label="row" :key="row.id" @change="handleBaseDataChange(row)">{{}}
        </el-checkbox>
      </template>
    </el-table-column>
    <el-table-column label="对比数据" width="55">
      <template #default="{ row }">
        <el-checkbox v-model="compar[row.id]" :label="row" :key="row.id" @change="handleComparativeDataChange(row)">
          {{}}
        </el-checkbox>
      </template>
    </el-table-column>
    <el-table-column prop="project_name" label="项目名称" column-key="project_name"
                     :filters=projectNames :filter-method="filterHandler" filter-placement="bottom-end"
    />
    <el-table-column prop="user_name" label="上传人员" width="80"
                     :filters=userNames
                     :filter-method="filterHandler" filter-placement="bottom-end"/>
    <el-table-column prop="os_version" label="系统版本" width="220"
                     :filters=osNames
                     :filter-method="filterHandler" filter-placement="bottom-end"/>
    <el-table-column prop="cpu_module_name" label="cpu型号" width="190"
                     :filters=cpuNames
                     :filter-method="filterHandler" filter-placement="bottom-end"/>
    <el-table-column prop="times" label="第几次" width="70"/>
    <el-table-column prop="ip" label="ip"/>
    <el-table-column prop="stream" label="stream" width="80"/>
    <el-table-column prop="lmbench" label="lmbench" width="90"/>
    <el-table-column prop="unixbench" label="unixbench" width="100"/>
    <el-table-column prop="fio" label="fio" width="50"/>
    <el-table-column prop="iozone" label="iozone" width="80"/>
    <el-table-column prop="cpu2006" label="cpu2006" width="90"/>
    <el-table-column prop="cpu2017" label="cpu2017" width="90"/>
    <el-table-column prop="jvm2008" label="jvm2008" width="90"/>
    <el-table-column prop="test_time" sortable label="录入时间"/>
    <el-table-column prop="message" label="描述"/>
  </el-table>
  <br>
  <div class="parent-container">
    <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 20, 30, 50, total]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
    >
    </el-pagination>
  </div>
</template>


<script>
// import axios from 'axios'
import {ElMessage} from 'element-plus';
import 'element-ui/lib/theme-chalk/index.css';
import { project, get_filter_name } from "@/api/api.js";

export default {

  data() {
    return {
      allProjectDatas: [], // 从后端获取的全部数据
      base: {}, // 用户选择的基准数据id
      compar: {}, // 用户选择的对比数据id
      selected: '',
      selectedType: 'stream', //给一个默认值
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      projectNames: [],
      userNames: [],
      osNames: [],
      cpuNames: [],
    }
  },

  created() {
    project().then(response => {
      console.log(response,111)
      this.allProjectDatas = response.data.data
      this.total = this.allProjectDatas.length;
    });
    get_filter_name().then((response) => {
      this.projectNames = response.data.data.projectNames
      this.userNames = response.data.data.userNames
      this.osNames = response.data.data.osNames
      this.cpuNames = response.data.data.cpuNames
    });
  },

  computed: {
    compData() {
      return this.allProjectDatas.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
      );
    },
  },
  methods: {
    //处理点击事件
    handleBaseDataChange(row) {
      if (!this.base[row.id]) {
        delete this.base[row.id];
      }
    },
    handleComparativeDataChange(row) {
      if (!this.compar[row.id]) {
        delete this.compar[row.id];
      }
    },
    restData() {
      this.base = {};
      this.compar = {};
    },
    //查询
    filterHandler(value, row, column) {
      console.log(value, 11)
      console.log(row, 22)
      console.log(column, 33)
      const property = column['property'];
      return row[property] === value;
    },

    // 分页
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },

    //跳转base页面
    ShowSingleData() {
      if (this.selectedType) {
        console.log(this.base, 11)
        const env_id = Object.keys(this.base).map(key => parseInt(key));
        if (env_id.length !== 1) {
          ElMessage.error('请选择一条数据作为基准数据');
          return
        } else {
          if (this.selectedType === "env") {
            this.$router.push({name: 'env', "params": {baseId: env_id[0]}});
          } else if (this.selectedType === "stream") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).stream) {
              this.$router.push({
                name: 'stream', "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有stream数据');
            }
          } else if (this.selectedType === "lmbench") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).lmbench) {
              this.$router.push({
                name: 'lmbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有lmbench数据');
            }
          } else if (this.selectedType === "unixbench") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).unixbench) {
              this.$router.push({
                name: 'unixbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有unixbench数据');
            }
          } else if (this.selectedType === "fio") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).fio) {
              this.$router.push({
                name: 'fio',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有fio数据');
            }
          } else if (this.selectedType === "iozone") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).iozone) {
              this.$router.push({
                name: 'iozone',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有iozone数据');
            }
          } else if (this.selectedType === "cpu2006") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).cpu2006) {
              this.$router.push({
                name: 'cpu2006',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有cpu2006数据');
            }
          } else if (this.selectedType === "cpu2017") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).cpu2017) {
              this.$router.push({
                name: 'cpu2017',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有cpu2017数据');
            }
          } else if (this.selectedType === "jvm2008") {
            if (this.allProjectDatas.find(item => item.id === env_id[0]).jvm2008) {
              this.$router.push({
                name: 'jvm2008',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有jvm2008数据');
            }
          }
        }
      } else {
        ElMessage.error('请选择数据类型');
      }
      console.log("跳转成功")
    },
    getComparativeData() {
      if (this.selectedType) {
        const env_id = Object.keys(this.base).map(key => parseInt(key));
        const baseData = this.allProjectDatas.find(item => env_id.includes(item.id))
        const env_ids = Object.keys(this.compar).map(key => parseInt(key));
        const comparData = this.allProjectDatas.filter(item => env_ids.includes(item.id))
        const comparsionIds = env_ids.join(',')
        const streams = comparData.map(project => {
          return project.stream
        })
        const unixbenchs = comparData.map(project => {
          return project.unixbench
        })
        const lmbenchs = comparData.map(project => {
          return project.lmbench
        })
        const fios = comparData.map(project => {
          return project.fio
        })
        const iozones = comparData.map(project => {
          return project.iozone
        })
        const cpu2006s = comparData.map(project => {
          return project.cpu2006
        })
        const cpu2017s = comparData.map(project => {
          return project.cpu2017
        })
        const jvm2008s = comparData.map(project => {
          return project.jvm2008
        })

        if (this.selectedType === "env") {
          ElMessage.error('环境信息数据不支持对比');
        } else if (this.selectedType === "stream") {
          if (baseData.stream && !streams.includes(0)) {
            this.$router.push({name: 'stream', "params": {baseId: env_id[0], comparsionIds: comparsionIds}});
          } else {
            ElMessage.error('该数据中有stream为空');
          }
        } else if (this.selectedType === "lmbench") {
          if (baseData.lmbench && !lmbenchs.includes(0)) {
            this.$router.push({
              name: 'lmbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有lmbench为空');
          }
        } else if (this.selectedType === "unixbench") {
          if (baseData.unixbench && !unixbenchs.includes(0)) {
            this.$router.push({
              name: 'unixbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有unixbench为空');
          }
        } else if (this.selectedType === "fio") {
          if (baseData.fio && !fios.includes(0)) {
            this.$router.push({
              name: 'fio',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有fio为空');
          }
        } else if (this.selectedType === "iozone") {
          if (baseData.iozone && !iozones.includes(0)) {
            this.$router.push({
              name: 'iozone',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有iozone为空');
          }
        } else if (this.selectedType === "cpu2006") {
          if (baseData.cpu2006 && !cpu2006s.includes(0)) {
            this.$router.push({
              name: 'cpu2006',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有cpu2006为空');
          }
        } else if (this.selectedType === "cpu2017") {
          if (baseData.cpu2017 && !cpu2017s.includes(0)) {
            this.$router.push({
              name: 'cpu2017',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有cpu2017为空');
          }
        } else if (this.selectedType === "jvm2008") {
          if (baseData.jvm2008 && !jvm2008s.includes(0)) {
            this.$router.push({
              name: 'jvm2008',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有jvm2008为空');
          }
        }
      } else {
        ElMessage.error('请选择数据类型');
      }
    },
  }
}
</script>

<style scoped>
#tatle-div {
  display: flex; /* 将 div 设置为弹性容器 */
  justify-content: center; /* 将按钮水平居中对齐 */
  align-items: center; /* 将按钮垂直居中对齐 */
}

.parent-container {
  display: flex;
  justify-content: center;
  /*background-color: #f2f2f2;*/
}
</style>

