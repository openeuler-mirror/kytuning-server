<template>
  <div id="tatle-div">
    <button id="bt1" @click="ShowSingleData">单条数据</button>
    <button id="bt2" @click="getSelectedData">数据对比</button>
    <div>数据类型: {{ selected }}</div>
    <select v-model="selectedType">
      <option disabled value="">请在下列选项中选择一个</option>
      <option value="env">环境信息</option>
      <option value="unixbench">unixbench</option>
      <option value="lmbench">lmbench</option>
      <option value="stream">stream</option>
      <option value="fio">fio</option>
      <option value="iozone">iozone</option>
      <option value="cpu2006">cpu2006</option>
      <option value="cpu2017">cpu2017</option>
      <option value="jvm2008">jvm2008</option>
    </select>
  </div>
  <div v-if="oneData">
    一次性只能查看一条数据信息
  </div>
  <div v-if="twoData">
    数据超过两条，请重新选择
  </div>
  <div class="table-container">
    <table class="custom-table">
      <thead>
      <tr>
        <th></th>
        <th>系统版本</th>
        <th>项目名称</th>
        <th>第几次</th>
        <th>架构</th>
        <th>serialnumber</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="project in allProjectDatas" :key="project.id">
        <td><input type="checkbox" v-model="userProjectData" :value="project"></td>
        <td>{{ project.os_version }}</td>
        <td>{{ project.project_name }}</td>
        <td>{{ project.times }}</td>
        <td>{{ project.arm }}</td>
        <td>{{ project.hwinfo_machineinfo_serialnumber }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      allProjectDatas: [], // 从后端获取的全部数据
      userProjectData: [], // 用户选择的数据
      selected: '',
      selectedType: '',
      twoData: false,
      oneData: false,
    }
  },
  created() {
    axios.get('/api/project/').then((response) => {
      this.allProjectDatas = response.data.data
    });
  },
  // created() {
  //   this.$http.get('/api/project/').then((response) => {
  //     this.allProjectDatas = response.data.data
  //   });
  // },


  methods: {
    ShowSingleData() {
      //跳转详情页面
      if (this.selectedType) {
        const env_id = this.userProjectData.map(project => {
          return project.env_id
        })
        if (env_id.length !== 1) {
          console.log(env_id, "选择一条数据作为详细信息查询")
          this.oneData = true
          return
        } else {
          // 跳转env详情页面
          if (this.selectedType === "env") {
            // this.$router.push({name: 'env', "params": {projectId: env_id[0], selectedType: this.selectedType}});
            this.$router.push({name: 'env', "params": {envId: env_id[0]}});
          }else if(this.selectedType === "stream"){
            this.$router.push({name: 'stream', "params": {envId: env_id[0]}});
          }

        }
      } else {
        console.log("请选择数据类型")
        return
      }
      console.log("跳转成功")
    },
    getSelectedData() {
      if (this.selectedType) {
        const selectedData = this.userProjectData.map(project => {
          return project.id
        })
        if (selectedData.length > 2) {
          // console.log(selectedData, "超过两条了")
          this.twoData = true
        } else {
          // 跳转数据对比页面
        }
      } else {
        console.log("请选择数据类型")
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

button {
  border: none;
  padding: 15px 30px;
  font-size: 16px;
  font-family: Arial, 微软雅黑;
  color: white;
  background: #447aa8;
  border-radius: 3px;
}

#bt1 {
  background: red;
}

#bt2 {
  background: blue;
  margin-left: 30px;
  margin-right: 100px;
}

.table-container {
  width: 100%;
  overflow-x: auto;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
  font-size: 14px;
}

.custom-table th,
.custom-table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

.custom-table th:first-child,
.custom-table td:first-child {
  position: sticky;
  left: 0;
  background-color: #f5f5f5;
  border-right: none;
}

.custom-table th:last-child,
.custom-table td:last-child {
  border-right: none;
}

.custom-table th {
  font-weight: bold;
  background-color: #f5f5f5;
  border-top: none;
}

.custom-table tbody tr:hover {
  background-color: #f5f5f5;
}
</style>
