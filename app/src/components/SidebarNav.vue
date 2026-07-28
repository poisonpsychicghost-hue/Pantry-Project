<template>
    <nav class="flex flex-col gap-6 p-4 bg-gray-800 h-full text-white">
        <!--NAVIGATION HERE-->
        <router-link to="/" class="nav-link" active-class="active-link">Home</router-link>
        <router-link to="/inventory" class="nav-link" active-class="active-link">Inventory</router-link>
        <router-link to="/shopping-list" class="nav-link" active-class="active-link">Shopping List</router-link>
        <router-link to="/expiration" class="nav-link" active-class="active-link">Expiration</router-link>
        <router-link to="/analytics" class="nav-link" active-class="active-link">Analytics</router-link>
        <router-link to="/settings" class="nav-link" active-class="active-link">Settings</router-link>
        <router-link to="/startup" class="nav-link" active-class="active-link">Login/Startup</router-link>
        <router-link to="/bulk-add" class="nav-link" active-class="active-link">Bulk Add</router-link>
    </nav>
</template>

<script setup>
// Compostables
</script>

<style scoped>
.nav-link {
    padding: 0.75rem 1rem;
    border-radius: 0.375rem;
    transition: all 0.1s;
    text-decoration: none;
    color: #fff;
}
.nav-link.hover,
.active-link {
    background-color: #2563eb;
    color: #fff;
}
</style>
