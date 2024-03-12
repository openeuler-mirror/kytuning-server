<template>
  <div style="overflow-x: auto;">
    <el-table :data="other_list" border :span-method="titleObjectSpanMethod" style="overflow-y: auto;"
              :show-header="false">
      <template v-for="i in numColumns" :key="i">
        <el-table-column :prop="`column${i}`" align="center"></el-table-column>
      </template>
    </el-table>
  </div>
  <div style="overflow-x: auto;">
    <el-table :data="tableDatas" border :span-method="objectSpanMethod" style="overflow-x: auto;" :show-header="false">
      <template v-for="i in numColumns" :key="i">
        <el-table-column :prop="`column${i}`" align="center"></el-table-column>
      </template>
    </el-table>
  </div>
</template>


<script>
import axios from 'axios'
import {ElTable, ElTableColumn} from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
  },
  data() {
    return {
      numColumns: 1,
      other_list: [],
      tableDatas: []
    }
  },
  created() {
    axios.get('/api/unixbench/?env_id=' + this.$route.params.baseId + '&comparativeIds=' + this.$route.params.comparativeIds).then((response) => {
      console.log(response.data.data, 11111)
      this.tableDatas = response.data.data.data
      this.other_list = response.data.data.others
      this.numColumns = Object.keys(response.data.data.others[0]).length
    })
  },
  methods: {
    titleObjectSpanMethod({columnIndex }) {
        if (columnIndex === 0) {
            return [1, 2];
          } else if (columnIndex === 1) {
            return [0, 0];
          }
      },
    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0) {
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
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
