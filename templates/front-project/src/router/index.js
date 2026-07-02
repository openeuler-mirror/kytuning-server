import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        path: '/',
        name: 'Login',
        hidden: true,
        component: () => import('@/components/kytuningLogin'),
    },
    {
        path: '/machine/list',
        name: '设备管理',
        iconClass: 'fa fa-users',
        component: () => import('@/components/KytuningHome'),
        children: [
            {
                name: '注册设备',
                path: '/machine/list',
                meta: {requiresAuth: true}, // 添加这一行，表示需要身份验证
                component: () => import('@/views/machineViews/MachineList'),
                children: []
            },
            {
                name: 'ks文件',
                path: '/ks/list',
                meta: {requiresAuth: true},
                component: () => import('@/views/machineViews/KSList.vue'),
                children: []
            },
            {
                name: 'ISO适配',
                path: '/ISO/list',
                meta: {requiresAuth: true},
                component: () => import('@/views/machineViews/ISOList.vue'),
                children: []
            },
            {
                name: '设备中心',
                path: '/server/list',
                meta: {requiresAuth: true},
                component: () => import('@/views/machineViews/ServerList.vue'),
                children: []
            },

        ]
    },
    {
        path: '/test/list',
        name: '测试管理',
        iconClass: 'fa fa-users',
        component: () => import('@/components/KytuningHome'),
        children: [
            {
                path: '/test/do_test',
                name: '日常测试',
                meta: {requiresAuth: true},
                component: () => import('@/views/testViews/DoTest'),
                // props:true  // 如果props设置为true，$route.params将被设置为组件属性记对象
            },
            {
                path: '/test/list',
                name: '日常测试列表',
                meta: {requiresAuth: true},
                component: () => import('@/views/testViews/DailyTestList.vue')
            },
            {
                path: '/test/monitor_test',
                name: '迭代测试',
                meta: {requiresAuth: true},
                component: () => import('@/views/testViews/MonitorTest'),
                // props:true  // 如果props设置为true，$route.params将被设置为组件属性记对象
            },
            {
                path: '/test/monitor_list',
                name: '迭代测试列表',
                meta: {requiresAuth: true},
                component: () => import('@/views/testViews/MinitorTestList')
            },
            // {
            //     path: '/test/do_test_yaml',
            //     name: '发起测试-yaml',
            //     meta: { requiresAuth: true },
            //     component: () => import('@/views/testViews/DoTest-yaml'),
            // },
            {
                path: '/test/config',
                name: '配置管理',
                meta: {requiresAuth: true},
                component: () => import('@/views/testViews/ConfigList')
            },
        ]
    },
    {
        path: '/projectData',
        name: '数据管理',
        iconClass: 'fa fa-users',
        component: () => import('@/components/KytuningHome'),
        children: [
            {
                path: '/tempData',
                name: '临时数据',
                meta: {requiresAuth: true},
                component: () => import('@/views/dataViews/ProjectTable.vue'),
            },
            {
                path: '/projectData',
                name: '项目数据',
                meta: {requiresAuth: true},
                component: () => import('@/views/dataViews/ProjectTable.vue'),
            },
        ]
    },
    {
        path: '/error/list',
        name: '错误管理',
        iconClass: 'fa fa-users',
        component: () => import('@/components/KytuningHome'),
        children: [
            {
                path: '/error/list',
                name: '错误列表',
                meta: {requiresAuth: true},
                component: () => import('@/views/errorViews/ErrorList')
            },
        ]
    },
    {
        name: 'env',
        path: '/env/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/EnvTable'),
    },
    {
        name: 'stream',
        path: '/stream/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/StreamTable'),
    },
    {
        name: 'lmbench',
        path: '/lmbench/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/LmbenchTable'),
    },
    {
        name: 'unixbench',
        path: '/unixbench/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/UnxibenchTable'),
    },
    {
        name: 'fio',
        path: '/fio/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/FioTable'),
    },
    {
        name: 'iozone',
        path: '/iozone/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/IozoneTable'),
    },
    {
        name: 'jvm2008',
        path: '/jvm2008/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/Jvm2008Table'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/Cpu2006Table'),
    },
    {
        name: 'cpu2017',
        path: '/cpu2017/:baseId/:comparsionIds?',
        meta: {requiresAuth: true},
        hidden: true,
        component: () => import('@/views/dataViews/Cpu2017Table'),
    }
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

