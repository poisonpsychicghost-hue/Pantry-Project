<template>

    <form @submit.prevent="handleSubmit" class="flex flex-col gap-4 p-4 bg-white rounded shadow">
        <!-- Category Selector -->
        <div class="flex gap-4">
            <input v-model="item.name" class="input" placeholder="Item Name" required>
            <select v-model="selectedCategory" @change="updateCategory" class="input" required>
                <option value="" disabled>Select Category</option>
                <option v-for="cat in categoryStore.items" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
            </select>
            
        </div>
        <!-- Base Item Data -->
        <div class="flex gap=4">
            <input v-model.number="item.quantity" type="number" class="input" placeholder="Quantity" min="1" required />
            <input v-model="item.unit" class="input" placeholder="Unit (e.g. lbs, packs)" required />
            <input v-model="item.expiration_date" type="date" class="input" required />
        </div>
        <!-- Category Specific Metadata -->
        <div v-if="selectedCategoryObject">
            <div v-for="key in selectedCategoryObject.metadata_keys" :key="key">
                <input
                    v-model="item.metadata[key]"
                    :placeholder="key.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())"
                    class="input"
                    :required="false"
                />
            </div>
            <p>Test Unseen Section</p>
        </div>
        <button class="bg-blue-600 text-white px-4 py-2 rounded" type="submit">
            {{ submitLabel }}
        </button>

    </form>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useCategoryStore } from '../stores/categoryStore'

// Props for Quick Add, Bulk Add, Card-Edit
const props = defineProps({
    submitLabel: {type: String, default: 'Add Item' },
    initialItem: {type: Object, default: () => ({}) }
})

// State
const categoryStore = useCategoryStore()
const item = ref({
    ...props.initialItem,
    metadata: props.initialItem.metadata ? { ...props.initialItem.metadata } : {}  
})
console.log("EntryField component mounted!")
onMounted(() => {
    categoryStore.fetchCategories()
})

// Category Selection
const selectedCategory = ref(item.value.category_id || '')
const selectedCategoryObject = computed(() => 
    categoryStore.items.find(cat => cat.id === selectedCategory.value)
)

// Metadata Keys For Category Selection
watch(selectedCategory, (id) => {
    item.value.category_id = id
    item.value.metadata = {}
})

function updateCategory(e) {
    
}

function handleSubmit() {
    console.log('Submitting:', item.value)

}



</script>

<style scoped>

</style>
