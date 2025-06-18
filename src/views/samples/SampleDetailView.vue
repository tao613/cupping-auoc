<template>
  <div class="sample-detail">
    <div class="page-header">
      <div class="header-content">
        <h1>{{ sample?.name || 'Loading...' }}</h1>
        <p class="subtitle">{{ sample?.origin || 'Loading sample details...' }}</p>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" @click="goBack">
          <i class="el-icon-back"></i>
          Back
        </button>
        <button class="btn btn-primary" @click="startCupping">
          <i class="el-icon-cup"></i>
          Start Cupping
        </button>
      </div>
    </div>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading sample details...</p>
    </div>

    <div v-else-if="error" class="error-state">
      <i class="el-icon-warning"></i>
      <p>{{ error }}</p>
      <button class="btn btn-primary" @click="fetchSample">Try Again</button>
    </div>

    <div v-else-if="sample" class="sample-content">
      <div class="content-grid">
        <!-- Basic Information -->
        <div class="card">
          <div class="card-header">
            <h3>Basic Information</h3>
          </div>
          <div class="card-body">
            <div class="info-grid">
              <div class="info-item">
                <label>Origin</label>
                <span>{{ sample.origin }}</span>
              </div>
              <div class="info-item">
                <label>Variety</label>
                <span>{{ sample.variety }}</span>
              </div>
              <div class="info-item">
                <label>Process</label>
                <span>{{ sample.process }}</span>
              </div>
              <div class="info-item">
                <label>Altitude</label>
                <span>{{ sample.altitude }}m</span>
              </div>
              <div class="info-item">
                <label>Harvest Date</label>
                <span>{{ formatDate(sample.harvestDate) }}</span>
              </div>
              <div class="info-item">
                <label>Roast Level</label>
                <span>{{ sample.roastLevel }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Cupping Notes -->
        <div class="card">
          <div class="card-header">
            <h3>Cupping Notes</h3>
          </div>
          <div class="card-body">
            <div v-if="sample.cuppingNotes?.length" class="notes-list">
              <div v-for="note in sample.cuppingNotes" :key="note.id" class="note-item">
                <div class="note-header">
                  <div class="cupper-info">
                    <div class="avatar">{{ getInitials(note.cupperName) }}</div>
                    <div class="details">
                      <span class="name">{{ note.cupperName }}</span>
                      <span class="date">{{ formatDate(note.date) }}</span>
                    </div>
                  </div>
                  <div class="score">{{ note.score }}/100</div>
                </div>
                <div class="note-content">
                  <p>{{ note.notes }}</p>
                </div>
                <div class="flavor-tags">
                  <span v-for="flavor in note.flavors" :key="flavor" class="tag">
                    {{ flavor }}
                  </span>
                </div>
              </div>
            </div>
            <div v-else class="empty-state">
              <p>No cupping notes available yet.</p>
              <button class="btn btn-primary" @click="startCupping">Start First Cupping</button>
            </div>
          </div>
        </div>

        <!-- Sample History -->
        <div class="card">
          <div class="card-header">
            <h3>Sample History</h3>
          </div>
          <div class="card-body">
            <div class="timeline">
              <div v-for="event in sample.history" :key="event.id" class="timeline-item">
                <div class="timeline-date">{{ formatDate(event.date) }}</div>
                <div class="timeline-content">
                  <h4>{{ event.title }}</h4>
                  <p>{{ event.description }}</p>
                </div>
              </div>
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

const sample = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchSample = async () => {
  loading.value = true
  error.value = null
  
  try {
    // TODO: Replace with actual API call
    const response = await fetch(`/api/samples/${route.params.id}`)
    if (!response.ok) throw new Error('Failed to fetch sample')
    sample.value = await response.json()
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

const startCupping = () => {
  router.push({
    name: 'new-cupping',
    params: { sampleId: route.params.id }
  })
}

onMounted(fetchSample)
</script>

<style scoped>
.sample-detail {
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

.notes-list {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.note-item {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-sm);
}

.note-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-sm);
}

.cupper-info {
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
  
  .date {
    font-size: 0.875rem;
    color: var(--color-text-secondary);
  }
}

.score {
  font-weight: 600;
  color: var(--color-primary);
}

.note-content {
  margin-bottom: var(--spacing-sm);
}

.flavor-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-xs);
}

.tag {
  padding: 0.25rem 0.5rem;
  background-color: rgba(var(--color-primary), 0.1);
  color: var(--color-primary);
  border-radius: var(--border-radius-sm);
  font-size: 0.875rem;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.timeline-item {
  display: flex;
  gap: var(--spacing-md);
}

.timeline-date {
  min-width: 100px;
  color: var(--color-text-secondary);
  font-size: 0.875rem;
}

.timeline-content {
  flex: 1;
  
  h4 {
    margin: 0 0 var(--spacing-xs);
    font-size: 1rem;
  }
  
  p {
    margin: 0;
    color: var(--color-text-secondary);
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