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
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="arch_name" label="架构"></el-table-column>
        <el-table-column prop="BMC_IP" label="BMC_IP"></el-table-column>
        <el-table-column prop="BMC_user_name" label="BMC_user_name"></el-table-column>
        <el-table-column prop="BMC_password" label="BMC_password"></el-table-column>
        <el-table-column prop="create_time" label="创建时间"></el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)">修改</el-button>
            <el-button type="danger" @click="del(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
  <div>
    <el-dialog :title="'新增设备数据'" v-model="dialogAddMachine" width="500px">
      <el-form :model="machineData" ref="machineForm" :rules="rules">
        <el-form-item label="设备名称" prop="machine_name">
          <el-input v-model="machineData.machine_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="CPU型号" prop="cpu_module_name">
          <el-input v-model="machineData.cpu_module_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="架构" prop="arch_name">
          <el-select v-model="machineData.arch_name" class="m-2" placeholder="请选择架构类型">
            <el-option v-for="item in archTypes" :key="item" :label="item" :value="item" placeholder="请选择架构类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="BMC_IP" prop="BMC_IP">
          <el-input v-model="machineData.BMC_IP" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="BMC_user_name" prop="BMC_user_name">
          <el-input v-model="machineData.BMC_user_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="BMC_password" prop="BMC_password">
          <el-input v-model="machineData.BMC_password" autocomplete="off"></el-input>
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
        'cpu_module_name': '',
        'arch_name': '',
        'BMC_IP': '',
        'BMC_user_name':'',
        'BMC_password':'',
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
      this.$refs.machineForm.validate((valid) => {
        if (valid) {
          this.dialogAddMachine = false;
          const machineData = {
            machine_name: this.machineData.machine_name,
            cpu_module_name: this.machineData.cpu_module_name,
            arch_name: this.machineData.arch_name,
            BMC_IP: this.machineData.BMC_IP,
            BMC_user_name: this.machineData.BMC_user_name,
            BMC_password: this.machineData.BMC_password,
          };
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

