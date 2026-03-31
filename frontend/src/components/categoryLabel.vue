<script setup lang="ts">
import { Category } from "@/models/product"
import { computed } from "vue"
import { ca } from "vuetify/locale";

const props = defineProps<{
  category: Category | string | undefined
}>()

const categoryColor = computed(() => {
  switch (props.category) {
    case Category.Accessory:
      return 'secondary'
    case Category.Saddle:
      return 'info'
    case Category.Stirrups:
      return 'accent'
    default:
      return 'grey'
  }
})

const categoryLabel = computed(() => {
  switch (props.category) {
    case Category.Accessory:
      return 'Accessory'
    case Category.Saddle:
      return 'Saddle'
    case Category.Stirrups:
      return 'Stirrups'
    case undefined:
      return 'Uncategorized'
    default:
      return props.category
  }
})
</script>

<template>
    <v-chip :color="categoryColor" class="ma-2"  size="small">
      {{ categoryLabel }}
    </v-chip>
</template>