<template>
  <div class="samples-view">
    <div class="page-header">
      <h1>Samples</h1>
      
      <div class="header-actions">
        <el-dropdown>
          <el-button type="primary">
            Action <i class="el-icon-arrow-down"></i>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="navigateTo('/samples/new')">
                <i class="el-icon-plus"></i> New Sample
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/samples/multiple')">
                <i class="el-icon-plus"></i> Add multiple samples
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/samples/edit')">
                <i class="el-icon-edit"></i> Edit Sample
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/shipments/new')">
                <i class="el-icon-box"></i> New Shipment
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/cupping-sessions/new')">
                <i class="el-icon-coffee-cup"></i> New Cupping Session
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/samples/compare')">
                <i class="el-icon-data-analysis"></i> Compare
              </el-dropdown-item>
              <el-dropdown-item @click="navigateTo('/samples/share')">
                <i class="el-icon-share"></i> Share
              </el-dropdown-item>
              <el-dropdown-item @click="downloadCSV">
                <i class="el-icon-download"></i> Download To CSV
              </el-dropdown-item>
              <el-dropdown-item @click="downloadAllCSV">
                <i class="el-icon-download"></i> Download All To CSV
              </el-dropdown-item>
              <el-dropdown-item @click="generateReport">
                <i class="el-icon-document"></i> Generate Combined Report
              </el-dropdown-item>
              <el-dropdown-item @click="generateLabel">
                <i class="el-icon-printer"></i> Generate Label
              </el-dropdown-item>
              <el-dropdown-item @click="showAdvancedSearch">
                <i class="el-icon-search"></i> Advance search
              </el-dropdown-item>
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
    
    <div class="samples-container">
      <div v-if="loading" class="loading-state">
        <el-spinner />
        <p>Loading samples...</p>
      </div>
      
      <div v-else-if="samples.length === 0" class="empty-state">
        <img src="@/assets/images/illustrations/no-results.svg" alt="No Results" class="icon" />
        <h2 class="title">No results found</h2>
        <p class="description">No samples have been added yet. Start by adding your first sample.</p>
        <el-button type="primary" @click="navigateTo('/samples/new')">
          <i class="el-icon-plus"></i> New Sample
        </el-button>
      </div>
      
      <div v-else>
        <!-- List View -->
        <div v-if="viewMode === 'list'" class="samples-list">
          <el-table :data="samples" style="width: 100%">
            <el-table-column prop="name" label="Name" />
            <el-table-column prop="country" label="Country" />
            <el-table-column prop="type" label="Type" />
            <el-table-column prop="grade" label="Grade" />
            <el-table-column prop="createdAt" label="Created At" />
            <el-table-column label="Actions" width="150">
              <template #default="scope">
                <el-button size="small" @click="viewSample(scope.row.id)">View</el-button>
                <el-button size="small" type="danger" @click="deleteSample(scope.row.id)">Delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        
        <!-- Grid View -->
        <div v-else class="samples-grid">
          <div v-for="sample in samples" :key="sample.id" class="sample-card">
            <h3>{{ sample.name }}</h3>
            <div class="sample-details">
              <p><strong>Country:</strong> {{ sample.country }}</p>
              <p><strong>Type:</strong> {{ sample.type }}</p>
              <p><strong>Grade:</strong> {{ sample.grade }}</p>
            </div>
            <div class="sample-actions">
              <el-button size="small" @click="viewSample(sample.id)">View</el-button>
              <el-button size="small" type="danger" @click="deleteSample(sample.id)">Delete</el-button>
            </div>
          </div>
        </div>
        
        <!-- Pagination -->
        <div class="pagination">
          <el-pagination
            layout="prev, pager, next"
            :total="totalSamples"
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
import { useSamplesStore } from '@/stores/samples.store'
import { useUiStore } from '@/stores/ui.store'

const router = useRouter()
const samplesStore = useSamplesStore()
const uiStore = useUiStore()

const samples = ref([])
const loading = ref(true)
const viewMode = ref('list')
const currentPage = ref(1)
const pageSize = ref(10)
const totalSamples = ref(0)

onMounted(async () => {
  await fetchSamples()
})

const fetchSamples = async () => {
  loading.value = true
  
  try {
    const response = await samplesStore.fetchSamples({
      page: currentPage.value,
      limit: pageSize.value
    })
    
    samples.value = response.data
    totalSamples.value = response.pagination.total
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to fetch samples'
    })
  } finally {
    loading.value = false
  }
}

const handlePageChange = (page) => {
  currentPage.value = page
  fetchSamples()
}

const navigateTo = (path) => {
  router.push(path)
}

const viewSample = (id) => {
  router.push(`/samples/${id}`)
}

const deleteSample = async (id) => {
  try {
    await samplesStore.deleteSample(id)
    
    uiStore.addNotification({
      type: 'success',
      message: 'Sample deleted successfully'
    })
    
    fetchSamples()
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to delete sample'
    })
  }
}

const downloadCSV = () => {
  // 实现下载CSV功能
  uiStore.addNotification({
    type: 'info',
    message: 'Downloading CSV...'
  })
}

const downloadAllCSV = () => {
  // 实现下载所有CSV功能
  uiStore.addNotification({
    type: 'info',
    message: 'Downloading all samples as CSV...'
  })
}

const generateReport = () => {
  // 实现生成报告功能
  uiStore.addNotification({
    type: 'info',
    message: 'Generating combined report...'
  })
}

const generateLabel = () => {
  // 实现生成标签功能
  uiStore.addNotification({
    type: 'info',
    message: 'Generating label...'
  })
}

const showAdvancedSearch = () => {
  // 实现高级搜索功能
  uiStore.addNotification({
    type: 'info',
    message: 'Advanced search feature coming soon'
  })
}
</script>

<style scoped>
.samples-view {
  padding: var(--spacing-md);
}

.samples-container {
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

.samples-grid {
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

.sample-card {
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  
  h3 {
    margin-top: 0;
    margin-bottom: var(--spacing-sm);
  }
  
  .sample-details {
    margin-bottom: var(--spacing-md);
    
    p {
      margin: var(--spacing-xs) 0;
    }
  }
  
  .sample-actions {
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
