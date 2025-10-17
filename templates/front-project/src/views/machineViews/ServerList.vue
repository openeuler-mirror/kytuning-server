<template>
  <div id="fixed-top">
    <!-- 搜索 -->
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="BMC_IP" label="BMC_IP"></el-table-column>
        <el-table-column prop="owner" label="当前负责人"></el-table-column>
        <el-table-column prop="server_IP" label="server_IP"></el-table-column>
        <el-table-column prop="os_version" label="系统版本"></el-table-column>
        <el-table-column prop="link_status" label="连接状态">
          <template #default="scope">
            <el-button
                v-if="scope.row.link_status"
                :type="scope.row.link_status === '在线' ? 'success' : 'danger'"
            >
              {{ scope.row.link_status }}
            </el-button>
          </template>
        </el-table-column>
        <el-table-column prop="task_status" label="任务状态"></el-table-column>
        <el-table-column prop="queue_user" label="排队人员"></el-table-column>
        <el-table-column prop="update_time" label="更新时间"></el-table-column>
        <el-table-column label="操作" width="200">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)" class="operate-button">编辑</el-button>
            <el-button type="danger" @click="finishedUsing(scope.row)"  class="operate-button">使用完成</el-button>
            <el-button type="success" @click="applyUse(scope.row)" class="operate-button">申请</el-button>
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
        <el-form-item label="操作系统版本" prop="os_version">
          <el-input v-model="machineData.os_version" autocomplete="off"></el-input>
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
import {machine_list, apply_use_machine, cancel_apply_use_machine, modify_server, finished_using} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'serverList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      modifyID: 0,
      machineData: {
        'server_IP': '',
        'server_user_name': '',
        'server_password': '',
        'os_version': '',
      },
      dialogModify: false,
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

    //修改数据
    modify(row) {
      this.dialogModify = true;
      this.modifyID = row.id
      this.machineData = {
        'server_IP': row.server_IP,
        'server_user_name': row.server_user_name,
        'server_password': row.server_password,
        'os_version': row.os_version,
      }
    },

    //确定修改数据
    applyUseSure() {
      this.dialogModify = false;
      const machineData_ = {
        id: this.modifyID,
        server_IP: this.machineData.server_IP,
        server_user_name: this.machineData.server_user_name,
        server_password: this.machineData.server_password,
        os_version: this.machineData.os_version,
      }
      modify_server(machineData_).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.getData()
        }
      })
    },
    //取消修改
    closeInfo() {
      this.dialogModify = false
    },

    //使用完成
    finishedUsing(row){
      if (row.owner) {
        finished_using({id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            this.getData()
          }else {
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
      }else {
        ElMessage({message: '当前没有申请人员，无需取消申请', type: 'error'})
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
</style>

