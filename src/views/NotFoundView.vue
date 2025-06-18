<template>
  <div class="not-found">
    <div class="content">
      <h1>404</h1>
      <h2>Page Not Found</h2>
      <p>The page you're looking for doesn't exist or has been moved.</p>
      <button class="btn btn-primary" @click="goHome">
        <i class="el-icon-home"></i>
        Back to Home
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
.not-found {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-lg);
  text-align: center;
  background-color: var(--color-background);
}

.content {
  max-width: 500px;
}

h1 {
  font-size: 8rem;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1;
  margin: 0;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 2rem;
  color: var(--color-text-primary);
  margin: var(--spacing-md) 0;
}

p {
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-xl);
  font-size: 1.125rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  font-size: 1.125rem;
  
  i {
    margin-right: var(--spacing-sm);
  }
}
</style> 