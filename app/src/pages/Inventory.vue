<script setup>
import { onMounted } from 'vue';
import {useInventoryStore} from '../stores/inventoryStore'
import FoodItemCard from '../components/FoodItemCard.vue';

const inventoryStore = useInventoryStore()

onMounted(() => {inventoryStore.fetchInventory()})

</script>

<template>
    <div>
       Inventory

       <div v-if="inventoryStore.loading">
        loading inventory...
       </div>
       <div v-if="inventoryStore.error">
        <p style="color: red;">
            error loading inventory: {{ inventoryStore.error.message || inventoryStore.error }}
        </p>
       </div>
       <div v-else>
        <div v-if="inventoryStore.items.length === 0">
            no items in inventory yet.
        </div>
            <div v-else>
                <FoodItemCard 
                v-for="item in inventoryStore.items" 
                :key="item.id"
                :item="item" />
            </div>
       </div>
    </div>
</template>

