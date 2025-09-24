<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:14:50 2024 +0800
-->
<template>
  <div class="menu">
    <el-aside width="200px">
      <el-menu
        router
        :default-active="activePath"
        class="el-menu-vertical-demo"
        background-color="#409EFF"
        text-color="#fff"
        active-text-color="#ffd04b">
        <template v-for="(item, index) in menus">
          <el-sub-menu :index="index + ''" :key="index" v-if="!item.hidden">
            <template #title>
              <span @click="handleClick(item.path)">{{item.name}}</span>
            </template>
            <el-menu-item
              :index="child.path"
              v-for="(child, index) in item.children"
              :key="index">
                <i :class="child.iconClass"></i>
                {{child.name}}
              </el-menu-item>
          </el-sub-menu>
        </template>
      </el-menu>
    </el-aside>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const menus = router.options.routes
const activePath = router.currentRoute.value.path
const handleClick = (path) => {router.push(path)}
</script>

<style lang="less">
.menu {
  height: 100%;
  .el-aside {
    height: 100%;
    .el-menu {
      height: 100%;
      .el-submenu__icon-arrow {
        display: none;
      }
    }
  }
}
</style>