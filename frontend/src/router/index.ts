import { createRouter, createWebHistory } from 'vue-router'
import CatalogView from '../views/CatalogView.vue'
import NewProductView from '@/views/NewProductView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Catalog',
      component: CatalogView,
    },
    {
      path: '/products/new',
      name: 'NewProduct',
      component: NewProductView,
    }
  ],
})

export default router
