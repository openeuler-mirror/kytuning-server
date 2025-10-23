/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Mar 7 14:25:09 2024 +0800
 */
 import {createApp} from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import service from './service'
import echarts from 'echarts'
//ElementPlus这个是页面的message信息
//vue2使用的是element-ui，vue3使用的就是element-plus
import ElementPlus from 'element-plus';
import 'element-plus/theme-chalk/index.css';


const app = createApp(App)
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
window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
    constructor(callback) {
        callback = debounce(callback, 16);
        super(callback);
    }
}

// 导航守卫
router.beforeEach((to, from, next) => {
    const requiresAuth = to.meta.requiresAuth;

    if (requiresAuth && !localStorage.getItem('token')) {
        // 如果需要身份验证且用户未登录，则重定向到登录页面
        next('/');
    } else {
        // 如果用户已登录或者路由不需要身份验证，则继续正常的导航
        next();
    }
});


app.config.globalProperties.$https = axios
app.config.globalProperties.service = service
app.config.globalProperties.$echarts = echarts
// 使用ElementPlus和Vue Router
app.use(ElementPlus).use(router).mount('#app')


