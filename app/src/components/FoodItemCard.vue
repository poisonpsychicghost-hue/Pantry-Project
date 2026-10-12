<script setup>
const props = defineProps({
    item: {
        type: Object,
        required: true,
    },
})

</script>

<template>
    <article class="food-item-card">
        <header>
            <h2>{{ item.name }}</h2>
            <span class="status">{{ item.status }}</span>
        </header>
        <div class="meta">
            <div>
                <strong>quantity:</strong>
                {{ item.quantity }} {{ item.unit }}
            </div>
            <strong>category:</strong>
            {{ item.category_id }}
        </div>
        <div>
            <strong>location:</strong>
            {{ item.location_id }}
        </div>
        <div>
            <strong>expires:</strong>
            {{ item.expiration_date }}
        </div>
        <p v-if="item.notes" class="notes">
            {{ item.notes }}
        </p>
    </article>
</template>

<style scoped>
.food-item-card {
    border: 1px solid #ccc;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    margin-bottom: 0.5rem;
}
header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.status {
    font-size: 0.8rem;
    text-transform: uppercase;
}
.meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.25rem 1rem;
    margin-top: 0.5rem;
}
.notes {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #555;
}

</style>
