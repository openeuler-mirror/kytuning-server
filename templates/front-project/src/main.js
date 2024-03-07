import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// const app = createApp(App)
// app.use(router)
// app.mount('#app')

createApp(App).use(router).mount('#app')



// import { createApp } from 'vue'
// import App from './App.vue'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'
// import locale from'element-plus/es/locale/lang/zh-cn'
// import axios from 'axios'
// const app = createApp(App)
// app.config.globalproperties.$http = axios
// app.use(ElementPlus,{locale}).mount( '#app')