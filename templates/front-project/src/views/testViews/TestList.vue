<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <AllHeader/>
    <el-container class="content">
      <Menu/>
      <el-container>
        <el-main>
          <div class="cont">
            <el-table :data="showData" tooltip-effect="dark" border style="width: 100%" :header-cell-style="{fontSize:'5px'}" class="tableHead">
              <el-table-column prop="project_name" label="项目名称"></el-table-column>
              <el-table-column prop="user_name" label="测试人员"></el-table-column>
              <el-table-column prop="ip" label="ip" width="125"></el-table-column>
              <el-table-column prop="stream" label="stream" width="70"></el-table-column>
              <el-table-column prop="lmbench" label="lmbench" width="80"></el-table-column>
              <el-table-column prop="unixbench" label="unixbench" width="90"></el-table-column>
              <el-table-column prop="fio" label="fio" width="50"></el-table-column>
              <el-table-column prop="iozone" label="iozone" width="70"></el-table-column>
              <el-table-column prop="jvm2008" label="jvm2008" width="80"></el-table-column>
              <el-table-column prop="cpu2006" label="cpu2006" width="80"></el-table-column>
              <el-table-column prop="cpu2017" label="cpu2017" width="80"></el-table-column>
              <el-table-column prop="test_result" label="运行结果"></el-table-column>
              <el-table-column label="操作" width="180">
                <template #default="scope">
                  <el-button type="primary" @click="down(scope.row)">日志</el-button>
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
                  :total="total"
              >
              </el-pagination>
            </div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>


</template>


<script scoped>
import {ElMessage} from 'element-plus';
import AllHeader from "@/components/common/AllHeader";
import Menu from "@/components/common/AllMenu";
import {test_case, down_message} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'testList',
  components: {
    AllHeader,
    Menu
  },
  mixins: [utils],
  data() {
    return {
      tableDatas: [],
    };
  },
  computed: {
    showData() {
      return this.tableDatas.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
      );
    },
  },
  created() {
    this.getData()
  },
  methods: {
    getData(){
      test_case('get', {}).then((response) => {
      this.tableDatas = response.data.data;
      this.total = this.tableDatas.length;
    });
    },
    down(row) {
      down_message({result_log_name: row.result_log_name}).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'log.tar')
        document.body.appendChild(link)
        link.click()
      }).catch(error => {
        if (error.code === "ERR_BAD_REQUEST"){ElMessage({message: "下载失败没有找到对应日志", type: 'warning'})}
        console.log(error)
      }).finally(() => {
        // excelDisabled 将被设置为 true，然后立即被设置为 false,禁用的时间非常短，不足以被用户察觉到。
        this.excelDisabled = false;
      });
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
            //更新页面数据，绑定key，每次key改变后就会刷新数据
            this.dialogFormVisible = false
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

