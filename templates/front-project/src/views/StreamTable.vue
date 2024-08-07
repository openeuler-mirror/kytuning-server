<template>
  <!--  <Header/>-->
  <div style="overflow-x: auto;" v-if="tableDatas.length > 0">
    <el-table :data="displayTableData" border :span-method="objectSpanMethod" style="overflow-x: auto;"
              :show-header="false">
      <template v-for="(value, key) in tableDatas[0]" :key="key">
        <el-table-column v-if="showAllData || !keysToHide.includes(key)" :prop="key" align="center" show-tooltip-when-overflow></el-table-column>
      </template>
    </el-table>
  </div>
  <br>
  <div style="position: fixed; bottom: 0; width: 100%; display: flex;">
    <el-button :id="bt1" type="primary" icon="el-icon-download" @click="exportTableData">导出表格数据</el-button>
    <el-button type="primary" icon="el-icon-view" @click="toggleDataVisibility">
      {{ showAllData ? '隐藏数据' : '显示全部数据' }}
    </el-button>
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
      tableDatas: [],
      showAllData: false,
      keysToHide: [],
    };
  },
  created() {
    axios.get('/api/stream/?env_id=' + this.$route.params.baseId + '&comparsionIds=' + this.$route.params.comparsionIds).then((response) => {
      this.tableDatas = response.data.data
      // this.other_list = response.data.data.others
      this.numColumns = Object.keys(this.tableDatas[0]).length

      this.numColumns = Object.keys(this.tableDatas[0]).length;
      this.showAllData = true; // 默认显示全部数据
      const keysToHide = Object.keys(this.tableDatas[0]).filter(key => {
        const value = this.tableDatas[0][key];
        return value.includes('Stream#');
      });
      this.keysToHide = keysToHide
    })
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
              row[key] = `Stream#${count}`; // 将"平均值"替换为"Stream#"
              count++;
            }
          });
        });
        return modifiedTableData;
      }
    }
  },
  methods: {
    toggleDataVisibility() {
      this.showAllData = !this.showAllData;
    },
    // 导出表格数据为 CSV 格式
    exportTableData() {
      const data = [this.tableDatas];

      // 生成 CSV 格式的数据字符串
      const csvData = data
          .map(rows => {
            return rows
                .map(row => {
                  return Object.values(row).map(value => `"${value}"`).join(",");
                }).join("\n");
          }).join("\n");

      // 创建并下载 CSV 文件
      const blob = new Blob(["\uFEFF" + csvData], {type: "text/csv;charset=utf-8;"});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "stream_data.csv";
      link.click();
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
        const _col = _row > 0 ? 1 : 0; // 为0是不执行合并。 为1是从当前单元格开始，执行合并1列
        return {
          rowspan: _row,
          colspan: _col,
        };
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
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");

button {
  border: none;
  padding: 15px 30px;
  font-size: 16px;
  font-family: Arial, 微软雅黑;
  color: white;
  background: #447aa8;
  border-radius: 3px;
}
</style>
