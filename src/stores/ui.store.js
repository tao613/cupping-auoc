import { defineStore } from 'pinia'

export const useUiStore = defineStore('ui', {
  state: () => ({
    sidebarCollapsed: false, // Desktop collapsed state
    sidebarOpen: false,      // Mobile open state
    isMobile: false,
    darkMode: false,
    notifications: [],
    loading: {
      global: false,
      components: {}
    }
  }),
  
  actions: {
    // Desktop sidebar collapse toggle
    toggleSidebarCollapsed() {
      this.sidebarCollapsed = !this.sidebarCollapsed
    },
    
    // Mobile sidebar open/close toggle
    toggleSidebar() {
      if (this.isMobile) {
        this.sidebarOpen = !this.sidebarOpen
      } else {
        this.sidebarCollapsed = !this.sidebarCollapsed
      }
    },
    
    // Check if mobile and update state
    checkMobile() {
      if (typeof window !== 'undefined') {
        const isMobile = window.innerWidth <= 768
        console.log('Checking mobile state:', { 
          windowWidth: window.innerWidth, 
          isMobile: isMobile,
          oldMobileState: this.isMobile 
        })
        this.isMobile = isMobile
        
        // Close mobile sidebar when switching to desktop
        if (!isMobile) {
          this.sidebarOpen = false
        }
      }
    },
    
    // Close mobile sidebar
    closeMobileSidebar() {
      if (this.isMobile) {
        this.sidebarOpen = false
      }
    },
    
    toggleDarkMode() {
      this.darkMode = !this.darkMode
      document.documentElement.classList.toggle('dark', this.darkMode)
    },
    
    addNotification(notification) {
      const id = Date.now()
      this.notifications.push({
        id,
        ...notification
      })
      
      // 自动移除通知
      if (notification.autoClose !== false) {
        setTimeout(() => {
          this.removeNotification(id)
        }, notification.duration || 3000)
      }
      
      return id
    },
    
    removeNotification(id) {
      this.notifications = this.notifications.filter(n => n.id !== id)
    },
    
    setLoading(component, status) {
      if (component === 'global') {
        this.loading.global = status
      } else {
        this.loading.components[component] = status
      }
    }
  }
})
