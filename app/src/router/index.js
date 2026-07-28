import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Inventory from '../pages/Inventory.vue'
import PantryItemDetail from '../pages/PantryItemDetail.vue'
import ShoppingList from '../pages/ShoppingList.vue'
import ShoppingItemDetail from '../pages/ShoppingItemDetail.vue'
import Expiration from '../pages/Expiration.vue'
import Analytics from '../pages/Analytics.vue'
import Settings from '../pages/Settings.vue'
import StartupLogin from '../pages/StartupLogin.vue'
import BulkAdd from '../pages/BulkAdd.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/inventory', name: 'Inventory', component: Inventory },
    { path: '/pantry-item', name: 'PantryItemDetail', component: PantryItemDetail },
    { path: '/shopping-list', name: 'ShoppingList', component: ShoppingList },
    { path: '/shopping-item', name: 'ShoppingItemDetail', component: ShoppingItemDetail },
    { path: '/expiration', name: 'Expiration', component: Expiration },
    { path: '/analytics', name: 'Analytics', component: Analytics },
    { path: '/settings', name: 'Settings', component: Settings },
    { path: '/login', name: 'StartupLogin', component: StartupLogin },
    { path: '/bulk-add', name: 'BulkAdd', component: BulkAdd },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
