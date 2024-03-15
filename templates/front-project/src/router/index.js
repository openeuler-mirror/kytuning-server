import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        name: 'hello',
        path: '/hello',
        component: () => import('@/components/HelloWorld')
    },
    {
        name: 'Test',
        path: '/test',
        component: () => import('@/views/test_1'),
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
        path: '/env/:baseId',
        component: () => import('@/views/EnvTable'),
        // props: true
    },
    // {
    //     name: 'unixbench',
    //     path: '/unixbench/:baseId',
    //     component: () => import('@/views/UnixbenchTable'),
    // },
    {
        name: 'unixbenchComparison',
        path: '/unixbenchComparison/:baseId/:comparsionIds?',
        component: () => import('@/views/UnxibenchComparisonTable'),
        props: true,
    },
    // {
    //     name: 'stream',
    //     path: '/stream/:baseId',
    //     component: () => import('@/views/StreamTable'),
    // },
    {
        name: 'streamComparison',
        path: '/streamComparison/:baseId/:comparsionIds?',
        component: () => import('@/views/StreamComparisonTable'),
    },
    // {
    //     name: 'lmbench',
    //     path: '/lmbench/:baseId',
    //     component: () => import('@/views/LmbenchTable'),
    // },
    {
        name: 'lmbenchComparison',
        path: '/lmbenchComparison/:baseId/:comparsionIds?',
        component: () => import('@/views/LmbenchComparisonTable'),
    },
    // {
    //     name: 'fio',
    //     path: '/fio/:baseId',
    //     component: () => import('@/views/FioTable'),
    // },
    {
        name: 'fioComparison',
        path: '/fioComparison/:baseId/:comparsionIds?',
        component: () => import('@/views/FioComparisonTable'),
    },
    // {
    //     name: 'iozone',
    //     path: '/iozone/:baseId',
    //     component: () => import('@/views/IozoneTable'),
    // },
    {
        name: 'iozoneComparison',
        path: '/iozoneComparison/:baseId/:comparsionIds?',
        component: () => import('@/views/IozoneComparisonTable'),
    },
    // {
    //     name: 'jvm2008',
    //     path: '/jvm2008/:baseId',
    //     component: () => import('@/views/Jvm2008sTable'),
    // },
    {
        name: 'jvm2008Comparison',
        path: '/jvm2008Comparison/:baseId/:comparsionIds?',
        component: () => import('@/views/Jvm2008ComparisonTable'),
    },
    {
        name: 'cpu2006',
        path: '/cpu2006/:baseId',
        component: () => import('@/views/Cpu2006Table'),
    },
    {
        name: 'cpu2006Comparison',
        path: '/cpu2006Comparison/:baseId/:comparsionIds?',
        component: () => import('@/views/Cpu2006ComparisonTable'),
    },
    {
        name: 'cpu2017Comparison',
        path: '/cpu2017Comparison/:baseId/:comparsionIds?',
        component: () => import('@/views/Cpu2017ComparisonTable'),
    },
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

