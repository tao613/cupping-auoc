<template>
  <div class="app-layout" :class="{ 
    'sidebar-collapsed': uiStore.sidebarCollapsed && !uiStore.isMobile,
    'mobile-sidebar-open': uiStore.isMobile && uiStore.sidebarOpen
  }">
    <AppSidebar />
    <div class="main-content">
      <AppHeader />
      <main>
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import { useUiStore } from '@/stores/ui.store'
import AppSidebar from './AppSidebar.vue'
import AppHeader from './AppHeader.vue'
import { onMounted, onUnmounted } from 'vue'

const uiStore = useUiStore()

// Handle window resize
const handleResize = () => {
  uiStore.checkMobile()
}

onMounted(() => {
  // Initialize mobile state
  uiStore.checkMobile()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})
</script>

<style scoped>
.app-layout {
  display: flex;
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100); /* Use JS-calculated viewport height */
  height: 100dvh; /* Dynamic viewport height for newer browsers */
  overflow: hidden;
  /* Mobile viewport optimization */
  min-height: -webkit-fill-available;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-left: 280px; /* Default sidebar width */
  transition: margin-left var(--transition-medium);
  /* Ensure proper height on mobile */
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100);
  height: 100dvh;
  min-height: -webkit-fill-available;
}

/* Desktop collapsed state */
.app-layout.sidebar-collapsed .main-content {
  margin-left: 70px;
}

/* Mobile styles */
@media (max-width: 768px) {
  .app-layout {
    /* Mobile-specific height adjustments */
    height: 100vh;
    height: calc(var(--mobile-vh, var(--vh, 1vh)) * 1px);
    height: 100dvh;
  }
  
  .main-content {
    margin-left: 0; /* No margin on mobile */
    /* Mobile viewport height */
    height: 100vh;
    height: calc(var(--mobile-vh, var(--vh, 1vh)) * 1px);
    height: 100dvh;
  }
  
  .app-layout.sidebar-collapsed .main-content {
    margin-left: 0; /* Override collapsed margin on mobile */
  }
  
  .app-layout.mobile-sidebar-open .main-content {
    margin-left: 0; /* Keep main content in place on mobile */
  }
}

main {
  flex: 1;
  overflow-y: auto;
  padding: var(--spacing-lg);
  background: var(--md-sys-color-background);
  /* Mobile optimization */
  -webkit-overflow-scrolling: touch;
  
  /* Ensure proper spacing on mobile */
  @media (max-width: 768px) {
    padding-bottom: calc(var(--spacing-lg) + env(safe-area-inset-bottom, 0px));
  }
}
</style>
