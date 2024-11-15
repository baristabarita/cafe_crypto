<script>
import { RouterLink, RouterView } from 'vue-router'
import PrimeVue from 'primevue/config'
import DefaultLayout from './layouts/DefaultLayout.vue'

export default {
  components: {
    RouterLink,
    RouterView,
    DefaultLayout
  },
  provide: {
    layout: 'default'
  },
  mounted() {
    this.$primevue.config.ripple = true
  }
}
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <component :is="$route.meta.layout || 'DefaultLayout'">
      <router-view v-slot="{ Component, route }">
        <transition :name="route.meta.transition || 'fade'" mode="out-in">
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>
    </component>
  </div>
</template>

<style>
/* Global styles */
body {
  background-color: #FAF7F0; /* Cafe light */
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>