<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <el-button type="success" @click="add" style="float: right;">新增</el-button>
    <div class="cont">
      <el-table :data="showData" :header-cell-style="{fontSize:'5px'}"
                tooltip-effect="dark" border style="width: 100%">
        <el-table-column prop="ISO_name" label="ISO名字" width="300"></el-table-column>
        <el-table-column prop="arch_name" label="架构"></el-table-column>
        <el-table-column prop="user_name" label="适配人员"></el-table-column>
        <el-table-column prop="boot_efi" label="启动项的路径"></el-table-column>
        <el-table-column prop="grub_cfg_path" label="grub文件路径"></el-table-column>
        <el-table-column prop="grub_menu_name" label="LABEL值"></el-table-column>
        <el-table-column prop="ks_file_name" label="ks文件名称"></el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <el-button type="primary" @click="modify(scope.row)">修改</el-button>
            <el-button type="danger" @click="del(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script scoped>
import {get_adapt_ISO} from "@/api/api";
import utils from '@/utils/utils';

export default {
  name: 'ISOList',
  mixins: [utils],
  data() {
    return {
      allDatas: [],
      machineData: {
        'ISO_name': '',
        'http_address': '',
        'arch_name': '',
        'user_name': '',
        'boot_efi': '',
        'grub_cfg_path': '',
        'grub_menu_name': '',
        'ks_file_name': '',
      },
      dialogAddMachine: false,
      modifyID: 0,
      dialogTitle: '新增ISO',
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      get_adapt_ISO('get', {}).then((response) => {
        this.allDatas = response.data.data
        this.total = this.allDatas.length;
        console.log(this.allDatas)
      });
    },

  }
}
;
</script>


<style scoped>
</style>

