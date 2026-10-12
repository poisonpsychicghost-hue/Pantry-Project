<script setup>
const props = defineProps({
    item: {
        type: Object,
        required: true,
    },
})

</script>

<template>
    <article class="shopping-item-card">
        <header>
            <h2>{{ item.name }}</h2>
            <span v-if="item.completed_at" class="status done">{{ item.completed_at }}</span>
        </header>
        <div class="meta">
            <div v-if="item.requested_by">
                <strong>Requested By:</strong>
                {{ item.requested_by }}
            </div>
            <div>
                <strong>{{ item.date_added }}</strong>
            </div>
            <div v-if="item.date_needed">
                {{ item.date_needed }}
            </div>
            <div v-if="item.fooditem_id">
                <strong>linked Pantry Id:</strong>
                {{ item.fooditem_id }}
            </div>
        </div>
        <p v-if="item-notes" class="notes">
            {{ item.notes }}
        </p>
    </article>
</template>

<style scoped>
.shopping-item-card {
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
.status.done {
    color: #1a7f37;
}
.status.pending {
    color: #b35a00;
}
.meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 0.25rem 1rem;
    margin-top: 0.5rem;
}
.notes {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #555;
}

</style>
