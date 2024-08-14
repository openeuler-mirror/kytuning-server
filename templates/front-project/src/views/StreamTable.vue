<template>
  <div>
    <Header :tableDatas="tableDatas" :dataName="dataName" :showAllData="showAllData" @data-loaded="handleDataLoaded"/>
    <div style="overflow-x: auto;">
      <el-table :data="displayTableData" border :span-method="objectSpanMethod" style="overflow-x: auto;"
                :show-header="false">
        <template v-for="(value, key, index) in tableDatas[0]" :key="key">
          <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key" :width="index < 2 ? '100' : ''"
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
import axios from 'axios';
import {ElTable, ElTableColumn} from 'element-plus';
import Header from "@/components/common/TableHeader.vue";

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
    };
  },
  created() {
    axios.get('/api/' + this.dataName + '/?env_id=' + this.$route.params.baseId + '&comparsionIds=' + this.$route.params.comparsionIds).then((response) => {
      this.tableDatas = response.data.data;
      this.numColumns = Object.keys(this.tableDatas[0]).length;
      this.showAllData = false; // 默认显示全部数据
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
              row[key] = value + this.dataName.charAt(0).toUpperCase() + this.dataName.slice(1) + "#" + `${count}`; // 将"平均值"替换为"Stream#"
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
    getCellClassName(row, key) {
      let value = row[key];
      if (typeof value === 'string' && value.endsWith('%')) {
        // 去除百分比符号 "%"
        value = value.replace('%', '');
         // 将百分比转换为小数
        value = parseFloat(value);
        if (value >= 5) {
          return 'green-cell';
        } else if (value < -5) {
          return 'red-cell';
        }
      }
      return '';
    },
    objectSpanMethod({rowIndex, columnIndex}) {
      // columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0) {
        const _row = this.displayTableData[rowIndex];
        if (_row && _row.span) {
          return {
            rowspan: _row.span.rowspan,
            colspan: _row.span.colspan,
          };
        }
      }
    },

  }
};
</script>

<style>
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
