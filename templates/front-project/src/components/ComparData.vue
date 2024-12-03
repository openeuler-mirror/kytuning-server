<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->
<template>
  <div class="tableCompar">
    <template v-if="isDataLoaded && isComparDataLoaded[baseId]">
      <el-table :data="comparDatas" border style="overflow-x: auto;" :show-header="false">
        <template v-for="i in numColumns" :key="i">
          <el-table-column :prop="`column${i}`" :width="i < 2 ? '100' : ''" align="center" show-tooltip-when-overflow></el-table-column>
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
      comparDatas: [],
      numColumns: 0,
      isDataLoaded: false,
    }
  },
  props: {
    titleIndex: {
      type: String,
      required: true,
    },
    dataName: {
      type: String,
      required: true,
    },
    baseId: {
      type: String,
      required: true,
    },
  },
  created() {
    axios.get('/api/' + this.dataName + '_data' + '/?env_id=' + this.baseId + '&index=' + this.titleIndex)
        // axios.get('/api/' + this.dataName + '_data' + '/?env_id=' + this.baseId)
        .then((response) => {
          this.comparDatas = response.data.data
          this.numColumns = Object.keys(this.comparDatas[0]).length
          const titleIndex_ = this.titleIndex + this.numColumns - 1
          this.$emit('data-loaded', this.baseId, titleIndex_, this.comparDatas)
          this.isDataLoaded = true
        })
  },
}
</script>

<style>
</style>
