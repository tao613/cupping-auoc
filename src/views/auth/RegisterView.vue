<template>
  <div class="register-view">
    <h1>Sign up to start your LADss free trial!</h1>
    <RegisterForm />
  </div>
</template>

<script setup>
import RegisterForm from '@/components/auth/RegisterForm.vue'
</script>

<style scoped>
.register-view {
  text-align: center;
  background: #181C23;
  min-height: 100vh;
  padding-top: 4rem;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #fff;
  font-weight: 700;
  letter-spacing: 1px;
}

@media (max-width: 768px) {
  h1 {
    font-size: 1.5rem;
  }
}
</style>
