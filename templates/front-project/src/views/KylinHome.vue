<template>
  <div class="login-container" :style="{ backgroundImage: `url(${background})` }">
    <div class="login-form">
      <h2 class="title">kytuning用户登录</h2>
      <form>
        <div class="form-group">
          <label for="username">用户名：</label>
          <input type="text" id="username" v-model="username" placeholder="请输入用户名"/>
        </div>
        <div class="form-group">
          <label for="password">密码：</label>
          <input type="password" id="password" v-model="password" placeholder="请输入密码"/>
        </div>
        <el-button type="submit" class="submit-button" @click="handleSubmit">登录</el-button>
      </form>
    </div>
  </div>
</template>


<script>
import background from '@/assets/background.jpg';
import { ElMessage } from 'element-plus';


export default {
  // name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  computed: {
    background() {
      return background;
    },
  },
  methods: {
    handleSubmit() {
       // 处理登录逻辑
      if(this.username === 'kylin' || this.password === '123456') {
        this.$router.push({name: 'project',});
      }else {
        // 提示用户名或密码错误
        ElMessage.error('用户名或密码错误');
      }
    },
  },
};
</script>


<style scoped>
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

.login-form {
  width: 400px;
  background-color: #fff;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  margin-bottom: 10px;
}

input {
  border: none;
  border-bottom: 1px solid #ccc;
  outline: none;
  font-size: 16px;
  padding: 10px;
}

.submit-button {
  background-color: #00bcd4;
  color: #fff;
  border: none;
  outline: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: #008ba3;
}

</style>

