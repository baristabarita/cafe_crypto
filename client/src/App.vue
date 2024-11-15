<script>
  
  import NavBar from './components/NavBar.vue';
  import Footer from './components/Footer.vue';

  export default {
  components: {
    NavBar,
    Footer,
  }
};
</script>


<template>
  <div id="app">
    <NavBar />
    <router-view/>
    <Footer />
  </div>

</template>

<style>
/* Global styles */
body {
  background-color: #FAF7F0; /* Cafe light */
}
</style>
