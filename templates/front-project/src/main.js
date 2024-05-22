import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import service from './service'
import echarts from 'echarts'
//ElementPlus这个是页面的message信息
//vue2使用的是element-ui，vue3使用的就是element-plus
import ElementPlus from 'element-plus';
import 'element-plus/theme-chalk/index.css';


//解决屏幕改变大小报错问题
const debounce = (fn, delay) => {
  let timer = null;
  return function () {
    let context = this;
    let args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      fn.apply(context, args);
    }, delay);
  }
}

const _ResizeObserver = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends _ResizeObserver{
  constructor(callback) {
    callback = debounce(callback, 16);
    super(callback);
  }
}


// createApp(App).use(router).mount('#app')
// createApp(App).use(ElementPlus).use(router).mount('#app')

const app = createApp(App)
app.config.globalProperties.$https = axios
app.config.globalProperties.service = service
app.config.globalProperties.$echarts = echarts
app.use(ElementPlus).use(router).mount('#app')


