<template>
  <div class="login-container" :style="{ backgroundImage: `url(${background})` }">
    <div class="login-form">
      <h2 class="title">kytuning用户登录</h2>
      <form>
        <div class="form-group">
          <label for="username">用户名：</label>
          <input type="text" id="username" v-model="form.username" placeholder="请输入用户名" @keyup.enter="handleEnterKey"
                 autocomplete="current-username" />
        </div>
        <div class="form-group">
          <label for="password">密码：</label>
          <input type="password" id="password" v-model="form.password" placeholder="请输入密码" @keyup.enter="handleEnterKey"
                 autocomplete="current-password"/>
        </div>
        <div class="button-wrapper">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button @click="handleReset">重置</el-button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import background from '@/assets/background.jpg';
import { ElMessage } from 'element-plus';
import { setToken,getToken,removeToken } from '@/utils/setToken.js'
import { login } from '@/api/api.js'

export default {
  name: 'kytuningLogin',
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    background() {
      return background;
    },
  },
  methods: {
    login() {
      login(this.form).then(res => {
        if (res.data.code === 200) {
          removeToken('token')
          removeToken('username')
          setToken('username', res.data.username)
          setToken('token', 'Bearer ' + res.data.token)
          this.$message({message: '登录成功', type: 'success'})
          this.$router.push('/project')
        }
      }).catch(error => {
    // 捕获错误
    if (error.response) {
      // 请求已发送，并且服务器返回非 2xx 响应
      ElMessage.error({message:'用户名或密码错误',duration: 1000});
    }
    })
    },
    handleEnterKey() {
      this.login();
    },
    handleReset() {
      this.username = '';
      this.password = '';
    },
  },
};
</script>


<style scoped>
.button-wrapper {
  display: flex;
  align-items: center;
}

.button-wrapper .el-button {
  padding: 15px 80px;
  /*margin-left: -100px;*/
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
</style>

