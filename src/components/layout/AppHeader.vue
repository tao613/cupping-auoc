<template>
  <header class="app-header">
    <div class="header-left">
      <!-- Mobile Menu Toggle Button -->
      <div class="mobile-menu-toggle" @click="uiStore.toggleSidebar">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 6h18M3 12h18M3 18h18" />
        </svg>
      </div>
      
      <!-- Search Bar -->
      <div class="search-container">
        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8" />
          <path d="M21 21l-4.35-4.35" />
        </svg>
        <input 
          type="text" 
          placeholder="Search"
          class="search-input"
          v-model="searchQuery"
        />
      </div>
    </div>
    
    <div class="header-right">
      <!-- Language Selector -->
      <div class="icon-button desktop-only" @click="toggleLanguage">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10" />
          <line x1="2" y1="12" x2="22" y2="12" />
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
        </svg>
      </div>
      
      <!-- Notifications -->
      <div class="icon-button desktop-only notification-button" @click="toggleNotifications">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
          <path d="M13.73 21a2 2 0 0 1-3.46 0" />
        </svg>
        <span v-if="notificationCount > 0" class="notification-badge">{{ notificationCount }}</span>
      </div>
      
      <!-- Help -->
      <div class="icon-button desktop-only" @click="openHelp">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10" />
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
          <line x1="12" y1="17" x2="12.01" y2="17" />
        </svg>
      </div>
      
      <!-- User Profile -->
      <div class="user-profile desktop-only" @click="toggleUserMenu">
        <div class="user-info">
          <span class="username">{{ currentUser.name }}</span>
        </div>
        <div class="user-avatar">
          {{ userInitials }}
        </div>
        
        <!-- User Dropdown Menu (Desktop only) -->
        <div class="user-dropdown desktop-only" :class="{ 'show': showUserMenu }">
          <div class="dropdown-item" @click="viewProfile">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
              <circle cx="12" cy="7" r="4" />
            </svg>
            <span>Profile</span>
          </div>
          <div class="dropdown-item" @click="openAccountSettings">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3" />
              <path d="M12 1v6m0 6v6" />
            </svg>
            <span>Account Settings</span>
          </div>
          <div class="dropdown-divider"></div>
          <div class="dropdown-item logout-item" @click="logout">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
              <polyline points="16,17 21,12 16,7" />
              <line x1="21" y1="12" x2="9" y2="12" />
            </svg>
            <span>Logout</span>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUiStore } from '@/stores/ui.store'
import { useAuthStore } from '@/stores/auth.store'

const route = useRoute()
const router = useRouter()
const uiStore = useUiStore()
const authStore = useAuthStore()

// Initialize mobile state on mount and window resize
onMounted(() => {
  uiStore.checkMobile()
  
  // Listen for window resize
  window.addEventListener('resize', uiStore.checkMobile)
})

// Cleanup on unmount
onUnmounted(() => {
  window.removeEventListener('resize', uiStore.checkMobile)
})

const searchQuery = ref('')
const showUserMenu = ref(false)
const notificationCount = ref(3)

// 使用真实的用户数据
const currentUser = computed(() => authStore.currentUser || { name: 'User', email: '' })

const userInitials = computed(() => {
  const user = currentUser.value
  if (!user.name) return 'U'
  const names = user.name.split(' ')
  if (names.length === 1) return names[0].charAt(0).toUpperCase()
  return (names[0].charAt(0) + names[names.length - 1].charAt(0)).toUpperCase()
})

// Methods
const toggleLanguage = () => {
  console.log('Toggle language')
}

const toggleNotifications = () => {
  console.log('Toggle notifications')
}

const openHelp = () => {
  console.log('Open help')
}

const toggleUserMenu = () => {
  // 桌面端显示下拉菜单
  showUserMenu.value = !showUserMenu.value
}

const viewProfile = () => {
  showUserMenu.value = false
  router.push('/profile')
}

const openAccountSettings = () => {
  showUserMenu.value = false
  router.push('/settings')
}

const logout = () => {
  showUserMenu.value = false
  // 使用 auth store 进行登出
  authStore.logout()
  router.push('/login')
}

// Close dropdown when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.user-profile')) {
    showUserMenu.value = false
  }
})
</script>

<style scoped>
.app-header {
  background-color: var(--md-sys-color-surface);
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
  padding: 0 var(--spacing-md);
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 10;
}

.header-left {
  flex: 1;
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  height: 100%;
}

.mobile-menu-toggle {
  width: 48px;
  height: 48px;
  border-radius: var(--md-sys-shape-corner-full);
  display: none;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color var(--transition-short);
  color: var(--md-sys-color-on-surface-variant);
}

.mobile-menu-toggle:hover {
  background-color: var(--md-sys-color-surface-container-highest);
}

.search-container {
  position: relative;
  width: 100%;
  max-width: 300px;
  /* display: flex; */
  align-items: center;
  height: 48px;
  flex: 1;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--md-sys-color-on-surface-variant);
  z-index: 1;
  pointer-events: none;
}

.search-input {
  width: 100%;
  height: 48px;
  padding: 0 16px 0 48px;
  border: 1px solid var(--md-sys-color-outline);
  border-radius: var(--md-sys-shape-corner-full);
  background: var(--md-sys-color-surface);
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-body-large-font-size);
  font-family: var(--md-sys-typescale-font-family);
  line-height: var(--md-sys-typescale-body-large-line-height);
  transition: border-color var(--transition-short);
  box-sizing: border-box;
  vertical-align: middle;
}

.search-input:focus {
  outline: none;
  border-color: var(--md-sys-color-primary);
  border-width: 2px;
  padding-left: 47px;
}

.search-input::placeholder {
  color: var(--md-sys-color-on-surface-variant);
  font-size: var(--md-sys-typescale-body-large-font-size);
  line-height: var(--md-sys-typescale-body-large-line-height);
}

.header-right {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  height: 48px;
}

.icon-button {
  width: 48px;
  height: 48px;
  border-radius: var(--md-sys-shape-corner-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color var(--transition-short);
  color: var(--md-sys-color-on-surface-variant);
  position: relative;
}

.icon-button:hover {
  background-color: var(--md-sys-color-surface-container-highest);
}

.notification-button {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  background: var(--md-sys-color-error);
  color: var(--md-sys-color-on-error);
  border-radius: var(--md-sys-shape-corner-full);
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: var(--md-sys-typescale-label-small-font-weight);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  cursor: pointer;
  padding: var(--spacing-xs);
  border-radius: var(--md-sys-shape-corner-small);
  transition: background-color var(--transition-short);
  position: relative;
  height: 48px;
}

.user-profile:hover {
  background-color: var(--md-sys-color-surface-container-highest);
}

.user-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  height: 48px;
}

.username {
  font-size: var(--md-sys-typescale-body-medium-font-size);
  font-weight: var(--md-sys-typescale-body-medium-font-weight);
  color: var(--md-sys-color-on-surface);
  line-height: var(--md-sys-typescale-body-medium-line-height);
  margin: 0;
  padding: 0;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--md-sys-shape-corner-full);
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: var(--md-sys-typescale-label-large-font-weight);
  font-size: var(--md-sys-typescale-label-medium-font-size);
}

.user-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: var(--spacing-xs);
  background: var(--md-sys-color-surface-container);
  border-radius: var(--md-sys-shape-corner-small);
  box-shadow: var(--md-sys-elevation-level-2);
  min-width: 200px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: opacity var(--transition-short), transform var(--transition-short), visibility var(--transition-short);
  z-index: 1000;
}

.user-dropdown.show {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  color: var(--md-sys-color-on-surface);
  cursor: pointer;
  transition: background-color var(--transition-short);
}

.dropdown-item:hover {
  background-color: rgba(var(--md-sys-color-primary-rgb), 0.08);
}

.dropdown-item svg {
  color: var(--md-sys-color-on-surface-variant);
}

.dropdown-divider {
  height: 1px;
  background: var(--md-sys-color-outline-variant);
  margin: var(--spacing-xs) 0;
}

.logout-item {
  color: var(--md-sys-color-error);
}

.logout-item svg {
  color: var(--md-sys-color-error);
}

/* Mobile Styles */
@media (max-width: 768px) {
  .mobile-menu-toggle {
    display: flex;
  }
  
  .search-container {
    max-width: none;
    flex: 1;
    margin-right: var(--spacing-sm);
  }
  
  .desktop-only {
    display: none;
  }
  
  .header-left {
    max-width: none;
  }
  
  .header-right {
    gap: 0;
  }
}

/* Tablet Styles */
@media (max-width: 992px) and (min-width: 769px) {
  .user-info {
    display: none;
  }
  
  .user-profile {
    padding: var(--spacing-xs) var(--spacing-sm);
  }
}
</style>
