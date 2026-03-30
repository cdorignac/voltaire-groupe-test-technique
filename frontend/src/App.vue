<script setup lang="ts">
import { RouterView } from 'vue-router'
import logo from '@/assets/Equistock.png'
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
