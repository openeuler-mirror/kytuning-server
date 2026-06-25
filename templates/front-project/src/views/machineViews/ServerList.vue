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
      <el-table :data="showData" :header-cell-style="{fontSize:'15px'}" tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="BMC_IP" label="BMC_IP" width="135">
          <template #default="scope">
            <el-link type="info" :href="'https://' + scope.row.BMC_IP" target="_blank">{{ scope.row.BMC_IP }}</el-link>
          </template>
        </el-table-column>
        <el-table-column prop="owner" label="使用人" width="70"></el-table-column>
        <el-table-column prop="server_IP" label="server_IP" width="130"></el-table-column>
        <el-table-column prop="iso_name" label="当前ISO"  width="220"></el-table-column>
        <el-table-column prop="link_status" label="连接状态">
          <template #default="scope">
            <el-button v-if="scope.row.link_status" :type="scope.row.link_status === '在线' ? 'success' : 'danger'">
              {{ scope.row.link_status }}
            </el-button>
          </template>
        </el-table-column>
        <el-table-column prop="queue_user" label="队列"></el-table-column>
        <el-table-column prop="update_time" label="更新时间" width="165"></el-table-column>
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
  </div>
  <div>
    <el-dialog :title="'编辑'" v-model="dialogModify" width="500px">
      <el-form :model="serverData" ref="machineForm" :rules="rules">
        <el-form-item label="服务器IP" prop="server_IP">
          <el-input v-model="serverData.server_IP" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="服务器用户名" prop="server_user_name">
          <el-input v-model="serverData.server_user_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="服务器密码" prop="server_password">
          <el-input v-model="serverData.server_password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="重构ISO名称" prop="new_iso_name">
          <el-select v-model="serverData.new_iso_name" placeholder="请选择ISO">
            <el-option v-for="item in isoList" :key="item.ISO_name" :label="item.ISO_name" :value="item.ISO_name"/>
          </el-select>
        </el-form-item>
        <el-form-item label="重构系统密码" prop="new_server_password" v-if="create_new_system">
          <el-input v-model="serverData.new_server_password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="根文件系统大小" prop="root_size" v-if="create_new_system">
          <el-input v-model.number="serverData.root_size" autocomplete="off" placeholder="建议50-300，单位为G" type="number" min="0" step="1"></el-input>
        </el-form-item>
        <el-form-item label="swap路径大小" prop="swap_size" v-if="create_new_system">
          <el-input v-model.number="serverData.swap_size" autocomplete="off" placeholder="单位为G" type="number" min="0" step="0.1"></el-input>
        </el-form-item>
        <el-form-item label="是否清空系统盘" prop="root_size" v-if="create_new_system">
          <el-switch style="display: block" v-model="serverData.clear_part" inactive-color="#13ce66" active-color="#ff4949" inactive-text="不清空" active-text="清空"></el-switch>
        </el-form-item>
        <el-form-item label="选择内核" prop="root_size" v-if="get_kernel">
          <el-switch style="display: block" v-model="serverData.kernel_type" inactive-color="#13ce66" active-color="#ff4949" inactive-text="419" active-text="510"></el-switch>
        </el-form-item>
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
      serverData: {
        'server_IP': '',
        'server_user_name': '',
        'server_password': '',
        'iso_name': '',
        'new_iso_name': '',
        'new_server_password': '',
        'root_size': '',
        'swap_size': '',
        'clear_part': false,
        'kernel_type': false,
      },
      isoList: [],
      dialogModify: false,
    };
  },
  computed: {
    create_new_system() {
      return this.serverData.new_iso_name && this.serverData.new_iso_name !== 'other(手动创建)';
    },
    get_kernel() {
      return ['uos-server-20-1060a-amd64.iso', 'uos-server-20-1060a-arm64.iso', 'uos-server-20-1060e-amd64.iso', 'uos-server-20-1060e-arm64.iso', 'uniontechos-server-20-1050a-amd64.iso', 'uniontechos-server-20-1050a-arm64.iso'].includes(this.serverData.new_iso_name);
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
        this.serverData = {
          'server_IP': row.server_IP,
          'server_user_name': row.server_user_name,
          'server_password': row.server_password,
          'new_iso_name': row.new_iso_name,
          'new_server_password': row.new_server_password,
          'root_size': row.root_size,
          'swap_size': row.swap_size,
          'clear_part': row.clear_part,
          'kernel_type': row.kernel_type,
        }
      } else {
        ElMessage({message: '不可查看或修改他人机器详情', type: 'success'})
      }
    },

    //确定修改数据
    applyUseSure() {
      const serverData_ = {
        id: this.modifyID,
        server_IP: this.serverData.server_IP,
        server_user_name: this.serverData.server_user_name,
        server_password: this.serverData.server_password,
        new_iso_name: this.serverData.new_iso_name,
        new_server_password: this.serverData.new_server_password,
        root_size: this.serverData.root_size,
        swap_size: this.serverData.swap_size,
        clear_part: this.serverData.clear_part,
        kernel_type: this.serverData.kernel_type,
      }
      if (this.serverData.new_iso_name && this.serverData.new_iso_name !== "other(手动创建)") {
        if (!this.serverData.new_server_password) {
          ElMessage({message: '重构系统请输入密码', type: 'warning'})
          return
        }
        if (!this.serverData.root_size || typeof this.serverData.root_size !== 'number') {
          ElMessage({message: '请输入根路径大小并确保是number类型', type: 'warning'})
          return
        }
        if (!this.serverData.swap_size || typeof this.serverData.swap_size !== 'number') {
          ElMessage({message: '请输入swap路径大小并确保是number类型', type: 'warning'})
          return
        }
        const newData = this.isoList.find(item => item.ISO_name === this.serverData.new_iso_name)
        if (newData.arch_name === this.modifySystemArchName) {
          this.dialogModify = false;
          modify_server(serverData_).then(response => {
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
        modify_server(serverData_).then(response => {
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
      apply_use_machine({id: row.id}).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.getData()
        }
      })
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
  }
};
</script>


<style scoped>
.operate-button {
  margin-left: 0;
  margin-right: 10px;
}
.parent-container {
  display: flex;
  justify-content: center;
  /*background-color: #f2f2f2;*/
}
</style>

