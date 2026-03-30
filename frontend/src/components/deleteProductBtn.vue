<script setup lang="ts">
import { type Product } from '@/models/product'
import { ref } from 'vue'
import { useProductStore } from '@/stores/productStore'

const props = defineProps<{
  product: Product
}>()

const store = useProductStore()

const dialog = ref(false)

const deleteProduct = () => {
  if (props.product.id !== undefined) {
    store.deleteProduct(props.product.id)
  }
  dialog.value = false
}
</script>

<template>
  <div class="text-center pa-4">
    <v-btn
      @click="dialog = true"
      title="Delete Product"
      density="compact"
      icon="mdi-trash-can-outline"
      color="error"
      variant="text"
      size="x-small"
    >
    </v-btn>

    <v-dialog v-model="dialog" width="auto">
      <v-card
        max-width="400"
        :text="`Are you sure you want to delete this product ${props.product.name}?`"
      >
        <template v-slot:actions>
          <v-btn text="Cancel" @click="dialog = false" class="mr-4"></v-btn>
          <v-btn color="primary" variant="flat" text="Delete" @click="deleteProduct()"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>
