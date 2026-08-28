<template>
  <header style="height: 64px; display: flex; align-items: center; justify-content: space-between; background: #000; box-shadow: 0 1px 3px rgba(0,0,0,0.07); padding: 0 1.5rem;">
    <button
      class="p-2 md:hidden" 
      @click="$emit('hamburger')"
      aria-label="Toggle Sidebar"
      >
      <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" >
        <path d="M4 6h18M4 13h18m4 20h18" />
      </svg>
    </button>
    <div class="font-bold text-xl" style=" color: #fff">Pantry Manager</div>
    <nav class="flex gap-4">
      <!--Navigation-->
      <router-link to="/" class="nav-link" exact-active-class="active-link">Home</router-link>
      <router-link to="/inventory" class="nav-link" active-class="active-link">Inventory</router-link>
      <router-link to="/shopping-list" class="nav-link" active-class="active-link">Shop-List</router-link>
      <router-link to="/bulk-add" class="nav-link" active-class="active-link">Bulk Add</router-link>
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
