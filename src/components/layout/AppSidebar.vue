<template>
  <div>
    <!-- Mobile Overlay -->
    <div 
      v-if="isMobile && uiStore.sidebarOpen" 
      class="sidebar-overlay" 
      @click="uiStore.toggleSidebar"
    ></div>
    
    <aside 
      class="sidebar" 
      :class="{ 
        'collapsed': uiStore.sidebarCollapsed && !isMobile,
        'mobile-open': isMobile && uiStore.sidebarOpen,
        'mobile-closed': isMobile && !uiStore.sidebarOpen
      }"
    >
      <div class="sidebar-header">
        <div class="logo-container">
          <span class="logo-text logo-text-bold" v-show="!uiStore.sidebarCollapsed || isMobile">LADss</span>
        </div>
        
        <!-- Collapse Toggle Button (Desktop Only) -->
        <button 
          v-if="!isMobile"
          class="collapse-toggle" 
          @click="handleCollapseToggle"
          :title="uiStore.sidebarCollapsed ? 'Expand sidebar' : 'Collapse sidebar'"
        >
          <!-- Collapse icon (arrow left) when sidebar is expanded -->
          <svg v-if="!uiStore.sidebarCollapsed" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 18l-6-6 6-6" />
          </svg>
          <!-- Expand icon (arrow right) when sidebar is collapsed -->
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18l6-6-6-6" />
          </svg>
        </button>
        
        <!-- Mobile Close Button -->
        <button 
          v-if="isMobile"
          class="mobile-close-button" 
          @click="uiStore.toggleSidebar"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- User Profile Section -->
      <div 
        class="user-section" 
        v-show="!uiStore.sidebarCollapsed || isMobile"
        @click="handleUserClick"
        :class="{ 'clickable': isMobile }"
      >
        <div class="user-avatar">
          <img 
            v-if="currentUser.avatar" 
            :src="currentUser.avatar" 
            :alt="currentUser.name"
            class="avatar-image"
          />
          <span v-else>{{ userInitials }}</span>
        </div>
        <div class="user-info">
          <div class="user-name">{{ currentUser.name || 'Rlexandra' }}</div>
          <div class="user-email">{{ currentUser.email || 'rlexandra@gmail.com' }}</div>
        </div>
      </div>

      <!-- Navigation Menu -->
      <nav class="nav-menu">
        <ul class="nav-list main-menu">
          <li class="nav-item" :class="{ active: $route.path === '/' }">
            <router-link to="/" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                <polyline points="9,22 9,12 15,12 15,22" />
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">Home</span>
            </router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.path.includes('/cuppers') }">
            <router-link to="/cuppers" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">Cuppers</span>
            </router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.path.includes('/cupping-sessions') }">
            <router-link to="/cupping-sessions" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z" />
                <circle cx="12" cy="12" r="3" />
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">Cupping sessions</span>
            </router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.path.includes('/samples') }">
            <router-link to="/samples" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2z" />
                <path d="M19 11h-4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2z" />
                <path d="M12 2v9" />
                <path d="M8 7l4-4 4 4" />
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">Samples</span>
            </router-link>
          </li>
        </ul>

        <!-- Divider -->
        <div class="nav-divider"></div>

        <!-- Secondary Menu -->
        <ul class="nav-list">
          <li class="nav-item" :class="{ active: $route.path === '/profile' }">
            <router-link to="/profile" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">My Profile</span>
            </router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.path === '/settings' }">
            <router-link to="/settings" class="nav-link">
              <svg class="nav-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="3"/>
                <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
              </svg>
              <span class="nav-text" v-show="!uiStore.sidebarCollapsed || isMobile">Settings</span>
            </router-link>
          </li>
        </ul>

        
        <!-- Log Out Button at Bottom -->
        <div class="logout-section" v-show="!uiStore.sidebarCollapsed || isMobile">
          <button class="logout-button" @click="handleLogout">
            <svg class="logout-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
              <polyline points="16,17 21,12 16,7" />
              <line x1="21" y1="12" x2="9" y2="12" />
            </svg>
            <span class="logout-text" v-show="!uiStore.sidebarCollapsed || isMobile">Log Out</span>
          </button>
        </div>
      </nav>
    </aside>
  </div>
</template>

<script setup>
import { useUiStore } from '@/stores/ui.store'
import { useAuthStore } from '@/stores/auth.store'
import { useRouter } from 'vue-router'
import { computed, onMounted, onUnmounted, ref } from 'vue'

const uiStore = useUiStore()
const authStore = useAuthStore()
const router = useRouter()

// Use the store's mobile state for consistency
const isMobile = computed(() => uiStore.isMobile)

// Reactive reference for dynamic viewport height
const dynamicHeight = ref('100vh')

// Get current user data
const currentUser = computed(() => authStore.currentUser || {
  name: 'Coffee Cupper',
  email: 'cupper@example.com',
  avatar: null
})

// Calculate user initials
const userInitials = computed(() => {
  const name = currentUser.value.name
  if (!name) return 'R'
  const names = name.split(' ')
  if (names.length === 1) return names[0].charAt(0).toUpperCase()
  return (names[0].charAt(0) + names[names.length - 1].charAt(0)).toUpperCase()
})

// Function to calculate and set dynamic viewport height
const updateViewportHeight = () => {
  // Calculate the actual viewport height
  const vh = window.innerHeight * 0.01
  document.documentElement.style.setProperty('--vh', `${vh}px`)
  
  // Set dynamic height for reactive updates
  dynamicHeight.value = `${window.innerHeight}px`
  
  // For mobile devices, adjust for browser UI
  if (isMobile.value) {
    const mobileVh = window.innerHeight
    document.documentElement.style.setProperty('--mobile-vh', `${mobileVh}px`)
  }
}

// Debounced resize handler to improve performance
let resizeTimeout
const debouncedResize = () => {
  clearTimeout(resizeTimeout)
  resizeTimeout = setTimeout(() => {
    updateViewportHeight()
    uiStore.checkMobile()
  }, 100)
}

// Handle window resize
const handleResize = () => {
  debouncedResize()
}

// Handle orientation change (important for mobile)
const handleOrientationChange = () => {
  // Small delay to allow browser to finish orientation change
  setTimeout(() => {
    updateViewportHeight()
  }, 300)
}

onMounted(() => {
  // Initialize viewport height and mobile state
  updateViewportHeight()
  uiStore.checkMobile()
  
  // Add event listeners
  window.addEventListener('resize', handleResize)
  window.addEventListener('orientationchange', handleOrientationChange)
  
  // Listen for browser UI changes on mobile (iOS Safari specific)
  if (isMobile.value) {
    window.addEventListener('scroll', updateViewportHeight, { passive: true })
    
    // iOS Safari specific: listen for visual viewport changes
    if (window.visualViewport) {
      window.visualViewport.addEventListener('resize', updateViewportHeight)
    }
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('orientationchange', handleOrientationChange)
  
  // Clean up mobile-specific listeners
  if (isMobile.value) {
    window.removeEventListener('scroll', updateViewportHeight)
    
    // iOS Safari specific: remove visual viewport listener
    if (window.visualViewport) {
      window.visualViewport.removeEventListener('resize', updateViewportHeight)
    }
  }
  
  // Clean up timeout
  if (resizeTimeout) {
    clearTimeout(resizeTimeout)
  }
})

// Handle collapse toggle with debugging
const handleCollapseToggle = () => {
  console.log('Collapse button clicked!', { 
    isMobile: isMobile.value, 
    currentState: uiStore.sidebarCollapsed 
  })
  uiStore.toggleSidebarCollapsed()
  console.log('After toggle:', { 
    newState: uiStore.sidebarCollapsed 
  })
}

// Handle user section click (mobile only)
const handleUserClick = () => {
  if (isMobile.value) {
    // Close sidebar first
    uiStore.closeMobileSidebar()
    // Navigate to profile
    router.push('/profile')
  }
}

// Handle logout
const handleLogout = () => {
  // Close mobile sidebar if open
  if (isMobile.value) {
    uiStore.closeMobileSidebar()
  }
  
  // Perform logout
  authStore.logout()
  
  // Navigate to login page
  router.push('/login')
}
</script>

<style scoped>
.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 49;
  /* Use dynamic viewport units for mobile compatibility */
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100); /* Fallback using JS-calculated vh */
  height: 100dvh; /* Dynamic viewport height - fallback for newer browsers */
}

.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  /* Use multiple viewport height strategies for maximum compatibility */
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100); /* Use JS-calculated viewport height */
  height: 100dvh; /* Dynamic viewport height - adjusts for browser UI */
  width: 280px;
  background: var(--md-sys-color-primary);
  color: white;
  padding: var(--spacing-lg) 0;
  transition: width var(--transition-medium), transform var(--transition-medium);
  z-index: 50;
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  
  /* iOS Safari specific fixes */
  -webkit-overflow-scrolling: touch;
  /* Add padding bottom to ensure content is accessible */
  padding-bottom: max(env(safe-area-inset-bottom), var(--spacing-lg));
  /* Ensure content doesn't get cut off by browser UI */
  min-height: -webkit-fill-available;
  min-height: 100vh;
  min-height: calc(var(--vh, 1vh) * 100);
  min-height: 100dvh;
}

.sidebar.collapsed {
  width: 70px;
}

/* Mobile styles */
@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
    width: 280px;
    /* Mobile-specific height adjustments */
    height: 100vh;
    height: calc(var(--mobile-vh, var(--vh, 1vh)) * 1px);
    height: 100dvh;
    min-height: -webkit-fill-available;
    /* Additional padding for iOS Safari bottom bar */
    padding-bottom: calc(max(env(safe-area-inset-bottom), var(--spacing-lg)) + var(--spacing-md));
    
    /* Ensure logout button is always accessible */
    .logout-section {
      margin-bottom: calc(env(safe-area-inset-bottom, 0px) + var(--spacing-md));
    }
  }
  
  .sidebar.mobile-open {
    transform: translateX(0);
  }
  
  .sidebar.mobile-closed {
    transform: translateX(-100%);
  }
  
  /* Additional mobile optimizations */
  .sidebar .nav-menu {
    /* Ensure scrollable area accounts for iOS Safari UI */
    max-height: calc(100vh - 200px);
    max-height: calc(var(--mobile-vh, var(--vh, 1vh)) * 1px - 200px);
    overflow-y: auto;
  }
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
}

.logo-container {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  flex: 1;
}

.logo-icon {
  flex-shrink: 0;
}

.logo-text {
  font-size: var(--md-sys-typescale-title-large-font-size);
  font-weight: var(--md-sys-typescale-title-large-font-weight);
  color: white;
}

.logo-text-bold {
  font-weight: 700; /* Bold */
}

.collapse-toggle, .mobile-close-button {
  width: 40px;
  height: 40px;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-radius: var(--md-sys-shape-corner-small);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color var(--transition-short);
}

.collapse-toggle:hover, .mobile-close-button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.user-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: 0 var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
  padding-bottom: var(--spacing-lg);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.user-section.clickable {
  cursor: pointer;
  transition: background-color var(--transition-short);
  border-radius: var(--md-sys-shape-corner-small);
  margin: 0 var(--spacing-md) var(--spacing-lg);
  padding: var(--spacing-md);
}

.user-section.clickable:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.user-section.clickable:active {
  background-color: rgba(255, 255, 255, 0.15);
}

.user-avatar {
  width: 48px;
  height: 48px;
  border-radius: var(--md-sys-shape-corner-full);
  background: rgba(255, 255, 255, 0.2);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: var(--md-sys-typescale-label-large-font-weight);
  font-size: var(--md-sys-typescale-body-medium-font-size);
  flex-shrink: 0;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-size: var(--md-sys-typescale-body-large-font-size);
  font-weight: var(--md-sys-typescale-body-large-font-weight);
  color: white;
  line-height: 1.2;
}

.user-email {
  font-size: var(--md-sys-typescale-body-small-font-size);
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.2;
  margin-top: 2px;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: var(--md-sys-shape-corner-full);
}

.nav-menu {
  padding: 0 var(--spacing-md);
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.main-menu {
  flex: 1;
}

.nav-item {
  margin-bottom: var(--spacing-xs);
}

.nav-item.active .nav-link {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  border-radius: var(--md-sys-shape-corner-small);
  transition: background-color var(--transition-short), color var(--transition-short);
  font-size: var(--md-sys-typescale-body-medium-font-size);
  font-weight: var(--md-sys-typescale-body-medium-font-weight);
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.nav-text {
  white-space: nowrap;
  overflow: hidden;
}

.nav-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  margin: var(--spacing-lg) 0;
}

/* Log Out Section */
.logout-section {
  margin-top: auto;
  padding: var(--spacing-lg) 0 0 0;
}

.logout-button {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  width: 100%;
  padding: var(--spacing-md);
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: var(--md-sys-shape-corner-small);
  color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
  transition: all var(--transition-short);
  font-size: var(--md-sys-typescale-body-medium-font-size);
  font-weight: var(--md-sys-typescale-body-medium-font-weight);
  text-align: left;
}

.logout-button:hover {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

.logout-button:active {
  background: rgba(255, 255, 255, 0.2);
}

.logout-icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.logout-text {
  flex: 1;
}

/* Collapsed state styles */
.sidebar.collapsed .nav-link {
  justify-content: center;
  padding: var(--spacing-sm);
}

.sidebar.collapsed .user-section {
  justify-content: center;
}

.sidebar.collapsed .sidebar-header {
  justify-content: center;
}

.sidebar.collapsed .collapse-toggle {
  margin-left: var(--spacing-sm);
}

.sidebar.collapsed .logout-button {
  justify-content: center;
  padding: var(--spacing-sm);
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .sidebar {
    width: 280px !important;
  }
  
  .sidebar.collapsed {
    width: 280px !important;
  }
}
</style>
