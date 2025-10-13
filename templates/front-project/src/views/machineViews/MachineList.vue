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
    <el-button type="success" @click="add" style="float: right;">新增</el-button>
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%" class="tableHead">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="arch_name" label="架构"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="ip" label="IP"></el-table-column>
        <el-table-column prop="os_version" label="操作系统"></el-table-column>
        <el-table-column prop="test_user" label="当前负责人"></el-table-column>
        <el-table-column prop="use_time" label="接手时间"></el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)">重构</el-button>
            <el-button type="danger" @click="del(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
  <div>
    <el-dialog :title="'新增设备数据'" v-model="dialogAddMachine" width="500px">
      <el-form :model="machineData" ref="machineForm" :rules="rules">
        <el-form-item label="设备名称" prop="errorDescription">
          <el-input v-model="machineData.machine_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="架构" prop="arch_name">
          <el-select v-model="machineData.arch_name" class="m-2" placeholder="请选择架构类型">
            <el-option v-for="item in archTypes" :key="item" :label="item" :value="item" placeholder="请选择架构类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="CPU型号" prop="cpu_module_name">
          <el-input v-model="machineData.cpu_module_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="IP" prop="ip">
          <el-input v-model="machineData.ip" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="操作系统" prop="os_version">
          <el-input v-model="machineData.os_version" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="addSure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {machine_list} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'michineList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      machineData: {
        'machine_name': '',
        'arch_name': '',
        'cpu_module_name': '',
        'ip': '',
        'os_version': '',
      },
      archTypes: ['x86', 'arm','mips','loongarch'],
      rules: {
        errType: [{required: true, message: '请选择错误类型', trigger: 'change'}],
      },
      dialogAddMachine: false,
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
      machine_list('get', {}).then((response) => {
        this.allDatas = response.data.data;
        this.total = this.allDatas.length;
      });
    },

    //新增
    add() {
      this.dialogAddMachine = true
    },
    //新增的取消
    closeInfo() {
      // 重置表单的验证状态
      this.$refs.machineForm.resetFields();
      this.dialogAddMachine = false
    },

    addSure() {
      //machineForm这个是上面form表单中的ref对应的标记
      console.log(this.$refs.machineForm, 111)
      this.$refs.machineForm.validate((valid) => {
        if (valid) {
          this.dialogAddMachine = false;
          const machineData = {
            machine_name: this.machineData.machine_name,
            arch_name: this.machineData.arch_name,
            cpu_module_name: this.machineData.cpu_module_name,
            ip: this.machineData.ip,
            os_version: this.machineData.os_version,
          };
          console.log(machineData,1111)
          machine_list('post', machineData).then((response) => {
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
      this.machineData = {
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
      this.machineData = {
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
      const machineData = {
        id: this.modifyID,
        error_type: this.machineData.errType,
        test_type: this.machineData.testType,
        error_description: this.machineData.errorDescription,
        error_log_excerpt: this.machineData.errorExport,
        error_log_path: this.machineData.errorLogPath,
        solution: this.machineData.solution,
      }
      machine_list('put', machineData).then(response => {
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
        machine_list('delete', {id: row.id}).then(response => {
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

