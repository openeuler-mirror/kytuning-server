<template>
  <div id="tatle-div">
    <button id="bt1" @click="ShowSingleData">单条数据</button>
    <button id="bt2" @click="getComparativeData">数据对比</button>
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
  <div class="table-container">
    <table class="custom-table">
      <thead>
      <tr>
        <th>单条数据或基准数据</th>
        <th>对比数据</th>
        <th>项目名称</th>
        <th>上传人员</th>
        <th>第几次</th>
        <th>系统版本</th>
        <th>cpu型号</th>
        <th>serialnumber</th>
        <th>stream</th>
        <th>lmbench</th>
        <th>unixbench</th>
        <th>fio</th>
        <th>iozone</th>
        <th>cpu2006</th>
        <th>cpu2017</th>
        <th>jvm2008</th>
        <th>录入时间</th>
        <th>描述</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="project in allProjectDatas" :key="project.id">
        <td style="text-align: center;">
          <label style="display: inline-block;">
            <input type="checkbox" v-model="baseData" :value="project">
          </label>
        </td>
        <td style="text-align: center;">
          <label style="display: inline-block;">
            <input type="checkbox" v-model="comparativeData" :value="project">
          </label>
        </td>
        <td>{{ project.project_name }}</td>
        <td>{{ project.user_name }}</td>
        <td>{{ project.times }}</td>
        <td>{{ project.os_version }}</td>
        <td>{{ project.cpu_module_name }}</td>
        <td>{{ project.hwinfo_machineinfo_serialnumber }}</td>
        <td>{{ project.stream }}</td>
        <td>{{ project.lmbench }}</td>
        <td>{{ project.unixbench }}</td>
        <td>{{ project.fio }}</td>
        <td>{{ project.iozone }}</td>
        <td>{{ project.cpu2006 }}</td>
        <td>{{ project.cpu2017 }}</td>
        <td>{{ project.jvm2008 }}</td>
        <td>{{ project.test_time }}</td>
        <td>{{ project.message }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import {ElMessage} from 'element-plus';

export default {
  data() {
    return {
      allProjectDatas: [], // 从后端获取的全部数据
      baseData: [], // 用户选择的基准数据
      comparativeData: [], // 用户选择的对比数据
      selected: '',
      selectedType: '',
    }
  },
  created() {
    axios.get('/api/project/').then((response) => {
      this.allProjectDatas = response.data.data
    });
  },

  methods: {
    // toggleCheckbox(event) {
    //   const project = event.target.dataset.project;
    //   const index = this.baseData.indexOf(project);
    //   if (index === -1) {
    //     this.baseData.push(project);
    //   } else {
    //     this.baseData.splice(index, 1);
    //   }
    // },

    ShowSingleData() {
      //跳转详情页面

      if (this.selectedType) {
        const env_id = this.baseData.map(project => {return project.env_id})
        if (env_id.length !== 1) {
          ElMessage.error('请选择基准数据');
          return
        } else {
          // 跳转env详情页面

          if (this.selectedType === "env") {
            this.$router.push({name: 'env', "params": {baseId: env_id[0]}});
          } else if (this.selectedType === "stream") {
            if (this.baseData[0].stream) {
              this.$router.push({
                name: 'stream',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有stream数据');
            }
          } else if (this.selectedType === "lmbench") {
            if (this.baseData[0].lmbench) {
              this.$router.push({
                name: 'lmbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有lmbench数据');
            }
          } else if (this.selectedType === "unixbench") {
            if (this.baseData[0].unixbench) {
              this.$router.push({
                name: 'unixbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有unixbench数据');
            }
          } else if (this.selectedType === "fio") {
            if (this.baseData[0].fio) {
              this.$router.push({
                name: 'fio',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有fio数据');
            }
          } else if (this.selectedType === "iozone") {
            if (this.baseData[0].iozone) {
              this.$router.push({
                name: 'iozone',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有iozone数据');
            }
          } else if (this.selectedType === "cpu2006") {
            if (this.baseData[0].cpu2006) {
              this.$router.push({
                name: 'cpu2006',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有cpu2006数据');
            }
          } else if (this.selectedType === "cpu2017") {
            if (this.baseData[0].cpu2017) {
              this.$router.push({
                name: 'cpu2017',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error('该数据没有cpu2017数据');
            }
          } else if (this.selectedType === "jvm2008") {
            if (this.baseData[0].jvm2008) {
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
        const env_id = this.baseData.map(project => {return project.env_id})
        const env_ids = this.comparativeData.map(project => {return project.env_id})
        const comparsionIds = env_ids.join(',')

        const streams = this.comparativeData.map(project => {return project.stream})
        const unixbenchs = this.comparativeData.map(project => {return project.unixbench})
        const lmbenchs = this.comparativeData.map(project => {return project.lmbench})
        const fios = this.comparativeData.map(project => {return project.fio})
        const iozones = this.comparativeData.map(project => {return project.iozone})
        const cpu2006s = this.comparativeData.map(project => {return project.cpu2006})
        const cpu2017s = this.comparativeData.map(project => {return project.cpu2017})
        const jvm2008s = this.comparativeData.map(project => {return project.jvm2008})

        if (this.selectedType === "env") {
          ElMessage.error('环境信息数据不支持对比');
        } else if (this.selectedType === "stream") {
          if (this.baseData[0].stream && !streams.includes(0)) {
            this.$router.push({
              name: 'stream',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有stream为空');
          }
        } else if (this.selectedType === "lmbench") {
          if (this.baseData[0].lmbench && !lmbenchs.includes(0)) {
            this.$router.push({
              name: 'lmbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有lmbench为空');
          }
        } else if (this.selectedType === "unixbench") {
          if (this.baseData[0].unixbench && !unixbenchs.includes(0)) {
            this.$router.push({
              name: 'unixbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有unixbench为空');
          }
        } else if (this.selectedType === "fio") {
          if (this.baseData[0].fio && !fios.includes(0)) {
            this.$router.push({
              name: 'fio',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有fio为空');
          }
        } else if (this.selectedType === "iozone") {
          if (this.baseData[0].iozone && !iozones.includes(0)) {
            this.$router.push({
              name: 'iozone',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有iozone为空');
          }
        } else if (this.selectedType === "cpu2006") {
          if (this.baseData[0].cpu2006 && !cpu2006s.includes(0)) {
            this.$router.push({
              name: 'cpu2006',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有cpu2006为空');
          }
        } else if (this.selectedType === "cpu2017") {
          if (this.baseData[0].cpu2017 && !cpu2017s.includes(0)) {
            this.$router.push({
              name: 'cpu2017',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error('该数据中有cpu2017为空');
          }
        } else if (this.selectedType === "jvm2008") {
          if (this.baseData[0].jvm2008 && !jvm2008s.includes(0)) {
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
