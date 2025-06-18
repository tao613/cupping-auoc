<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            type="text"
            id="username"
            v-model="username"
            required
            placeholder="Enter your username"
            :disabled="authStore.loading"
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder="Enter your password"
            :disabled="authStore.loading"
          />
        </div>
        <div v-if="authStore.error" class="error-message">
          {{ authStore.error }}
        </div>
        <button type="submit" class="submit-btn" :disabled="authStore.loading">
          {{ authStore.loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
      <div class="register-link">
        Don't have an account? 
        <router-link to="/register">Register here</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')

const handleLogin = async () => {
  // 清除之前的错误
  authStore.clearError()
  
  try {
    await authStore.login({
      username: username.value,
      password: password.value
    })
    
    // 登录成功，路由会自动重定向
    router.push('/')
  } catch (error) {
    // 错误已经在store中处理了
    console.error('Login failed:', error)
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 200px);
  background: var(--md-sys-color-background);
}

.login-box {
  background: var(--md-sys-color-surface);
  padding: 2rem;
  border-radius: var(--md-sys-shape-corner-large);
  box-shadow: var(--md-sys-elevation-level-2);
  width: 100%;
  max-width: 400px;
  border: 1px solid var(--md-sys-color-outline-variant);
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-headline-medium-font-size);
  font-weight: var(--md-sys-typescale-headline-medium-font-weight);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: var(--md-sys-typescale-body-medium-font-weight);
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-body-medium-font-size);
}

input {
  padding: 1rem;
  border: 1px solid var(--md-sys-color-outline);
  border-radius: var(--md-sys-shape-corner-extra-small);
  font-size: var(--md-sys-typescale-body-large-font-size);
  background: var(--md-sys-color-surface);
  color: var(--md-sys-color-on-surface);
  transition: border-color var(--transition-medium);
}

input:focus {
  outline: none;
  border-color: var(--md-sys-color-primary);
  border-width: 2px;
  padding: calc(1rem - 1px);
}

input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.submit-btn {
  background-color: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  padding: 0.75rem;
  border: none;
  border-radius: var(--md-sys-shape-corner-full);
  font-size: var(--md-sys-typescale-label-large-font-size);
  font-weight: var(--md-sys-typescale-label-large-font-weight);
  cursor: pointer;
  transition: background-color var(--transition-short), box-shadow var(--transition-short);
  height: 40px;
}

.submit-btn:hover:not(:disabled) {
  box-shadow: var(--md-sys-elevation-level-1);
}

.submit-btn:disabled {
  background-color: var(--md-sys-color-outline);
  color: var(--md-sys-color-on-surface-variant);
  cursor: not-allowed;
  box-shadow: none;
}

.error-message {
  color: var(--md-sys-color-error);
  text-align: center;
  font-size: var(--md-sys-typescale-body-medium-font-size);
  padding: var(--spacing-sm);
  background: var(--md-sys-color-error-container);
  border-radius: var(--md-sys-shape-corner-extra-small);
}

.register-link {
  text-align: center;
  margin-top: 1.5rem;
  color: var(--md-sys-color-on-surface-variant);
  font-size: var(--md-sys-typescale-body-medium-font-size);
}

.register-link a {
  color: var(--md-sys-color-primary);
  text-decoration: none;
  font-weight: var(--md-sys-typescale-body-medium-font-weight);
}

.register-link a:hover {
  text-decoration: underline;
}
</style> 