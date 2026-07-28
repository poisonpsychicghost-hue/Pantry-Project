<template>
  <header style="height: 64px; display: flex; align-items: center; justify-content: space-between; background: #000; box-shadow: 0 1px 3px rgba(0,0,0,0.07); padding: 0 1.5rem;">
    <div class="font-bold text-xl" style=" color: #fff">Pantry Manager</div>
    <nav class="flex gap-4">
      <router-link to="/" class="nav-link" exact-active-class="active-link">Home</router-link>
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
