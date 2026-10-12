import { defineStore } from 'pinia'
import axios from 'axios'

export const useShoppingStore = defineStore('shoppinglist', {
  state: () => ({
    items: [],
    loading: false,
    error: null,
  }),
  actions: {
    // Fetch all Shopping Items
    async fetchShopping() {
      this.loading = true
      try {
        const response = await axios.get('/api/shoppingitems/shoppingitems/')
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
        const response = await axios.post('/api/shoppingitems/shoppingitems/', item)
        this.items.push(response.data)
        this.error = null
      } catch (e) {
        this.error = e
      }
    },

    // Get single Shopping Item by id
    async fetchById(id) {
      this.loading = true
      try {
        const response = await axios.get(`/api/shoppingitems/shoppingitems/${id}`)
        this.error = null
        return response.data
      } catch (e) {
        this.error = e
        throw e
      } finally {
        this.loading = false
      }
    },

    // Update a Shopping Item 
    async updateItem(id, updates) {
      try {
        const response = await axios.patch(`/api/shoppingitems/shoppingitems/${id}`, updates)
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
        await axios.delete(`/api/shoppingitems/shoppingitems/${id}`)
        this.items = this.items.filter(i => i.id !== id)
        this.error = null
      } catch (e) {
        this.error = e
      }
    },

    // Get Shopping Item(s) By Name
    async fetchByName(name) {
      this.loading = true
      try {
        const response = await axios.get('/api/shoppingitems/shoppingitems/search/', {
          params: { name },
        })
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