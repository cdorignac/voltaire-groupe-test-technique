<script setup lang="ts">
import { RouterView } from 'vue-router'
import logo from '@/assets/Equistock.png'
import { useProductStore } from './stores/productStore';
import { computed } from 'vue';

const productStore = useProductStore()

const hasSuccessMessage = computed(() => !!productStore.success)
const hasErrorMessage = computed(() => !!productStore.error)
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-title>
        <v-img :src="logo" alt="Equistock Logo" height="30" />
      </v-app-bar-title>
    </v-app-bar>
    <v-main>
      <v-container>
        <v-alert
          v-model="hasSuccessMessage"
          closable
          type="success"
          variant="tonal"
          :text="productStore.success"
          density="compact"
        ></v-alert>
        <v-alert
          v-model="hasErrorMessage"
          closable
          type="error"
          variant="tonal"
          :text="productStore.error"
          density="compact"
        ></v-alert>
        <RouterView />
      </v-container>
    </v-main>
    <v-footer
      class="d-flex align-center justify-center ga-2 flex-wrap flex-grow-1 py-3 border-t border-primaru-y"
      color="surface"
    >
      <p class="text-center">&copy; 2026 Equistock. All rights reserved.</p>
    </v-footer>
  </v-app>
</template>
