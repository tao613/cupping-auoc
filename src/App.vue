<template>
  <div class="app">
    <AppLayout v-if="shouldShowLayout" />
    <div v-else class="auth-layout">
      <router-view />
    </div>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'
import AppLayout from './components/layout/AppLayout.vue'

export default {
  name: 'App',
  components: {
    AppLayout
  },
  setup() {
    const route = useRoute()
    const authStore = useAuthStore()
    
    const shouldShowLayout = computed(() => {
      // 不在登录、注册页面时显示主布局
      return !['/login', '/register'].includes(route.path)
    })

    // 初始化认证状态
    onMounted(async () => {
      await authStore.initialize()
    })

    return {
      shouldShowLayout
    }
  }
}
</script>

<style>
.app {
  min-height: 100vh;
}

.auth-layout {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--md-sys-color-background);
}

/* 全局样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--md-sys-typescale-font-family);
  line-height: 1.6;
  color: var(--md-sys-color-on-background);
  background-color: var(--md-sys-color-background);
}
</style>
