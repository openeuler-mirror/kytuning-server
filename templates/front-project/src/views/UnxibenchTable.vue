<template>
  <div>
    <Header :tableDatas="tableDatas" :dataName="dataName" :showAllData="showAllData" @data-loaded="handleDataLoaded"/>
    <div style="overflow-x: auto;">
      <el-table :data="displayTableData" border :span-method="objectSpanMethod" style="overflow-x: auto;"
                :show-header="false" :row-class-name="tableRowClassName" highlight-current-row>
        <template v-for="(value, key, index) in tableDatas[0]" :key="key">
          <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key"
                           :width="index === 0 ? '100' :(index === 1 ? '360' : '')" align="center">
            <template v-slot="{ row }" >
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
import Header from "@/components/common/TableHeader.vue";
import { unixbench } from "@/api/api.js";

export default {
  components: {
    ElTable,
    ElTableColumn,
    Header
  },
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
    unixbench(this.paramsData).then((response) => {
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
  computed: {
    displayTableData() {
      if (this.showAllData) {
        return this.tableDatas;
      } else {
        let count = 1;
        const modifiedTableData = JSON.parse(JSON.stringify(this.tableDatas)); // 深拷贝原始数据
        modifiedTableData.forEach(row => {
          Object.entries(row).forEach(([key, value]) => {
            if (typeof value === 'string' && key.startsWith('column') && value.startsWith('平均值')) {
              row[key] = value + this.dataName.charAt(0).toUpperCase() + this.dataName.slice(1) + "#" + `${count}`; // 将"平均值"替换为"this.dataName#"
              count++;
            }
          });
        });
        return modifiedTableData;
      }
    }
  },
  methods: {
    handleDataLoaded(value) {
      this.showAllData = value;
      // 在这里处理子组件的数据
    },
    tableRowClassName({rowIndex}) {
        if (rowIndex === 15) {
          return 'warning-row';
        } else if (rowIndex === 28) {
          return 'success-row';
        }
        return '';
    },
    getCellClassName(row, key) {
      let value = row[key];
      if (typeof value === 'string' && value.endsWith('%')) {
        // 去除百分比符号 "%"
        value = value.replace('%', '');
         // 将百分比转换为小数
        value = parseFloat(value);
        if (value >= 5) {
          console.log(value,111)
          return 'green-cell';
        } else if (value < -5) {
          return 'red-cell';
        }
      }
      return '';
    },
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
};
</script>

<style>
/*@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");*/
/*表格大小，调整为一页显示全部*/
.el-table__body .cell {
  height: 15px;
  line-height: 15px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}

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
