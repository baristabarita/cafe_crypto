<!-- pages/HomePage.vue -->
<script>
import Header from "../components/common/Header.vue";
import BaseButton from "../components/ui/BaseButton.vue";
import FileInput from "../components/ui/FileInput.vue";
// import { encryptFile, decryptFile } from "../services/api";

export default {
  name: "HomePage",
  components: {
    Header,
    BaseButton,
    FileInput,
  },
  data() {
    return {
      mode: null,
      file: null,
      isProcessing: false,
      error: null,
      successMessage: null,
    };
  },
  computed: {
    isFormValid() {
      return this.mode && this.file;
    },
    buttonText() {
      if (this.isProcessing) return "Processing...";
      return this.mode === "encrypt" ? "Start Encryption" : "Start Decryption";
    },
  },
  methods: {
    setMode(mode) {
      this.mode = mode;
      this.clearMessages();
    },
    handleFileSelected(file) {
      this.file = file;
      this.clearMessages();
    },
    clearMessages() {
      this.error = null;
      this.successMessage = null;
    },
    async processFile() {
      if (!this.isFormValid) return;

      this.isProcessing = true;
      this.clearMessages();

      try {
        const processFunction = this.mode === "encrypt" ? encryptFile : decryptFile;
        const response = await processFunction(this.file);
        
        // Handle successful response
        this.successMessage = `File successfully ${this.mode}ed!`;
        
        // Handle file download if provided by the server
        if (response.data.downloadUrl) {
          window.location.href = response.data.downloadUrl;
        }
      } catch (err) {
        this.error = err.response?.data?.message || 
          `Failed to ${this.mode} file. Please try again.`;
      } finally {
        this.isProcessing = false;
      }
    },
  },
};
</script>

<template>
  <div class="min-h-screen flex flex-col items-center bg-cafeLight">
    <!-- Header Section -->
    <Header />

    <!-- Main Content Section -->
    <div class="flex-grow flex items-center justify-center w-full p-6">
      <div class="bg-white flex flex-col p-8 rounded-lg shadow-lg max-w-xl w-full">
        <h1 class="text-2xl font-bold text-cafeAccent text-center mb-6">
          File Encryption and Decryption
        </h1>

        <!-- Mode Selection -->
        <div class="flex justify-center mb-8 space-x-4">
          <BaseButton
            @click="setMode('encrypt')"
            :variant="mode === 'encrypt' ? 'primary' : 'secondary'"
          >
            Encrypt
          </BaseButton>
          <BaseButton
            @click="setMode('decrypt')"
            :variant="mode === 'decrypt' ? 'primary' : 'secondary'"
          >
            Decrypt
          </BaseButton>
        </div>

        <!-- File Upload -->
        <div class="mb-8">
          <FileInput
            id="file-upload"
            :label="mode ? `Select file to ${mode}` : 'Select a file'"
            accept=".txt,.pdf,.doc,.docx"
            @file-selected="handleFileSelected"
          />
        </div>

        <!-- Status Messages -->
        <div v-if="error || successMessage" class="mb-6">
          <p v-if="error" class="text-red-500 text-center">{{ error }}</p>
          <p v-if="successMessage" class="text-green-500 text-center">
            {{ successMessage }}
          </p>
        </div>

        <!-- Action Button -->
        <div class="text-center">
          <BaseButton
            @click="processFile"
            :disabled="!isFormValid || isProcessing"
            variant="primary"
          >
            <span v-if="isProcessing" class="flex items-center">
              <i class="pi pi-spinner pi-spin mr-2"></i>
              {{ buttonText }}
            </span>
            <span v-else>{{ buttonText }}</span>
          </BaseButton>
        </div>
      </div>
    </div>
  </div>
</template>