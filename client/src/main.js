import { createApp } from 'vue'
import 'primeicons/primeicons.css'
import './style.css'
import PrimeVue from "primevue/config"
import Aura from "@primevue/themes/aura"
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './pages/HomePage.vue'
import AboutPage from './pages/AboutPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/about', component: AboutPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(App);
app.use(PrimeVue, {
    theme:{
        preset: Aura,
        options: {
            cssLayer: {
                name: 'primevue',
                order: 'tailwind-base, primevue, tailwind-utilities'
            }
        }
    }
});
app.use(router); // Use the router
app.mount('#app');
