<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 11 16:52:35 2024 +0800
-->
<template>
  <div>
    <Header :tableDatas="tableDatas" :dataName="dataName" @data-loaded="handleDataLoaded"/>
    <div style="overflow-x: auto;">
      <el-table :data="tableDatas" border :span-method="objectSpanMethod" style="overflow-x: auto;"
                :show-header="false">
        <template v-for="i in numColumns" :key="i">
          <!--        <el-table-column :prop="`column${i}`" align="center" :width="i === 1 ? '100px' : i === 2 ? '150px' : i === 3 ? '250px' : null"></el-table-column>-->
          <el-table-column :prop="`column${i}`" align="center"></el-table-column>
        </template>
      </el-table>
    </div>
  </div>
</template>


<script>
import {ElTable, ElTableColumn} from 'element-plus';
import {env} from "@/api/api";
import Header from "@/components/common/envHeader";

export default {
  components: {
    ElTable,
    ElTableColumn,
    Header,
  },
  data() {
    return {
      numColumns: 4,
      tableDatas: [],
      dataName: this.$route.name,
    }
  },
  created() {
    env({'env_id': this.$route.params.baseId}).then((response) => {
      this.tableDatas = response.data.data.data
    });
  },
  methods: {
    handleDataLoaded(value) {
      console.log(value,111)
      // 在这里处理子组件的数据
    },

    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0 || columnIndex === 1 ) {
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
          } else if (colIndex === 1){
            if (item['column2'] === arr[index - 1]['column2']) {
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
}
;
</script>

<style>
/*对比值的背景色*/
.green-cell {
  color:green;
  background-color: greenyellow;
  /* 其他样式属性 */
}
.red-cell {
  color:red;
  background-color: pink;
  /* 其他样式属性 */
}
</style>
