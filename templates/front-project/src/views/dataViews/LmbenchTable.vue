<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->
<template>
  <div>
    <div id="fixed-top">
      <TableHeader :tableDatas="tableDatas" :dataName="dataName" :showAllData="showAllData" @data-loaded="handleDataLoaded"/>
    </div>
    <div style="overflow-x: auto;">
      <el-table :data="displayTableData" border :span-method="objectSpanMethod" style="overflow-x: auto;" :show-header="false" highlight-current-row>
        <template v-for="(value, key,index) in tableDatas[0]" :key="key">
          <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key" :width="index < 2 ? '130' : ''" align="center">
            <template v-slot="{ row }">
              <div :class="getCellClassName(row, key)">
                {{ row[key] }}
              </div>
            </template>
          </el-table-column>
        </template>
      </el-table>
    </div>
    <div>
      <el-card class="box-card" style="white-space: pre-line;">
        {{ analyzeData }}
      </el-card>
    </div>
  </div>
</template>

<script>
import {ElTable, ElTableColumn} from 'element-plus';
import TableHeader from "@/components/common/TableHeader.vue";
import {lmbench} from "@/api/api.js";
import utils from "@/utils/utils";
import '@/assets/css/global.css';

export default {
  name: 'lmbenchTable',
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
      analyzeData: [],
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
      lmbench(this.paramsData).then((response) => {
        if (response.data.data.datas) {
          this.tableDatas = response.data.data.datas;
          this.analyzeData = response.data.data.analyze_data;
          this.numColumns = Object.keys(this.tableDatas[0]).length;
          this.showAllData = false; // 默认显示平均数据
          const keysToHide = Object.keys(this.tableDatas[0]).filter(key => {
            const value = this.tableDatas[0][key];
            return value.includes(this.dataName.charAt(0).toUpperCase() + this.dataName.slice(1) + "#");
          });
          this.keysToHide = keysToHide;
        } else {
          this.tableDatas = [];
          this.analyzeData = '';
          this.keysToHide = '';
        }
      });
    },
  }
};
</script>

<style scoped>
.red-cell {
  color: red;
  background-color: pink;
  /* 其他样式属性 */
}

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
