<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:57:55 2024 +0800
-->
<template>
  <div>
    <div id="fixed-top">
      <TableHeader :tableDatas="tableDatas" :dataName="dataName" :showAllData="showAllData" @data-loaded="handleDataLoaded"/>
    </div>
    <div style="overflow-x: auto;">
      <el-table :data="displayTableData" border style="overflow-x: auto;"
                :show-header="false" highlight-current-row>
        <template v-for="(value, key, index) in tableDatas[0]" :key="key">
          <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key" :width="index === 0 ? '210' : ''"
                           align="center">
            <template v-slot="{ row }">
              <div :class="getCellClassName(row, key)">
                {{ row[key] }}
              </div>
            </template>
          </el-table-column>
        </template>
      </el-table>
    </div>
  </div>
</template>


<script>
import {ElTable, ElTableColumn} from 'element-plus';
import TableHeader from "@/components/common/TableHeader.vue";
import {iozone} from "@/api/api.js";
import utils from "@/utils/utils";
import '@/assets/css/global.css';

export default {
  name: 'iozoneTable',
  components: {
    ElTable,
    ElTableColumn,
    TableHeader
  },
  mixins: [utils],
  data() {
    return {
      numColumns: 1,
      tableDatas: [],
      keysToHide: [],
      showAllData: false,
      dataName: this.$route.name,
      paramsData: {
        env_id: this.$route.params.baseId,
        comparsionIds: this.$route.params.comparsionIds,
      },
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      iozone(this.paramsData).then((response) => {
        this.tableDatas = response.data.data;
        this.numColumns = Object.keys(this.tableDatas[0]).length;
        this.showAllData = false; // 默认显示平均数据
        const keysToHide = Object.keys(this.tableDatas[0]).filter(key => {
          const value = this.tableDatas[0][key];
          return value.includes(this.dataName.charAt(0).toUpperCase() + this.dataName.slice(1) + "#");
        });
        this.keysToHide = keysToHide;
      });
    },
  }
}
;
</script>

<style scoped>

#fixed-top {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
}

.el-table {
  margin-top: 68px;
}
</style>
