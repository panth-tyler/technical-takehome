<template>
  <q-page class="row items-center justify-evenly">
    <counter-item />
  </q-page>
</template>

<script setup lang="ts">
import CounterItem from 'components/CounterItem.vue';

defineOptions({
  name: 'IndexPage',
});
</script>
