import { defineStore } from 'pinia'

export const useCuppersStore = defineStore('cuppers', {
  state: () => ({
    cuppers: [],
    stats: {
      members: 0,
      admins: 0,
      pendingInvites: 0,
      seatsAvailable: 0
    },
    loading: false,
    error: null,
    pagination: {
      page: 1,
      limit: 10,
      total: 0
    }
  }),
  
  getters: {
    getCupperById: (state) => (id) => {
      return state.cuppers.find(cupper => cupper.id === id)
    }
  },
  
  actions: {
    async fetchCuppers(params = {}) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟获取品鉴师列表
        const response = {
          data: [],
          pagination: {
            page: params.page || 1,
            limit: params.limit || 10,
            total: 0
          }
        }
        
        this.cuppers = response.data
        this.pagination = response.pagination
        return response
      } catch (error) {
        this.error = error.message || 'Failed to fetch cuppers'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async fetchCupperStats() {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟获取品鉴师统计数据
        const stats = {
          members: 1,
          admins: 1,
          pendingInvites: 0,
          seatsAvailable: 1
        }
        
        this.stats = stats
        return stats
      } catch (error) {
        this.error = error.message || 'Failed to fetch cupper stats'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async inviteCupper(email) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟邀请品鉴师
        const newInvite = {
          id: Date.now(),
          email,
          status: 'pending',
          createdAt: new Date().toISOString()
        }
        
        this.stats.pendingInvites++
        return newInvite
      } catch (error) {
        this.error = error.message || 'Failed to invite cupper'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async updateCupperPermissions(cupperId, permissions) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟更新品鉴师权限
        const index = this.cuppers.findIndex(c => c.id === cupperId)
        
        if (index !== -1) {
          const updatedCupper = {
            ...this.cuppers[index],
            ...permissions,
            updatedAt: new Date().toISOString()
          }
          
          this.cuppers[index] = updatedCupper
          
          // 更新管理员统计
          if (permissions.isAdmin !== undefined) {
            if (permissions.isAdmin && !this.cuppers[index].isAdmin) {
              this.stats.admins++
            } else if (!permissions.isAdmin && this.cuppers[index].isAdmin) {
              this.stats.admins--
            }
          }
          
          return updatedCupper
        }
        
        throw new Error('Cupper not found')
      } catch (error) {
        this.error = error.message || 'Failed to update cupper permissions'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})
