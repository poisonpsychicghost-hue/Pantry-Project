<template>
    <SidebarNav />
    <div class="flex flex-col flex-1">
        <TopAppBar />
        <router-view />
        <FloatingAddButton />
    </div>
    <p> Test</p>
</template>

<script setup>
import SidebarNav from './components/SidebarNav.vue'
import TopAppBar from './components/TopAppBar.vue'
import FloatingAddButton from './components/FloatingAddButton.vue'
</script>

<style scoped>

</style>
