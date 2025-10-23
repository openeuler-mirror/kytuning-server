<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'15px'}"
                tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="BMC_IP" label="BMC_IP"></el-table-column>
        <el-table-column prop="owner" label="当前负责人"></el-table-column>
        <el-table-column prop="server_IP" label="server_IP"></el-table-column>
        <el-table-column prop="iso_name" label="当前ISO"></el-table-column>
        <el-table-column prop="link_status" label="连接状态">
          <template #default="scope">
            <el-button v-if="scope.row.link_status" :type="scope.row.link_status === '在线' ? 'success' : 'danger'">
              {{ scope.row.link_status }}
            </el-button>
          </template>
        </el-table-column>
        <el-table-column prop="queue_user" label="排队人员"></el-table-column>
        <el-table-column prop="update_time" label="更新时间" width="145"></el-table-column>
        <el-table-column label="操作" width="300">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)" class="operate-button">编辑</el-button>
            <el-button type="danger" @click="finishedUsing(scope.row)" class="operate-button">使用完成</el-button>
            <el-button type="success" @click="updateStatus(scope.row)" class="operate-button">更新状态</el-button>
          </template>
        </el-table-column>
        <el-table-column label="申请" width="200">
          <template #default="scope">
            <el-button type="primary" @click="applyUse(scope.row)" class="operate-button">申请</el-button>
            <el-button type="danger" @click="cancelApplyUse(scope.row)" class="operate-button">取消申请</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
  <div>
    <el-dialog :title="'编辑'" v-model="dialogModify" width="500px">
      <el-form :model="machineData" ref="machineForm" :rules="rules">
        <el-form-item label="服务器IP" prop="server_IP">
          <el-input v-model="machineData.server_IP" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="服务器用户名" prop="server_user_name">
          <el-input v-model="machineData.server_user_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="服务器密码" prop="server_password">
          <el-input v-model="machineData.server_password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="重构ISO名称" prop="new_iso_name">
          <el-select v-model="machineData.new_iso_name" placeholder="请选择ISO">
            <el-option v-for="item in isoList" :key="item.ISO_name" :label="item.ISO_name" :value="item.ISO_name"/>
          </el-select>
        </el-form-item>
        <el-form-item label="重构系统密码" prop="new_server_password" v-if="showNewServerPassword">
          <el-input v-model="machineData.new_server_password" autocomplete="off"></el-input>
        </el-form-item>
        <el-button type="success" @click="addiso('form')">新增ISO</el-button>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="applyUseSure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {
  machine_list,
  apply_use_machine,
  cancel_apply_use_machine,
  modify_server,
  finished_using,
  update_status,
  adapt_ISO
} from "@/api/api";
import utils from '@/utils/utils';
import {getToken} from "@/utils/setToken";


export default {
  name: 'serverList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      modifyID: 0,
      modifySystemArchName: NaN,
      modifyISOArchName: NaN,
      machineData: {
        'server_IP': '',
        'server_user_name': '',
        'server_password': '',
        'iso_name': '',
        'new_iso_name': '',
        'new_server_password': '',
      },
      isoList: [],
      dialogModify: false,
    };
  },
  computed: {
    showNewServerPassword() {
      return this.machineData.new_iso_name && this.machineData.new_iso_name !== 'other(手动创建)';
    },
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

    //修改数据
    modify(row) {
      if (row.owner === getToken('chinesename') || getToken('chinesename') === 'root' || !row.owner) {
        adapt_ISO('get', {}).then((response) => {
          this.isoList = response.data.data
        });
        this.dialogModify = true;
        this.modifyID = row.id
        this.modifySystemArchName = row.arch_name
        this.machineData = {
          'server_IP': row.server_IP,
          'server_user_name': row.server_user_name,
          'server_password': row.server_password,
          'new_iso_name': row.new_iso_name,
          'new_server_password': row.new_server_password,
        }
      } else {
        ElMessage({message: '不可查看或修改他人机器详情', type: 'success'})
      }
    },

    //确定修改数据
    applyUseSure() {
      const machineData_ = {
        id: this.modifyID,
        server_IP: this.machineData.server_IP,
        server_user_name: this.machineData.server_user_name,
        server_password: this.machineData.server_password,
        new_iso_name: this.machineData.new_iso_name,
        new_server_password: this.machineData.new_server_password,
      }
      if (this.machineData.new_iso_name && this.machineData.new_iso_name !== "other(手动创建)") {
        if (!this.machineData.new_server_password) {
          ElMessage({message: '重构系统请输入密码', type: 'success'})
          return
        }
        const newData = this.isoList.find(item => item.ISO_name === this.machineData.new_iso_name)
        if (newData.arch_name === this.modifySystemArchName) {
          this.dialogModify = false;
          modify_server(machineData_).then(response => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              this.getData()
            }
          })
        } else {
          ElMessage({message: '你的机器架构和ISO类型不匹配', type: 'warning'})
        }

      } else {
        this.dialogModify = false;
        modify_server(machineData_).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }
        })
      }
    },
    //取消修改
    closeInfo() {
      this.dialogModify = false
    },

    //使用完成
    finishedUsing(row) {
      if (row.owner) {
        finished_using({id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          } else {
            ElMessage({message: response.data.message, type: 'success'})
          }
        })
      } else {
        ElMessage({message: '目前机器无人使用', type: 'error'})
      }
    },

    //申请使用
    applyUse(row) {
      if (row.queue_user) {
        ElMessage({message: '已存在申请人员，请稍后再试', type: 'error'})
      } else {
        apply_use_machine({id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }
        })
      }
    },

    //取消申请 1、判断取消人员和申请人是否一致（前后端同时判断，保证数据可靠性）；2、是否存在申请人员（前端判断）
    cancelApplyUse(row) {
      if (row.queue_user) {
        cancel_apply_use_machine({id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }
        })
      } else {
        ElMessage({message: '当前没有申请人员，无需取消申请', type: 'error'})
      }
    },
    updateStatus(row) {
      if (row.owner) {
        update_status({id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }
        })
      } else {
        ElMessage({message: '无人使用无需更新', type: 'success'})
      }
    },
    addiso() {
      ElMessage({message: '待开发', type: 'success'})
    }
  }
};
</script>


<style scoped>
.operate-button {
  margin-left: 0;
  margin-right: 10px;
}
</style>

