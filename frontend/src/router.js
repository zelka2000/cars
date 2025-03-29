import { createRouter, createWebHistory } from 'vue-router'
import RaceCalendar from './components/RaceCalendar.vue'
import TeamList from './components/TeamList.vue'
import DriverPoints from './components/DriverPoints.vue'

const routes = [
  { path: '/', redirect: '/calendar' },
  { path: '/calendar', component: RaceCalendar },
  { path: '/teams', component: TeamList },
  { path: '/points', component: DriverPoints }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 