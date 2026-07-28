<template>
  <div class="flex h-screen">
    <SidebarNav class="w-64" />
    </div>
    <div class="flex-1 flex flex-col">
      <TopAppBar />
      <main class="flex-1 overflow-y-auto">
        <router-view />
        <FloatingAddButton />
      </main>
    </div>

</template>

<script setup>
import SidebarNav from './components/SidebarNav.vue'
import TopAppBar from './components/TopAppBar.vue'
import FloatingAddButton from './components/FloatingAddButton.vue'
</script>

<style scoped>

</style>
