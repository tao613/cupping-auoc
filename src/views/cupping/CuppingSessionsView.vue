<template>
  <div class="cupping-sessions-view">
    <div class="page-header">
      <h1>Cupping sessions</h1>
      <h2>Let's start cupping!</h2>
      
      <div class="header-actions">
        <el-button type="primary" @click="navigateTo('/cupping-sessions/new')">
          <i class="el-icon-plus"></i> New cupping session
        </el-button>
        
        <el-button plain @click="exportData">
          <i class="el-icon-download"></i> Export
        </el-button>
        
        <el-dropdown>
          <el-button plain>
            No filter <i class="el-icon-arrow-down"></i>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>All sessions</el-dropdown-item>
              <el-dropdown-item>My sessions</el-dropdown-item>
              <el-dropdown-item>Shared with me</el-dropdown-item>
              <el-dropdown-item>Archived</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        
        <div class="view-toggles">
          <button :class="{ active: viewMode === 'list' }" @click="viewMode = 'list'">
            <i class="el-icon-menu"></i>
          </button>
          <button :class="{ active: viewMode === 'grid' }" @click="viewMode = 'grid'">
            <i class="el-icon-s-grid"></i>
          </button>
        </div>
      </div>
    </div>
    
    <div class="sessions-container">
      <div v-if="loading" class="loading-state">
        <el-spinner />
        <p>Loading cupping sessions...</p>
      </div>
      
      <div v-else-if="sessions.length === 0" class="empty-state">
        <img src="@/assets/images/illustrations/no-results.svg" alt="No Results" class="icon" />
        <h2 class="title">No results found</h2>
        <p class="description">No cupping sessions have been created yet. Start by creating your first session.</p>
        <el-button type="primary" @click="navigateTo('/cupping-sessions/new')">
          <i class="el-icon-plus"></i> New cupping session
        </el-button>
      </div>
      
      <div v-else>
        <!-- List View -->
        <div v-if="viewMode === 'list'" class="sessions-list">
          <el-table :data="sessions" style="width: 100%">
            <el-table-column prop="name" label="Name" />
            <el-table-column prop="date" label="Date" />
            <el-table-column prop="location" label="Location" />
            <el-table-column prop="sampleCount" label="Samples" />
            <el-table-column prop="cupperCount" label="Cuppers" />
            <el-table-column prop="status" label="Status">
              <template #default="scope">
                <el-tag :type="getStatusType(scope.row.status)">
                  {{ scope.row.status }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column label="Actions" width="150">
              <template #default="scope">
                <el-button size="small" @click="viewSession(scope.row.id)">View</el-button>
                <el-button size="small" type="danger" @click="deleteSession(scope.row.id)">Delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        
        <!-- Grid View -->
        <div v-else class="sessions-grid">
          <div v-for="session in sessions" :key="session.id" class="session-card">
            <h3>{{ session.name }}</h3>
            <div class="session-details">
              <p><strong>Date:</strong> {{ session.date }}</p>
              <p><strong>Location:</strong> {{ session.location }}</p>
              <p><strong>Samples:</strong> {{ session.sampleCount }}</p>
              <p><strong>Cuppers:</strong> {{ session.cupperCount }}</p>
              <p>
                <el-tag :type="getStatusType(session.status)">
                  {{ session.status }}
                </el-tag>
              </p>
            </div>
            <div class="session-actions">
              <el-button size="small" @click="viewSession(session.id)">View</el-button>
              <el-button size="small" type="danger" @click="deleteSession(session.id)">Delete</el-button>
            </div>
          </div>
        </div>
        
        <!-- Pagination -->
        <div class="pagination">
          <el-pagination
            layout="prev, pager, next"
            :total="totalSessions"
            :page-size="pageSize"
            :current-page="currentPage"
            @current-change="handlePageChange"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCuppingStore } from '@/stores/cupping.store'
import { useUiStore } from '@/stores/ui.store'

const router = useRouter()
const cuppingStore = useCuppingStore()
const uiStore = useUiStore()

const sessions = ref([])
const loading = ref(true)
const viewMode = ref('list')
const currentPage = ref(1)
const pageSize = ref(10)
const totalSessions = ref(0)

onMounted(async () => {
  await fetchSessions()
})

const fetchSessions = async () => {
  loading.value = true
  
  try {
    const response = await cuppingStore.fetchSessions({
      page: currentPage.value,
      limit: pageSize.value
    })
    
    sessions.value = response.data
    totalSessions.value = response.pagination.total
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to fetch cupping sessions'
    })
  } finally {
    loading.value = false
  }
}

const handlePageChange = (page) => {
  currentPage.value = page
  fetchSessions()
}

const navigateTo = (path) => {
  router.push(path)
}

const viewSession = (id) => {
  router.push(`/cupping-sessions/${id}`)
}

const deleteSession = async (id) => {
  try {
    await cuppingStore.deleteSession(id)
    
    uiStore.addNotification({
      type: 'success',
      message: 'Cupping session deleted successfully'
    })
    
    fetchSessions()
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to delete cupping session'
    })
  }
}

const exportData = () => {
  // 实现导出功能
  uiStore.addNotification({
    type: 'info',
    message: 'Exporting data...'
  })
}

const getStatusType = (status) => {
  switch (status) {
    case 'completed':
      return 'success'
    case 'in_progress':
      return 'warning'
    case 'pending':
      return 'info'
    default:
      return ''
  }
}
</script>

<style scoped>
.cupping-sessions-view {
  padding: var(--spacing-md);
}

.sessions-container {
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
}

.sessions-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: var(--spacing-md);
  
  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @media (min-width: 992px) {
    grid-template-columns: repeat(3, 1fr);
  }
}

.session-card {
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  
  h3 {
    margin-top: 0;
    margin-bottom: var(--spacing-sm);
  }
  
  .session-details {
    margin-bottom: var(--spacing-md);
    
    p {
      margin: var(--spacing-xs) 0;
    }
  }
  
  .session-actions {
    display: flex;
    justify-content: flex-end;
    gap: var(--spacing-sm);
  }
}

.pagination {
  margin-top: var(--spacing-lg);
  display: flex;
  justify-content: center;
}
</style>
