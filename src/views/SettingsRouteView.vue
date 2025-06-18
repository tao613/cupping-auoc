<template>
  <component :is="currentSettingsComponent" />
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useUiStore } from '@/stores/ui.store'
import ProfileView from './ProfileView.vue' // 桌面端设置页面使用ProfileView
import MobileSettingsView from './MobileSettingsView.vue'

const uiStore = useUiStore()

// 在组件挂载时检查移动端状态
onMounted(() => {
  uiStore.checkMobile()
})

// 根据设备类型选择组件
const currentSettingsComponent = computed(() => {
  return uiStore.isMobile ? MobileSettingsView : ProfileView
})
</script> 