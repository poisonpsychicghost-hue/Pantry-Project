import { defineStore } from 'pinia'
import axios from 'axios'

export const useInventoryLocationStore = defineStore('locations', {
    state: () => ({
        items: [],
        loading: false,
        error: null,
    }),
    actions: {

        // Fetch All Inventory Locations
        async fetchLocations() {
            this.loading = true
            try {
                const response = await axios.get('/api/inventorylocations')
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },
        
        //Add User Created Locations
        async createLocation(location) {
            try {
                const response = await axios.create('/api/inventorylocations', location)
                this.items.push(response.data)
            } catch (e) {
                this.error = e
            }
        },

        // Update User Created Locations
        async updateLocation(id, updates) {
            try {
                const response = await axios.patch(`/api/inventorylocations/${id}`, updates)
                const idx = this.items.findIndex(i => i.id === id)
                if (idx !== -1) this.items[idx] = response.data
                this.err = null
            } catch (e) {
                this.error = e
            }
        },

        // Get a Location by ID
        async getLocation(id) {
            this.loading = true
            try {
                const response = await axios.get(`/api/inventorylocations/${id}`)
                this.item = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Delete an User Created Location
        async deleteLocation(id) {
            try {
                const response = await axios.delete(`/api/inventoryloactions/${id}`)
                this.items = this.items.filter(i => i.id !== id)
                this.error = null
            } catch (e) {
                this.error = e
            }
        }
    }
})
