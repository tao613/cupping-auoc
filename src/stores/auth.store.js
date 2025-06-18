import { defineStore } from 'pinia'
import { authService } from '@/services/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    loading: false,
    error: null,
    initialized: false
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.token,
    currentUser: (state) => state.user
  },
  
  actions: {
    // 初始化认证状态
    async initialize() {
      if (this.initialized) return
      
      this.initialized = true
      
      if (this.token) {
        try {
          // 验证token并获取用户信息
          await this.refreshUserInfo()
        } catch (error) {
          // token无效，清理状态
          this.logout()
        }
      }
    },
    
    async login(credentials) {
      this.loading = true
      this.error = null
      
      try {
        // 调用真实API进行登录
        const response = await authService.login(credentials.email || credentials.username, credentials.password)
        
        // 存储token
        this.token = response.access_token
        localStorage.setItem('token', response.access_token)
        
        // 获取用户信息
        const userInfo = await authService.getCurrentUser()
        this.user = userInfo
        localStorage.setItem('user', JSON.stringify(userInfo))
        
        return response
      } catch (error) {
        this.error = error.response?.data?.detail || error.message || 'Login failed'
        this.logout() // 清理状态
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async register(userData) {
      this.loading = true
      this.error = null
      
      try {
        // 调用真实API进行注册
        const response = await authService.register(userData)
        
        // 注册成功后，不自动登录，让用户手动登录
        return response
      } catch (error) {
        this.error = error.response?.data?.detail || error.message || 'Registration failed'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    async logout() {
      // 清理前端状态
      this.token = null
      this.user = null
      this.error = null
      
      // 清理localStorage
      authService.logout()
    },
    
    async refreshUserInfo() {
      if (!this.token) return
      
      try {
        const userInfo = await authService.getCurrentUser()
        this.user = userInfo
        localStorage.setItem('user', JSON.stringify(userInfo))
      } catch (error) {
        // 如果获取用户信息失败，可能token已过期
        console.error('Failed to refresh user info:', error)
        this.logout()
        throw error
      }
    },
    
    // 更新用户资料
    async updateProfile(profileData) {
      this.loading = true
      this.error = null
      
      try {
        const updatedUser = await authService.updateProfile(profileData)
        this.user = updatedUser
        localStorage.setItem('user', JSON.stringify(updatedUser))
        return updatedUser
      } catch (error) {
        this.error = error.response?.data?.detail || error.message || 'Profile update failed'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    // 修改密码
    async changePassword(passwordData) {
      this.loading = true
      this.error = null
      
      try {
        await authService.changePassword(passwordData)
        return true
      } catch (error) {
        this.error = error.response?.data?.detail || error.message || 'Password change failed'
        throw error
      } finally {
        this.loading = false
      }
    },
    
    // 检查token是否有效
    async validateToken() {
      if (!this.token) return false
      
      try {
        await authService.getCurrentUser()
        return true
      } catch (error) {
        this.logout()
        return false
      }
    },
    
    // 清除错误状态
    clearError() {
      this.error = null
    }
  }
})
