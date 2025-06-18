import axios from 'axios';

// 根据环境自动选择API地址
const getApiUrl = () => {
    // 生产环境：使用相对路径（通过nginx代理到后端）
    if (import.meta.env.PROD) {
        return '/api';
    }
    // 开发环境：直接连接到后端服务
    return 'http://localhost:8000';
};

const API_URL = getApiUrl();

const api = axios.create({
    baseURL: API_URL,
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// 请求拦截器：自动添加认证头
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 响应拦截器：处理通用错误
api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        const originalRequest = error.config;
        
        // 如果是401错误且不是登录请求，说明token过期
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            
            // 清除过期的token
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            
            // 重定向到登录页
            if (window.location.pathname !== '/login') {
                window.location.href = '/login';
            }
            
            return Promise.reject(error);
        }
        
        // 处理网络错误
        if (!error.response) {
            error.message = 'Network error. Please check your connection.';
        } else {
            // 处理服务器错误
            const message = error.response.data?.detail || error.response.data?.message || 'An error occurred';
            error.message = message;
        }
        
        return Promise.reject(error);
    }
);

export const coffeeService = {
    // 获取所有咖啡
    getAllCoffees: async () => {
        const response = await api.get('/coffees');
        return response.data;
    },

    // 获取单个咖啡详情
    getCoffeeById: async (id) => {
        const response = await api.get(`/coffees/${id}`);
        return response.data;
    },

    // 创建新咖啡
    createCoffee: async (coffeeData) => {
        const response = await api.post('/coffees', coffeeData);
        return response.data;
    },
};

export default api; 