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
        component: () => import('@/views/ProjectTable.vue'),
    },
    {
        name: 'env',
        // path: '/env/:projectId :selectedType',
        path: '/env/:envId',
        component: () => import('@/views/EnvTable.vue'),
        // props: true
    },
    {
        name: 'stream',
        path: '/stream/:envId',
        component: () => import('@/views/StreamTable'),
        // props: true
    },
    {
        name: 'unixbench',
        path: '/unixbench/:envId',
        component: () => import('@/views/UnixbenchTable'),
    },


]
export default createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes
})

