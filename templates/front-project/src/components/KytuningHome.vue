<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div class="login-container" :style="{ backgroundImage: `url(${background})` }">
    <el-button class="button" size="large" >首页</el-button>
    <el-button class="button" size="large" >设备管理</el-button>
    <el-button size="large" @click="goTest">测试管理</el-button>
    <el-button size="large" @click="projectData">数据管理</el-button>
  </div>
</template>


<script>
import background from '@/assets/login.jpg';

export default {

  name: 'kytuningHome',
  computed: {
    background() {
      return background;
    },
  },
  methods: {
    projectData() {
      this.$router.push('/project')
    },
    goTest(){
      this.$router.push('/test')
    },
  }
};
</script>


<style scoped>
button {
  width: 250px;
  height: 50px;
  font-size: 40px;
}

.login-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>

