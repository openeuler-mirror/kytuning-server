/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Wed May 22 13:46:05 2024 +0800
 */
import axios from 'axios'
import { getToken } from '@/utils/setToken.js'
import { ElMessage } from 'element-plus'

const service = axios.create({
    baseURL: '/api/', // baseURL会自动加在请求地址上
    timeout: 50000
})

// 添加请求拦截器
service.interceptors.request.use((config) => {
    // 在请求之前做些什么(获取并设置token)
    config.headers['Authorization'] = getToken('token')
    // config.headers['Content-Type'] = 'application/json'
    return config
}, (error) => {
    return Promise.reject(error)
})

// 添加响应拦截器
service.interceptors.response.use((response) => {
    // 对响应数据做些什么
    let { code, message } = response.data
    if(code !== 200) {
        if (response.config.url === '/download_excel/'){
            if (response.status === 200){ElMessage({message: message || '表格制作完成，正在导出。', type: 'success'})}}
        else if (response.config.url === '/down_message/'){
            if (response.status === 200){ElMessage({message: message || '下载日志完成。', type: 'success'})}}
        else {ElMessage({message: message || 'error', type: 'warning'})}
    }
    return response
}, (error) => {
    return Promise.reject(error)
})

export default service