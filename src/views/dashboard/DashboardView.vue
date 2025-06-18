<template>
  <div class="dashboard-view">
    <h1>Welcome, {{ userName }}!</h1>
    
    <div class="quick-access-cards">
      <QuickAccessCard 
        title="Cuppers" 
        icon="user"
        @click="navigateTo('/cuppers')" 
      />
      <QuickAccessCard 
        title="Start cupping" 
        icon="coffee"
        @click="navigateTo('/cupping-sessions/new')" 
      />
      <QuickAccessCard 
        title="Samples" 
        icon="collection"
        @click="navigateTo('/samples')" 
      />
    </div>
    
    <div class="dashboard-sections">
      <div class="section">
        <h2>My latest activity</h2>
        <div class="activity-summary">
          <div class="no-activity">
            <img src="@/assets/images/illustrations/no-activity.svg" alt="No Activity" />
            <p>No Activity</p>
          </div>
        </div>
      </div>
      
      <div class="section">
        <h2>Cupping Productivity Information</h2>
        <div class="productivity-stats">
          <div class="stat-card">
            <div class="icon orange">
              <i class="el-icon-collection"></i>
            </div>
            <div class="content">
              <div class="title">Samples Cupped</div>
              <div class="count">0</div>
            </div>
          </div>
          
          <div class="stat-card">
            <div class="icon orange">
              <i class="el-icon-coffee-cup"></i>
            </div>
            <div class="content">
              <div class="title">Cupping Sessions</div>
              <div class="count">0</div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="section">
        <h2>Upcoming Cupping Session</h2>
        <div class="upcoming-sessions">
          <div class="calendar-icon">
            <img src="@/assets/images/illustrations/calendar.svg" alt="Calendar" />
          </div>
          <p>No upcoming Cupping Session will be held. Add more Cupping Session below</p>
          <el-button type="primary" @click="navigateTo('/cupping-sessions/new')">
            <i class="el-icon-plus"></i>
            New Cupping Session
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'
import QuickAccessCard from '@/components/dashboard/QuickAccessCard.vue'

const router = useRouter()
const authStore = useAuthStore()

const userName = computed(() => {
  return authStore.currentUser?.name || 'User'
})

const navigateTo = (path) => {
  router.push(path)
}
</script>

<style scoped>
.dashboard-view {
  padding: var(--spacing-md);
}

h1 {
  font-size: 1.8rem;
  margin-bottom: var(--spacing-lg);
}

.quick-access-cards {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-xl);
  
  @media (min-width: 768px) {
    grid-template-columns: repeat(3, 1fr);
  }
}

.dashboard-sections {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-lg);
  
  @media (min-width: 992px) {
    grid-template-columns: repeat(2, 1fr);
  }
}

.section {
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
  
  h2 {
    font-size: 1.2rem;
    margin-bottom: var(--spacing-md);
    color: var(--color-text-primary);
  }
}

.activity-summary {
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.no-activity {
  text-align: center;
  
  img {
    width: 80px;
    height: 80px;
    margin-bottom: var(--spacing-sm);
    opacity: 0.7;
  }
  
  p {
    color: var(--color-text-secondary);
  }
}

.productivity-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-md);
}

.stat-card {
  display: flex;
  align-items: center;
  padding: var(--spacing-md);
  background-color: #f9f9f9;
  border-radius: var(--border-radius-sm);
  
  .icon {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: var(--spacing-md);
    font-size: 1.5rem;
    
    &.orange {
      background-color: var(--color-secondary);
      color: white;
    }
  }
  
  .content {
    .title {
      font-size: 0.875rem;
      color: var(--color-text-secondary);
      margin-bottom: var(--spacing-xs);
    }
    
    .count {
      font-size: 1.5rem;
      font-weight: bold;
    }
  }
}

.upcoming-sessions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 200px;
  text-align: center;
  
  .calendar-icon {
    margin-bottom: var(--spacing-md);
    
    img {
      width: 80px;
      height: 80px;
    }
  }
  
  p {
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-md);
    max-width: 300px;
  }
}
</style>
