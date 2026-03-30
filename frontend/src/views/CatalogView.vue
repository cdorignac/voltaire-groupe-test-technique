<script setup lang="ts">
import { Category, type Product } from '@/models/product'
import { useProductStore } from '@/stores/productStore'
import { onMounted, ref, type Ref } from 'vue'
import CategoryLabel from '@/components/categoryLabel.vue'

const store = useProductStore()

const headers = [
  { title: 'Name', key: 'name', headerProps: { class: 'font-weight-bold' } },
  { title: 'Category', key: 'category', headerProps: { class: 'font-weight-bold' } },
  { title: 'Price (€)', key: 'price', headerProps: { class: 'font-weight-bold' } },
  { title: 'Stock', key: 'stock', headerProps: { class: 'font-weight-bold' } },
]

const search = ref('')
const selectedCategory: Ref<null | Category> = ref(null)
const selectedStockStatus = ref(false)

onMounted(async () => {
  await getAllProducts()
})

const getAllProducts = async () => {
  store.fetchProducts(selectedStockStatus.value, selectedCategory.value)
}
</script>

<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">All Products</h1>
    <v-row class="mb-5 mt-12" align="center">
      <v-col cols="12" md="5">
        <v-btn-toggle
          v-model="selectedCategory"
          border
          divided
          density="compact"
          @update:model-value="getAllProducts()"
        >
          <v-btn :value="null"> All </v-btn>
          <v-btn :value="Category.Accessory"> Accessory </v-btn>
          <v-btn :value="Category.Saddle"> Saddle </v-btn>
          <v-btn :value="Category.Stirrups"> Stirrups </v-btn>
        </v-btn-toggle>
      </v-col>
      <v-col cols="12" md="2">
        <v-switch
          v-model="selectedStockStatus"
          color="primary"
          label="In stock"
          hide-details
          density="compact"
          @update:model-value="getAllProducts()"
        ></v-switch>
      </v-col>
      <v-col cols="12" md="5">
        <v-text-field
          v-model="search"
          density="compact"
          label="Search"
          prepend-inner-icon="mdi-magnify"
          variant="solo-filled"
          flat
          hide-details
          single-line
        ></v-text-field>
      </v-col>
    </v-row>

    <v-data-table
      :headers="headers"
      :items="store.products"
      :search="search"
      :loading="store.loading"
      no-data-text="No products found."
    >
      <template #item.category="{ item }">
        <category-label :category="item.category" />
      </template>
    </v-data-table>
  </div>
</template>
