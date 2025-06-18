<template>
  <div class="home">
    <h1>Welcome to LADss</h1>
    
    <!-- 功能模块导航 -->
    <div class="feature-nav">
      <router-link to="/samples" class="feature-card">
        <div class="feature-icon">📄</div>
        <h3>Samples</h3>
        <p>Manage your coffee samples</p>
      </router-link>
      
      <router-link to="/cupping-sessions/new" class="feature-card">
        <div class="feature-icon">➕</div>
        <h3>Start Cupping</h3>
        <p>Begin a new cupping session</p>
      </router-link>
      
      <router-link to="/cupping-sessions" class="feature-card">
        <div class="feature-icon">📝</div>
        <h3>Cupping Sessions</h3>
        <p>View your cupping history</p>
      </router-link>
      
      <router-link to="/cuppers" class="feature-card">
        <div class="feature-icon">👤</div>
        <h3>Cuppers</h3>
        <p>Manage cupping team members</p>
      </router-link>
    </div>

    <!-- 咖啡列表 -->
    <div class="coffee-list">
      <h2>Recent Coffees</h2>
      <div v-if="loading" class="loading">
        Loading coffees...
      </div>
      <div v-else-if="error" class="error">
        {{ error }}
      </div>
      <div v-else class="coffee-grid">
        <div v-for="coffee in coffees" :key="coffee.id" class="coffee-card">
          <img :src="coffee.image_url" :alt="coffee.name" class="coffee-image">
          <div class="coffee-info">
            <h3>{{ coffee.name }}</h3>
            <p class="origin">Origin: {{ coffee.origin }}</p>
            <p class="roast-level">Roast Level: {{ coffee.roast_level }}</p>
            <p class="price">${{ coffee.price.toFixed(2) }}</p>
            <p class="description">{{ coffee.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { coffeeService } from '../services/api';
import { authService } from '../services/auth';

export default {
  name: 'HomeView',
  setup() {
    const router = useRouter();
    const coffees = ref([]);
    const loading = ref(true);
    const error = ref('');

    const fetchCoffees = async () => {
      try {
        loading.value = true;
        error.value = '';
        
        // 检查认证状态
        if (!authService.isAuthenticated()) {
          router.push('/login');
          return;
        }
        
        const data = await coffeeService.getAllCoffees();
        coffees.value = data;
      } catch (err) {
        if (err.response?.status === 401) {
          // 如果未授权，清除token并重定向到登录页
          authService.logout();
          router.push('/login');
        } else {
          // 暂时忽略API错误，显示空列表
          error.value = 'Coffee data is not available yet.';
          coffees.value = [];
          console.warn('Coffee API not available:', err);
        }
      } finally {
        loading.value = false;
      }
    };

    onMounted(() => {
      fetchCoffees();
    });

    return {
      coffees,
      loading,
      error
    };
  }
};
</script>

<style scoped>
.home {
  padding: 2rem;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

h2 {
  margin: 2rem 0 1rem;
  color: #333;
}

/* 功能模块导航样式 */
.feature-nav {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

/* 移动端响应式 */
@media (max-width: 768px) {
  .home {
    padding: 1rem;
  }
  
  .feature-nav {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .feature-card {
    padding: 1rem;
  }
  
  .feature-icon {
    font-size: 1.5rem;
  }
  
  .feature-card h3 {
    font-size: 1rem;
  }
  
  .feature-card p {
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .feature-nav {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
  
  .coffee-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0.5rem;
  }
}

.feature-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: block;
}

.feature-card h3 {
  margin: 0.5rem 0;
  color: #333;
}

.feature-card p {
  color: #666;
  font-size: 0.9rem;
  margin: 0;
}

/* 咖啡列表样式 */
.coffee-list {
  max-width: 1200px;
  margin: 0 auto;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.error {
  color: #dc3545;
}

.coffee-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

.coffee-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.coffee-card:hover {
  transform: translateY(-5px);
}

.coffee-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.coffee-info {
  padding: 1.5rem;
}

.coffee-info h3 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.origin, .roast-level {
  color: #666;
  margin: 0.25rem 0;
  font-size: 0.9rem;
}

.price {
  color: #4CAF50;
  font-weight: bold;
  margin: 0.5rem 0;
}

.description {
  color: #666;
  font-size: 0.9rem;
  margin: 0.5rem 0;
  line-height: 1.4;
}
</style> 