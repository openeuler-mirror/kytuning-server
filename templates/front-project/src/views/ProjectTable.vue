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
      <el-button @click="mergeData()" type="danger" plain>合并数据</el-button>
      <el-button @click="restData()" type="info" plain>取消选择</el-button>
      <el-button @click="goHome" type="warning" plain>返回首页</el-button>
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
      <option value="jvm2008">jvm2008</option>
      <option value="cpu2006">cpu2006</option>
      <option value="cpu2017">cpu2017</option>
    </select>

  </div>
  <br>

  <el-table
      ref="multipleTable"
      :data="showData"
      tooltip-effect="dark"
      border
      style="width: 100%"
      :key="itemKey"
      :header-cell-style="{fontSize:'5px'}"
      class="tableHead"
  >
    <el-table-column label="基准数据" width="50">
      <template #default="{ row }">
        <el-checkbox v-model="base[row.env_id]" :label="row" :key="row.id" @change="handleBaseDataChange(row)">{{}}
        </el-checkbox>
      </template>
    </el-table-column>
    <el-table-column label="对比数据" width="50">
      <template #default="{ row }">
        <el-checkbox v-model="compar[row.env_id]" :label="row" :key="row.id" @change="handleComparativeDataChange(row)">
          {{}}
        </el-checkbox>
      </template>
    </el-table-column>
    <el-table-column prop="project_name" label="项目名称" column-key="project_name"
                     :filters=projectNames :filter-method="filterHandler" filter-placement="bottom-end">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.project_name }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="user_name" label="上传人员" :filters=userNames
                     :filter-method="filterHandler" filter-placement="bottom-end">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.user_name }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="os_version" label="系统版本" width="210"
                     :filters=osNames
                     :filter-method="filterHandler" filter-placement="bottom-end">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.os_version }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="cpu_module_name" label="cpu型号" width="190"
                     :filters=cpuNames
                     :filter-method="filterHandler" filter-placement="bottom-end">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu_module_name }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="times" label="第几次" width="70">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.times }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="ip" label="ip" width="125">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.ip }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="stream" label="stream" width="70">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.stream }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="lmbench" label="lmbench" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.lmbench }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="unixbench" label="unixbench" width="90">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.unixbench }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="fio" label="fio" width="40">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.fio }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="iozone" label="iozone" width="70">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.iozone }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="jvm2008" label="jvm2008" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.jvm2008 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="cpu2006" label="cpu2006" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2006 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="cpu2017" label="cpu2017" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2017 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="test_time" sortable label="录入时间" width="100">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.test_time }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="message" label="描述">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.message }}</div>
      </template>
    </el-table-column>
    <el-table-column label="操作" width="180">
      <template #default="scope">
        <el-button type="primary" @click="edit(scope.row)">修改</el-button>
        <el-button type="danger" @click="del(scope.row)">删除</el-button>
  </template>
    </el-table-column>
  </el-table>
  <br>
  <el-dialog :title="'修改project信息'" v-model="dialogFormVisible" width="500px">
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
import {project, getFilterName, mergeData, get_project} from "@/api/api.js";

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
    get_project({baseId: '',comparsionIds: ''}).then((response) => {
      this.allProjectDatas = response.data.data
      this.total = this.allProjectDatas.length;
    });
    getFilterName().then((response) => {
      this.projectNames = response.data.data.projectNames
      this.userNames = response.data.data.userNames
      this.osNames = response.data.data.osNames
      this.cpuNames = response.data.data.cpuNames
    });
  },

  computed: {
    showData() {
      return this.allProjectDatas.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
      );
    },
  },
  methods: {
    goHome(){this.$nextTick(() => {this.$router.push('/test')})},
    handleRowClick(row) {
      // const id = row.id
      const env_id = row.env_id
      const stream = row.stream
      const lmbench = row.lmbench
      const unixbench = row.unixbench
      const fio = row.fio
      const iozone = row.iozone
      const jvm2008 = row.jvm2008
      const cpu2006 = row.cpu2006
      const cpu2017 = row.cpu2017
      if (stream){
        this.selectedType = 'stream'
      }else if(lmbench){
        this.selectedType = 'lmbench'
      }else if(unixbench){
        this.selectedType = 'unixbench'
      }else if(fio){
        this.selectedType = 'fio'
      }else if(iozone){
        this.selectedType = 'iozone'
      }else if(jvm2008){
        this.selectedType = 'jvm2008'
      }else if(cpu2006){
        this.selectedType = 'cpu2006'
      }else if(cpu2017){
        this.selectedType = 'cpu2017'
      }
      this.base[env_id] = true;
      this.ShowSingleData()

    },
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
      this.$confirm(`确认删除此行数据吗？`, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        project('delete', {id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            //更新页面数据，绑定key，每次key改变后就会刷新数据
            this.itemKey = Math.random()
            this.refreshData();
            this.dialogFormVisible = false
          }
        })
      })
    },

    //更新数据后刷新页面数据
    refreshData() {
      // 调用 getProjects() 方法重新获取数据
      get_project({baseId: '',comparsionIds: ''}).then((response) => {
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
      this.itemKey = Math.random()
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
      const env_id = Object.keys(this.base).map(key => parseInt(key));
      if (env_id.length !== 1) {
        ElMessage.error({message: '请选择一条数据作为基准数据', duration: 1000});
        return
      }
      const baseData = this.allProjectDatas.find(item => item.env_id === env_id[0])
      if (this.selectedType !== "env") {
        if (this.selectedType === 'stream') {
          if (baseData.stream) {
            this.selectedType = 'stream'
          } else if (baseData.lmbench) {
            this.selectedType = 'lmbench'
          } else if (baseData.unixbench) {
            this.selectedType = 'unixbench'
          } else if (baseData.fio) {
            this.selectedType = 'fio'
          } else if (baseData.iozone) {
            this.selectedType = 'iozone'
          } else if (baseData.jvm2008) {
            this.selectedType = 'jvm2008'
          } else if (baseData.cpu2006) {
            this.selectedType = 'cpu2006'
          } else if (baseData.cpu2017) {
            this.selectedType = 'cpu2017'
          }
        }
      }
      this.$router.push({name: this.selectedType, "params": {baseId: env_id[0], comparsionIds: ''}});
    },
    getComparativeData() {
      const env_id = Object.keys(this.base).map(key => parseInt(key));
      const baseData = this.allProjectDatas.find(item => env_id.includes(item.env_id))
      const env_ids = Object.keys(this.compar).map(key => parseInt(key));
      const comparsionIds = env_ids.join(',')
      if (env_id.length !== 1 || env_ids.length === 0) {
        ElMessage.error({message: '请选择一条基准数据和至少一条对比数据', duration: 1000});
        return;
      }
      //判断base数据中的第一个有值的数据
      if (this.selectedType !== "env") {
        if (this.selectedType === 'stream') {
          if (baseData.stream) {
            this.selectedType = 'stream'
          } else if (baseData.lmbench) {
            this.selectedType = 'lmbench'
          } else if (baseData.unixbench) {
            this.selectedType = 'unixbench'
          } else if (baseData.fio) {
            this.selectedType = 'fio'
          } else if (baseData.iozone) {
            this.selectedType = 'iozone'
          } else if (baseData.jvm2008) {
            this.selectedType = 'jvm2008'
          } else if (baseData.cpu2006) {
            this.selectedType = 'cpu2006'
          } else if (baseData.cpu2017) {
            this.selectedType = 'cpu2017'
          }
        }
      }
      this.$router.push({name: this.selectedType, "params": {baseId: env_id[0], comparsionIds: comparsionIds}});
    },
    mergeData(){
      const env_id = Object.keys(this.base).map(key => parseInt(key));
      const env_ids = Object.keys(this.compar).map(key => parseInt(key));
      if (env_id.length !== 1 || env_ids.length === 0) {
        ElMessage.error({message: '请选择一条基准数据和至少一条对比数据(合并)', duration: 1000});
        return;
      }
      mergeData({env_id: env_id, env_ids: env_ids}).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          //更新页面数据，绑定key，每次key改变后就会刷新数据
          this.itemKey = Math.random()
          this.refreshData();
          this.dialogFormVisible = false
          this.restData()
        }
      })
    }
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
.tableHead {
  /*font-size: 15px;*/
  /*color: red;*/
}
</style>

