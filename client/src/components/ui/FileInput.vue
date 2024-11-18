<!-- components/ui/FileInput.vue -->
<template>
  <div class="w-full">
    <label
      :for="id"
      class="block text-sm font-medium text-gray-700 mb-2"
    >
      {{ label }}
    </label>
    <div
      class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-dashed rounded-md transition-colors cursor-pointer"
      :class="[
        uploadedFile 
          ? 'border-green-500 bg-green-50' 
          : 'border-gray-300 hover:border-cafeAccent'
      ]"
      @dragover.prevent
      @drop.prevent="handleDrop"
    >
      <div class="space-y-1 text-center">
        <!-- Show different icons based on upload status -->
        <template v-if="uploadedFile">
          <i class="pi pi-check-circle text-4xl text-green-500"></i>
          <div class="flex flex-col space-y-2">
            <span class="text-sm text-green-600 font-medium">File Uploaded Successfully!</span>
            <span class="text-xs text-gray-500">{{ uploadedFile.name }}</span>
            <span class="text-xs text-gray-400">
              {{ formatFileSize(uploadedFile.size) }}
            </span>
            <button 
              @click.stop="handleRemoveFile"
              class="text-xs text-gray-500 hover:text-gray-700 font-bold"
            >
              Remove File
            </button>
          </div>
        </template>
        <template v-else>
          <i class="pi pi-upload text-4xl text-gray-400"></i>
          <div class="flex text-sm text-gray-600">
            <label
              :for="id"
              class="relative cursor-pointer rounded-md font-medium text-cafeAccent hover:text-cafeDark focus-within:outline-none"
            >
              <span>Upload a file</span>
              <input
                :id="id"
                type="file"
                class="sr-only"
                @change="handleFileSelect"
                :accept="accept"
              />
            </label>
            <p class="pl-1">or drag and drop</p>
          </div>
          <p class="text-xs text-gray-500">
            {{ acceptedFileTypes }}
          </p>
        </template>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: 'FileInput',
  props: {
    label: {
      type: String,
      default: 'File'
    },
    accept: {
      type: String,
      default: '*'
    },
    id: {
      type: String,
      required: true
    },
    uploadedFile: {
      type: File,
      default: null
    }
  },
  computed: {
    acceptedFileTypes() {
      return this.accept === '*' 
        ? 'All file types supported'
        : `Supported files: ${this.accept}`
    }
  },
  methods: {
    handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        this.$emit('file-selected', file)
      }
    },
    handleDrop(event) {
      const file = event.dataTransfer.files[0]
      if (file) {
        this.$emit('file-selected', file)
      }
    },
    handleRemoveFile() {
      this.$emit('file-selected', null)
    },
    formatFileSize(bytes) {
      if (bytes === 0) return '0 Bytes'
      
      const k = 1024
      const sizes = ['Bytes', 'KB', 'MB', 'GB']
      const i = Math.floor(Math.log(bytes) / Math.log(k))
      
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
    }
  }
}
</script>