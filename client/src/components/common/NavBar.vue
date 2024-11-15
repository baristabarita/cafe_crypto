<!-- components/common/NavBar.vue -->
<script>
const navigationItems = [
  { name: 'Home', path: '/' },
  { name: 'About', path: '/about' }
];

export default {
  name: "NavBar",
  data() {
    return {
      menuOpen: false,
      navigationItems
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    closeMenu() {
      this.menuOpen = false;
    }
  },
  watch: {
    $route() {
      this.closeMenu();
    }
  }
};
</script>

<template>
  <header class="bg-cafeAccent shadow-md font-bitter sticky top-0 z-50">
    <nav class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
      <!-- Logo Section -->
      <div class="flex items-center">
        <router-link to="/" class="flex items-center space-x-2">
          <img src="/images/logo2.png" alt="Logo" class="h-12 w-auto ml-5" />
        </router-link>
      </div>

      <!-- Navigation Links -->
      <div class="hidden md:flex space-x-4">
        <router-link
          v-for="item in navigationItems"
          :key="item.path"
          :to="item.path"
          class="text-white transition-colors duration-200 px-3 py-2 rounded-md text-sm font-medium"
          :class="{ 
            'bg-cafeDark': $route.path === item.path,
            'hover:bg-cafeDark/80': $route.path !== item.path 
          }"
        >
          {{ item.name }}
        </router-link>
      </div>

      <!-- Mobile Menu Button -->
      <button
        @click="toggleMenu"
        class="md:hidden text-white hover:bg-cafeDark p-2 rounded-md transition-colors duration-200"
        aria-label="Toggle menu"
      >
        <i :class="['pi', menuOpen ? 'pi-times' : 'pi-bars']"></i>
      </button>
    </nav>

    <!-- Mobile Menu with Transition -->
    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="transform -translate-y-full opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform -translate-y-full opacity-0"
    >
      <div v-if="menuOpen" class="md:hidden bg-cafeDark">
        <router-link
          v-for="item in navigationItems"
          :key="item.path"
          :to="item.path"
          class="block text-white transition-colors duration-200 px-4 py-3 text-base hover:bg-cafeAccent"
          :class="{ 'bg-cafeAccent': $route.path === item.path }"
        >
          {{ item.name }}
        </router-link>
      </div>
    </transition>
  </header>
</template>