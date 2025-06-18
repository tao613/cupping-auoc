<template>
  <component :is="currentProfileComponent" />
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useUiStore } from '@/stores/ui.store'
import ProfileView from './ProfileView.vue'
import MobileProfileView from './MobileProfileView.vue'

const uiStore = useUiStore()

// 在组件挂载时检查移动端状态
onMounted(() => {
  uiStore.checkMobile()
})

// 根据设备类型选择组件
const currentProfileComponent = computed(() => {
  return uiStore.isMobile ? MobileProfileView : ProfileView
})
</script> 