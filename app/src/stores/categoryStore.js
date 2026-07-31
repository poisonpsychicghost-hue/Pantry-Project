import { defineStore } from 'pinia'
import axios from 'axios'

export const useCategoryStore = defineStore('categories',{
    state: () => ({
        items: [],
        loading: false,
        error: null
    }),
    actions:{

        async fetchCategories() {
            this.loading = true
            try {
                const response = await axios.get('/api/categories/')
                console.log("Response:", response.data)
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        async getCategory(id) {
            this.loading = true
            try {
                const response = await axios.get(`/api/categories/${id}`)
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        }
    }
})
