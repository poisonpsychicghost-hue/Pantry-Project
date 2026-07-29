import { defineStore } from 'pinia'
import axios from 'axios'

export const useSettingStore = defineStore('settings', {
    state: () => ({
        items: [],
        loading: false,
        error: null,
    }),
    actions: {

        // Get Settings from Household ID
        async getSettings(id) {
            this.loading = true
            try {
                const response = await axios.get(`/api/household/${id}`)
                this.settings = response.data.settings
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Update Settings with Household ID
        async updateSettings(id, updates) {
            this.loading = true
            try {
                const response = await axios.patch(`/api/households/${id}`, updates)
                this.settings = response.data.settings
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        }
    }
})