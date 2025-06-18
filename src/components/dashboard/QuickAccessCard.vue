<template>
  <div class="quick-access-card" @click="$emit('click')">
    <div class="icon">
      <i :class="`el-icon-${icon}`"></i>
    </div>
    <div class="title">{{ title }}</div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  }
})

defineEmits(['click'])
</script>

<style scoped>
.quick-access-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-lg);
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
  height: 100%;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
  }
  
  .icon {
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: var(--spacing-md);
    font-size: 2.5rem;
    color: var(--color-primary);
  }
  
  .title {
    font-size: 1.125rem;
    font-weight: 500;
  }
}
</style>
