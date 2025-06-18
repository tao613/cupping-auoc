<template>
  <div class="login-view">
    <h1>Sign in to start your cupping session!</h1>
    <LoginForm />
  </div>
</template>

<script setup>
import LoginForm from '@/components/auth/LoginForm.vue'
</script>

<style scoped>
.login-view {
  text-align: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: var(--color-text-primary);
}

@media (max-width: 768px) {
  h1 {
    font-size: 1.5rem;
  }
}
</style>
