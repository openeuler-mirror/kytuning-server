<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div class="home">
    <AllHeader/>
    <el-container class="content">
      <Menu/>
      <el-container>
        <el-main style="padding-top: 0px;">
          <div class="cont">
            <router-view></router-view>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script scoped>
import AllHeader from "@/components/common/AllHeader";

import Menu from "@/components/common/AllMenu";
import utils from "@/utils/utils";

export default {
  name: 'KytuningHome',
  mixins: [utils],
  components: {
    AllHeader,
    Menu,
  }
}
</script>
<style lang="less">
.home {
  width: 100%;
  height: 100%;
  //overflow: scroll;

  .content {
    position: absolute;
    width: 100%;
    top: 68px;
    bottom: 0;

    .cont {
      margin: 20px 0;
    }
  }
}
</style>
