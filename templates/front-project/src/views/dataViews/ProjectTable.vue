<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div>
    <div class="floating-buttons">
      <div style="display: flex; justify-content: space-between; width: 85%;">
        <div style="display: flex; justify-content: space-between; width: 86%;margin-left: 7%;">
          <el-form-item label="项目名称：">
            <el-select v-model="user_filter.project_name" class="m-2" placeholder="请选择项目名称" filterable allow-create clearable>
              <el-option v-for="item in filter.project_name" :key="item" :label="item" :value="item" placeholder="请输入项目名称"/>
            </el-select>
          </el-form-item>
          <el-form-item label="上传人员：">
            <el-select v-model="user_filter.user_name" class="m-2" placeholder="请选择上传人员">
              <el-option v-for="item in filter.user_name" :key="item" :label="item" :value="item" placeholder="请选择上传人员"/>
            </el-select>
          </el-form-item>
          <el-form-item label="系统版本：">
            <el-select v-model="user_filter.os_names" class="m-2" placeholder="请选择系统版本" filterable allow-create clearable>
              <el-option v-for="item in filter.os_names" :key="item" :label="item" :value="item" placeholder="请选择系统版本"/>
            </el-select>
          </el-form-item>
          <el-form-item label="cpu型号：">
            <el-select v-model="user_filter.cpu_names" class="m-2" placeholder="请选择cpu型号" filterable allow-create clearable>
              <el-option v-for="item in filter.cpu_names" :key="item" :label="item" :value="item" placeholder="请选择cpu型号"/>
            </el-select>
          </el-form-item>
        </div>
        <el-button type="primary" style="margin-left: 20px; " @click="search">搜索</el-button>
        <el-button type="warning" style="margin-left: 50px;" @click="filterReset">重置</el-button>
      </div>
      <div id="tatle-div">
        <el-row class="mb-4">
          <el-button @click="getComparativeData()" type="primary" plain>数据对比</el-button>
          <el-button @click="mergeData()" type="danger" plain>合并数据</el-button>
          <el-button @click="searchComparData()" type="success">修改对比数据</el-button>
        </el-row>
      </div>
    </div>
    <br>
    <el-table :data="showData" tooltip-effect="dark" border style="width: 100%" class="tableHead" :header-cell-style="{fontSize:'15px'}">
      <el-table-column fixed="left" prop="id" label="ID" width="65">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.env_id }}</div>
        </template>
      </el-table-column>
      <el-table-column fixed="left" prop="project_name" label="项目名称" column-key="project_name" width="150"
                       :filters=projectNames :filter-method="filterHandler" filter-placement="bottom-end">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.project_name }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="project_message" label="描述" width="145">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.project_message }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="user_name" label="上传人员" :filters=userNames :filter-method="filterHandler" width="80" filter-placement="bottom-end">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.user_name }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="os_version" label="系统版本" width="245" :filters=osNames :filter-method="filterHandler" filter-placement="bottom-end">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.os_version }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="cpu_module_name" label="cpu型号" width="195" :filters=cpuNames :filter-method="filterHandler" filter-placement="bottom-end">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu_module_name }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="ip" label="ip" width="130">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.ip }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="stream" label="stream" width="80">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.stream }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="lmbench" label="lmbench" width="95">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.lmbench }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="unixbench" label="unixbench" width="105">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.unixbench }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="fio" label="fio" width="50">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.fio }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="iozone" label="iozone" width="80">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.iozone }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="jvm2008" label="jvm2008" width="100">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.jvm2008 }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="cpu2006" label="cpu2006" width="90">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2006 }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="cpu2017" label="cpu2017" width="90">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2017 }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="project_data" label="是否入库" width="90">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.project_data }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="test_time" sortable label="录入时间" width="110">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.test_time }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="error_message" label="存储错误描述">
        <template #default="scope">
          <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.error_message }}</div>
        </template>
      </el-table-column>
      <el-table-column label="操作" fixed="right" :width="getActionColumnWidth">
        <template #default="scope">
          <el-button v-if="$route.path === '/tempData'" type="success" @click="addProject(scope.row)"
                     class="operate-button">入库
          </el-button>
          <el-button type="primary" @click="addCompar(scope.row)" class="operate-button">选择</el-button>
          <el-button type="warning" @click="edit(scope.row)" class="operate-button">修改</el-button>
          <el-button type="danger" @click="del(scope.row)" class="operate-button">删除</el-button>
        </template>
      </el-table-column>
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
          :total="total">
      </el-pagination>
    </div>
  </div>
  <div>
    <el-dialog :title="'修改project信息'" v-model="dialogPutProject" width="500px">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="项目名称" width="80px" prop="project_name">
          <el-input v-model="form.project_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="project_message" width="80px" prop="project_message">
          <el-input v-model="form.project_message" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeInfo('form')">取 消</el-button>
          <el-button type="primary" @click="sure('form')">确 定</el-button>
        </span>
      </template>
    </el-dialog>
    <el-drawer v-model="boolCompar" :show-close="false">
      <template #header="{  titleId, titleClass }">
        <h4 :id="titleId" :class="titleClass">数据对比</h4>
        <el-button type="danger" @click="reset">重置</el-button>
      </template>
      <el-table :data="compars" tooltip-effect="dark" border height="500" style="width: 100%" class="tableHead">
        <el-table-column label="ID" prop="env_id"/>
        <el-table-column label="项目名称" prop="project_name" show-overflow-tooltip/>
        <!--        </el-table-column>-->
        <el-table-column label="描述" prop="project_message"/>
        <el-table-column label="操作">
          <template #default="scope">
            <el-button type="danger" @click="delCompar(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-drawer>
  </div>
</template>

<script>
import {ElMessage} from 'element-plus';
import {project, getFilterName, mergeData} from "@/api/api.js";
import utils from '@/utils/utils';
import {getToken, removeToken, setToken} from '@/utils/setToken.js'

export default {
  name: 'ProjectTable',
  mixins: [utils],
  data() {
    return {
      boolCompar: false,
      allDatas: [], // 从后端获取的全部数据
      compars: [],
      projectNames: [],//筛选项目名称
      userNames: [],//筛选用户名称
      osNames: [],//筛选os版本
      cpuNames: [],//筛选cpu型号
      dialogPutProject: false,
      //用户修改后的数据
      form: {
        id: 0,
        project_name: "",
        project_message: "",
      },
      rules: {
        project_name: [{required: true, message: '请输入项目名称'}],
      },
      //搜索栏展示的数据
      filter: {
        project_name: "",
        user_name: "",
        os_names: "",
        cpu_names: "",
      },
      //用户输入的数据
      user_filter: {
        ProjectWeb: false,
        project_name: "",
        user_name: "",
        os_names: "",
        cpu_names: "",
      },
    }
  },
  watch: {
    $route(to) {
      // 路由变化时执行的逻辑
      if (to.path === '/projectData' || to.path === '/tempData') {
        // 执行重新获取数据的操作
        this.getData()
      }
    }
  },
  created() {
    this.getData()
  },
  computed: {
    getActionColumnWidth() {
      // 根据当前路由路径动态设置操作列的宽度
      return this.$route.path === '/projectData' ? '240px' : '190px';
    },
  },
  methods: {
    //获取页面数据
    getData() {
      const session_filter = JSON.parse(getToken('filter', this.user_filter))
      let requestData;
      if (session_filter) {
        requestData = {
          baseId: '',
          comparsionIds: '',
          ProjectWeb: this.$route.path === '/projectData',
          project_name: session_filter.project_name,
          user_name: session_filter.user_name,
          os_names: session_filter.os_names,
          cpu_names: session_filter.cpu_names,
        };
        // 还原搜索栏信息
        this.user_filter.project_name = session_filter.project_name
        this.user_filter.user_name = session_filter.user_name
        this.user_filter.os_names = session_filter.os_names
        this.user_filter.cpu_names = session_filter.cpu_names
      } else {
        requestData = {
          baseId: '',
          comparsionIds: '',
          ProjectWeb: this.$route.path === '/projectData',
        };
      }
      project('get', requestData).then((response) => {
        this.allDatas = response.data.data
        this.total = this.allDatas.length;
      });
      getFilterName().then((response) => {
        this.projectNames = response.data.data.projectNames
        this.userNames = response.data.data.userNames
        this.osNames = response.data.data.osNames
        this.cpuNames = response.data.data.cpuNames
        this.filter.project_name = response.data.data.project_name
        this.filter.user_name = response.data.data.user_name
        this.filter.os_names = response.data.data.os_names
        this.filter.cpu_names = response.data.data.cpu_names
      });
    },
    search() {
      this.user_filter.ProjectWeb = this.$route.path === '/projectData'
      project('get', this.user_filter).then((response) => {
        this.allDatas = response.data.data
        this.total = this.allDatas.length;
      });
    },
    filterReset() {
      this.user_filter = {
        ProjectWeb: "",
        project_name: "",
        user_name: "",
        os_names: "",
        cpu_names: "",
      }
      removeToken('filter');
      this.getData()
    },
    //数据对比
    getComparativeData() {
      if (this.compars.length === 0) {
        ElMessage({message: '请选择一条基准数据和至少一条对比数据', type: 'warning'});
        return;
      }
      const List1 = [this.compars[0].stream, this.compars[0].lmbench, this.compars[0].unixbench, this.compars[0].fio, this.compars[0].iozone, this.compars[0].jvm2008, this.compars[0].cpu2006, this.compars[0].cpu2017]
      const List2 = ['stream', 'lmbench', 'unixbench', 'fio', 'iozone', 'jvm2008', 'cpu2006', 'cpu2017']
      const firstNonZeroIndex = List1.findIndex(num => num !== 0);
      const selectedType = List2[firstNonZeroIndex]
      const comparsionIds = Object.values(this.compars).map(item => item.env_id);
      setToken('filter', JSON.stringify(this.user_filter))
      this.$router.push({
        name: selectedType,
        "params": {baseId: comparsionIds[0], comparsionIds: comparsionIds.slice(1).join(', ')}
      });
    },
    //查看对比数据
    searchComparData() {
      this.boolCompar = true
    },
    //删除对比数据
    delCompar(row) {
      this.compars = this.compars.filter(item => item.id !== row.id);
    },
    //重置对比数据
    reset() {
      this.compars = []
    },
    //合并数据
    mergeData() {
      if (this.compars.length < 2) {
        ElMessage({message: '至少选择两条数据进行合并', type: 'warning'});
        return;
      }
      const env_ids = Object.values(this.compars).map(item => item.env_id);
      mergeData({env_id: env_ids[0], env_ids: env_ids.slice(1)}).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.getData()
          this.dialogPutProject = false
          //清空合并列表数据
          this.compars = []
        }
      })
    },
    //入库
    addProject(row) {
      this.form = {...row}
      this.form.project_data = true
      project('put', this.form).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          //更新页面数据，绑定key，每次key改变后就会刷新数据
          this.dialogPutProject = false
          this.getData()
        }
      });
    },
    //增加对比数据
    addCompar(row) {
      const compar_num = this.compars.filter(item => item && typeof item === 'object' && !Array.isArray(item)).length;
      if (compar_num < 10) {
        this.compars.push(row);
      } else {
        ElMessage({message: '对比数据不可以超过10个', type: 'warning'});
      }
    },
    //修改project数据
    edit(row) {
      this.form = {...row}
      this.dialogPutProject = true
    },
    //确定修改
    sure(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          project('put', this.form).then(response => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              this.dialogPutProject = false
              this.getData()
            }
          });
        }
      })
    },
    //取消修改
    closeInfo() {
      this.dialogPutProject = false
    },
    //删除
    del(row) {
      if (!row.project_data) {
        this.$confirm(`确认删除此行数据吗？`, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          project('delete', {id: row.id}).then(response => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              this.dialogPutProject = false
              this.getData()
            }
          })
        })
      } else {
        ElMessage({message: '不可以在临时数据表中删除已入库的数据', type: 'warning'});
      }
    },
    //查询
    filterHandler(value, row, column) {
      const property = column['property'];
      return row[property] === value;
    },
    //选择框只能单选
    handleSelection(val) {
      this.testData = val[0];
      if (val.length > 1) {
        this.$refs.testTable.clearSelection();
        this.$refs.testTable.toggleRowSelection(val.pop());
      }
    },
    //数据页面时点击后跳转至对应数据详情页面
    handleRowClick(row) {
      const List1 = [row.stream, row.lmbench, row.unixbench, row.fio, row.iozone, row.jvm2008, row.cpu2006, row.cpu2017]
      const List2 = ['stream', 'lmbench', 'unixbench', 'fio', 'iozone', 'jvm2008', 'cpu2006', 'cpu2017']
      const firstNonZeroIndex = List1.findIndex(num => num !== 0);
      this.selectedType = List2[firstNonZeroIndex]
      setToken('filter', JSON.stringify(this.user_filter))
      this.$router.push({
        name: this.selectedType,
        "params": {baseId: row.env_id, comparsionIds: ''}
      });
    },
  }
}
</script>

<style scoped>
.floating-buttons {
  position: sticky;
  top: 0;
  background-color: #fff; /* Set your desired background color */
  z-index: 10;
}


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

.operate-button {
  margin-left: 0;
  margin-right: 10px;
}

</style>

