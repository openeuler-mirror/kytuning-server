<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <AllHeader/>
    <el-container class="content">
      <Menu />
    </el-container>
  </div>



</template>


<script>

import AllHeader from "@/components/common/AllHeader";
import Menu from "@/components/common/AllMenu";

export default {
  components: {
    AllHeader,
    Menu
  },
  name: 'kytuningHome',
  methods: {
    projectData() {
      this.$router.push('/project')
    },
    goTest(){},
  }
};
</script>


<style scoped>
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    font-size: 50px;
    color: red;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>

