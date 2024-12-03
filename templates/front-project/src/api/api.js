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

// project
export function project(type, data) {
    return service({
        method: type,
        url: '/project/',
        data
    })
}

// 筛选字段接口
export function get_filter_name() {
    return service({
        method: 'get',
        url: '/get_filter_name/',
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



// 学生列表删除接口
export function studentDel(id) {
    return service({
        method: 'delete',
        url: `/students/${id}`
    })
}

// 信息列表新增接口
// export function info(data) {
//     data = qs.stringify(data)
//     return service({
//         method: 'post',
//         url: '/info',
//         data
//     })
// }

/*
// 信息列表新增和修改接口
export function info(type, data) {
    data = qs.stringify(data)
    let obj = { method: type, url: '/info', data }
    return service(obj)
}
*/


// 信息列表查询接口
export function getInfo() {
    return service({
        method: 'get',
        url: '/info'
    })
}

// 信息列表删除接口
export function infoDel(id) {
    return service({
        method: 'delete',
        url: `/info/${id}`
    })
}

// 数据概览接口
export function dataview() {
    return service({
        method: 'get',
        url: '/dataview'
    })
}

// 旅游地图接口
export function travel() {
    return service({
        method: 'get',
        url: '/travel'
    })
}