/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Mar 7 14:16:46 2024 +0800
 */
import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        name: 'Login',
        path: '/',
        hidden: true,
        component: () => import('@/components/kytuningLogin'),
    },
    {
        name: 'kytuningHome',
        path: '/kytuningHome',
        hidden: true,
        component: () => import('@/components/kytuningHome'),
    },
    {
        name: '设备管理',
        path: '/test1',
        component: () => import('@/views/testViews/TestList'),
        children: []
    },
    {
        name: '测试管理',
        path: '/test',
        redirect: '/test/list',
        children: [
            {
                path: '/test/list',
                name: '测试列表',
                component: () => import('@/views/testViews/TestList')
            },
            {
                path: '/test/do_test/',
                name: '发起测试',
                component: () => import('@/views/testViews/DoTest')
            },
            {
                path: '/test/config',
                name: '配置管理',
                component: () => import('@/views/testViews/DoTest')
            },
        ]
    },
    {
        name: '数据管理',
        path: '/project',
        component: () => import('@/views/dataViews/ProjectTable'),
        children: [
            {
                path: '/data/linshishuju',
                name: '临时数据',
                component: () => import('@/views/dataViews/ProjectTable')
            },
            {
                path: '/project',
                name: '项目数据',
                component: () => import('@/views/dataViews/ProjectTable')
            },
        ]
    },
    {
        name: 'env',
        path: '/env/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/EnvTable'),
        props: true,
    },
    {
        name: 'stream',
        path: '/stream/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/StreamTable'),
    },
    {
        name: 'lmbench',
        path: '/lmbench/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/LmbenchTable'),
    },
    {
        name: 'unixbench',
        path: '/unixbench/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/UnxibenchTable'),
        props: true,
    },
    {
        name: 'fio',
        path: '/fio/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/FioTable'),
    },
    {
        name: 'iozone',
        path: '/iozone/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/IozoneTable'),
    },
    {
        name: 'jvm2008',
        path: '/jvm2008/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/Jvm2008Table'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/Cpu2006Table'),
    },
    {
        name: 'cpu2017',
        path: '/cpu2017/:baseId/:comparsionIds?',
        hidden: true,
        component: () => import('@/views/dataViews/Cpu2017Table'),
    },
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

