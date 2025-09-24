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
      <Menu />
      <el-container>
        <el-main>
          <div class="cont">
              <el-table
      ref="multipleTable"
      :data="compData"
      tooltip-effect="dark"
      border
      style="width: 100%"
      :key="itemKey"
      :header-cell-style="{fontSize:'5px'}"
      class="tableHead"
  >
    <el-table-column prop="project_name" label="项目名称" column-key="project_name">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.project_name }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="user_name" label="测试人员" >
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.user_name }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="ip" label="ip" width="125">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.ip }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="stream" label="stream" width="70">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.stream }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="lmbench" label="lmbench" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.lmbench }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="unixbench" label="unixbench" width="90">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.unixbench }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="fio" label="fio" width="50">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.fio }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="iozone" label="iozone" width="70">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.iozone }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="jvm2008" label="jvm2008" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.jvm2008 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="cpu2006" label="cpu2006" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2006 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="cpu2017" label="cpu2017" width="80">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.cpu2017 }}</div>
      </template>
    </el-table-column>
    <el-table-column prop="message" label="运行结果">
      <template #default="scope">
        <div @click="handleRowClick(scope.row)" style="cursor: pointer;">{{ scope.row.message }}</div>
      </template>
    </el-table-column>
    <el-table-column label="操作" width="180">
      <template #default="scope">
        <el-button type="primary" @click="edit(scope.row)">查看详细日志</el-button>
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


<script>

import AllHeader from "@/components/common/AllHeader";
import Menu from "@/components/common/AllMenu";

export default {
  components: {
    AllHeader,
    Menu
  },
  name: 'kytuningHome',
  methods: {
    projectData() {
      this.$router.push('/project')
    },
    goTest(){},
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

