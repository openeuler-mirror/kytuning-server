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
        component: () => import('@/views/ProjectsTable'),
    },
    {
        name: 'env',
        // path: '/env/:projectId :selectedType',
        path: '/env/:envId',
        component: () => import('@/views/EnvsTable'),
        // props: true
    },
    // {
    //     name: 'stream',
    //     // path: '/env/:projectId :selectedType',
    //     path: '/stream/:envId',
    //     component: () => import('@/views/EnvsTable'),
    //     // props: true
    // }
]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

