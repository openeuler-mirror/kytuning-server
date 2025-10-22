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
    <el-button type="success" @click="add" style="float: right;">新增</el-button>
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="ISO_name" label="ISO名称" width="300"></el-table-column>
        <el-table-column prop="arch_name" label="架构"></el-table-column>
        <el-table-column prop="user_name" label="适配人员"></el-table-column>
        <el-table-column prop="boot_efi" label="启动项的路径"></el-table-column>
        <el-table-column prop="grub_cfg_path" label="grub文件路径"></el-table-column>
        <el-table-column prop="grub_menu_name" label="LABEL值"></el-table-column>
        <el-table-column prop="ks_file_name" label="ks文件名称"></el-table-column>
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
    <el-dialog :title="dialogTitle" v-model="dialogAddMachine" width="500px">
      <el-form :model="machineData" ref="machineForm" :rules="rules">
        <el-form-item label="ISO下载地址" prop="http_address">
          <el-input v-model="machineData.http_address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="架构" prop="arch_name">
          <el-select v-model="machineData.arch_name" class="m-2" placeholder="请选择架构类型">
            <el-option v-for="item in archTypes" :key="item" :label="item" :value="item" placeholder="请选择架构类型"/>
          </el-select>
        </el-form-item>
        <el-form-item label="启动项的路径" prop="boot_efi">
          <el-input v-model="machineData.boot_efi" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="grub.cfg文件路径" prop="grub_cfg_path">
          <el-input v-model="machineData.grub_cfg_path" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="LABEL值" prop="grub_menu_name">
          <el-input v-model="machineData.grub_menu_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="ks文件名称" prop="ks_file_name">
          <el-input v-model="machineData.ks_file_name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="dialogTitle === '新增ISO' ? addSure('form') : modifySure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {adapt_ISO} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'michineList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      machineData: {
        'ISO_name': '',
        'http_address': '',
        'arch_name': '',
        'user_name': '',
        'boot_efi': '',
        'grub_cfg_path': '',
        'grub_menu_name': '',
        'ks_file_name': '',
      },
      archTypes: ['x86', 'aarch', 'mips', 'loongarch'],
      dialogAddMachine: false,
      modifyID: 0,
      dialogTitle: '新增ISO',
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      adapt_ISO('get', {}).then((response) => {
        this.allDatas = response.data.data
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
      this.$refs.machineForm.validate((valid) => {
        if (valid) {
          this.dialogAddMachine = false;
          const machineData_ = {
            http_address: this.machineData.http_address,
            arch_name: this.machineData.arch_name,
            boot_efi: this.machineData.boot_efi,
            grub_cfg_path: this.machineData.grub_cfg_path,
            grub_menu_name: this.machineData.grub_menu_name,
            ks_file_name: this.machineData.ks_file_name,
          };
          adapt_ISO('post', machineData_).then((response) => {
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
      this.dialogTitle = '修改设备信息'
      this.dialogAddMachine = true
      this.modifyID = row.id
      this.machineData = {
        http_address: row.http_address,
        arch_name: row.arch_name,
        boot_efi: row.boot_efi,
        grub_cfg_path: row.grub_cfg_path,
        grub_menu_name: row.grub_menu_name,
        ks_file_name: row.ks_file_name
      }
    },
    //确定修改数据
    modifySure() {
      this.dialogAddMachine = false;
      const machineData_ = {
            id: this.modifyID,
            http_address: this.machineData.http_address,
            arch_name: this.machineData.arch_name,
            boot_efi: this.machineData.boot_efi,
            grub_cfg_path: this.machineData.grub_cfg_path,
            grub_menu_name: this.machineData.grub_menu_name,
            ks_file_name: this.machineData.ks_file_name,
          };
      adapt_ISO('put', machineData_).then(response => {
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
        adapt_ISO('delete', {id: row.id}).then(response => {
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
</style>
