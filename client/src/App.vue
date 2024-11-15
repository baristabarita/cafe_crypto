<script setup>
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  import { ref } from 'vue';

  const text = ref('')
</script>


<template>
  <div>
    <span class="text-xl font-bold mb-4 block">Hello World</span>
    <InputText v-model="text" />
    <Button label="Save" />
    {{ text }}
  </div>

</template>


