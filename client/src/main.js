import { createApp } from 'vue'
import './style.css'
import PrimeVue from "primevue/config"
import Aura from "@primevue/themes/aura"
import App from './App.vue'

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
})
app.mount('#app')
