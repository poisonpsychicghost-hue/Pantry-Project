import { defineStore } from 'pinia'
import axios from 'axios'

export const useInventoryStore = defineStore('inventory', {
    state: () => ({
        items: [],
        loading: false,
        error: null,
    }),
    actions: {

        // Fetch all Inventory Items From Backend API
        async fetchInventory() {
            this.loading = true
            try {
                const response = await axios.get('/api/fooditems')
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Add Item to Inventory
        async addItem(item) {
            try {
                const response = await axios.post('/api/fooditems', item)
                this.item.push(response.data)
            } catch (e) {
                this.error = e
            }
        },

        // Update an Inventory Item 
        async updateItem(id, updates) {
            try {
                const response = await axios.patch(`/api/fooditems/${id}`, updates)
                const idx = this.items.findIndex(i => i.id === id)
                if (idx !== -1) this.items[idx] = response.data
                this.error = null
            } catch (e) {
                this.error = e
            }
        },

        // Delete an Item by ID
        async deleteItem(id) {
            try {
                await axios.delete(`/api/fooditems/${id}`)
                this.items = this.items.filter(i => i.id !== id)
                this.error = null
            } catch (e) {
                this.error = e
            }
        },

        // Get Item By Name
        async fetchByName(name) {
            this.loading = true
            try {
                const response = await axios.get('/api/fooditems/search/', {params: { name }})
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Get Items By Status
        async fetchByStatus(status) {
            this.loading = true
            try {
                const response = await axios.get('/api/fooditems/search/', {params: { status }})
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        }

    },
})
