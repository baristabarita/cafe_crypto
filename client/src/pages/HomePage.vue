<script>
    import Header from "../components/Header.vue";

    export default {
        components: {
            Header,
        },
        data() {
            return {
                mode: null, // 'encrypt' or 'decrypt'
                file: null, // The file to be encrypted or decrypted
            };
        },
        methods: {
            setMode(mode) {
                this.mode = mode;
            },
            handleFileUpload(event) {
                this.file = event.target.files[0];
            },
            processFile() {
                if (this.mode && this.file) {
                    // Here you would send the file to the backend API for processing (encrypt/decrypt)
                    console.log(`Processing ${this.mode} for file:`, this.file.name);
                }
            },
        },
    };
</script>

<template>
    <div class="min-h-screen flex flex-col items-center bg-cafeLight">
      <!-- Navbar (ensure it’s included in the layout, not duplicated here) -->
  
      <!-- Header Section (no gap between navbar and header) -->
      <Header />
  
      <!-- Main Content Section -->
      <div class="flex-grow flex items-center justify-center w-full">
        <div class="bg-white flex flex-col p-8 rounded-lg shadow-lg max-w-xl w-full items-center justify-center">
          <h1 class="text-2xl font-bold text-cafeAccent text-center mb-4">
            File Encryption and Decryption
          </h1>
  
          <!-- Select Mode Section -->
          <div class="flex justify-center mb-6">
            <button @click="setMode('encrypt')" :class="{
                'bg-cafeAccent text-white': mode === 'encrypt',
                'bg-cafeDark text-white': mode !== 'encrypt'
              }" class="px-6 py-2 rounded-md mr-4">
              Encrypt
            </button>
            <button @click="setMode('decrypt')" :class="{
                'bg-cafeAccent text-white': mode === 'decrypt',
                'bg-cafeDark text-white': mode !== 'decrypt'
              }" class="px-6 py-2 rounded-md">
              Decrypt
            </button>
          </div>
  
          <!-- File Upload Section -->
          <div class="mb-6 w-full">
            <input type="file" @change="handleFileUpload"
              class="px-4 py-2 border border-cafeDark rounded-md w-full" />
          </div>
  
          <div v-if="file" class="text-center mb-6">
            <p class="text-cafeAccent">Selected File: {{ file.name }}</p>
          </div>
  
          <!-- Action Button Section -->
          <div class="text-center">
            <button v-if="file" @click="processFile" :disabled="!mode"
              class="px-6 py-2 bg-cafeAccent text-white rounded-md">
              {{ "Start " + (mode === "encrypt" ? "Encryption" : "Decryption") }}
            </button>
          </div>
        </div>
      </div>
  
      <!-- Footer (ensure it’s included in the layout, not duplicated here) -->
    </div>
  </template>

<style scoped>
/* Add any custom styles for your homepage */
</style>
