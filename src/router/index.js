import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import { useAuthStore } from '@/stores/auth.store'

// 路由配置
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { requiresAuth: false, guest: true }
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: { requiresAuth: false, guest: true }
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/ProfileRouteView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import('../views/SettingsRouteView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/dashboard/DashboardView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/samples',
    name: 'samples',
    component: () => import('../views/samples/SamplesView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/samples/new',
    name: 'new-sample',
    component: () => import('../views/samples/NewSampleView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/samples/:id',
    name: 'sample-detail',
    component: () => import('../views/samples/SampleDetailView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/cupping-sessions',
    name: 'cupping-sessions',
    component: () => import('../views/cupping/CuppingSessionsView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/cupping-sessions/new',
    name: 'new-cupping-session',
    component: () => import('../views/cupping/NewCuppingSessionView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/cupping-sessions/:id',
    name: 'cupping-session-detail',
    component: () => import('../views/cupping/CuppingSessionDetailView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/cuppers',
    name: 'cuppers',
    component: () => import('../views/cuppers/CuppersView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('../views/NotFoundView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// 导航守卫
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // 检查是否需要认证
  const requiresAuth = to.meta.requiresAuth
  const isGuestPage = to.meta.guest // 登录、注册页面
  
  // 如果有token，验证其有效性
  if (authStore.token) {
    const isValid = await authStore.validateToken()
    if (!isValid) {
      // token无效，清理状态并重定向到登录页
      if (requiresAuth) {
        next('/login')
        return
      }
    }
  }
  
  if (requiresAuth && !authStore.isAuthenticated) {
    // 需要认证但用户未登录，重定向到登录页
    next('/login')
  } else if (isGuestPage && authStore.isAuthenticated) {
    // 已登录用户访问登录/注册页，重定向到首页
    next('/')
  } else {
    next()
  }
})

export default router
