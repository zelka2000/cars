// Импортируем необходимые функции из Vue Router
import { createRouter, createWebHistory } from 'vue-router'
// Импортируем компоненты для маршрутов
import TeamList from '../components/TeamList.vue'
import RaceCalendar from '../components/RaceCalendar.vue'
import DriverPoints from '../components/DriverPoints.vue'

// Создаем экземпляр маршрутизатора
const router = createRouter({
  // Используем HTML5 History API для чистых URL
  history: createWebHistory(),
  // Определяем маршруты
  routes: [
    {
      path: '/',  // Корневой путь
      name: 'teams',  // Имя маршрута
      component: TeamList  // Компонент для отображения
    },
    {
      path: '/races',  // Путь к календарю гонок
      name: 'races',
      component: RaceCalendar
    },
    {
      path: '/drivers',  // Путь к очкам пилотов
      name: 'drivers',
      component: DriverPoints
    }
  ]
})

export default router 