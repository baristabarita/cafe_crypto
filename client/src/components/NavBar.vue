<script>
    export default {
        name: "NavBar",
        data() {
            return {
            menuOpen: false,
            };
        },
        methods: {
            toggleMenu() {
            this.menuOpen = !this.menuOpen;
            },
        },
    };
</script>

<template>
  <header class="bg-cafeAccent shadow-md font-bitter">
    <nav class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
      <!-- Logo Section -->
      <div class="flex items-center">
        <img src="/images/logo2.png" alt="Logo" class="h-12 w-auto mr-3" />
      </div>

      <!-- Navigation Links -->
      <div class="hidden md:flex space-x-4">
        <router-link
          to="/"
          class="text-white hover:bg-cafeDark px-3 py-2 rounded-md text-sm font-medium"
        >
          Home
        </router-link>
        <router-link
          to="/about"
          class="text-white hover:bg-cafeDark px-3 py-2 rounded-md text-sm font-medium"
        >
          About
        </router-link>
      </div>

      <!-- Mobile Menu Button -->
      <button
        @click="toggleMenu"
        class="md:hidden text-white hover:bg-cafeDark p-2 rounded-md"
      >
        <i class="pi pi-bars"></i>
        <!-- PrimeVue Icon -->
      </button>
    </nav>

    <!-- Mobile Menu -->
    <div v-if="menuOpen" class="md:hidden bg-blue-600">
      <router-link
        to="/"
        class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md text-base"
      >
        Home
      </router-link>
      <router-link
        to="/about"
        class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md text-base"
      >
        About
      </router-link>
      <router-link
        to="/services"
        class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md text-base"
      >
        Services
      </router-link>
      <router-link
        to="/contact"
        class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md text-base"
      >
        Contact
      </router-link>
    </div>
  </header>
</template>
