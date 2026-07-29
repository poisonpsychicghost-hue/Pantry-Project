import { defineStore } from 'pinia'
import axios from 'axios'

export const useShoppingStore = defineStore('shoppinglist', {
    state: () => ({
        items: [],
        loading: false,
        error: null,
    }),
    actions: {

        // Fetch all Shopping Items From Backend API
        async fetchShopping() {
            this.loading = true
            try {
                const response = await axios.get('/api/shoppingitems')
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Add Item to Shopping List
        async addItem(item) {
            try {
                const response = await axios.post('/api/shoppingitems', item)
                this.item.push(response.data)
            } catch (e) {
                this.error = e
            }
        },

        // Update a Shopping Item 
        async updateItem(id, updates) {
            try {
                const response = await axios.patch(`/api/shoppingitems/${id}`, updates)
                const idx = this.items.findIndex(i => i.id === id)
                if (idx !== -1) this.items[idx] = response.data
                this.error = null
            } catch (e) {
                this.error = e
            }
        },

        // Delete a Shopping Item by ID
        async deleteItem(id) {
            try {
                await axios.delete(`/api/shoppingitems/${id}`)
                this.items = this.items.filter(i => i.id !== id)
                this.error = null
            } catch (e) {
                this.error = e
            }
        },

        // Get Shopping Item By Name
        async fetchByName(name) {
            this.loading = true
            try {
                const response = await axios.get('/api/shoppingitems/search/', {params: { name }})
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },
    },
})
