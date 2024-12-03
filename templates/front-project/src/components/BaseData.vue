<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->
<template>
  <!--  <div style="overflow-x: auto;">-->
  <div>
    <template v-if="isDataLoaded">
      <el-table :data="tableDatas" border style="overflow-x: auto;" :show-header="false">
        <template v-for="i in numColumns" :key="i">
          <el-table-column :prop="`column${i}`" :width="i < 2 ? '100' : ''" align="center"
                           show-tooltip-when-overflow></el-table-column>
        </template>
      </el-table>
    </template>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      tableDatas: [],
      numColumns: 0,
      isDataLoaded: false,
    }
  },
  props: {
    dataName: {
      type: String,
      required: true
    },
    baseId: {
      type: String,
      required: true
    },
    comparsionIds: {
      type: String,
      required: true
    }
  },
  created() {
    axios.get('/api/' + this.dataName + '_data' + '/?env_id=' + this.baseId + '&index=1').then((response) => {
      this.tableDatas = response.data.data
      this.numColumns = Object.keys(this.tableDatas[0]).length
      this.isDataLoaded = true;
      this.$emit('data-loaded', this.numColumns, this.tableDatas);
    })
  },
  methods: {},
};
</script>

<style>
</style>
