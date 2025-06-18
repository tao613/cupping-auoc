# Vue 3 项目结构设计

基于对Tastify网站的全面分析，以下是详细的Vue 3项目结构设计。

```
tastify-clone/
├── public/                  # 静态资源
│   ├── favicon.ico
│   ├── index.html
│   └── images/              # 图片资源
│       └── logo.png
│
├── src/                     # 源代码
│   ├── assets/              # 项目资源
│   │   ├── images/          # 图片资源
│   │   │   ├── logo.png
│   │   │   ├── illustrations/  # 插图资源
│   │   │   └── icons/       # 图标资源
│   │   │
│   │   └── styles/          # 样式文件
│   │       ├── main.scss    # 主样式文件
│   │       ├── variables.scss # 变量定义
│   │       ├── reset.scss   # 样式重置
│   │       ├── animations.scss # 动画效果
│   │       └── components/  # 组件样式
│   │
│   ├── components/          # 通用组件
│   │   ├── layout/          # 布局组件
│   │   │   ├── AppLayout.vue  # 主布局容器
│   │   │   ├── AppSidebar.vue # 侧边栏
│   │   │   ├── AppHeader.vue  # 顶部导航
│   │   │   └── AppFooter.vue  # 页脚
│   │   │
│   │   ├── auth/            # 认证相关组件
│   │   │   ├── LoginForm.vue
│   │   │   ├── RegisterForm.vue
│   │   │   ├── RoleSelector.vue
│   │   │   └── OrganizationSelector.vue
│   │   │
│   │   ├── dashboard/       # 仪表盘组件
│   │   │   ├── WelcomeCard.vue
│   │   │   ├── QuickAccessCard.vue
│   │   │   ├── ActivitySummary.vue
│   │   │   ├── ProductivityStats.vue
│   │   │   └── UpcomingSessionsCalendar.vue
│   │   │
│   │   ├── samples/         # 样品相关组件
│   │   │   ├── SampleList.vue
│   │   │   ├── SampleForm.vue
│   │   │   ├── SampleFilters.vue
│   │   │   ├── SampleCard.vue
│   │   │   └── EmptyState.vue
│   │   │
│   │   ├── cupping/         # 品鉴相关组件
│   │   │   ├── CuppingSessionList.vue
│   │   │   ├── CuppingSessionForm.vue
│   │   │   ├── CuppingProtocolSelector.vue
│   │   │   ├── SampleIdStructureSelector.vue
│   │   │   ├── CupperInviteForm.vue
│   │   │   └── EmptyState.vue
│   │   │
│   │   ├── cuppers/         # 品鉴师相关组件
│   │   │   ├── CupperList.vue
│   │   │   ├── CupperCard.vue
│   │   │   ├── CupperInviteForm.vue
│   │   │   └── CupperStatsCard.vue
│   │   │
│   │   └── ui/              # UI组件
│   │       ├── BaseButton.vue
│   │       ├── BaseInput.vue
│   │       ├── BaseSelect.vue
│   │       ├── BaseCheckbox.vue
│   │       ├── BaseRadio.vue
│   │       ├── BaseCard.vue
│   │       ├── BaseModal.vue
│   │       ├── BaseDatePicker.vue
│   │       ├── BaseTimePicker.vue
│   │       ├── BaseDropdown.vue
│   │       ├── BaseTable.vue
│   │       ├── BasePagination.vue
│   │       ├── BaseEmptyState.vue
│   │       ├── BaseAlert.vue
│   │       └── BaseToast.vue
│   │
│   ├── views/               # 页面视图
│   │   ├── auth/
│   │   │   ├── LoginView.vue
│   │   │   └── RegisterView.vue
│   │   │
│   │   ├── dashboard/
│   │   │   └── DashboardView.vue
│   │   │
│   │   ├── samples/
│   │   │   ├── SamplesView.vue
│   │   │   ├── SampleDetailView.vue
│   │   │   └── NewSampleView.vue
│   │   │
│   │   ├── shipments/
│   │   │   ├── ShipmentsView.vue
│   │   │   └── NewShipmentView.vue
│   │   │
│   │   ├── cupping/
│   │   │   ├── CuppingSessionsView.vue
│   │   │   ├── NewCuppingSessionView.vue
│   │   │   └── CuppingSessionDetailView.vue
│   │   │
│   │   └── cuppers/
│   │       ├── CuppersView.vue
│   │       └── CupperDetailView.vue
│   │
│   ├── router/              # 路由配置
│   │   ├── index.js
│   │   └── routes/
│   │       ├── auth.routes.js
│   │       ├── dashboard.routes.js
│   │       ├── samples.routes.js
│   │       ├── cupping.routes.js
│   │       ├── cuppers.routes.js
│   │       └── index.js
│   │
│   ├── stores/              # Pinia状态管理
│   │   ├── index.js
│   │   ├── auth.store.js
│   │   ├── user.store.js
│   │   ├── samples.store.js
│   │   ├── cupping.store.js
│   │   ├── cuppers.store.js
│   │   └── ui.store.js
│   │
│   ├── services/            # API服务
│   │   ├── api.service.js   # API基础配置
│   │   ├── auth.service.js
│   │   ├── samples.service.js
│   │   ├── cupping.service.js
│   │   └── cuppers.service.js
│   │
│   ├── utils/               # 工具函数
│   │   ├── validators.js
│   │   ├── formatters.js
│   │   ├── helpers.js
│   │   └── storage.js
│   │
│   ├── constants/           # 常量定义
│   │   ├── routes.constants.js
│   │   ├── api.constants.js
│   │   ├── cupping.constants.js
│   │   └── ui.constants.js
│   │
│   ├── composables/         # 可复用的组合式函数
│   │   ├── useAuth.js
│   │   ├── usePagination.js
│   │   ├── useForm.js
│   │   └── useNotification.js
│   │
│   ├── App.vue              # 根组件
│   └── main.js              # 入口文件
│
├── .eslintrc.js             # ESLint配置
├── .prettierrc              # Prettier配置
├── vite.config.js           # Vite配置
├── package.json             # 项目依赖
└── README.md                # 项目说明
```

## 技术栈详情

### 核心框架
- **Vue 3**: 使用Composition API进行组件开发
- **Vue Router**: 管理应用路由
- **Pinia**: 状态管理库，Vue 3推荐的Vuex替代品

### UI和样式
- **Element Plus**: UI组件库，提供丰富的表单控件和数据展示组件
- **SCSS**: CSS预处理器，支持变量、嵌套、混合等特性
- **自定义组件**: 根据Tastify设计风格定制组件

### 构建工具
- **Vite**: 现代前端构建工具，提供更快的开发体验

### HTTP客户端
- **Axios**: 处理API请求

### 代码质量
- **ESLint**: 代码质量检查
- **Prettier**: 代码格式化

## 路由设计

```javascript
// router/routes/index.js
import authRoutes from './auth.routes';
import dashboardRoutes from './dashboard.routes';
import samplesRoutes from './samples.routes';
import cuppingRoutes from './cupping.routes';
import cuppersRoutes from './cuppers.routes';

const routes = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  ...authRoutes,
  ...dashboardRoutes,
  ...samplesRoutes,
  ...cuppingRoutes,
  ...cuppersRoutes,
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFoundView.vue')
  }
];

export default routes;

// router/routes/auth.routes.js
export default [
  {
    path: '/sign-in',
    name: 'login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: { requiresAuth: false, layout: 'auth' }
  },
  {
    path: '/sign-up',
    name: 'register',
    component: () => import('@/views/auth/RegisterView.vue'),
    meta: { requiresAuth: false, layout: 'auth' }
  }
];

// router/routes/dashboard.routes.js
export default [
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/dashboard/DashboardView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  }
];

// router/routes/samples.routes.js
export default [
  {
    path: '/samples',
    name: 'samples',
    component: () => import('@/views/samples/SamplesView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/samples/new',
    name: 'new-sample',
    component: () => import('@/views/samples/NewSampleView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  },
  {
    path: '/samples/:id',
    name: 'sample-detail',
    component: () => import('@/views/samples/SampleDetailView.vue'),
    meta: { requiresAuth: true, layout: 'default' }
  }
];

// 其他路由文件类似...
```

## 状态管理设计

使用Pinia创建以下几个主要的store:

1. **authStore**: 处理用户认证状态
   ```javascript
   // stores/auth.store.js
   import { defineStore } from 'pinia';
   import AuthService from '@/services/auth.service';
   import { useUserStore } from './user.store';

   export const useAuthStore = defineStore('auth', {
     state: () => ({
       token: localStorage.getItem('token') || null,
       isAuthenticated: !!localStorage.getItem('token'),
       loading: false,
       error: null
     }),
     actions: {
       async login(credentials) {
         this.loading = true;
         this.error = null;
         try {
           const response = await AuthService.login(credentials);
           this.setToken(response.token);
           const userStore = useUserStore();
           await userStore.fetchUserProfile();
           return response;
         } catch (error) {
           this.error = error.message;
           throw error;
         } finally {
           this.loading = false;
         }
       },
       async register(userData) {
         // 实现注册逻辑
       },
       logout() {
         // 实现登出逻辑
       },
       setToken(token) {
         this.token = token;
         this.isAuthenticated = true;
         localStorage.setItem('token', token);
       },
       clearToken() {
         this.token = null;
         this.isAuthenticated = false;
         localStorage.removeItem('token');
       }
     }
   });
   ```

2. **samplesStore**: 管理样品数据
   ```javascript
   // stores/samples.store.js
   import { defineStore } from 'pinia';
   import SamplesService from '@/services/samples.service';

   export const useSamplesStore = defineStore('samples', {
     state: () => ({
       samples: [],
       currentSample: null,
       loading: false,
       error: null,
       pagination: {
         page: 1,
         limit: 10,
         total: 0
       }
     }),
     getters: {
       getSampleById: (state) => (id) => {
         return state.samples.find(sample => sample.id === id);
       }
     },
     actions: {
       async fetchSamples(params = {}) {
         // 实现获取样品列表逻辑
       },
       async fetchSampleById(id) {
         // 实现获取单个样品逻辑
       },
       async createSample(sampleData) {
         // 实现创建样品逻辑
       },
       async updateSample(id, sampleData) {
         // 实现更新样品逻辑
       },
       async deleteSample(id) {
         // 实现删除样品逻辑
       }
     }
   });
   ```

3. **cuppingStore**: 管理咖啡品鉴会话
   ```javascript
   // stores/cupping.store.js
   import { defineStore } from 'pinia';
   import CuppingService from '@/services/cupping.service';

   export const useCuppingStore = defineStore('cupping', {
     state: () => ({
       sessions: [],
       currentSession: null,
       loading: false,
       error: null
     }),
     actions: {
       async fetchSessions() {
         // 实现获取品鉴会话列表逻辑
       },
       async fetchSessionById(id) {
         // 实现获取单个品鉴会话逻辑
       },
       async createSession(sessionData) {
         // 实现创建品鉴会话逻辑
       },
       async updateSession(id, sessionData) {
         // 实现更新品鉴会话逻辑
       },
       async deleteSession(id) {
         // 实现删除品鉴会话逻辑
       },
       async inviteCuppers(sessionId, cupperIds) {
         // 实现邀请品鉴师逻辑
       }
     }
   });
   ```

4. **cuppersStore**: 管理品鉴师数据
   ```javascript
   // stores/cuppers.store.js
   import { defineStore } from 'pinia';
   import CuppersService from '@/services/cuppers.service';

   export const useCuppersStore = defineStore('cuppers', {
     state: () => ({
       cuppers: [],
       stats: {
         members: 0,
         admins: 0,
         pendingInvites: 0,
         seatsAvailable: 0
       },
       loading: false,
       error: null
     }),
     actions: {
       async fetchCuppers() {
         // 实现获取品鉴师列表逻辑
       },
       async fetchCupperStats() {
         // 实现获取品鉴师统计数据逻辑
       },
       async inviteCupper(email) {
         // 实现邀请品鉴师逻辑
       },
       async updateCupperPermissions(cupperId, permissions) {
         // 实现更新品鉴师权限逻辑
       }
     }
   });
   ```

5. **uiStore**: 管理UI状态
   ```javascript
   // stores/ui.store.js
   import { defineStore } from 'pinia';

   export const useUiStore = defineStore('ui', {
     state: () => ({
       sidebarCollapsed: false,
       darkMode: false,
       notifications: [],
       loading: {
         global: false,
         components: {}
       }
     }),
     actions: {
       toggleSidebar() {
         this.sidebarCollapsed = !this.sidebarCollapsed;
       },
       toggleDarkMode() {
         this.darkMode = !this.darkMode;
         document.documentElement.classList.toggle('dark', this.darkMode);
       },
       addNotification(notification) {
         this.notifications.push({
           id: Date.now(),
           ...notification
         });
       },
       removeNotification(id) {
         this.notifications = this.notifications.filter(n => n.id !== id);
       },
       setLoading(component, status) {
         if (component === 'global') {
           this.loading.global = status;
         } else {
           this.loading.components[component] = status;
         }
       }
     }
   });
   ```

## 组件设计

### 布局组件

1. **AppLayout.vue**: 主布局容器
   ```vue
   <template>
     <div class="app-layout" :class="{ 'sidebar-collapsed': uiStore.sidebarCollapsed }">
       <AppSidebar />
       <div class="main-content">
         <AppHeader />
         <main>
           <slot></slot>
         </main>
         <AppFooter />
       </div>
     </div>
   </template>
   ```

2. **AppSidebar.vue**: 侧边栏导航
   ```vue
   <template>
     <aside class="sidebar" :class="{ 'collapsed': uiStore.sidebarCollapsed }">
       <div class="logo">
         <img src="@/assets/images/logo.png" alt="Tastify Logo" />
       </div>
       <nav class="nav-menu">
         <router-link to="/dashboard" class="nav-item">
           <i class="icon-home"></i>
           <span>Home</span>
         </router-link>
         <router-link to="/cuppers" class="nav-item">
           <i class="icon-users"></i>
           <span>Cuppers</span>
         </router-link>
         <router-link to="/cupping-sessions" class="nav-item">
           <i class="icon-cup"></i>
           <span>Cupping sessions</span>
         </router-link>
         <router-link to="/samples" class="nav-item">
           <i class="icon-sample"></i>
           <span>Samples</span>
         </router-link>
         <router-link to="/sample-shipments" class="nav-item">
           <i class="icon-shipment"></i>
           <span>Sample Shipments</span>
         </router-link>
         <!-- 其他导航项 -->
       </nav>
     </aside>
   </template>
   ```

### 认证组件

1. **LoginForm.vue**: 登录表单
   ```vue
   <template>
     <form @submit.prevent="handleSubmit" class="login-form">
       <h2>Sign in to start your cupping session!</h2>
       
       <div class="form-group">
         <label for="email">E-Mail</label>
         <BaseInput 
           id="email"
           v-model="form.email"
           type="email"
           :error="errors.email"
           required
         />
       </div>
       
       <div class="form-group">
         <label for="password">Password</label>
         <BaseInput 
           id="password"
           v-model="form.password"
           type="password"
           :error="errors.password"
           required
         />
       </div>
       
       <BaseButton type="submit" :loading="loading">Sign In</BaseButton>
       
       <div class="form-links">
         <router-link to="/forgot-password">Forgot your password?</router-link>
         <router-link to="/sign-up">Sign up</router-link>
       </div>
     </form>
   </template>
   ```

### 样品组件

1. **SampleList.vue**: 样品列表
   ```vue
   <template>
     <div class="sample-list">
       <div class="list-header">
         <BaseDropdown label="Sort By" :options="sortOptions" v-model="sortBy" />
         <BaseDropdown label="Action" :options="actionOptions" @select="handleAction" />
         <div class="view-toggles">
           <button @click="viewMode = 'list'" :class="{ active: viewMode === 'list' }">
             <i class="icon-list"></i>
           </button>
           <button @click="viewMode = 'grid'" :class="{ active: viewMode === 'grid' }">
             <i class="icon-grid"></i>
           </button>
         </div>
       </div>
       
       <BaseEmptyState 
         v-if="!samples.length"
         title="No results found"
         description="Try adding a new sample or changing your filters"
         icon="sample-empty"
       />
       
       <template v-else>
         <div :class="['samples-container', `view-${viewMode}`]">
           <SampleCard 
             v-for="sample in samples" 
             :key="sample.id" 
             :sample="sample"
             @click="viewSample(sample.id)"
           />
         </div>
         <BasePagination 
           :total="totalSamples"
           :current-page="currentPage"
           :per-page="perPage"
           @page-change="handlePageChange"
         />
       </template>
     </div>
   </template>
   ```

### 品鉴会话组件

1. **CuppingSessionForm.vue**: 创建品鉴会话表单
   ```vue
   <template>
     <form @submit.prevent="handleSubmit" class="cupping-session-form">
       <div class="form-header">
         <h2>{{ sessionName }}</h2>
         <button type="button" class="edit-button" @click="isEditingName = true">
           <i class="icon-edit"></i>
         </button>
       </div>
       
       <BaseButton type="button" @click="startCuppingNow">
         Start cupping now
       </BaseButton>
       
       <div class="form-row">
         <div class="form-group">
           <label>Start date</label>
           <BaseDatePicker v-model="form.startDate" />
         </div>
         <div class="form-group">
           <label>Start time</label>
           <BaseTimePicker v-model="form.startTime" />
         </div>
       </div>
       
       <div class="form-row">
         <div class="form-group">
           <label>End date</label>
           <BaseDatePicker v-model="form.endDate" />
         </div>
         <div class="form-group">
           <label>End time</label>
           <BaseTimePicker v-model="form.endTime" />
         </div>
       </div>
       
       <div class="form-group">
         <label>Location</label>
         <BaseInput v-model="form.location" />
       </div>
       
       <div class="form-group">
         <label>Description</label>
         <BaseTextarea v-model="form.description" />
       </div>
       
       <div class="form-group">
         <label>Sample id structure</label>
         <div class="sample-id-options">
           <BaseRadio v-model="form.sampleIdStructure" value="numbers" label="Numbers (1,2,3)" />
           <BaseRadio v-model="form.sampleIdStructure" value="digit" label="3 Digit (e.g. 257)" />
           <BaseRadio v-model="form.sampleIdStructure" value="letter" label="Letter (e.g. A, B)" />
         </div>
       </div>
       
       <div class="form-group">
         <label>Cupping protocol</label>
         <BaseSelect v-model="form.cuppingProtocol" :options="protocolOptions" />
       </div>
       
       <div class="form-group">
         <label>Number of samples</label>
         <BaseInput type="number" v-model.number="form.numberOfSamples" min="1" />
       </div>
       
       <div class="form-group">
         <BaseCheckbox v-model="form.blind" label="Blind" />
       </div>
       
       <div class="form-group">
         <label>Combo Cupping</label>
         <BaseCheckbox v-model="form.enableComboCupping" label="Enable combo cupping" />
       </div>
       
       <div class="form-group">
         <label>Custom number of cups</label>
         <BaseCheckbox v-model="form.enableCustomCups" label="Enable custom number of cups" />
       </div>
       
       <div class="cupper-invite-section">
         <h3>Invite cuppers</h3>
         <CupperInviteForm @invite="inviteCupper" />
         <div v-if="invitedCuppers.length" class="invited-cuppers">
           <div v-for="cupper in invitedCuppers" :key="cupper.id" class="invited-cupper">
             {{ cupper.name }}
             <button type="button" @click="removeCupper(cupper.id)">
               <i class="icon-remove"></i>
             </button>
           </div>
         </div>
         <p v-else>No guest cuppers invited</p>
       </div>
       
       <div class="form-actions">
         <BaseButton type="submit" variant="primary">Save</BaseButton>
         <BaseButton type="button" variant="secondary" @click="cancel">Discard</BaseButton>
       </div>
     </form>
   </template>
   ```

### 品鉴师组件

1. **CupperList.vue**: 品鉴师列表
   ```vue
   <template>
     <div class="cupper-list">
       <div class="stats-cards">
         <CupperStatsCard 
           title="Members" 
           :count="stats.members" 
           icon="members" 
           color="orange"
         />
         <CupperStatsCard 
           title="Admins" 
           :count="stats.admins" 
           icon="admin" 
           color="orange"
         />
         <CupperStatsCard 
           title="Pending invites" 
           :count="stats.pendingInvites" 
           icon="invite" 
           color="orange"
         />
         <CupperStatsCard 
           title="Seats available" 
           :count="stats.seatsAvailable" 
           icon="seat" 
           color="orange"
         />
       </div>
       
       <div class="search-bar">
         <BaseInput 
           v-model="searchQuery" 
           placeholder="Search name or email" 
           prefix-icon="search"
         />
       </div>
       
       <BaseTable :columns="columns" :data="filteredCuppers">
         <template #cell-name="{ row }">
           <div class="cupper-name">
             <div class="avatar">{{ getInitials(row.name) }}</div>
             <div>
               <div>{{ row.name }}</div>
               <div class="email">{{ row.email }}</div>
             </div>
           </div>
         </template>
         
         <template #cell-canCreateSession="{ row }">
           <BaseCheckbox 
             :modelValue="row.canCreateSession"
             @update:modelValue="updatePermission(row.id, 'canCreateSession', $event)"
             disabled-icon
           />
         </template>
         
         <template #cell-admin="{ row }">
           <BaseCheckbox 
             :modelValue="row.isAdmin"
             @update:modelValue="updatePermission(row.id, 'isAdmin', $event)"
             disabled-icon
           />
         </template>
         
         <template #cell-active="{ row }">
           <BaseCheckbox 
             :modelValue="row.isActive"
             @update:modelValue="updatePermission(row.id, 'isActive', $event)"
             disabled-icon
           />
         </template>
         
         <template #cell-actions="{ row }">
           <BaseDropdown 
             icon="more-vertical" 
             :options="getActionOptions(row)"
             @select="(action) => handleAction(action, row)"
           />
         </template>
       </BaseTable>
       
       <BasePagination 
         :total="totalCuppers"
         :current-page="currentPage"
         :per-page="perPage"
         @page-change="handlePageChange"
       />
     </div>
   </template>
   ```

## 主要页面视图

1. **DashboardView.vue**: 仪表盘页面
   ```vue
   <template>
     <div class="dashboard">
       <h1>Welcome, {{ user.name }}!</h1>
       
       <div class="quick-access-cards">
         <QuickAccessCard 
           title="Cuppers" 
           icon="users" 
           @click="navigateTo('/cuppers')" 
         />
         <QuickAccessCard 
           title="Start cupping" 
           icon="cup" 
           @click="navigateTo('/cupping-sessions/new')" 
         />
         <QuickAccessCard 
           title="Samples" 
           icon="sample" 
           @click="navigateTo('/samples')" 
         />
       </div>
       
       <div class="dashboard-sections">
         <div class="section">
           <h2>My latest activity</h2>
           <ActivitySummary :activities="activities" />
         </div>
         
         <div class="section">
           <h2>Cupping Productivity Information</h2>
           <ProductivityStats 
             :samples-count="stats.samplesCupped"
             :sessions-count="stats.cuppingSessions"
           />
         </div>
         
         <div class="section">
           <h2>Upcoming Cupping Session</h2>
           <UpcomingSessionsCalendar :sessions="upcomingSessions" />
         </div>
       </div>
     </div>
   </template>
   ```

2. **SamplesView.vue**: 样品列表页面
   ```vue
   <template>
     <div class="samples-view">
       <div class="page-header">
         <h1>Samples</h1>
         <div class="header-actions">
           <BaseDropdown 
             label="Sort By" 
             :options="sortOptions" 
             v-model="sortBy" 
           />
           <BaseDropdown 
             label="Action" 
             :options="actionOptions" 
             @select="handleAction" 
           />
           <div class="view-toggles">
             <button @click="viewMode = 'list'" :class="{ active: viewMode === 'list' }">
               <i class="icon-list"></i>
             </button>
             <button @click="viewMode = 'grid'" :class="{ active: viewMode === 'grid' }">
               <i class="icon-grid"></i>
             </button>
           </div>
         </div>
       </div>
       
       <SampleList 
         :samples="samples"
         :loading="loading"
         :view-mode="viewMode"
         @view-sample="viewSample"
       />
     </div>
   </template>
   ```

3. **CuppingSessionsView.vue**: 品鉴会话列表页面
   ```vue
   <template>
     <div class="cupping-sessions-view">
       <div class="page-header">
         <h1>Cupping sessions</h1>
         <h2>Let's start cupping!</h2>
         
         <div class="header-actions">
           <BaseButton 
             icon="plus" 
             @click="createNewSession"
           >
             New cupping session
           </BaseButton>
           <BaseButton 
             icon="export" 
             variant="outline"
           >
             Export
           </BaseButton>
           <BaseDropdown 
             label="No filter" 
             :options="filterOptions" 
             @select="applyFilter"
           />
           <div class="view-toggles">
             <button @click="viewMode = 'list'" :class="{ active: viewMode === 'list' }">
               <i class="icon-list"></i>
             </button>
             <button @click="viewMode = 'grid'" :class="{ active: viewMode === 'grid' }">
               <i class="icon-grid"></i>
             </button>
           </div>
         </div>
       </div>
       
       <CuppingSessionList 
         :sessions="sessions"
         :loading="loading"
         :view-mode="viewMode"
         @view-session="viewSession"
       />
     </div>
   </template>
   ```

4. **CuppersView.vue**: 品鉴师管理页面
   ```vue
   <template>
     <div class="cuppers-view">
       <div class="page-header">
         <h1>Cuppers</h1>
         <h2>Manage cuppers</h2>
         
         <div class="header-actions">
           <BaseButton 
             icon="plus" 
             @click="inviteMember"
           >
             Invite member
           </BaseButton>
           <BaseButton 
             icon="upgrade" 
             variant="outline"
           >
             Upgrade plans
           </BaseButton>
         </div>
       </div>
       
       <CupperList 
         :cuppers="cuppers"
         :stats="stats"
         :loading="loading"
         @update-permission="updatePermission"
         @invite-member="inviteMember"
       />
     </div>
   </template>
   ```

## 响应式设计

为确保网站在不同设备上都能良好显示，将实现以下响应式设计策略：

1. **使用媒体查询**：针对不同屏幕尺寸定义样式
   ```scss
   // styles/variables.scss
   $breakpoints: (
     xs: 0,
     sm: 576px,
     md: 768px,
     lg: 992px,
     xl: 1200px,
     xxl: 1400px
   );
   
   @mixin respond-to($breakpoint) {
     $value: map-get($breakpoints, $breakpoint);
     
     @if $value != null {
       @media (min-width: $value) {
         @content;
       }
     } @else {
       @error "Unknown breakpoint: #{$breakpoint}";
     }
   }
   ```

2. **弹性布局**：使用Flexbox和Grid布局
   ```scss
   .dashboard {
     display: flex;
     flex-direction: column;
     gap: 1.5rem;
     
     .quick-access-cards {
       display: grid;
       grid-template-columns: repeat(1, 1fr);
       gap: 1rem;
       
       @include respond-to(md) {
         grid-template-columns: repeat(2, 1fr);
       }
       
       @include respond-to(lg) {
         grid-template-columns: repeat(3, 1fr);
       }
     }
     
     .dashboard-sections {
       display: flex;
       flex-direction: column;
       gap: 1.5rem;
       
       @include respond-to(lg) {
         flex-direction: row;
         flex-wrap: wrap;
         
         .section {
           flex: 1 1 calc(50% - 0.75rem);
         }
       }
     }
   }
   ```

3. **移动优先设计**：从小屏幕开始设计，然后扩展到大屏幕
   ```scss
   .app-layout {
     display: flex;
     flex-direction: column;
     
     @include respond-to(lg) {
       flex-direction: row;
     }
     
     .sidebar {
       position: fixed;
       bottom: 0;
       left: 0;
       right: 0;
       height: 60px;
       z-index: 100;
       
       @include respond-to(lg) {
         position: sticky;
         top: 0;
         height: 100vh;
         width: 250px;
       }
       
       &.collapsed {
         @include respond-to(lg) {
           width: 70px;
         }
       }
     }
     
     .main-content {
       flex: 1;
       margin-bottom: 60px;
       
       @include respond-to(lg) {
         margin-bottom: 0;
       }
     }
   }
   ```

## 主题和样式

为实现Tastify的视觉风格，将定义以下主题变量：

```scss
// styles/variables.scss
:root {
  // 颜色
  --color-primary: #7e57c2; // 紫色
  --color-secondary: #ff8a65; // 橙色
  --color-success: #4caf50;
  --color-warning: #ff9800;
  --color-danger: #f44336;
  --color-info: #2196f3;
  
  // 中性色
  --color-text-primary: #333333;
  --color-text-secondary: #666666;
  --color-text-tertiary: #999999;
  --color-background: #ffffff;
  --color-border: #e0e0e0;
  
  // 字体
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-size-base: 16px;
  
  // 间距
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  
  // 圆角
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
  
  // 阴影
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  
  // 过渡
  --transition-fast: 0.15s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.5s ease;
}
```

## 总结

这个详细的项目结构设计涵盖了Tastify网站的所有主要功能和页面，包括：

1. **用户认证**：登录和注册功能
2. **仪表盘**：用户活动和统计概览
3. **样品管理**：样品列表、详情和创建
4. **品鉴会话**：会话列表、创建和管理
5. **品鉴师管理**：团队成员和权限管理

使用Vue 3的Composition API和Pinia状态管理，结合Element Plus组件库，可以高效地实现这些功能，并确保良好的用户体验和代码可维护性。

项目结构遵循模块化和组件化原则，使代码组织清晰，便于扩展和维护。响应式设计确保网站在各种设备上都能良好运行。
