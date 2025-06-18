<template>
  <div class="new-cupping-session-view">
    <div class="page-header">
      <h1>Start your cupping session</h1>
      <router-link to="/cupping-sessions" class="back-link">
        <i class="el-icon-arrow-left"></i> Back to Cupping sessions
      </router-link>
    </div>
    
    <div class="form-container">
      <el-form @submit.prevent="saveSession" label-position="top">
        <div class="form-header">
          <div class="session-title">
            <h2>Cupping Session {{ formattedDate }}</h2>
            <el-button type="text" @click="editTitle">
              <i class="el-icon-edit"></i>
            </el-button>
          </div>
          
          <div class="start-now-toggle">
            <span>Start cupping now</span>
            <el-switch v-model="startNow" />
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Start date">
              <el-date-picker
                v-model="form.startDate"
                type="date"
                placeholder="Select date"
                :disabled="startNow"
              />
            </el-form-item>
            
            <el-form-item label="Start time">
              <el-time-picker
                v-model="form.startTime"
                placeholder="Select time"
                :disabled="startNow"
              />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="End date">
              <el-date-picker
                v-model="form.endDate"
                type="date"
                placeholder="Select date"
              />
            </el-form-item>
            
            <el-form-item label="End time">
              <el-time-picker
                v-model="form.endTime"
                placeholder="Select time"
              />
            </el-form-item>
          </div>
          
          <el-form-item label="Location">
            <el-input
              v-model="form.location"
              placeholder="Enter location"
            >
              <template #prefix>
                <i class="el-icon-location"></i>
              </template>
            </el-input>
          </el-form-item>
          
          <el-form-item label="Description">
            <el-input
              v-model="form.description"
              type="textarea"
              rows="3"
              placeholder="Enter session description"
            />
          </el-form-item>
        </div>
        
        <div class="form-section">
          <h3>Invite cuppers</h3>
          
          <div class="invite-options">
            <el-button @click="selectAll">Select all</el-button>
            <el-button @click="clearAll">Clear all</el-button>
          </div>
          
          <div class="invite-form">
            <el-form-item label="Invite guest to cupping session">
              <div class="guest-input">
                <el-input
                  v-model="guestEmail"
                  placeholder="Name or E-Mail"
                />
                <el-button @click="addGuest">Add guest</el-button>
              </div>
            </el-form-item>
            
            <div class="guest-list" v-if="invitedGuests.length > 0">
              <div v-for="(guest, index) in invitedGuests" :key="index" class="guest-item">
                <span>{{ guest }}</span>
                <el-button type="text" @click="removeGuest(index)">
                  <i class="el-icon-close"></i>
                </el-button>
              </div>
            </div>
            
            <div v-else class="no-guests">
              <p>No guest cuppers invited</p>
              <p class="note">These users will be notified when the session is saved</p>
            </div>
          </div>
        </div>
        
        <div class="form-section">
          <h3>Sample id structure</h3>
          
          <div class="id-structure-options">
            <el-radio-group v-model="form.idStructure">
              <el-radio label="numbers">Numbers (1,2,3...)</el-radio>
              <el-radio label="digits">3 Digit (e.g. 257)</el-radio>
              <el-radio label="letters">Letter (i.e. A, B...)</el-radio>
            </el-radio-group>
          </div>
        </div>
        
        <div class="form-section">
          <h3>Cupping protocol</h3>
          
          <el-form-item>
            <el-select v-model="form.protocol" placeholder="Select protocol">
              <el-option label="Arabica" value="arabica" />
              <el-option label="Robusta" value="robusta" />
              <el-option label="SCA" value="sca" />
              <el-option label="Custom" value="custom" />
            </el-select>
          </el-form-item>
          
          <div class="protocol-note">
            <p>* SCA Coffee Value Assessment Beta Version 2023 Form</p>
          </div>
        </div>
        
        <div class="form-section">
          <h3>Number of samples</h3>
          
          <div class="samples-input">
            <el-input-number v-model="form.sampleCount" :min="1" :max="100" />
            <el-checkbox v-model="form.isBlind">Blind</el-checkbox>
          </div>
        </div>
        
        <div class="form-section">
          <h3>Combo Cupping</h3>
          
          <el-checkbox v-model="form.comboCupping">Enable combo cupping</el-checkbox>
        </div>
        
        <div class="form-section">
          <h3>Custom number of cups</h3>
          
          <el-checkbox v-model="form.customCupCount">Enable custom number of cups</el-checkbox>
        </div>
        
        <div class="form-actions">
          <el-button type="primary" native-type="submit" :loading="loading">Save</el-button>
          <el-button @click="cancel">Discard</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCuppingStore } from '@/stores/cupping.store'
import { useUiStore } from '@/stores/ui.store'

const router = useRouter()
const cuppingStore = useCuppingStore()
const uiStore = useUiStore()

const loading = ref(false)
const startNow = ref(true)
const guestEmail = ref('')
const invitedGuests = ref([])

// 当前日期格式化
const today = new Date()
const formattedDate = computed(() => {
  return today.toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' })
})

const form = reactive({
  title: `Cupping Session ${formattedDate.value}`,
  startDate: today,
  startTime: today,
  endDate: new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000), // 一周后
  endTime: today,
  location: '',
  description: '',
  idStructure: 'numbers',
  protocol: 'arabica',
  sampleCount: 1,
  isBlind: false,
  comboCupping: false,
  customCupCount: false
})

const editTitle = () => {
  const newTitle = prompt('Enter session title', form.title)
  if (newTitle) {
    form.title = newTitle
  }
}

const selectAll = () => {
  // 在实际应用中，这里会选择所有可用的品鉴师
  uiStore.addNotification({
    type: 'info',
    message: 'All cuppers selected'
  })
}

const clearAll = () => {
  invitedGuests.value = []
}

const addGuest = () => {
  if (guestEmail.value.trim()) {
    invitedGuests.value.push(guestEmail.value.trim())
    guestEmail.value = ''
  }
}

const removeGuest = (index) => {
  invitedGuests.value.splice(index, 1)
}

const saveSession = async () => {
  loading.value = true
  
  try {
    // 准备会话数据
    const sessionData = {
      title: form.title,
      startDate: startNow.value ? today : form.startDate,
      startTime: startNow.value ? today : form.startTime,
      endDate: form.endDate,
      endTime: form.endTime,
      location: form.location,
      description: form.description,
      idStructure: form.idStructure,
      protocol: form.protocol,
      sampleCount: form.sampleCount,
      isBlind: form.isBlind,
      comboCupping: form.comboCupping,
      customCupCount: form.customCupCount,
      guests: invitedGuests.value
    }
    
    // 创建会话
    const newSession = await cuppingStore.createSession(sessionData)
    
    uiStore.addNotification({
      type: 'success',
      message: 'Cupping session created successfully'
    })
    
    // 导航到会话列表
    router.push('/cupping-sessions')
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: error.message || 'Failed to create cupping session'
    })
  } finally {
    loading.value = false
  }
}

const cancel = () => {
  router.push('/cupping-sessions')
}
</script>

<style scoped>
.new-cupping-session-view {
  padding: var(--spacing-md);
}

.back-link {
  display: inline-flex;
  align-items: center;
  margin-bottom: var(--spacing-md);
  color: var(--color-primary);
  
  i {
    margin-right: var(--spacing-xs);
  }
}

.form-container {
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-lg);
  
  .session-title {
    display: flex;
    align-items: center;
    
    h2 {
      margin: 0;
      margin-right: var(--spacing-xs);
    }
  }
  
  .start-now-toggle {
    display: flex;
    align-items: center;
    
    span {
      margin-right: var(--spacing-sm);
    }
  }
}

.form-section {
  margin-bottom: var(--spacing-xl);
  
  h3 {
    font-size: 1.1rem;
    margin-bottom: var(--spacing-md);
  }
}

.form-row {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  
  @media (min-width: 768px) {
    flex-direction: row;
    
    .el-form-item {
      flex: 1;
      margin-bottom: 0;
    }
  }
}

.invite-options {
  display: flex;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-md);
}

.guest-input {
  display: flex;
  gap: var(--spacing-sm);
}

.guest-list {
  margin-top: var(--spacing-md);
}

.guest-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-sm);
  background-color: #f5f7fa;
  border-radius: var(--border-radius-sm);
  margin-bottom: var(--spacing-xs);
}

.no-guests {
  margin-top: var(--spacing-md);
  color: var(--color-text-secondary);
  
  .note {
    font-size: 0.85rem;
    margin-top: var(--spacing-xs);
  }
}

.id-structure-options {
  margin-bottom: var(--spacing-md);
}

.protocol-note {
  margin-top: var(--spacing-sm);
  font-size: 0.85rem;
  color: var(--color-text-secondary);
}

.samples-input {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.form-actions {
  display: flex;
  gap: var(--spacing-md);
  margin-top: var(--spacing-xl);
}
</style>
