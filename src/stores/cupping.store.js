import { defineStore } from 'pinia'

export const useCuppingStore = defineStore('cupping', {
  state: () => ({
    sessions: [],
    currentSession: null,
    loading: false,
    error: null,
    pagination: {
      page: 1,
      limit: 10,
      total: 0
    }
  }),
  
  getters: {
    getSessionById: (state) => (id) => {
      return state.sessions.find(session => session.id === id)
    }
  },
  
  actions: {
    async fetchSessions(params = {}) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟获取品鉴会话列表
        const response = {
          data: [],
          pagination: {
            page: params.page || 1,
            limit: params.limit || 10,
            total: 0
          }
        }
        
        this.sessions = response.data
        this.pagination = response.pagination
        return response
      } catch (error) {
        this.error = error.message || 'Failed to fetch cupping sessions'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async fetchSessionById(id) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟获取单个品鉴会话
        const session = this.sessions.find(s => s.id === id) || null
        
        this.currentSession = session
        return session
      } catch (error) {
        this.error = error.message || 'Failed to fetch cupping session'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async createSession(sessionData) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟创建品鉴会话
        const newSession = {
          id: Date.now(),
          ...sessionData,
          createdAt: new Date().toISOString(),
          status: 'pending'
        }
        
        this.sessions.unshift(newSession)
        this.pagination.total++
        return newSession
      } catch (error) {
        this.error = error.message || 'Failed to create cupping session'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async updateSession(id, sessionData) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟更新品鉴会话
        const index = this.sessions.findIndex(s => s.id === id)
        
        if (index !== -1) {
          const updatedSession = {
            ...this.sessions[index],
            ...sessionData,
            updatedAt: new Date().toISOString()
          }
          
          this.sessions[index] = updatedSession
          
          if (this.currentSession && this.currentSession.id === id) {
            this.currentSession = updatedSession
          }
          
          return updatedSession
        }
        
        throw new Error('Cupping session not found')
      } catch (error) {
        this.error = error.message || 'Failed to update cupping session'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async deleteSession(id) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟删除品鉴会话
        const index = this.sessions.findIndex(s => s.id === id)
        
        if (index !== -1) {
          this.sessions.splice(index, 1)
          this.pagination.total--
          
          if (this.currentSession && this.currentSession.id === id) {
            this.currentSession = null
          }
          
          return true
        }
        
        throw new Error('Cupping session not found')
      } catch (error) {
        this.error = error.message || 'Failed to delete cupping session'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async inviteCuppers(sessionId, cupperIds) {
      this.loading = true
      this.error = null
      
      try {
        // 在实际应用中，这里会调用API
        // 模拟邀请品鉴师
        const session = this.sessions.find(s => s.id === sessionId)
        
        if (!session) {
          throw new Error('Cupping session not found')
        }
        
        // 更新会话中的品鉴师列表
        const updatedSession = {
          ...session,
          cuppers: [...(session.cuppers || []), ...cupperIds],
          updatedAt: new Date().toISOString()
        }
        
        const index = this.sessions.findIndex(s => s.id === sessionId)
        this.sessions[index] = updatedSession
        
        if (this.currentSession && this.currentSession.id === sessionId) {
          this.currentSession = updatedSession
        }
        
        return updatedSession
      } catch (error) {
        this.error = error.message || 'Failed to invite cuppers'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})
