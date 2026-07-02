<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Wed Aug 21 10:54:14 2024 +0800
-->
<template>
  <div id="fixed-top">
    <!-- 搜索 -->
    <el-button type="success" @click="add" style="float: right;">新增</el-button>
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'15px'}" tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="ks_name" label="ks文件名称"></el-table-column>
        <el-table-column prop="message" label="备注信息"></el-table-column>
        <!--        <el-table-column prop="ks_content" label="ks文件内容"></el-table-column>-->
        <el-table-column prop="user_name" label="管理人员"></el-table-column>
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
    <el-dialog :title="dialogTitle" v-model="dialogAddKsFile" width="1000px">
      <el-form :model="ksFileData" ref="ksFileForm" label-width="100px">
        <el-form-item label="ks文件名称" prop="http_address">
          <el-input v-model="ksFileData.ks_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="备注信息" prop="http_address">
          <el-input v-model="ksFileData.message" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="ks文件内容" prop="http_address">
          <el-input type="textarea" :rows="20" placeholder="请输入内容" v-model="ksFileData.ks_content"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="closeInfo('form')">取 消</el-button>
        <el-button type="primary" @click="dialogTitle === '新增ks文件' ? addSure('form') : modifySure('form')">确 定</el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {ksList} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'ksList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      ksFileData: {
        'ks_name': '',
        'message': '',
        'ks_content': '',
      },
      dialogAddKsFile: false,
      modifyID: 0,
      dialogTitle: '',
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      ksList('get', {}).then((response) => {
        this.allDatas = response.data.data
        this.total = this.allDatas.length;
      });
    },
    //新增
    add() {
      this.dialogTitle = '新增ks文件'
      this.reset()
      this.dialogAddKsFile = true
    },
    //新增的取消
    closeInfo() {
      // 重置表单的验证状态
      this.reset()
      this.dialogAddKsFile = false
    },
    addSure() {
      this.$refs.ksFileForm.validate((valid) => {
        if (valid) {
          this.dialogAddKsFile = false;
          const ksFileData_ = {
            ks_name: this.ksFileData.ks_name,
            message: this.ksFileData.message,
            ks_content: this.ksFileData.ks_content,
          };
          ksList('post', ksFileData_).then((response) => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'});
              this.reset()
            }
          });
        } else {
          ElMessage({message: '请填写正确信息', type: 'warning'})
          return false;
        }
      });
    },
    reset() {
      this.ksFileData = {
        ks_name: '',
        message: '',
        ks_content: '',
      }
      this.getData()
    },
    //修改数据
    modify(row) {
      this.dialogTitle = '修改ks文件按信息'
      this.dialogAddKsFile = true
      this.modifyID = row.id
      this.ksFileData = {
        ks_name: row.ks_name,
        message: row.message,
        ks_content: row.ks_content,
      }
    },
    //确定修改数据
    modifySure() {
      this.dialogAddKsFile = false;
      const ksFileData_ = {
        id: this.modifyID,
        ks_name: this.ksFileData.ks_name,
        message: this.ksFileData.message,
        ks_content: this.ksFileData.ks_content,
      };
      ksList('put', ksFileData_).then(response => {
        if (response.data.code === 200) {
          ElMessage({message: response.data.message, type: 'success'})
          this.reset()
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
        ksList('delete', {id: row.id}).then(response => {
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
