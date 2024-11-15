import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import AboutPage from '@/pages/AboutPage.vue'

const routes = [
  {
    path: '/',
    component: HomePage,
    meta: { layout: 'default' }
  },
  {
    path: '/about',
    component: AboutPage,
    meta: { layout: 'default' }
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})