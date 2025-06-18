<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item brand-name">
        LADss
      </router-link>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <template v-if="isAuthenticated">
          <span class="navbar-item">
            Welcome, {{ username }}
          </span>
          <a class="navbar-item" @click="handleLogout">
            Logout
          </a>
        </template>
        <template v-else>
          <router-link to="/login" class="navbar-item">
            Login
          </router-link>
          <router-link to="/register" class="navbar-item">
            Register
          </router-link>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { authService } from '../services/auth';

export default {
  name: 'Navbar',
  setup() {
    const router = useRouter();
    const isAuthenticated = ref(false);
    const username = ref('');

    const checkAuth = async () => {
      isAuthenticated.value = authService.isAuthenticated();
      if (isAuthenticated.value) {
        try {
          const user = await authService.getCurrentUser();
          username.value = user.username;
        } catch (error) {
          console.error('Error fetching user:', error);
          handleLogout();
        }
      }
    };

    const handleLogout = () => {
      authService.logout();
      isAuthenticated.value = false;
      username.value = '';
      router.push('/login');
    };

    onMounted(() => {
      checkAuth();
    });

    return {
      isAuthenticated,
      username,
      handleLogout
    };
  }
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: #181C23;
  box-shadow: none;
}

.navbar-brand {
  font-size: 2rem;
  font-weight: bold;
}

.brand-name {
  color: #fff;
  font-weight: 700;
  letter-spacing: 1px;
  text-decoration: none;
}

.navbar-menu {
  display: flex;
  align-items: center;
}

.navbar-end {
  display: flex;
  gap: 1rem;
}

.navbar-item {
  text-decoration: none;
  color: #fff;
  cursor: pointer;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
  font-weight: 500;
}

.navbar-item:hover {
  background-color: #23272F;
}

.navbar-item.router-link-active {
  color: #4CAF50;
}
</style> 