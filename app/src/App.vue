<template>
  <div class="relative min-h-screen flex flex-col">
    <TopAppBar @hamburger="openSidebar" />

    <Transition
      enter-active-class="transition duration-150 ease-out"
      enter-from-class="opacity-0 -translate-x-4"
      enter-to-class="opacity-100 translate-x-0"
      leave-active-class="transition duration-100 ease-in"
      leave-from-class="opacity-100 translate-x-0"
      leave-to-class="opacity-0 -translate-x-4"
    >
      <SidebarNav
        v-if="sidebarOpen"
        class="fixed top-0 left-0 h-full z-50"
        @close="closeSidebar"
      />
    </Transition>

    <Transition
      enter-active-class="transition duration-150 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-100 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="sidebarOpen"
        class="fixed inset-0 bg-black/60 z-40"
        @click="closeSidebar"
      ></div>
    </Transition>

    <main class="flex-1 overflow-y-auto bg-gray-100 p-6">
      <router-view />

    </main>

    <footer class="text-center p-4 bg-gray-200">
      Sirius Studios 2026 – Dev Credits
    </footer>
  </div>
</template>

<script setup>
import SidebarNav from './components/SidebarNav.vue'
import TopAppBar from './components/TopAppBar.vue'
import FloatingAddButton from './components/FloatingAddButton.vue'
import { ref, onMounted, onBeforeUnmount } from 'vue'

const sidebarOpen = ref(false)
const windowWidth = ref(window.innerWidth)

function updateWidth() {
  windowWidth.value = window.innerWidth
}
function openSidebar() {
  sidebarOpen.value = true
}
function closeSidebar() {
  sidebarOpen.value = false
}

onMounted(() => {
  window.addEventListener('resize', updateWidth)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWidth)
})
</script>

<style scoped>
</style>