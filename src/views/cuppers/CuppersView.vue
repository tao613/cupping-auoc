<template>
  <div class="cuppers-view">
    <div class="page-header">
      <h1>Cuppers</h1>
      <h2>Manage cuppers</h2>
      
      <div class="header-actions">
        <el-button type="primary" @click="showInviteModal">
          <i class="el-icon-plus"></i> Invite member
        </el-button>
        
        <el-button plain @click="showUpgradePlans">
          <i class="el-icon-s-promotion"></i> Upgrade plans
        </el-button>
      </div>
    </div>
    
    <div class="stats-cards">
      <div class="stat-card">
        <div class="icon orange">
          <i class="el-icon-user-solid"></i>
        </div>
        <div class="content">
          <div class="count">{{ stats.members }}</div>
          <div class="title">Members</div>
        </div>
      </div>
      
      <div class="stat-card">
        <div class="icon orange">
          <i class="el-icon-star-on"></i>
        </div>
        <div class="content">
          <div class="count">{{ stats.admins }}</div>
          <div class="title">Admins</div>
        </div>
      </div>
      
      <div class="stat-card">
        <div class="icon orange">
          <i class="el-icon-user"></i>
        </div>
        <div class="content">
          <div class="count">{{ stats.pendingInvites }}</div>
          <div class="title">Pending invites</div>
        </div>
      </div>
      
      <div class="stat-card">
        <div class="icon orange">
          <i class="el-icon-user-solid"></i>
        </div>
        <div class="content">
          <div class="count">{{ stats.seatsAvailable }}</div>
          <div class="title">Seats available</div>
        </div>
      </div>
    </div>
    
    <div class="cuppers-container">
      <div class="search-bar">
        <el-input
          placeholder="Search name or email"
          prefix-icon="el-icon-search"
          v-model="searchQuery"
          @input="handleSearch"
        />
      </div>
      
      <div v-if="loading" class="loading-state">
        <el-spinner />
        <p>Loading cuppers...</p>
      </div>
      
      <div v-else-if="cuppers.length === 0" class="empty-state">
        <img src="@/assets/images/illustrations/no-results.svg" alt="No Results" class="icon" />
        <h2 class="title">No results found</h2>
        <p class="description">No cuppers have been added yet. Start by inviting team members.</p>
        <el-button type="primary" @click="showInviteModal">
          <i class="el-icon-plus"></i> Invite member
        </el-button>
      </div>
      
      <div v-else>
        <div class="cuppers-table">
          <el-table :data="cuppers" style="width: 100%">
            <el-table-column label="Name" min-width="200">
              <template #default="scope">
                <div class="user-info">
                  <div class="avatar">{{ getUserInitials(scope.row) }}</div>
                  <div>
                    <div class="name">{{ scope.row.name }}</div>
                    <div class="email">{{ scope.row.email }}</div>
                  </div>
                </div>
              </template>
            </el-table-column>
            
            <el-table-column label="Can create cupping session" width="200">
              <template #default="scope">
                <el-checkbox v-model="scope.row.canCreateSession" @change="updatePermissions(scope.row)" />
              </template>
            </el-table-column>
            
            <el-table-column label="Admin" width="120">
              <template #default="scope">
                <el-checkbox v-model="scope.row.isAdmin" @change="updatePermissions(scope.row)" />
              </template>
            </el-table-column>
            
            <el-table-column label="Active" width="120">
              <template #default="scope">
                <el-checkbox v-model="scope.row.isActive" @change="updatePermissions(scope.row)" />
              </template>
            </el-table-column>
            
            <el-table-column label="Last activity" width="200">
              <template #default="scope">
                {{ formatDate(scope.row.lastActivity) }}
              </template>
            </el-table-column>
            
            <el-table-column label="Actions" width="100">
              <template #default="scope">
                <el-dropdown>
                  <i class="el-icon-more"></i>
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item @click="removeCupper(scope.row.id)">
                        <i class="el-icon-delete"></i> Remove
                      </el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
                </el-dropdown>
              </template>
            </el-table-column>
          </el-table>
        </div>
        
        <!-- Pagination -->
        <div class="pagination">
          <el-pagination
            layout="prev, pager, next"
            :total="totalCuppers"
            :page-size="pageSize"
            :current-page="currentPage"
            @current-change="handlePageChange"
          />
        </div>
      </div>
    </div>
    
    <!-- Invite Modal -->
    <el-dialog
      title="Invite new member"
      v-model="inviteModalVisible"
      width="500px"
    >
      <el-form @submit.prevent="sendInvite">
        <el-form-item label="Name">
          <el-input v-model="inviteForm.name" placeholder="Enter name" />
        </el-form-item>
        
        <el-form-item label="Email">
          <el-input v-model="inviteForm.email" placeholder="Enter email" required />
        </el-form-item>
        
        <el-form-item label="Role">
          <el-select v-model="inviteForm.role" placeholder="Select role">
            <el-option label="Member" value="member" />
            <el-option label="Admin" value="admin" />
          </el-select>
        </el-form-item>
        
        <el-form-item>
          <el-button type="primary" native-type="submit" :loading="inviteLoading">
            Send Invite
          </el-button>
          <el-button @click="inviteModalVisible = false">Cancel</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useCuppersStore } from '@/stores/cuppers.store'
import { useUiStore } from '@/stores/ui.store'

const cuppersStore = useCuppersStore()
const uiStore = useUiStore()

const cuppers = ref([])
const loading = ref(true)
const stats = reactive({
  members: 0,
  admins: 0,
  pendingInvites: 0,
  seatsAvailable: 0
})
const searchQuery = ref('')
const currentPage = ref(1)
const pageSize = ref(10)
const totalCuppers = ref(0)

// Invite modal
const inviteModalVisible = ref(false)
const inviteLoading = ref(false)
const inviteForm = reactive({
  name: '',
  email: '',
  role: 'member'
})

onMounted(async () => {
  await Promise.all([
    fetchCuppers(),
    fetchStats()
  ])
})

const fetchCuppers = async () => {
  loading.value = true
  
  try {
    const response = await cuppersStore.fetchCuppers({
      page: currentPage.value,
      limit: pageSize.value,
      search: searchQuery.value
    })
    
    cuppers.value = response.data
    totalCuppers.value = response.pagination.total
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to fetch cuppers'
    })
  } finally {
    loading.value = false
  }
}

const fetchStats = async () => {
  try {
    const statsData = await cuppersStore.fetchCupperStats()
    Object.assign(stats, statsData)
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to fetch cupper stats'
    })
  }
}

const handlePageChange = (page) => {
  currentPage.value = page
  fetchCuppers()
}

const handleSearch = () => {
  currentPage.value = 1
  fetchCuppers()
}

const updatePermissions = async (cupper) => {
  try {
    await cuppersStore.updateCupperPermissions(cupper.id, {
      canCreateSession: cupper.canCreateSession,
      isAdmin: cupper.isAdmin,
      isActive: cupper.isActive
    })
    
    uiStore.addNotification({
      type: 'success',
      message: 'Permissions updated successfully'
    })
    
    // Refresh stats
    fetchStats()
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to update permissions'
    })
  }
}

const removeCupper = async (id) => {
  try {
    // In a real app, this would call an API to remove the cupper
    uiStore.addNotification({
      type: 'success',
      message: 'Cupper removed successfully'
    })
    
    // Refresh data
    fetchCuppers()
    fetchStats()
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to remove cupper'
    })
  }
}

const showInviteModal = () => {
  inviteModalVisible.value = true
}

const sendInvite = async () => {
  if (!inviteForm.email) {
    uiStore.addNotification({
      type: 'error',
      message: 'Email is required'
    })
    return
  }
  
  inviteLoading.value = true
  
  try {
    await cuppersStore.inviteCupper(inviteForm.email)
    
    uiStore.addNotification({
      type: 'success',
      message: 'Invitation sent successfully'
    })
    
    inviteModalVisible.value = false
    inviteForm.name = ''
    inviteForm.email = ''
    inviteForm.role = 'member'
    
    // Refresh stats
    fetchStats()
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: 'Failed to send invitation'
    })
  } finally {
    inviteLoading.value = false
  }
}

const showUpgradePlans = () => {
  uiStore.addNotification({
    type: 'info',
    message: 'Upgrade plans feature coming soon'
  })
}

const getUserInitials = (user) => {
  if (!user.name) return user.email.charAt(0).toUpperCase()
  
  const names = user.name.split(' ')
  if (names.length === 1) return names[0].charAt(0).toUpperCase()
  return (names[0].charAt(0) + names[names.length - 1].charAt(0)).toUpperCase()
}

const formatDate = (date) => {
  if (!date) return 'Never'
  return new Date(date).toLocaleString()
}
</script>

<style scoped>
.cuppers-view {
  padding: var(--spacing-md);
}

.stats-cards {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
  
  @media (min-width: 576px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @media (min-width: 992px) {
    grid-template-columns: repeat(4, 1fr);
  }
}

.stat-card {
  display: flex;
  align-items: center;
  padding: var(--spacing-md);
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
}

.cuppers-container {
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
}

.search-bar {
  margin-bottom: var(--spacing-md);
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl);
}

.user-info {
  display: flex;
  align-items: center;
  
  .avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background-color: var(--color-primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: var(--spacing-sm);
  }
  
  .name {
    font-weight: 500;
  }
  
  .email {
    font-size: 0.85rem;
    color: var(--color-text-secondary);
  }
}

.pagination {
  margin-top: var(--spacing-lg);
  display: flex;
  justify-content: center;
}
</style>
