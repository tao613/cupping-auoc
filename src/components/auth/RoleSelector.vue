<template>
  <div class="role-selector">
    <el-radio-group v-model="selectedRole" @change="emitChange">
      <div class="role-grid">
        <el-radio v-for="role in roles" :key="role.value" :label="role.value" class="role-option">
          {{ role.label }}
        </el-radio>
      </div>
    </el-radio-group>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: null
  }
})

const emit = defineEmits(['update:modelValue'])

const roles = [
  { value: 'quality_control', label: 'Quality Control' },
  { value: 'barista', label: 'Barista' },
  { value: 'trader', label: 'Trader' },
  { value: 'homebrewer', label: 'Homebrewer' },
  { value: 'coffee_buyer', label: 'Coffee Buyer' },
  { value: 'owner', label: 'Owner' },
  { value: 'educator', label: 'Educator' },
  { value: 'judge', label: 'Judge' },
  { value: 'logistic', label: 'Logistic' },
  { value: 'other', label: 'Other' }
]

const selectedRole = ref(props.modelValue)

watch(() => props.modelValue, (newValue) => {
  selectedRole.value = newValue
})

const emitChange = () => {
  emit('update:modelValue', selectedRole.value)
}
</script>

<style scoped>
.role-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.role-option {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-sm);
  transition: all var(--transition-fast);
}

.role-option:hover {
  border-color: var(--color-primary);
}

@media (max-width: 576px) {
  .role-grid {
    grid-template-columns: 1fr;
  }
}
</style>
