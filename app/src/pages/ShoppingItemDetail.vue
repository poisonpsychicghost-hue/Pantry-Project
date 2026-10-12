<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useShoppingStore } from '../stores/shoppingListStore'
import ShoppingItemCard from '../components/ShoppingItemCard.vue'

const route = useRoute()
const shoppingStore = useShoppingStore()

const item = ref(null)
const localLoading = ref(false)
const localError = ref(null)

onMounted(async () => {
    const id = route.params.id
    localLoading.value = true
    try {
        const data = await shoppingStore.fetchById(id)
        item.value = data
        localError.value = null
    } catch (e) {
        localError.value = e
    } finally {
        localLoading.value = false
    }
})

</script>

<template>
    <div>
        <h2>Shopping Item</h2>

        <div v-if="localLoading">
            loading shopping item...
        </div>

        <div v-if="localError">
            <p style="color: red;">Error loading Shopping Item: {{ localError.message || localError}}</p>
        </div>
        <div v-else-if="!item">
            <p>Item not Found</p>
        </div>

        <div v-else>
            <ShoppingItemCard :item="item" />
        </div>
        <pre>item debug: {{ item }}</pre>
    </div>
</template>