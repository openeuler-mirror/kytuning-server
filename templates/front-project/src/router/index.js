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
        name: 'Home',
        path: '/',
        component: () => import('@/components/kytuningLogin'),
    },
    {
        path: '/project',
        name: 'project',
        component: () => import('@/views/ProjectTable'),
    },
    {
        name: 'env',
        path: '/env/:baseId/:comparsionIds?',
        component: () => import('@/views/EnvTable'),
        props: true,
    },
    {
        name: 'stream',
        path: '/stream/:baseId/:comparsionIds?',
        component: () => import('@/views/StreamTable'),
    },
    {
        name: 'lmbench',
        path: '/lmbench/:baseId/:comparsionIds?',
        component: () => import('@/views/LmbenchTable'),
    },
    {
        name: 'unixbench',
        path: '/unixbench/:baseId/:comparsionIds?',
        component: () => import('@/views/UnxibenchTable'),
        props: true,
    },
    {
        name: 'fio',
        path: '/fio/:baseId/:comparsionIds?',
        component: () => import('@/views/FioTable'),
    },
    {
        name: 'iozone',
        path: '/iozone/:baseId/:comparsionIds?',
        component: () => import('@/views/IozoneTable'),
    },
    {
        name: 'jvm2008',
        path: '/jvm2008/:baseId/:comparsionIds?',
        component: () => import('@/views/Jvm2008Table'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId/:comparsionIds?',
        component: () => import('@/views/Cpu2006Table'),
    },
    {
        name: 'cpu2017',
        path: '/cpu2017/:baseId/:comparsionIds?',
        component: () => import('@/views/Cpu2017Table'),
    },
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

