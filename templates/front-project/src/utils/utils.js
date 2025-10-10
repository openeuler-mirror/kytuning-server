/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Wed May 22 14:08:49 2024 +0800
 */
export default {
  data() {
    return {
      currentPage: 1, //当前页数
      pageSize: 10, // 每页显示条数
      total: 0, // 总条数
      itemKey: 0, //更新数据后生成随机数从而刷新页面数据
    };
  },

  methods: {
    //分页
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage = 1;
    },
    //分页
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    //处理展示的数据
    handleDataLoaded(value) {
      this.showAllData = value;
      // 在这里处理子组件的数据
    },
    //选择框只能单选
    handleSelection(val) {
      this.testData = val[0];
      if (val.length > 1) {
        this.$refs.testTable.clearSelection();
        this.$refs.testTable.toggleRowSelection(val.pop());
      }
    },
    //数据页面时点击后跳转至对应数据详情页面
    handleRowClick(row) {
      const List1 = [row.stream, row.lmbench, row.unixbench, row.fio, row.iozone, row.jvm2008, row.cpu2006, row.cpu2017]
      const List2 = ['stream', 'lmbench', 'unixbench', 'fio', 'iozone', 'jvm2008', 'cpu2006', 'cpu2017']
      const firstNonZeroIndex = List1.findIndex(num => num !== 0);
      this.selectedType = List2[firstNonZeroIndex]
      this.$router.push({name: this.selectedType, "params": {baseId: row.env_id, comparsionIds: ''}});
    },
  },
};