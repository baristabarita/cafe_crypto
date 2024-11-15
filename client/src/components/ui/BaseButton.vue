<!-- components/ui/BaseButton.vue -->
<template>
    <button
      :class="[
        'px-6 py-2 rounded-md transition-colors',
        variant === 'primary' ? 'bg-cafeAccent text-white hover:bg-cafeDark' : 
        variant === 'secondary' ? 'bg-cafeDark text-white hover:bg-cafeAccent' :
        'bg-gray-200 text-gray-700 hover:bg-gray-300'
      ]"
      :disabled="disabled"
      @click="$emit('click')"
    >
      <slot></slot>
    </button>
  </template>
  
  <script>
  export default {
    name: 'BaseButton',
    props: {
      variant: {
        type: String,
        default: 'primary',
        validator: value => ['primary', 'secondary', 'default'].includes(value)
      },
      disabled: {
        type: Boolean,
        default: false
      }
    }
  }
  </script>
  