<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->

<template>
  <div id="fixed-top">
    <div class="cont">
      <el-table :data="showData" tooltip-effect="dark" border style="width: 100%" :header-cell-style="{fontSize:'15px'}" class="tableHead">
        <el-table-column prop="project_name" label="项目名称"></el-table-column>
        <el-table-column prop="user_name" label="测试人员" width="90"></el-table-column>
        <el-table-column prop="ip" label="ip" width="125"></el-table-column>
        <el-table-column prop="stream" label="stream" width="80"></el-table-column>
        <el-table-column prop="lmbench" label="lmbench" width="95"></el-table-column>
        <el-table-column prop="unixbench" label="unixbench" width="105"></el-table-column>
        <el-table-column prop="fio" label="fio" width="50"></el-table-column>
        <el-table-column prop="iozone" label="iozone" width="80"></el-table-column>
        <el-table-column prop="jvm2008" label="jvm2008" width="100"></el-table-column>
        <el-table-column prop="cpu2006" label="cpu2006" width="90"></el-table-column>
        <el-table-column prop="cpu2017" label="cpu2017" width="90"></el-table-column>
        <el-table-column prop="test_time" label="测试开始时间" width="150"></el-table-column>
        <el-table-column prop="test_result" label="运行结果"></el-table-column>
        <el-table-column label="操作" width="280">
          <template #default="scope">
            <el-button type="primary" @click="downLog(scope.row)">日志</el-button>
            <el-button type="danger" @click="stop_test(scope.row)">终止测试</el-button>
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
            :total="total">
        </el-pagination>
      </div>
    </div>
  </div>
</template>


<script scoped>
import {ElMessage} from 'element-plus';
import {test_case, stop_test} from "@/api/api";
import utils from '@/utils/utils';
import {getToken} from "@/utils/setToken";

export default {
  name: 'testList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      test_case('get', {test_type: '日常测试'}).then((response) => {
        this.allDatas = response.data.data;
        this.total = this.allDatas.length;
      });
    },
    stop_test(row) {
      if (row.test_result === '运行中') {
        if (row.user_name === getToken('chinesename')) {
          stop_test({test_id: row.id}).then((response) => {
            if (response.data.code === 200) {
              ElMessage({message: response.data.message, type: 'success'})
              this.getData()
            }
          });
        } else {
          ElMessage({message: '不可终止他人的测试任务', type: 'error'});
        }
      } else {
        ElMessage({message: '任务已完成，无需终止', type: 'warning'});
      }
    },
    del(row) {
      this.$confirm(`确认删除此行数据吗？`, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        test_case('delete', {id: row.id}).then(response => {
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

