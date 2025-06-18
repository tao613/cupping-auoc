<template>
  <div class="auth-layout">
    <div class="auth-container">
      <div class="auth-logo">
        <img src="@/assets/images/logo.png" alt="Tastify Logo" />
      </div>
      <div class="auth-content">
        <router-view />
      </div>
      <div class="auth-illustration">
        <img src="@/assets/images/illustrations/auth-illustration.svg" alt="Authentication Illustration" />
      </div>
    </div>
  </div>
</template>

<script setup>
// Auth layout component
</script>

<style scoped>
.auth-layout {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
  padding: var(--spacing-md);
}

.auth-container {
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  background-color: white;
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  position: relative;
}

.auth-logo {
  padding: var(--spacing-lg);
  display: flex;
  justify-content: center;
}

.auth-logo img {
  height: 40px;
}

.auth-content {
  padding: 0 var(--spacing-lg) var(--spacing-lg);
  max-width: 450px;
  margin: 0 auto;
}

.auth-illustration {
  display: none;
}

@media (min-width: 768px) {
  .auth-container {
    flex-direction: row;
    min-height: 600px;
  }
  
  .auth-logo {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 10;
  }
  
  .auth-content {
    flex: 1;
    padding: var(--spacing-xl);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .auth-illustration {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    background-color: var(--color-primary);
    padding: var(--spacing-lg);
  }
  
  .auth-illustration img {
    max-width: 100%;
    max-height: 400px;
  }
}
</style>
