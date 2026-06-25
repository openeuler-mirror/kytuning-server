<template>
  <div id="fixed-top">
    <el-button type="success" @click="add" style="float: right;">新增</el-button>
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'15px'}" tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="machine_name" label="设备名称"></el-table-column>
        <el-table-column prop="cpu_module_name" label="CPU型号"></el-table-column>
        <el-table-column prop="arch_name" label="架构"></el-table-column>
        <el-table-column prop="BMC_IP" label="BMC_IP"></el-table-column>
        <el-table-column prop="creator" label="创建人员"></el-table-column>
        <el-table-column prop="create_time" label="创建时间"></el-table-column>
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
            :page-sizes="[5, 10, 20, 30, 50, total]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total">
        </el-pagination>
      </div>
    </div>
  </div>
  <div>
    <el-dialog :title="dialogTitle" v-model="dialogAddMachine" width="500px">
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
        <el-button type="primary" @click="dialogTitle === '新增设备' ? addSure('form') : modifySure('form')">确 定
        </el-button>
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
        'BMC_user_name': '',
        'BMC_password': '',
      },
      archTypes: ['x86', 'aarch', 'mips', 'loongarch'],
      dialogAddMachine: false,
      modifyID: 0,
      dialogTitle: '',
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
      this.dialogTitle = '新增设备'
      this.reset()
      this.dialogAddMachine = true
    },
    //新增的取消
    closeInfo() {
      // 重置表单的验证状态
      this.reset()
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
          this.reset()
        } else {
          ElMessage({message: response.data.messag, type: 'warning'})
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

