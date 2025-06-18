import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  build: {
    // 调整chunk大小警告限制
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        // 手动分割chunks以优化加载性能
        manualChunks: {
          // Vue相关库
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          // UI和样式库
          'ui-vendor': [],
          // 工具库
          'utils': []
        }
      }
    }
  }
})
