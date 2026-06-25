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
          <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key" :width="index < 4 ? '85' : ''" align="center">
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
import {cpu2017} from "@/api/api.js";
import utils from "@/utils/utils";
import '@/assets/css/global.css';

export default {
  name: 'cpu2017Table',
  components: {
    ElTable,
    ElTableColumn,
    TableHeader
  },
  mixins: [utils],
  data() {
    return {
      tableDatas: [],
      keysToHide: [],
      analyzeData: [],
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
      cpu2017(this.paramsData).then((response) => {
        if (response.data.data.datas) {
          this.tableDatas = response.data.data.datas;
          this.analyzeData = response.data.data.analyze_data;
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
    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0 || columnIndex === 1 || columnIndex === 2 || columnIndex === 3) {
        const _row = this.filterData(this.tableDatas, columnIndex).one[rowIndex];
        const _col = _row > 0 ? 1 : 0;  // 为0是不执行合并。 为1是从当前单元格开始，执行合并1列
        return {
          rowspan: _row,
          colspan: _col,
        }
      }
    },
    filterData(arr, colIndex) {
      let spanOneArr = [];
      let concatOne = 0;
      arr.forEach((item, index) => {
        if (index === 0) {
          spanOneArr.push(1);
        } else {
          //first second 分别表示表格数据第一列和第二列对应的参数字段，根据实际参数修改
          if (colIndex === 0) {
            if (item.column1 === arr[index - 1].column1) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          } else if (colIndex === 1) {
            if (item.column2 === arr[index - 1].column2) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          } else if (colIndex === 2) {
            if (item.column3 === arr[index - 1].column3) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          } else if (colIndex === 3) {
            if (item.column4 === arr[index - 1].column4) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          }
        }
      });
      return {
        one: spanOneArr,
      };
    }
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
