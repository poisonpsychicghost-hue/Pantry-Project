<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useInventoryStore } from '../stores/inventoryStore';
import FoodItemCard from '../components/FoodItemCard.vue';

const route = useRoute()
const inventoryStore = useInventoryStore()

const item = ref(null)
const localLoading = ref(false)
const localError = ref(null)

onMounted(async () => {
    const id = route.params.id
    localLoading.value = true
    try {
        const data = await inventoryStore.fetchById(id)
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
        <h1>Pantry Item</h1>

        <div v-if="localLoading">locading item...</div>

        <div v-else-if="localError">
            <p style="color: red;">
                error loading item: {{ localError.message || localError }}
            </p>
        </div>

        <div v-else-if="!item">
            <p>Item not found.</p>
        </div>

        <div v-else>
            <FoodItemCard :item="item" />
        </div>
    </div>
    <div>
        <pre>Item: {{ item || 'no item'}}</pre>
    </div>
</template>