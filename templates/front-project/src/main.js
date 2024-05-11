import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

//ElementPlus这个是页面的message信息
//vue2使用的是element-ui，vue3使用的就是element-plus
import ElementPlus from 'element-plus';
import 'element-plus/theme-chalk/index.css';

// const app = createApp(App)
// app.use(router)
// app.mount('#app')

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


createApp(App).use(router).mount('#app')
createApp(App).use(ElementPlus).use(router).mount('#app')


