<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:35:57 2024 +0800
-->
<template>
  <div class="footer">
    <el-card>
      <el-button type="primary" icon="el-icon-download" @click="exportTableData">导出表格数据</el-button>
      <el-button type="primary" icon="el-icon-view" @click="toggleDataVisibility">
        {{ showAllData ? '隐藏数据' : '显示全部数据' }}
      </el-button>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      localShowAllData: this.showAllData
    }
  },
  props: {
    tableDatas: Array,    // 接收 table-datas 属性
    dataName: String,
    showAllData: null
  },
  methods: {
    toggleDataVisibility() {
      this.localShowAllData = !this.localShowAllData;
      this.$emit('data-loaded', this.localShowAllData);
    },
    // 导出表格数据为 CSV 格式
    exportTableData() {
      const data = [this.tableDatas];

      // 生成 CSV 格式的数据字符串
      const csvData = data.map(rows => {
        return rows.map(row => {
          return Object.values(row).map(value => `"${value}"`).join(",");
        }).join("\n");
      }).join("\n");

      // 创建并下载 CSV 文件
      const blob = new Blob(["\uFEFF" + csvData], {type: "text/csv;charset=utf-8;"});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = this.dataName + '_table';
      link.click();
    },
  }
}
</script>