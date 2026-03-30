<script setup lang="ts">
import { Category } from '@/models/product'
import router from '@/router'
import { useProductStore } from '@/stores/productStore'
import { reactive, ref } from 'vue'

const store = useProductStore()

const newProduct = reactive({
  name: '',
  category: null,
  price: 0,
  stock: 0,
})

const isValid = ref(false)

const stringRules = [
  (v: string) => !!v || 'This field is required',
  (v: string) => (v && v.length >= 3) || 'Minimum 3 characters',
]

const priceRules = [
  (v: number) => (v !== null && v !== undefined) || 'This field is required',
  (v: number) => v > 0 || 'Value must be positive',
]

const stockRules = [(v: number) => (v !== null && v !== undefined) || 'This field is required']

const categoryRules = [(v: Category) => !!v || 'This field is required']

const addProduct = async () => {
  await store.createProduct(newProduct)
  router.push('/')
}
</script>

<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold">Add new product</h1>
    <v-form v-model="isValid" class="mt-12 mb-5" v-if="!store.loading">
      <v-text-field
        v-model="newProduct.name"
        :rules="stringRules"
        label="Product name"
        class="mb-4"
      ></v-text-field>
      <v-text-field
        v-model="newProduct.price"
        :rules="priceRules"
        label="Price (€)"
        class="mb-4"
      ></v-text-field>
      <v-number-input
        v-model="newProduct.stock"
        :rules="stockRules"
        label="Stock"
        :min="0"
        class="mb-4"
      ></v-number-input>
      <v-select
        v-model="newProduct.category"
        label="Category"
        :items="Object.values(Category)"
        :rules="categoryRules"
        class="mb-4"
      ></v-select>
      <div class="d-flex justify-space-between gap-4">
        <v-btn to="/">Cancel</v-btn>
        <v-btn color="primary" @click="addProduct()" :disabled="!isValid">Add new product</v-btn>
      </div>
    </v-form>
    <v-progress-circular v-else color="primary" indeterminate></v-progress-circular>
  </div>
</template>
