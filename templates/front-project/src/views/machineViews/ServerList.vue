<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <!-- 搜索 -->
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%" class="tableHead">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="owner" label="当前负责人"></el-table-column>
        <el-table-column prop="server_IP" label="server_IP"></el-table-column>
        <el-table-column prop="os_version" label="系统版本"></el-table-column>
        <el-table-column prop="link_status" label="链接状态"></el-table-column>
        <el-table-column prop="task_status" label="任务状态"></el-table-column>
        <el-table-column prop="queue_user" label="排队人员"></el-table-column>
        <el-table-column prop="update_time" label="更新时间"></el-table-column>
        <el-table-column label="操作" width="200">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)">重构</el-button>
            <el-button type="success" @click="del(scope.row)">申请使用</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {machine_list} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'serverList',
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
      dialogTitle:'新增设备',
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
          const machineData_ = {
            machine_name: this.machineData.machine_name,
            cpu_module_name: this.machineData.cpu_module_name,
            arch_name: this.machineData.arch_name,
            BMC_IP: this.machineData.BMC_IP,
            BMC_user_name: this.machineData.BMC_user_name,
            BMC_password: this.machineData.BMC_password,
          };
          machine_list('post', machineData_).then((response) => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'});
              this.getData();
              this.reset()
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
        machine_name: '',
        cpu_module_name: '',
        arch_name: '',
        BMC_IP: '',
        BMC_user_name: '',
        BMC_password: '',
      }
      this.getData()
    },

    //修改数据
    modify(row) {
      this.dialogTitle='修改设备信息'
      this.dialogAddMachine = true
      this.modifyID = row.id
      this.machineData = {
        machine_name: row.machine_name,
        cpu_module_name: row.cpu_module_name,
        arch_name: row.arch_name,
        BMC_IP: row.BMC_IP,
        BMC_user_name: row.BMC_user_name,
        BMC_password: row.BMC_password,
      }
    },
    //确定修改数据
    modifySure() {
      this.dialogAddMachine = false;
      const machineData_ = {
        id: this.modifyID,
        machine_name: this.machineData.machine_name,
        cpu_module_name: this.machineData.cpu_module_name,
        arch_name: this.machineData.arch_name,
        BMC_IP: this.machineData.BMC_IP,
        BMC_user_name: this.machineData.BMC_user_name,
        BMC_password: this.machineData.BMC_password,
      }

      machine_list('put', machineData_).then(response => {
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

