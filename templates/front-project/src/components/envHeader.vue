<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 11 16:52:35 2024 +0800
-->
<template>
  <div class="footer">
    <el-card>
      <el-row class="mb-4">
        <el-button type="primary" @click="exportTableData">导出表格数据</el-button>
        <el-button type="primary" @click="$router.back()">返回上一步</el-button>
      </el-row>
    </el-card>
  </div>
</template>


<script>
export default {
  props: {
    tableDatas: Array,    // 接收 table-datas 属性
    dataName: String,
    showAllData: null
  },
  methods: {
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