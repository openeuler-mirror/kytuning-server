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
            <el-table ref="configData" :data="showData" tooltip-effect="dark" border style="width: 100%"
                :key="itemKey" :header-cell-style="{fontSize:'5px'}" class="tableHead">

               <el-table-column prop="project_name" label="测试项目名称"/>
               <el-table-column prop="user_name" label="测试人员"/>
               <el-table-column prop="test_ip" label="测试机器IP"/>
               <el-table-column prop="stream_number" label="stream"/>
               <el-table-column prop="lmbench_number" label="lmbench"/>
               <el-table-column prop="unixbench_number" label="unixbench"/>
               <el-table-column prop="fio_number" label="fio"/>
               <el-table-column prop="iozone_number" label="iozone"/>
               <el-table-column prop="jvm2008_number" label="jvm2008"/>
               <el-table-column prop="cpu2006_number" label="cpu2006"/>
               <el-table-column prop="cpu2017_number" label="cpu2017"/>
               <el-table-column prop="message" label="描述"/>
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
import {down_message,user_config} from "@/api/api";

export default {
  name: 'testList',
  components: {
    AllHeader,
    Menu
  },
  data() {
    return {
      configData: [],
      numColumns: 1,
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      itemKey: 0, //更新数据后生成随机数从而刷新页面数据
    };
  },
  computed: {
    showData() {
      return this.configData.slice(
          (this.currentPage - 1) * this.pageSize,
          this.currentPage * this.pageSize
      );
    },
  },
  created() {
    this.itemKey = Math.random()
    user_config('get', {}).then((response) => {
      this.configData = response.data.data;
      this.total = this.configData.length;
      this.numColumns = Object.keys(this.configData[0]).length;
    });
  },
  methods: {
    // 分页
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    modify(row) {
      down_message({id: row.id}).then((response) => {
        console.log(response,111)
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
        console.log(row.id,111)
        user_config('delete', {id: row.id}).then(response => {
          if (response.data.code === 200) {
            ElMessage({message: response.data.message, type: 'success'})
            //更新页面数据，绑定key，每次key改变后就会刷新数据
            this.itemKey = Math.random()
            this.refreshData();
            this.dialogFormVisible = false
          }
        })
      })
    },

    //更新数据后刷新页面数据
    refreshData() {
      user_config('get', {}).then((response) => {
        this.configData = response.data.data;
        this.total = this.configData.length;
        this.numColumns = Object.keys(this.configData[0]).length;
      }).catch(error => {
        console.error(error);
      });
    },
  }
};
</script>


<style scoped>
.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
  font-size: 50px;
  color: red;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>

