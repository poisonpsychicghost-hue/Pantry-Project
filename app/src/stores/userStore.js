import { defineStore } from 'pinia'
import axios from 'axios'

export const useInventoryLocationStore = defineStore('users', {
    state: () => ({
        items: [],
        loading: false,
        error: null,
    }),
    actions: {
        // Get Full HouseHold Data by ID
        async getFullHouseholdData(id) {
            this.loading = true
            try {
                const response = await axios.get(`/api/household/${id}`)
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Get Household by Id then User by Key
        async getHouseholdUser(id, userKey) {
            const household = await axios.getFullHouseholdData(id)
            const user = household.member.find(u => u.userKey === userKey)
            return user
        },

        // Update Household User Data
        async updateHouseholdUsers(id, updates) {
            this.loading = true 
            try {
                const response = await axios.patch(`/api/household/${id}`, updates)
                this.items = response.data
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },


        // Create Household (for Login/Startup 'create account' feature)
        async createHouseHold(data) {
            this.loading = true
            try {
                const response = await axios.post('/api/household/', data)
                this.error = null
                return response.data
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        },

        // Delete Household (Terminate Account)
        async deleteHousehold(id) {
            this.loading = true
            try {
                const response = await axios.delete(`/api/household/${id}`)
                this.error = null
            } catch (e) {
                this.error = e
            } finally {
                this.loading = false
            }
        }

    }
})