<script setup>
import { onMounted } from 'vue'
import { useShoppingStore } from '../stores/shoppingListStore' // adjust filename if different
import ShoppingItemCard from '../components/ShoppingItemCard.vue'

const shoppingStore = useShoppingStore()

onMounted(() => {
  shoppingStore.fetchShopping()
})
</script>

<template>
  <div>
    <h1>shopping list</h1>

    <div v-if="shoppingStore.loading">
      loading shopping items…
    </div>

    <div v-else-if="shoppingStore.error">
      <p style="color: red;">
        error loading shopping items:
        {{ shoppingStore.error.message || shoppingStore.error }}
      </p>
    </div>

    <div v-else>
      <div v-if="shoppingStore.items.length === 0">
        no shopping items yet.
      </div>
      <div v-else>
        <ShoppingItemCard
          v-for="item in shoppingStore.items"
          :key="item.id"
          :item="item"
        />
      </div>
    </div>
  </div>
</template>