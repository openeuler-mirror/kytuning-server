<template>
  <h1>Kylin</h1>
  <h6>欢迎使用kytuing分析工具，请点击下一步进行进入project页面</h6>
  <button @click="toProject">下一步</button>
</template>

<script>
export default {
  methods: {
    toProject() {
      this.$router.push({name: 'project',});
      console.log("跳转成功")
    },
  }
}
</script>

<style scoped>
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