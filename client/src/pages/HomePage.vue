<template>
  <div class="min-h-screen flex flex-col items-center bg-cafeLight">
    <Header />

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

        <!-- File Upload Section -->
        <div v-if="mode" class="space-y-6">
          <!-- Main File Upload -->
          <FileInput
            id="main-file-upload"
            :label="mode === 'decrypt' ? 'Select encrypted file' : 'Select file to encrypt'"
            accept="*"
            @file-selected="file => handleFileSelected(file, 'main')"
            :uploaded-file="files.main"
          />

          <!-- Key File Upload (only for decryption) -->
          <FileInput
            v-if="mode === 'decrypt'"
            id="key-file-upload"
            label="Select key file"
            accept="*"
            @file-selected="file => handleFileSelected(file, 'key')"
            :uploaded-file="files.key"
          />

          <!-- Action Buttons -->
          <div class="text-center mt-6 space-y-4">
            <BaseButton
              @click="processFile"
              :disabled="!isFormValid || isProcessing"
              variant="primary"
              class="w-full"
            >
              <span class="flex items-center justify-center space-x-2">
                <i v-if="isProcessing" class="pi pi-spinner animate-spin"></i>
                <span>{{ buttonText }}</span>
              </span>
            </BaseButton>

            <!-- Download Section -->
            <div v-if="downloadUrls.length > 0" class="space-y-2">
              <div class="space-y-2">
                <BaseButton
                  v-for="download in downloadUrls"
                  :key="download.url"
                  @click="() => downloadFile(download.url)"
                  variant="success"
                  class="w-full flex items-center justify-center space-x-2"
                >
                  <i class="pi pi-download"></i>
                  <span>{{ download.label }}</span>
                </BaseButton>
              </div>
            </div>

            <!-- Add More Files Button -->
            <BaseButton
              v-if="!isProcessing && (downloadUrls.length > 0 || files.main)"
              @click="clearForm"
              variant="secondary"
              class="w-full"
            >
              Process Another File
            </BaseButton>
          </div>
        </div>
      </div>
    </div>

    <!-- Processing Animation -->
    <ProcessingAnimation v-if="isProcessing" />
  </div>
</template>

<script>
import Header from "../components/common/Header.vue";
import BaseButton from "../components/ui/BaseButton.vue";
import FileInput from "../components/ui/FileInput.vue";
import ProcessingAnimation from "../components/ui/ProcessingAnimation.vue";
import { encryptFile, decryptFile, downloadFile } from "../services/api";

export default {
  name: "HomePage",
  components: {
    Header,
    BaseButton,
    FileInput,
    ProcessingAnimation,
  },
  data() {
    return {
      mode: null,
      files: {
        main: null,
        key: null,
      },
      downloadUrls: [],
      isProcessing: false,
    };
  },
  computed: {
    isFormValid() {
      if (this.mode === "encrypt") {
        return this.files.main !== null;
      }
      return this.files.main !== null && this.files.key !== null;
    },
    buttonText() {
      if (!this.mode) return "Select Mode";
      if (this.isProcessing) return "Processing...";
      return this.mode === "encrypt" ? "Encrypt File" : "Decrypt File";
    },
  },
  methods: {
    setMode(mode) {
      this.mode = mode;
      this.clearForm();
    },
    handleFileSelected(file, type = "main") {
      this.files[type] = file;
      if (file === null) {
        this.downloadUrls = [];
      }
    },

    clearForm() {
      this.files = { main: null, key: null };
      this.downloadUrls = [];
    },

    async processFile() {
      if (!this.isFormValid) return;

      this.isProcessing = true;
      this.downloadUrls = [];

      try {
        let response;
        if (this.mode === "encrypt") {
          response = await encryptFile(this.files.main);
          await new Promise(resolve => setTimeout(resolve, 3000));
        } else {
          response = await decryptFile(this.files.main, this.files.key);
          await new Promise(resolve => setTimeout(resolve, 3000));
        }

        this.downloadUrls = [
          ...(response.data.encrypted_file_url
            ? [{ label: "Download Encrypted File", url: response.data.encrypted_file_url }]
            : []),
          ...(response.data.keys_file_url
            ? [{ label: "Download Key File", url: response.data.keys_file_url }]
            : []),
          ...(response.data.decrypted_file_url
            ? [{ label: "Download Decrypted File", url: response.data.decrypted_file_url }]
            : []),
        ];
      } catch (err) {
        console.error(err);
        this.downloadUrls = [];
      } finally {
        this.isProcessing = false;
      }
    },

    async downloadFile(url) {
      if (!url) return;
      
      try {
        this.isProcessing = true;
        await downloadFile(url);
      } catch (error) {
        console.error(error);
      } finally {
        this.isProcessing = false;
      }
    },
  },
};
</script>