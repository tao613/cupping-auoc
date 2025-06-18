import api from './api';

export const authService = {
    // 用户注册
    register: async (userData) => {
        const response = await api.post('/users/register', userData);
        return response.data;
    },

    // 用户登录
    login: async (username, password) => {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);
        
        const response = await api.post('/users/token', formData, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        if (response.data.access_token) {
            localStorage.setItem('token', response.data.access_token);
        }
        return response.data;
    },

    // 获取当前用户信息
    getCurrentUser: async () => {
        const response = await api.get('/users/me');
        return response.data;
    },

    // 更新用户资料
    updateProfile: async (profileData) => {
        const response = await api.put('/users/me', profileData);
        return response.data;
    },

    // 修改密码
    changePassword: async (passwordData) => {
        const response = await api.put('/users/me/password', passwordData);
        return response.data;
    },

    // 登出
    logout: () => {
        localStorage.removeItem('token');
    },

    // 检查是否已登录
    isAuthenticated: () => {
        return !!localStorage.getItem('token');
    }
}; 