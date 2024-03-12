import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        name: 'hello',
        path: '/hello',
        component: () => import('@/components/HelloWorld')
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
        // path: '/env/:env_id :selectedType',
        path: '/env/:baseId',
        component: () => import('@/views/EnvTable'),
        // props: true
    },
    {
        name: 'unixbench',
        path: '/unixbench/:baseId',
        component: () => import('@/views/UnixbenchTable'),
    },
    {
        name: 'unixbenchComparison',
        path: '/unixbenchComparison/:baseId/:comparativeIds?',
        component: () => import('@/views/UnxibenchComparisonTable'),
        props: true,
    },
    {
        name: 'stream',
        path: '/stream/:baseId',
        component: () => import('@/views/StreamTable'),
    },
    {
        name: 'streamComparison',
        path: '/streamComparison/:baseId/:comparativeIds?',
        component: () => import('@/views/StreamComparisonTable'),
    },
    {
        name: 'lmbench',
        path: '/lmbench/:baseId',
        component: () => import('@/views/LmbenchTable'),
    },
    {
        name: 'fio',
        path: '/fio/:baseId',
        component: () => import('@/views/FioTable'),
    },
    {
        name: 'fioComparison',
        path: '/fioComparison/:baseId/:comparativeIds?',
        component: () => import('@/views/FioComparisonTable'),
    },
    {
        name: 'iozone',
        path: '/iozone/:baseId',
        component: () => import('@/views/IozoneTable'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId',
        component: () => import('@/views/Cpu2006Table'),
    },
    // {
    //     name: 'jvm2008',
    //     path: '/jvm2008/:baseId',
    //     component: () => import('@/views/Jvm2008sTable'),
    // },
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

