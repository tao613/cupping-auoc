<template>
  <div class="organization-selector">
    <el-radio-group v-model="selectedOrg" @change="emitChange">
      <div class="org-grid">
        <el-radio v-for="org in organizations" :key="org.value" :label="org.value" class="org-option">
          {{ org.label }}
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

const organizations = [
  { value: 'farmer_cooperative', label: 'Farmers/ Cooperative/ Exporter/ Miller' },
  { value: 'importer', label: 'Importer' },
  { value: 'wholesale_roaster', label: 'Wholesale roaster' },
  { value: 'retail_roaster', label: 'Retail roaster' },
  { value: 'ngo', label: 'NGO' },
  { value: 'education', label: 'Education' }
]

const selectedOrg = ref(props.modelValue)

watch(() => props.modelValue, (newValue) => {
  selectedOrg.value = newValue
})

const emitChange = () => {
  emit('update:modelValue', selectedOrg.value)
}
</script>

<style scoped>
.org-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.org-option {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-sm);
  transition: all var(--transition-fast);
}

.org-option:hover {
  border-color: var(--color-primary);
}

@media (max-width: 576px) {
  .org-grid {
    grid-template-columns: 1fr;
  }
}
</style>
