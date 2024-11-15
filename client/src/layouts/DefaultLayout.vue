<!-- layouts/DefaultLayout.vue -->
<template>
    <div class="min-h-screen flex flex-col">
      <NavBar />
      <main class="flex-grow">
        <slot></slot>
      </main>
      <Footer />
    </div>
  </template>
  
  <script>
  import NavBar from '../components/common/NavBar.vue'
  import Footer from '../components/common/Footer.vue'
  
  export default {
    name: 'DefaultLayout',
    components: {
      NavBar,
      Footer
    }
  }
  </script>