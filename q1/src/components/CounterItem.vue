<script setup lang="ts">
import { ref } from 'vue';

const count = ref(0);

function increment() {
  count.value++;
}
function decrement() {
  count.value--;
}

function reset() {
  count.value = 0;
}
</script>

<template>
  <div class="q-pa-sm column items-center">
    <h3>Counter: {{ count }}</h3>
    <q-btn-group outline>
      <q-btn @click="increment" outline label="Increment" />
      <q-btn @click="decrement" outline label="Decrement" />
      <q-btn @click="reset" outline label="Reset" />
    </q-btn-group>
  </div>
</template>
