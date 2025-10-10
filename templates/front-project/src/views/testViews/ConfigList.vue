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
              <el-table-column prop="config_name" label="配置文件名称"/>
              <el-table-column prop="message" label="描述"/>
              <el-table-column label="操作" width="90">
                <template #default="scope">
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
import {user_config} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'configList',
  mixins: [utils],
  components: {
    AllHeader,
    Menu
  },
  data() {
    return {
      configData: [],
      userConfig: {},
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
    this.getData()
  },
  methods: {
    getData(){
      user_config('get', {}).then((response) => {
      this.configData = response.data.data;
      this.total = this.configData.length;
    });
    },
    del(row) {
      this.$confirm(`确认删除此行数据吗？`, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        user_config('delete', {id: row.id}).then(response => {
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

