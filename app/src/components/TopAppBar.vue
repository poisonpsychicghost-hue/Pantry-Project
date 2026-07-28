<template>
  <header class="h-16 flex items-center px-6 bg-white shadow">
    <div class="font-bold text-xl">Pantry Manager</div>
    <nav class="flex gap-4">
      <router-link to="/" class="nav-link" active-class="active-link">Home</router-link>
      <router-link to="/settings" class="nav-link" active-class="active-link">Settings</router-link>
    </nav>
  </header>
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
