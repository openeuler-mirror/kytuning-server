<template>
  <div class="footer">
    <el-card>
        <el-button :id="bt1" type="primary" icon="el-icon-download" @click="exportTableData">导出表格数据</el-button>
    </el-card>
  </div>
</template>
<script>
export default {
  props: {
    otherList: Array,    // 接收 other-list 属性
    tableDatas: Array,    // 接收 table-datas 属性
    dataName:String
  },
  methods:{
     // 导出表格数据为 CSV 格式
    exportTableData() {
      const data = [this.otherList, this.tableDatas];
      console.log(this.otherList,777);
      console.log(this.tableDatas,888);

      // 生成 CSV 格式的数据字符串
      const csvData = data.map(rows => {
        return rows.map(row => {
          return Object.values(row).map(value => `"${value}"`).join(",");
        }).join("\n");
      }).join("\n");

      // 创建并下载 CSV 文件
      const blob = new Blob(["\uFEFF" + csvData], { type: "text/csv;charset=utf-8;" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = this.dataName;
      link.click();
    },
  }
}
</script>