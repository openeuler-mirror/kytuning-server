<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 11 16:52:35 2024 +0800
-->
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
      :key="itemKey"
  >
    <el-table-column label="基准数据" width="55">
      <template #default="{ row }">
<!--        <el-checkbox v-model="base[row.id]" :label="row" :key="row.id" @change="handleBaseDataChange(row)">{{}}-->
        <el-checkbox v-model="base[row.env_id]" :label="row" :key="row.id" @change="handleBaseDataChange(row)">{{}}
        </el-checkbox>
      </template>
    </el-table-column>
    <el-table-column label="对比数据" width="55">
      <template #default="{ row }">
        <el-checkbox v-model="compar[row.env_id]" :label="row" :key="row.id" @change="handleComparativeDataChange(row)">
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

    <el-table-column label="操作" width="180">
      <template #default="scope">
        <el-button type="primary" @click="edit(scope.row)">修改</el-button>
                <el-button type="danger" @click="del(scope.row)">删除</el-button>
  </template>
    </el-table-column>
  </el-table>
  <br>
<el-dialog :title="修改project信息" v-model="dialogFormVisible" width="500px">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="project_name">
          <el-input v-model="form.project_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="message" :label-width="formLabelWidth" prop="message">
          <el-input v-model="form.message" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeInfo('form')">取 消</el-button>
          <el-button type="primary" @click="sure('form')"
          >确 定
          </el-button
          >
        </span>
      </template>
    </el-dialog>
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
import {ElMessage} from 'element-plus';
import 'element-ui/lib/theme-chalk/index.css';
import { project, get_filter_name } from "@/api/api.js";


export default {
  data() {
    return {
      showEditButton: true,
      showDeleteButton: false,
      allProjectDatas: [], // 从后端获取的全部数据
      base: {}, // 用户选择的基准数据id
      compar: {}, // 用户选择的对比数据id
      selected: '',
      selectedType: 'stream', //给一个默认值
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      projectNames: [],//筛选项目名称
      userNames: [],//筛选用户名称
      osNames: [],//筛选os版本
      cpuNames: [],//筛选cpu型号

      itemKey: 0, //跟新数据后生成随机数从而刷新页面数据
      dialogFormVisible: false,
      form: {
        id: 0,
        project_name: "",
        message: "",
      },//用户修改后的数据
      formLabelWidth: "80px",
      rules: {
        project_name: [{required: true, message: '请输入项目名称'}],
      },
    }
  },

  created() {
    project('get','').then(response => {
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
    sure(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          // // 发送数据
          project('put', this.form).then(response => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              //更新页面数据，绑定key，每次key改变后就会刷新数据
              this.itemKey = Math.random()
              this.refreshData();
              this.dialogFormVisible = false
            }
          });
        }
      })
    },
    edit(row) {
      this.form = {...row}
      this.dialogFormVisible = true
    },
    closeInfo(form) {
      this.$refs[form].resetFields()
      this.dialogFormVisible = false
    },
    del(row) {
      project('delete', {id: row.id}).then(response => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              //更新页面数据，绑定key，每次key改变后就会刷新数据
              this.itemKey = Math.random()
              this.refreshData();
              this.dialogFormVisible = false
            }
          })
    },

    //更新数据后刷新页面数据
    refreshData() {
      // 调用 getProjects() 方法重新获取数据
      project('get', '').then(response => {
        this.allProjectDatas = response.data.data
        this.total = this.allProjectDatas.length;
      }).catch(error => {
        console.error(error);
      });
    },

    //处理前两列的选择框
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
        const env_id = Object.keys(this.base).map(key => parseInt(key));
        if (env_id.length !== 1) {
          ElMessage.error({message:'请选择一条数据作为基准数据',duration: 1000});
          return
        } else {
          if (this.selectedType === "env") {
            this.$router.push({name: 'env', "params": {baseId: env_id[0]}});
          } else if (this.selectedType === "stream") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).stream) {
              this.$router.push({
                name: 'stream', "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有stream数据',duration: 1000});
            }
          } else if (this.selectedType === "lmbench") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).lmbench) {
              this.$router.push({
                name: 'lmbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有lmbench数据',duration: 1000});
            }
          } else if (this.selectedType === "unixbench") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).unixbench) {
              this.$router.push({
                name: 'unixbench',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有unixbench数据',duration: 1000});
            }
          } else if (this.selectedType === "fio") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).fio) {
              this.$router.push({
                name: 'fio',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有fio数据',duration: 1000});
            }
          } else if (this.selectedType === "iozone") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).iozone) {
              this.$router.push({
                name: 'iozone',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有iozone数据',duration: 1000});
            }
          } else if (this.selectedType === "cpu2006") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).cpu2006) {
              this.$router.push({
                name: 'cpu2006',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有cpu2006数据',duration: 1000});
            }
          } else if (this.selectedType === "cpu2017") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).cpu2017) {
              this.$router.push({
                name: 'cpu2017',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有cpu2017数据',duration: 1000});
            }
          } else if (this.selectedType === "jvm2008") {
            if (this.allProjectDatas.find(item => item.env_id === env_id[0]).jvm2008) {
              this.$router.push({
                name: 'jvm2008',
                "params": {baseId: env_id[0], comparsionIds: ''}
              });
            } else {
              ElMessage.error({message:'该数据没有jvm2008数据',duration: 1000});
            }
          }
        }
      } else {
        ElMessage.error({message:'请选择数据类型',duration: 1000});
      }
      console.log("跳转成功")
    },
    getComparativeData() {
      if (this.selectedType) {
        const env_id = Object.keys(this.base).map(key => parseInt(key));
        const baseData = this.allProjectDatas.find(item => env_id.includes(item.env_id))
        const env_ids = Object.keys(this.compar).map(key => parseInt(key));
        const comparData = this.allProjectDatas.filter(item => env_ids.includes(item.env_id))
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
          ElMessage.error({message:'环境信息数据不支持对比',duration: 1000});
        } else if (this.selectedType === "stream") {
          if (baseData.stream && !streams.includes(0)) {
            this.$router.push({name: 'stream', "params": {baseId: env_id[0], comparsionIds: comparsionIds}});
          } else {
            ElMessage.error({message:'该数据中有stream为空',duration: 1000});
          }
        } else if (this.selectedType === "lmbench") {
          if (baseData.lmbench && !lmbenchs.includes(0)) {
            this.$router.push({
              name: 'lmbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有lmbench为空',duration: 1000});
          }
        } else if (this.selectedType === "unixbench") {
          if (baseData.unixbench && !unixbenchs.includes(0)) {
            this.$router.push({
              name: 'unixbench',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有unixbench为空',duration: 1000});
          }
        } else if (this.selectedType === "fio") {
          if (baseData.fio && !fios.includes(0)) {
            this.$router.push({
              name: 'fio',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有fio为空',duration: 1000});
          }
        } else if (this.selectedType === "iozone") {
          if (baseData.iozone && !iozones.includes(0)) {
            this.$router.push({
              name: 'iozone',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有iozone为空',duration: 1000});
          }
        } else if (this.selectedType === "cpu2006") {
          if (baseData.cpu2006 && !cpu2006s.includes(0)) {
            this.$router.push({
              name: 'cpu2006',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有cpu2006为空',duration: 1000});
          }
        } else if (this.selectedType === "cpu2017") {
          if (baseData.cpu2017 && !cpu2017s.includes(0)) {
            this.$router.push({
              name: 'cpu2017',
              "params": {baseId: env_id[0],comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有cpu2017为空',duration: 1000});
          }
        } else if (this.selectedType === "jvm2008") {
          if (baseData.jvm2008 && !jvm2008s.includes(0)) {
            this.$router.push({
              name: 'jvm2008',
              "params": {baseId: env_id[0], comparsionIds: comparsionIds}
            });
          } else {
            ElMessage.error({message:'该数据中有jvm2008为空',duration: 1000});
          }
        }
      } else {
        ElMessage.error({message:'请选择数据类型',duration: 1000});
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

