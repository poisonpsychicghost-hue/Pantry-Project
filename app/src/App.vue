<template>
  <div style="display: flex; height: 100vh;">
    <SidebarNav style="width: 250px; background: #222; color: #fff;" />
    <div style="flex: 1; display: flex; flex-direction: column;">
      <TopAppBar />
      <main style="flex: 1; overflow: auto; background: #f9fafb; padding: 24px;">
        <router-view />
        <EntryField />
      </main>
    </div>
  </div>
</template>

<script setup>
import SidebarNav from './components/SidebarNav.vue'
import TopAppBar from './components/TopAppBar.vue'
import FloatingAddButton from './components/FloatingAddButton.vue'
import EntryField from './components/EntryField.vue';
</script>

<style scoped>

</style>
