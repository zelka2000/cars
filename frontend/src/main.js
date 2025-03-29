// Импортируем функцию создания приложения Vue
import { createApp } from 'vue'
// Импортируем библиотеку Element Plus
import ElementPlus from 'element-plus'
// Импортируем стили Element Plus
import 'element-plus/dist/index.css'
// Импортируем корневой компонент
import App from './App.vue'
// Импортируем настройки маршрутизации
import router from './router'

// Создаем экземпляр приложения
const app = createApp(App)
// Подключаем Element Plus
app.use(ElementPlus)
// Подключаем маршрутизатор
app.use(router)
// Монтируем приложение в DOM
app.mount('#app')
