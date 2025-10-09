<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 11 16:52:35 2024 +0800
-->
<template>
  <div id="fixed-top">
    <AllHeader/>
    <el-container class="content">
      <Menu/>
      <el-container>
        <el-main>
          <!-- 搜索 -->
          <div style="display: flex; justify-content: space-between; width: 85%;padding-top: 20px;">
            <div style="display: flex; justify-content: space-between; width: 86%;margin-left: 7%;">
              <el-form-item label="错误类型：">
                <el-select v-model="errorData.errType" class="m-2" placeholder="请选择错误类型">
                  <el-option v-for="item in errTypes" :key="item" :label="item" :value="item" placeholder="请输入错误类型"/>
                </el-select>
              </el-form-item>
              <el-form-item label="测试类型：">
                <el-select v-model="errorData.testType" class="m-2" placeholder="请选择测试类型">
                  <el-option v-for="item in testTypes" :key="item" :label="item" :value="item" placeholder="请选择测试类型"/>
                </el-select>
              </el-form-item>
              <el-form-item label="错误描述：">
                <el-input v-model="errorData.errorDescription" placeholder="请输入关键词"/>
              </el-form-item>
              <el-form-item label="日志节选：">
                <el-input v-model="errorData.errorExport" placeholder="请输入关键词"/>
              </el-form-item>
            </div>
            <el-button type="primary" style=" margin-left: 20px; " @click="search">搜索</el-button>
            <el-button type="success" style=" margin-left: 50px;" @click="add">新增</el-button>
            <el-button type="warning" style=" margin-left: 50px;" @click="reset">重置</el-button>
          </div>
          <div class="cont">
            <el-table :data="showData" :key="itemKey" :header-cell-style="{fontSize:'5px'}"
                      tooltip-effect="dark" border style="width: 100%" class="tableHead">
              <el-table-column prop="error_type" label="错误类型"></el-table-column>
              <el-table-column prop="user_name" label="操作人员"></el-table-column>
              <el-table-column prop="test_type" label="测试类型"></el-table-column>
              <el-table-column prop="error_description" label="错误描述"></el-table-column>
              <el-table-column prop="error_log_excerpt" label="错误日志节选"></el-table-column>
              <el-table-column prop="solution" label="解决方案"></el-table-column>
              <el-table-column label="详细日志" width="180">
                <template #default="scope">
                  <el-button type="primary" @click="down(scope.row)">日志</el-button>
                </template>
              </el-table-column>
              <el-table-column label="操作" width="180">
                <template #default="scope">
                  <el-button type="primary" @click="modify(scope.row)">修改</el-button>
                  <el-button type="danger" @click="del(scope.row)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
            <br>
            <div class="parent-container">
              <el-pagination
                  @size-change="handleSizeChange"
                  @current-change="handleCurrentChange"
                  :current-page="currentPage"
                  :page-sizes="[5, 10, 20, 30, 50]"
                  :page-size="pageSize"
                  layout="total, sizes, prev, pager, next, jumper"
                  :total="total"
              >
              </el-pagination>
            </div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
  <div>
    <el-dialog :title="'新增error数据'" v-model="errorPostDialog" width="500px">
      <el-form :model="errorData" :rules="rules" ref="errorData">
        <el-form-item label="错误类型" :label-width="formLabelWidth" prop="errType">
          <el-select v-model="errorData.errType" class="m-2" placeholder="请选择错误类型">
            <el-option v-for="item in errTypes" :key="item" :label="item" :value="item" placeholder="请输入错误类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="测试类型" :label-width="formLabelWidth" prop="testType">
          <el-select v-model="errorData.testType" class="m-2" placeholder="请选择测试类型">
            <el-option v-for="item in testTypes" :key="item" :label="item" :value="item" placeholder="请选择测试类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="错误描述" :label-width="formLabelWidth" prop="errorDescription">
          <el-input v-model="errorData.errorDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="日志节选" :label-width="formLabelWidth" prop="errorExport">
          <el-input v-model="errorData.errorExport" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="请选择错误的测试数据" :label-width="formLabelWidth" prop="errorLogPath">
          <el-button type="warning" class="button-style" plain @click="selectTestList">选择测试数据</el-button>
        </el-form-item>
        <el-form-item label="解决方案" :label-width="formLabelWidth" prop="solution">
          <el-input v-model="errorData.solution" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="addSure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
  <div>
    <el-dialog :title="'修改error数据'" v-model="errorPutDialog" width="500px">
      <el-form :model="errorData" :rules="rules" ref="errorData">
        <el-form-item label="错误类型" :label-width="formLabelWidth" prop="errType">
          <el-select v-model="errorData.errType" class="m-2" placeholder="请选择错误类型">
            <el-option v-for="item in errTypes" :key="item" :label="item" :value="item" placeholder="请输入错误类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="测试类型" :label-width="formLabelWidth" prop="testType">
          <el-select v-model="errorData.testType" class="m-2" placeholder="请选择测试类型">
            <el-option v-for="item in testTypes" :key="item" :label="item" :value="item" placeholder="请选择测试类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="错误描述" :label-width="formLabelWidth" prop="errorDescription">
          <el-input v-model="errorData.errorDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="日志节选" :label-width="formLabelWidth" prop="errorExport">
          <el-input v-model="errorData.errorExport" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="解决方案" :label-width="formLabelWidth" prop="solution">
          <el-input v-model="errorData.solution" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="modifySure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
  <div>
    <el-dialog :title="'选择测试数据'" v-model="testDialog" width="800px">
      <el-table ref="testTable" :data="testDatas" @selection-change="handleSelection"
                tooltip-effect="dark" border height="500" style="width: 100%" class="tableHead">
        <el-table-column type="selection" width="55"/>
        <el-table-column prop="project_name" label="测试项目名称"/>
        <el-table-column prop="ip" label="测试机器ip"/>
        <el-table-column prop="test_result" label="测试运行结果"/>
        <el-table-column prop="user_name" label="测试人员"/>
      </el-table>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeTest">取 消</el-button>
          <el-button type="primary" @click="selectTestSure(scope)">确 定</el-button>
        </span>
      </template>
    </el-dialog>

  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import AllHeader from "@/components/common/AllHeader";
import Menu from "@/components/common/AllMenu";
import {down_message, error_list, test_case} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'errorList',
  mixins: [utils],
  components: {
    AllHeader,
    Menu,
  },
  data() {
    return {
      tableDatas: [],
      iterations: {},
      errTypes: ['编译类型错误', '运行类型错误'],
      testTypes: ['stream', 'lmbench', 'unixbench', 'fio', 'iozone', 'jvm2008', 'cpu2006', 'cpu2017', 'other'],
      errorData: {
        errType: '',
        testType: '',
        errorDescription: '',
        errorExport: '',
        errorLogPath: '',
        solution: '',
      },
      rules: {
        errType: [{required: true, message: '请选择错误类型'}],
        testType: [{required: true, message: '请选择测试类型'}],
        errorDescription: [{required: true, message: '请输入错误描述'}],
        errorExport: [{required: true, message: '请输入错误日志节选'}],
        solution: [{required: true, message: '请输入解决方案'}],
      },
      errorPostDialog: false,
      errorPutDialog: false,
      testDialog: false,
      testData: '',
      testDatas: [],
      modifyID: 0,
    };
  },
  computed: {
    showData() {
      return this.tableDatas.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
      );
    },
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      this.itemKey = Math.random()
      error_list('get', {}).then((response) => {
        this.tableDatas = response.data.data;
        this.total = this.tableDatas.length;
      });
    },
    search() {
      error_list('get', {
        error_type: this.errorData.errType,
        test_type: this.errorData.testType,
        error_description: this.errorData.errorDescription,
        error_log_excerpt: this.errorData.errorExport
      }).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.tableDatas = response.data.data;
          this.total = this.tableDatas.length;
        }
      })
    },
    down(row) {
      down_message({result_log_name: row.error_log_path}).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'log.tar')
        document.body.appendChild(link)
        link.click()
      }).catch(error => {
        if (error.code === "ERR_BAD_REQUEST") {
          ElMessage({message: "下载失败没有找到对应日志", type: 'warning'})
        }
      }).finally(() => {
        // excelDisabled 将被设置为 true，然后立即被设置为 false,禁用的时间非常短，不足以被用户察觉到。
        this.excelDisabled = false;
      });
    },

    reset(){
      this.errorData= {
        errType: '',
        testType: '',
        errorDescription: '',
        errorExport: '',
        errorLogPath: '',
        solution: '',
      }
      this.getData()
    },

    add() {
      this.errorPostDialog = true
    },
    closeInfo() {
      this.errorPostDialog = false
      this.errorPutDialog = false
    },
    closeTest() {
      this.testDialog = false
    },
    selectTestList() {
      this.testDialog = true
      test_case('get', {}).then((response) => {
        this.testDatas = response.data.data;
      });
      this.testDialog = true
    },
    handleSelection(val) {
      this.testData = val[0];
      if (val.length > 1) {
        this.$refs.testTable.clearSelection();
        this.$refs.testTable.toggleRowSelection(val.pop());
      }
    },
    selectTestSure() {
      this.errorData.errorLogPath = this.testData.result_log_name
      this.testDialog = false
    },
    addSure() {
      this.errorPostDialog = false;
      const errData = {
        error_type: this.errorData.errType,
        test_type: this.errorData.testType,
        error_description: this.errorData.errorDescription,
        error_log_excerpt: this.errorData.errorExport,
        error_log_path: this.errorData.errorLogPath,
        solution: this.errorData.solution,
      }
      error_list('post', errData).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.getData()
        }
      })
    },

    modify(row) {
      this.errorPutDialog = true
      this.modifyID = row.id
      this.errorData = {
        errType: row.error_type,
        testType: row.test_type,
        errorDescription: row.error_description,
        errorExport: row.error_log_excerpt,
        solution: row.solution,
      }
    },
    modifySure() {
      this.errorPutDialog = false;
      const errData = {
        id: this.modifyID,
        error_type: this.errorData.errType,
        test_type: this.errorData.testType,
        error_description: this.errorData.errorDescription,
        error_log_excerpt: this.errorData.errorExport,
        error_log_path: this.errorData.errorLogPath,
        solution: this.errorData.solution,
      }
      error_list('put', errData).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.getData()
        }
      })
    },

    del(row) {
      this.$confirm(`确认删除此行数据吗？`, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        error_list('delete', {id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }
        })
      })
    },
  }
};
</script>


<style scoped>
.parent-container {
  display: flex;
  justify-content: center;
  /*background-color: #f2f2f2;*/
}
</style>

