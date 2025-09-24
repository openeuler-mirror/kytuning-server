<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->
<template>
  <div class="header">
    <el-header>
      <div class="title">kytuning管理系统</div>
      <div v-for="(item, index) in $route.matched" :key="index" class="name">{{ item.name }}</div>
      <div>{{ name }}</div>
    </el-header>
  </div>
</template>
<script>
import { getToken } from '@/utils/setToken.js'
export default {
    data() {
        return {
            name: ''
        }
    },
    created() {
        this.name = getToken('username')
    }
}
</script>
<style lang="less" scoped>
.header {
    .el-header {
        background: #2578b5;
        color: #fff;
        line-height: 60px;
        display: flex;
        justify-content: space-between;
        .title {
            width: 200px;
            font-size: 24px;

          .name {
            background: #2578b5;
            color: #fff;
            font-size: 24px;
          }
        }
    }
}
</style>