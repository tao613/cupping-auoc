<template>
  <div class="mobile-profile-view">
    <!-- Header with back button -->
    <div class="profile-header">
      <button class="back-button" @click="goBack">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
      </button>
      <h1 class="page-title">Profile</h1>
    </div>

    <!-- User Avatar and Info -->
    <div class="user-section">
      <div class="user-avatar">
        <img 
          v-if="user.avatar" 
          :src="user.avatar" 
          :alt="user.name"
          class="avatar-image"
        />
        <div v-else class="avatar-placeholder">
          {{ userInitials }}
        </div>
      </div>
      <h2 class="user-name">{{ user.name || 'Annabelle Sanderts' }}</h2>
      <p class="user-position">{{ user.position || 'HEAD OF MARKETING' }}</p>
    </div>

    <!-- Portfolio Section -->
    <div class="portfolio-section">
      <div class="portfolio-item" v-for="asset in portfolio" :key="asset.name">
        <div class="asset-info">
          <span class="asset-name">{{ asset.name }}</span>
          <span class="asset-change" :class="{ 
            'positive': asset.change > 0, 
            'negative': asset.change < 0 
          }">
            {{ asset.change > 0 ? '+' : '' }}{{ asset.change.toFixed(2) }}%
          </span>
        </div>
      </div>
    </div>

    <!-- Stats Section -->
    <div class="stats-section">
      <div class="stat-item">
        <div class="stat-number">{{ stats.followers }}</div>
        <div class="stat-label">FOLLOWERS</div>
      </div>
      <div class="stat-item">
        <div class="stat-number">{{ stats.fundsEth }}</div>
        <div class="stat-label">FUNDS (ETH)</div>
      </div>
      <div class="stat-item">
        <div class="stat-number">{{ stats.profit }}</div>
        <div class="stat-label">PROFIT (%)</div>
      </div>
    </div>

    <!-- Settings Option -->
    <div class="settings-section">
      <div class="settings-item" @click="goToSettings">
        <span>Settings</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 18l6-6-6-6"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'

const router = useRouter()
const authStore = useAuthStore()

// User data
const user = computed(() => authStore.currentUser || {
  name: 'Annabelle Sanderts',
  position: 'HEAD OF MARKETING',
  avatar: null
})

const userInitials = computed(() => {
  const name = user.value.name
  if (!name) return 'AS'
  const names = name.split(' ')
  if (names.length === 1) return names[0].charAt(0).toUpperCase()
  return (names[0].charAt(0) + names[names.length - 1].charAt(0)).toUpperCase()
})

// Portfolio data
const portfolio = ref([
  { name: 'US Dollars', change: -0.24 },
  { name: 'Bitcoin', change: -2.28 },
  { name: 'Ethereum', change: 4.01 },
  { name: 'Ripple', change: -0.82 }
])

// Stats data
const stats = ref({
  followers: '12k',
  fundsEth: '98',
  profit: '20'
})

// Methods
const goBack = () => {
  router.go(-1)
}

const goToSettings = () => {
  router.push('/settings')
}
</script>

<style scoped>
.mobile-profile-view {
  min-height: 100vh;
  background: var(--md-sys-color-surface);
  padding: 0 var(--spacing-lg);
}

.profile-header {
  display: flex;
  align-items: center;
  padding: var(--spacing-lg) 0 var(--spacing-md) 0;
  gap: var(--spacing-md);
}

.back-button {
  width: 40px;
  height: 40px;
  border: none;
  background: none;
  border-radius: var(--md-sys-shape-corner-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--md-sys-color-on-surface);
  transition: background-color var(--transition-short);
}

.back-button:hover {
  background-color: var(--md-sys-color-surface-container);
}

.page-title {
  font-size: var(--md-sys-typescale-headline-medium-font-size);
  font-weight: var(--md-sys-typescale-headline-medium-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0;
}

.user-section {
  text-align: center;
  padding: var(--spacing-xl) 0;
}

.user-avatar {
  width: 120px;
  height: 120px;
  margin: 0 auto var(--spacing-md);
  border-radius: var(--md-sys-shape-corner-full);
  overflow: hidden;
  background: var(--md-sys-color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  font-size: 48px;
  font-weight: var(--md-sys-typescale-display-medium-font-weight);
  color: var(--md-sys-color-on-primary);
}

.user-name {
  font-size: var(--md-sys-typescale-headline-small-font-size);
  font-weight: var(--md-sys-typescale-headline-small-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0 0 var(--spacing-xs) 0;
}

.user-position {
  font-size: var(--md-sys-typescale-body-medium-font-size);
  color: var(--md-sys-color-on-surface-variant);
  margin: 0;
  letter-spacing: 0.5px;
}

.portfolio-section {
  margin: var(--spacing-xl) 0;
}

.portfolio-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md) 0;
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
}

.portfolio-item:last-child {
  border-bottom: none;
}

.asset-info {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.asset-name {
  font-size: var(--md-sys-typescale-body-large-font-size);
  color: var(--md-sys-color-on-surface);
  font-weight: var(--md-sys-typescale-body-large-font-weight);
}

.asset-change {
  font-size: var(--md-sys-typescale-body-large-font-size);
  font-weight: var(--md-sys-typescale-body-large-font-weight);
}

.asset-change.positive {
  color: #4CAF50;
}

.asset-change.negative {
  color: var(--md-sys-color-error);
}

.stats-section {
  background: var(--md-sys-color-primary);
  border-radius: var(--md-sys-shape-corner-medium);
  padding: var(--spacing-xl);
  display: flex;
  justify-content: space-around;
  margin: var(--spacing-xl) 0;
}

.stat-item {
  text-align: center;
  color: var(--md-sys-color-on-primary);
}

.stat-number {
  font-size: var(--md-sys-typescale-headline-medium-font-size);
  font-weight: var(--md-sys-typescale-headline-medium-font-weight);
  margin-bottom: var(--spacing-xs);
}

.stat-label {
  font-size: var(--md-sys-typescale-label-small-font-size);
  font-weight: var(--md-sys-typescale-label-small-font-weight);
  letter-spacing: 0.5px;
  opacity: 0.9;
}

.settings-section {
  margin-top: var(--spacing-xl);
}

.settings-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md) 0;
  cursor: pointer;
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-body-large-font-size);
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
  transition: background-color var(--transition-short);
}

.settings-item:hover {
  background-color: var(--md-sys-color-surface-container);
  margin: 0 calc(-1 * var(--spacing-lg));
  padding: var(--spacing-md) var(--spacing-lg);
}

.settings-item svg {
  color: var(--md-sys-color-on-surface-variant);
}
</style> 