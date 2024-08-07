<template>
  <!--  <Header/>-->
  <div style="overflow-x: auto;" v-if="tableDatas.length > 0">
    <el-table :data="filteredTableData" border :span-method="objectSpanMethod" style="overflow-x: auto;" :show-header="false">
      <template v-for="i in numColumns" :key="i">
        <el-table-column v-if="showAllData || i < 3" :prop="`column${i}`" :width="i < 2 ? '100' : ''" align="center" show-tooltip-when-overflow></el-table-column>
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
import { ElTable, ElTableColumn } from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
  },
  data() {
    return {
      numColumns: 1,
      other_list: [],
      tableDatas: [
        {'column1': 'Stream', 'column2': '', 'column3': 'Stream#1',
          'column4': '平均值(基准数据)',
          'column5': 'Stream#3',
          'column6': '平均数据',
          'column7': '对比值'
        },
        {'column1': '执行命令', 'column2': '', 'column3': 'xx', 'column4': 'xx', 'column5': 'xx', 'column6': 'xx', 'column7': ''},
        {'column1': '修改参数：', 'column2': '', 'column3': '参数', 'column4': '参数', 'column5': '参数', 'column6': '参数', 'column7': ''},
        {
          'column1': '单线程',
          'column2': 'Array size',
          'column3': 80000000,
          'column4': 80000000,
          'column5': 80000000,
          'column6': 80000000,
          'column7': '-99.00%'
        },
        {
          'column1': '单线程',
          'column2': 'Copy',
          'column3': 12326.7845,
          'column4': 12326.7845,
          'column5': 12326.7845,
          'column6': 12326.7845,
          'column7': '-99.00%'
        },
        {
          'column1': '单线程',
          'column2': 'Scale',
          'column3': 11945.0908,
          'column4': 11945.0908,
          'column5': 11945.0908,
          'column6': 11945.0908,
          'column7': '-99.00%'
        },
        {
          'column1': '单线程',
          'column2': 'Add',
          'column3': 12482.9315,
          'column4': 12482.9315,
          'column5': 12482.9315,
          'column6': 12482.9315,
          'column7': '-99.00%'
        },
        {
          'column1': '单线程',
          'column2': 'Triad',
          'column3': 12456.3631,
          'column4': 12456.3631,
          'column5': 12456.3631,
          'column6': 12456.3631,
          'column7': '-99.00%'
        },
        {
          'column1': '多线程',
          'column2': 'Array size',
          'column3': 80000000,
          'column4': 80000000,
          'column5': 80000000,
          'column6': 80000000,
          'column7': '-99.00%'
        },
        {
          'column1': '多线程',
          'column2': 'Copy',
          'column3': 34418.7734,
          'column4': 34418.7734,
          'column5': 34418.7734,
          'column6': 34418.7734,
          'column7': '-99.00%'
        },
        {
          'column1': '多线程',
          'column2': 'Scale',
          'column3': 34176.2257,
          'column4': 34176.2257,
          'column5': 34176.2257,
          'column6': 34176.2257,
          'column7': '-99.00%'
        },
        {
          'column1': '多线程',
          'column2': 'Add',
          'column3': 39649.7559,
          'column4': 39649.7559,
          'column5': 39649.7559,
          'column6': 39649.7559,
          'column7': '-99.00%'
        },
        {
          'column1': '多线程',
          'column2': 'Triad',
          'column3': 39655.6133,
          'column4': 39655.6133,
          'column5': 39655.6133,
          'column6': 39655.6133,
          'column7': '-99.00%'
        }
      ],
      showAllData: false,
    };
  },
  created() {
    this.numColumns = Object.keys(this.tableDatas[0]).length;
    this.showAllData = true; // 默认显示全部数据
    const keysToHide = Object.keys(this.tableDatas[0]).filter(key => {
      const value = this.tableDatas[0][key];
      return value.includes('Stream#');
    });
    console.log(keysToHide, 222)
  },
  computed: {
    filteredTableData() {
      if (this.showAllData) {
        return this.tableDatas;
      } else {
        return this.tableDatas.filter(row => {
          return Object.values(row).some(value => {
            value !== '' && !value.includes('Stream#');
            console.log(value, 11)
            return value
          });
        });
      }
    },
  },
  methods: {
    toggleDataVisibility() {
      this.showAllData = !this.showAllData;
    },
    // 导出表格数据为 CSV 格式
    exportTableData() {
      const data = [this.other_list, this.tableDatas];

      // 生成 CSV 格式的数据字符串
      const csvData = data
          .map(rows => {
            return rows
                .map(row => {
                  return Object.values(row).map(value => `"${value}"`).join(",");
                })
                .join("\n");
          })
          .join("\n");

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
