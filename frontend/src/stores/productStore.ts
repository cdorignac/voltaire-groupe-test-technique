import type { Category, Product } from '@/models/product'
import api from '@/stores/api'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'

export const useProductStore = defineStore('productStore', () => {
  const products = ref([])
  const loading = ref(false)
  const error: Ref<undefined | string> = ref(undefined)
  const success: Ref<undefined | string> = ref(undefined)

  async function fetchProducts(inStock: boolean, category?: Category | null) {
    loading.value = true
    try {
      const categoryParams = category ? `&category=${category}` : ''
      const url = `/products?in_stock=${inStock}${categoryParams}`
      const response = await api.get(url)
      products.value = response.data
    } catch (err) {
      error.value = 'Failed to load products'
    } finally {
      loading.value = false
    }
  }

  async function createProduct(product: Omit<Product, 'id'>) {
    try {
      const response = await api.post('/products', product) 
      products.value.push(response.data)
      success.value = `Product ${product.name} created successfully`
      setTimeout(() => {
        success.value = undefined
      }, 10000)
    } catch (err) {
      error.value = 'Failed to create product'
    } finally {
      loading.value = false
    }
  }
  return {
    products,
    loading,
    error,
    success,
    fetchProducts,
    createProduct,
  }
})
