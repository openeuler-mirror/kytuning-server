<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 11 16:52:35 2024 +0800
-->
<template>
  <div id="fixed-top">
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
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%" class="tableHead">
        <el-table-column prop="error_type" label="错误类型"></el-table-column>
        <el-table-column prop="user_name" label="操作人员"></el-table-column>
        <el-table-column prop="test_type" label="测试类型"></el-table-column>
        <el-table-column prop="error_description" label="错误描述"></el-table-column>
        <el-table-column prop="error_log_excerpt" label="错误日志节选"></el-table-column>
        <el-table-column prop="solution" label="解决方案"></el-table-column>
        <el-table-column label="详细日志" width="180">
          <template #default="scope">
            <el-button type="primary" @click="downLog(scope.row)">日志</el-button>
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
  </div>
  <div>
    <el-dialog :title="'新增error数据'" v-model="dialogErrorPost" width="500px">
      <el-form :model="errorData" ref="errorForm" :rules="rules">
        <el-form-item label="错误类型" prop="errType">
          <el-select v-model="errorData.errType" class="m-2" placeholder="请选择错误类型">
            <el-option v-for="item in errTypes" :key="item" :label="item" :value="item" placeholder="请输入错误类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="测试类型" prop="testType">
          <el-select v-model="errorData.testType" class="m-2" placeholder="请选择测试类型">
            <el-option v-for="item in testTypes" :key="item" :label="item" :value="item" placeholder="请选择测试类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="错误描述" prop="errorDescription">
          <el-input v-model="errorData.errorDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="日志节选" prop="errorExport">
          <el-input v-model="errorData.errorExport" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="请选择错误的测试数据" prop="errorLogPath">
          <el-button type="warning" class="button-style" plain @click="selectTestList">选择测试数据</el-button>
        </el-form-item>
        <el-form-item label="解决方案" prop="solution">
          <el-input v-model="errorData.solution" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="addSure('form')">确 定</el-button>
      </template>
    </el-dialog>

    <el-dialog :title="'修改error数据'" v-model="dialogErrorPut" width="500px">
      <el-form :model="errorData" :rules="rules" ref="errorData">
        <el-form-item label="错误类型" prop="errType">
          <el-select v-model="errorData.errType" class="m-2" placeholder="请选择错误类型">
            <el-option v-for="item in errTypes" :key="item" :label="item" :value="item" placeholder="请输入错误类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="测试类型" prop="testType">
          <el-select v-model="errorData.testType" class="m-2" placeholder="请选择测试类型">
            <el-option v-for="item in testTypes" :key="item" :label="item" :value="item" placeholder="请选择测试类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="错误描述" prop="errorDescription">
          <el-input v-model="errorData.errorDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="日志节选" prop="errorExport">
          <el-input v-model="errorData.errorExport" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="解决方案" prop="solution">
          <el-input v-model="errorData.solution" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="modifySure('form')">确 定</el-button>
      </template>
    </el-dialog>

    <el-dialog :title="'选择测试数据'" v-model="dialogTest" width="800px">
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
// import AllHeader from "@/components/common/AllHeader";
// import Menu from "@/components/common/AllMenu";
import {error_list, test_case} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'errorList',
  mixins: [utils],
  // components: {
  //   AllHeader,
  //   Menu,
  // },
  data() {
    return {
      allDatas: [],
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
        errType: [{required: true, message: '请选择错误类型', trigger: 'change'}],
        testType: [{required: true, message: '请选择测试类型', trigger: 'change'}],
        errorDescription: [{required: true, message: '请输入错误描述', trigger: 'blur'}],
        errorExport: [{required: true, message: '请输入错误日志节选', trigger: 'blur'}],
        errorLogPath: [{required: true, message: '请选中错误数据', trigger: 'blur'}],
        solution: [{required: true, message: '请输入解决方案', trigger: 'blur'}],
      },
      dialogErrorPost: false,
      dialogErrorPut: false,
      dialogTest: false,
      testData: '',
      testDatas: [],
      modifyID: 0,
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      error_list('get', {}).then((response) => {
        this.allDatas = response.data.data;
        this.total = this.allDatas.length;
      });
    },
    //查找
    search() {
      error_list('get', {
        error_type: this.errorData.errType,
        test_type: this.errorData.testType,
        error_description: this.errorData.errorDescription,
        error_log_excerpt: this.errorData.errorExport
      }).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.allDatas = response.data.data;
          this.total = this.allDatas.length;
        }
      })
    },

    //新增
    add() {
      this.dialogErrorPost = true
    },
    //新增的取消
    closeInfo() {
      // 重置表单的验证状态
      this.$refs.errorForm.resetFields();
      this.dialogErrorPost = false
      this.dialogErrorPut = false
    },
    //新增中的测试数据列表
    selectTestList() {
      this.dialogTest = true
      test_case('get', {}).then((response) => {
        this.testDatas = response.data.data;
      });
      this.dialogTest = true
    },
    //新增中的选中测试数据
    selectTestSure() {
      this.errorData.errorLogPath = this.testData.result_log_name
      this.dialogTest = false
    },
    //选择框只能单选
    handleSelection(val) {
      this.testData = val[0];
      if (val.length > 1) {
        this.$refs.testTable.clearSelection();
        this.$refs.testTable.toggleRowSelection(val.pop());
      }
    },
    //选择测试数据的取消
    closeTest() {
      this.dialogTest = false
    },

    addSure() {
      //errorForm这个是上面form表单中的ref对应的标记
      console.log(this.$refs.errorForm, 111)
      this.$refs.errorForm.validate((valid) => {
        if (valid) {
          this.dialogErrorPost = false;
          const errData = {
            error_type: this.errorData.errType,
            test_type: this.errorData.testType,
            error_description: this.errorData.errorDescription,
            error_log_excerpt: this.errorData.errorExport,
            error_log_path: this.errorData.errorLogPath,
            solution: this.errorData.solution,
          };
          error_list('post', errData).then((response) => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'});
              this.getData();
            }
          });
        } else {
          ElMessage({message: '请填写正确信息', type: 'success'})
          return false;
        }
      });
    },

    reset() {
      this.errorData = {
        errType: '',
        testType: '',
        errorDescription: '',
        errorExport: '',
        errorLogPath: '',
        solution: '',
      }
      this.getData()
    },
    //修改数据
    modify(row) {
      this.dialogErrorPut = true
      this.modifyID = row.id
      this.errorData = {
        errType: row.error_type,
        testType: row.test_type,
        errorDescription: row.error_description,
        errorExport: row.error_log_excerpt,
        solution: row.solution,
      }
    },
    //确定修改数据
    modifySure() {
      this.dialogErrorPut = false;
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
    //删除数据
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
}
;
</script>


<style scoped>
.parent-container {
  display: flex;
  justify-content: center;
  /*background-color: #f2f2f2;*/
}
</style>

