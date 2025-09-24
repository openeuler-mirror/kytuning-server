/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Mon May 20 11:10:24 2024 +0800
 */
// 项目中我们大多数时候都会把对应的接口请求封装成api来调用
import service from '../service.js'

// 登录接口
export function login(data) {
    return service({
        method: 'post',
        url: '/api-token-auth/',
        data
    })
}



// 测试管理列表
export function test_case(params) {
    return service({
        method: 'get',
        url: '/test_case/',
        params
    })
}

// project
export function get_project(params) {
    return service({
        method: 'get',
        url: '/project/',
        params
    })
}

// project
export function project(type, data) {
    return service({
        method: type,
        url: '/project/',
        data
    })
}

// project 合并数据接口
export function mergeData(data) {
    return service({
        method: 'post',
        url: '/merge_data/',
        data
    })
}

// 筛选字段接口
export function getFilterName() {
    return service({
        method: 'get',
        url: '/get_filter_name/',
    })
}

// env
export function env(params) {
    return service({
        method: 'get',
        url: '/env/',
        params
    })
}

// stream
export function stream(params) {
    return service({
        method: 'get',
        url: '/stream/',
        params
    })
}

// stream
export function streamNew(params) {
    return service({
        method: 'get',
        url: '/streamNew/',
        params
    })
}

// lmbench
export function lmbench(params) {
    return service({
        method: 'get',
        url: '/lmbench/',
        params
    })
}

// unixbench
export function unixbench(params) {
    return service({
        method: 'get',
        url: '/unixbench/',
        params
    })
}

// fio
export function fio(params) {
    return service({
        method: 'get',
        url: '/fio/',
        params
    })
}

// iozone
export function iozone(params) {
    return service({
        method: 'get',
        url: '/iozone/',
        params
    })
}

// jvm2008
export function jvm2008(params) {
    return service({
        method: 'get',
        url: '/jvm2008/',
        params
    })
}

// cpu2006
export function cpu2006(params) {
    return service({
        method: 'get',
        url: '/cpu2006/',
        params
    })
}

// cpu2017
export function cpu2017(params) {
    return service({
        method: 'get',
        url: '/cpu2017/',
        params
    })
}

// 下载excel表格接口
export function download_excel(params) {
    return service({
        method: 'get',
        url: '/download_excel/',
        responseType: 'blob',
        params
    })
}

