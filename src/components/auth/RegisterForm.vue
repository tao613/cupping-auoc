<template>
  <form @submit.prevent="handleSubmit" class="register-form">
    <div class="step" v-if="currentStep === 1">
      <div class="form-group">
        <label for="email">E-Mail</label>
        <el-input 
          id="email"
          v-model="form.email"
          type="email"
          placeholder="Enter your email"
          :class="{ 'error': errors.email }"
          required
        />
        <div v-if="errors.email" class="error-message">{{ errors.email }}</div>
      </div>
      
      <div class="form-section">
        <h3>Please choose one role that fits you the most</h3>
        <div class="role-options">
          <RoleSelector v-model="form.role" />
        </div>
      </div>
      
      <el-button type="primary" @click="nextStep" class="next-btn">
        Continue
      </el-button>
    </div>
    
    <div class="step" v-if="currentStep === 2">
      <div class="form-section">
        <h3>What does your organization do in coffee?</h3>
        <div class="org-options">
          <OrganizationSelector v-model="form.organization" />
        </div>
      </div>
      
      <div class="form-section">
        <h3>Are you a Q Grader?</h3>
        <div class="q-grader-options">
          <el-radio-group v-model="form.isQGrader">
            <el-radio :label="true">Yes</el-radio>
            <el-radio :label="false">No</el-radio>
          </el-radio-group>
        </div>
      </div>
      
      <div class="form-actions">
        <el-button @click="prevStep" class="prev-btn">
          Back
        </el-button>
        <el-button type="primary" native-type="submit" :loading="loading" class="submit-btn">
          Sign Up
        </el-button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'
import { useUiStore } from '@/stores/ui.store'
import RoleSelector from './RoleSelector.vue'
import OrganizationSelector from './OrganizationSelector.vue'

const router = useRouter()
const authStore = useAuthStore()
const uiStore = useUiStore()

const currentStep = ref(1)
const loading = ref(false)

const form = reactive({
  email: '',
  role: null,
  organization: null,
  isQGrader: false
})

const errors = reactive({
  email: '',
  role: '',
  organization: ''
})

const validateStep1 = () => {
  let isValid = true
  
  // Reset errors
  errors.email = ''
  errors.role = ''
  
  // Validate email
  if (!form.email) {
    errors.email = 'Email is required'
    isValid = false
  } else if (!/\S+@\S+\.\S+/.test(form.email)) {
    errors.email = 'Email is invalid'
    isValid = false
  }
  
  // Validate role
  if (!form.role) {
    errors.role = 'Please select a role'
    isValid = false
  }
  
  return isValid
}

const validateStep2 = () => {
  let isValid = true
  
  // Reset errors
  errors.organization = ''
  
  // Validate organization
  if (!form.organization) {
    errors.organization = 'Please select an organization type'
    isValid = false
  }
  
  return isValid
}

const nextStep = () => {
  if (validateStep1()) {
    currentStep.value++
  }
}

const prevStep = () => {
  currentStep.value--
}

const handleSubmit = async () => {
  if (!validateStep2()) return
  
  loading.value = true
  
  try {
    await authStore.register({
      email: form.email,
      role: form.role,
      organization: form.organization,
      isQGrader: form.isQGrader
    })
    
    uiStore.addNotification({
      type: 'success',
      message: 'Registration successful'
    })
    
    router.push('/dashboard')
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: error.message || 'Registration failed'
    })
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-form {
  max-width: 500px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-section {
  margin-bottom: 2rem;
  text-align: left;
}

h3 {
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.next-btn, .submit-btn {
  width: 100%;
  margin-top: 1rem;
  height: 44px;
  font-size: 1rem;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.prev-btn {
  flex: 1;
}

.submit-btn {
  flex: 2;
}

.error-message {
  color: var(--color-danger);
  font-size: 0.85rem;
  margin-top: 0.25rem;
}

.role-options, .org-options {
  margin-top: 1rem;
}

.q-grader-options {
  margin-top: 1rem;
}
</style>
