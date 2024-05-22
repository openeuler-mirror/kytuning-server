import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        name: 'Test',
        path: '/test',
        component: () => import('@/views/test_1'),
    },
    {
        name: 'tablehome',
        path: '/tablehome',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'Home',
        path: '/',
        component: () => import('@/views/KylinHome'),
    },
    {
        path: '/project',
        name: 'project',
        component: () => import('@/views/ProjectTable'),
    },
    {
        name: 'env',
        path: '/env/:baseId/',
        component: () => import('@/views/EnvTable'),
        props: true,
    },
    {
        name: 'unixbench',
        path: '/unixbench/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
        props: true,
    },
    {
        name: 'stream',
        path: '/stream/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'lmbench',
        path: '/lmbench/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'fio',
        path: '/fio/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'iozone',
        path: '/iozone/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'jvm2008',
        path: '/jvm2008/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
    {
        name: 'cpu2017',
        path: '/cpu2017/:baseId/:comparsionIds?',
        component: () => import('@/components/common/TableHome'),
    },
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

