<template>
    <div class="relative w-full">
      <!-- Background Image -->
      <img 
        src="/images/header.jpg" 
        alt="Cafe Crypto Header" 
        class="w-full h-[50vh] object-cover"
      />
      
      <!-- Text Overlay -->
      <div class="absolute inset-0 flex flex-col items-center justify-center bg-black bg-opacity-40">
        <h1 class="text-8xl text-shadow-custom font-bold font-satisfy text-white drop-shadow-md">Cafe Crypto</h1>
        <p class="text-white text-md font-bitter mt-7 drop-shadow-md">Where Your Files Are Brewed with Security ☕️</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Header",
  };
  </script>
  
  <style scoped>
  /* Add any additional custom styles here */
  </style>
  