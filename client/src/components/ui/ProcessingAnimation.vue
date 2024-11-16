<!-- components/ProcessingAnimation.vue -->
<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-8 rounded-lg shadow-xl flex flex-col items-center">
        <!-- Spinner Animation -->
        <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-cafeAccent mb-4"></div>
        
        <!-- Processing Text -->
        <p class="text-lg font-semibold text-gray-700">Processing your file...</p>
        <p class="text-sm text-gray-500 mt-2">Please wait while we handle your request</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProcessingAnimation'
  }
  </script>
  
  <style scoped>
  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
  
  .animate-spin {
    animation: spin 1s linear infinite;
  }
  </style>