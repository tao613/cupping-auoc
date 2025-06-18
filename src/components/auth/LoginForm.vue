<template>
  <form @submit.prevent="handleSubmit" class="login-form">
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
    
    <div class="form-group">
      <label for="password">Password</label>
      <el-input 
        id="password"
        v-model="form.password"
        type="password"
        placeholder="Enter your password"
        :class="{ 'error': errors.password }"
        required
        show-password
      />
      <div v-if="errors.password" class="error-message">{{ errors.password }}</div>
    </div>
    
    <el-button type="primary" native-type="submit" :loading="loading" class="submit-btn">
      Sign In
    </el-button>
    
    <div class="form-links">
      <router-link to="/forgot-password">Forgot your password?</router-link>
      <router-link to="/sign-up">Sign up</router-link>
    </div>
  </form>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'
import { useUiStore } from '@/stores/ui.store'

const router = useRouter()
const authStore = useAuthStore()
const uiStore = useUiStore()

const form = reactive({
  email: '',
  password: ''
})

const errors = reactive({
  email: '',
  password: ''
})

const loading = ref(false)

const validateForm = () => {
  let isValid = true
  
  // Reset errors
  errors.email = ''
  errors.password = ''
  
  // Validate email
  if (!form.email) {
    errors.email = 'Email is required'
    isValid = false
  } else if (!/\S+@\S+\.\S+/.test(form.email)) {
    errors.email = 'Email is invalid'
    isValid = false
  }
  
  // Validate password
  if (!form.password) {
    errors.password = 'Password is required'
    isValid = false
  }
  
  return isValid
}

const handleSubmit = async () => {
  if (!validateForm()) return
  
  loading.value = true
  
  try {
    await authStore.login({
      email: form.email,
      password: form.password
    })
    
    uiStore.addNotification({
      type: 'success',
      message: 'Login successful'
    })
    
    router.push('/dashboard')
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: error.message || 'Login failed'
    })
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.submit-btn {
  width: 100%;
  margin-top: 1rem;
  height: 44px;
  font-size: 1rem;
}

.form-links {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
  font-size: 0.9rem;
}

.error-message {
  color: var(--color-danger);
  font-size: 0.85rem;
  margin-top: 0.25rem;
}
</style>
