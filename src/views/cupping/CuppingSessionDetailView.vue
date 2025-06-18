<template>
  <div class="cupping-session-detail">
    <div class="page-header">
      <div class="header-content">
        <h1>Cupping Session</h1>
        <p class="subtitle">{{ formatDate(session?.date) || 'Loading session details...' }}</p>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" @click="goBack">
          <i class="el-icon-back"></i>
          Back
        </button>
        <button v-if="!session?.completed" class="btn btn-primary" @click="completeSession">
          <i class="el-icon-check"></i>
          Complete Session
        </button>
      </div>
    </div>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading session details...</p>
    </div>

    <div v-else-if="error" class="error-state">
      <i class="el-icon-warning"></i>
      <p>{{ error }}</p>
      <button class="btn btn-primary" @click="fetchSession">Try Again</button>
    </div>

    <div v-else-if="session" class="session-content">
      <div class="content-grid">
        <!-- Session Information -->
        <div class="card">
          <div class="card-header">
            <h3>Session Information</h3>
          </div>
          <div class="card-body">
            <div class="info-grid">
              <div class="info-item">
                <label>Date</label>
                <span>{{ formatDate(session.date) }}</span>
              </div>
              <div class="info-item">
                <label>Status</label>
                <span :class="['status', session.completed ? 'completed' : 'in-progress']">
                  {{ session.completed ? 'Completed' : 'In Progress' }}
                </span>
              </div>
              <div class="info-item">
                <label>Location</label>
                <span>{{ session.location }}</span>
              </div>
              <div class="info-item">
                <label>Participants</label>
                <span>{{ session.participants?.length || 0 }} cuppers</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Samples -->
        <div class="card">
          <div class="card-header">
            <h3>Samples</h3>
          </div>
          <div class="card-body">
            <div v-if="session.samples?.length" class="samples-list">
              <div v-for="sample in session.samples" :key="sample.id" class="sample-item">
                <div class="sample-info">
                  <h4>{{ sample.name }}</h4>
                  <p>{{ sample.origin }}</p>
                </div>
                <div class="sample-actions">
                  <button class="btn btn-text" @click="viewSample(sample.id)">
                    View Details
                  </button>
                </div>
              </div>
            </div>
            <div v-else class="empty-state">
              <p>No samples added to this session yet.</p>
            </div>
          </div>
        </div>

        <!-- Participants -->
        <div class="card">
          <div class="card-header">
            <h3>Participants</h3>
          </div>
          <div class="card-body">
            <div v-if="session.participants?.length" class="participants-list">
              <div v-for="participant in session.participants" :key="participant.id" class="participant-item">
                <div class="participant-info">
                  <div class="avatar">{{ getInitials(participant.name) }}</div>
                  <div class="details">
                    <span class="name">{{ participant.name }}</span>
                    <span class="role">{{ participant.role }}</span>
                  </div>
                </div>
                <div class="participant-status">
                  <span :class="['status', participant.completed ? 'completed' : 'pending']">
                    {{ participant.completed ? 'Completed' : 'Pending' }}
                  </span>
                </div>
              </div>
            </div>
            <div v-else class="empty-state">
              <p>No participants added to this session yet.</p>
            </div>
          </div>
        </div>

        <!-- Notes -->
        <div class="card">
          <div class="card-header">
            <h3>Session Notes</h3>
          </div>
          <div class="card-body">
            <div v-if="session.notes" class="notes-content">
              <p>{{ session.notes }}</p>
            </div>
            <div v-else class="empty-state">
              <p>No notes added to this session yet.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { format } from 'date-fns'

const route = useRoute()
const router = useRouter()

const session = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchSession = async () => {
  loading.value = true
  error.value = null
  
  try {
    // TODO: Replace with actual API call
    const response = await fetch(`/api/cupping-sessions/${route.params.id}`)
    if (!response.ok) throw new Error('Failed to fetch session')
    session.value = await response.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

const formatDate = (date) => {
  return date ? format(new Date(date), 'MMM d, yyyy') : 'N/A'
}

const getInitials = (name) => {
  return name
    .split(' ')
    .map(word => word[0])
    .join('')
    .toUpperCase()
}

const goBack = () => {
  router.back()
}

const viewSample = (sampleId) => {
  router.push({
    name: 'sample-detail',
    params: { id: sampleId }
  })
}

const completeSession = async () => {
  try {
    // TODO: Replace with actual API call
    const response = await fetch(`/api/cupping-sessions/${route.params.id}/complete`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to complete session')
    await fetchSession() // Refresh session data
  } catch (err) {
    error.value = err.message
  }
}

onMounted(fetchSession)
</script>

<style scoped>
.cupping-session-detail {
  padding: var(--spacing-lg);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--spacing-xl);
}

.header-content {
  h1 {
    font-size: 2rem;
    margin-bottom: var(--spacing-xs);
  }

  .subtitle {
    color: var(--color-text-secondary);
  }
}

.header-actions {
  display: flex;
  gap: var(--spacing-md);
}

.content-grid {
  display: grid;
  gap: var(--spacing-lg);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .content-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.card {
  background: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
}

.card-header {
  padding: var(--spacing-md);
  border-bottom: 1px solid var(--color-border);
  
  h3 {
    margin: 0;
    font-size: 1.25rem;
  }
}

.card-body {
  padding: var(--spacing-md);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--spacing-md);
}

.info-item {
  label {
    display: block;
    color: var(--color-text-secondary);
    font-size: 0.875rem;
    margin-bottom: var(--spacing-xs);
  }
  
  span {
    font-weight: 500;
  }
}

.status {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  border-radius: var(--border-radius-sm);
  font-size: 0.875rem;
  font-weight: 500;
  
  &.completed {
    background-color: rgba(var(--color-success), 0.1);
    color: var(--color-success);
  }
  
  &.in-progress {
    background-color: rgba(var(--color-warning), 0.1);
    color: var(--color-warning);
  }
  
  &.pending {
    background-color: rgba(var(--color-text-secondary), 0.1);
    color: var(--color-text-secondary);
  }
}

.samples-list,
.participants-list {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.sample-item,
.participant-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-sm);
}

.sample-info {
  h4 {
    margin: 0 0 var(--spacing-xs);
    font-size: 1rem;
  }
  
  p {
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 0.875rem;
  }
}

.participant-info {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: var(--color-primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
}

.details {
  display: flex;
  flex-direction: column;
  
  .name {
    font-weight: 500;
  }
  
  .role {
    font-size: 0.875rem;
    color: var(--color-text-secondary);
  }
}

.notes-content {
  p {
    margin: 0;
    white-space: pre-wrap;
  }
}

.loading-state,
.error-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
  text-align: center;
  
  i {
    font-size: 2rem;
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-md);
  }
  
  p {
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-md);
  }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(var(--color-primary), 0.3);
  border-radius: 50%;
  border-top-color: var(--color-primary);
  animation: spin 1s linear infinite;
  margin-bottom: var(--spacing-md);
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style> 