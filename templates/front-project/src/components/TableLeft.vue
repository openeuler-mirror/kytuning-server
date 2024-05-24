<template>
<!--  <div style="overflow-x: auto;">-->
  <div>
    <template v-if="isDataLoaded">
      <el-table :data="tableTitle" border :span-method="objectSpanMethod" style="overflow-x: auto;" :show-header="false">
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
      tableTitle: [],
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
  },
  created() {
    axios.get('/api/' + this.dataName + '_title/').then((response) => {
      this.tableTitle = response.data.data
      this.numColumns = Object.keys(this.tableTitle[0]).length
      this.isDataLoaded = true;
      this.$emit('data-loaded', this.tableTitle);
    })
  },
  methods: {
    titleObjectSpanMethod({columnIndex}) {
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
        const _row = this.filterData(this.tableTitle, columnIndex).one[rowIndex];
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
    },
  },
};
</script>

<style>
.header {
  background-color: #f0f0f0;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}
</style>
