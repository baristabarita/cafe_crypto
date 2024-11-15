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
        class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md hover:border-cafeAccent transition-colors cursor-pointer"
        @dragover.prevent
        @drop.prevent="handleDrop"
      >
        <div class="space-y-1 text-center">
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
      }
    }
  }
  </script>