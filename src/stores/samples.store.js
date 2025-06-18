import { defineStore } from 'pinia'
import samplesService from '@/services/samples.service'

export const useSamplesStore = defineStore('samples', {
  state: () => ({
    samples: [],
    currentSample: null,
    loading: false,
    error: null,
    pagination: {
      page: 1,
      limit: 10,
      total: 0,
      total_pages: 0,
      has_next: false,
      has_prev: false
    },
    stats: {
      total_samples: 0,
      by_type: {},
      by_country: []
    }
  }),
  
  getters: {
    getSampleById: (state) => (id) => {
      return state.samples.find(sample => sample.id === id)
    },
    
    activeSamples: (state) => {
      return state.samples.filter(sample => sample.is_active)
    },
    
    samplesByCountry: (state) => {
      const grouped = {}
      state.samples.forEach(sample => {
        if (!grouped[sample.country]) {
          grouped[sample.country] = []
        }
        grouped[sample.country].push(sample)
      })
      return grouped
    },
    
    samplesByType: (state) => {
      const grouped = {}
      state.samples.forEach(sample => {
        if (!grouped[sample.sample_type]) {
          grouped[sample.sample_type] = []
        }
        grouped[sample.sample_type].push(sample)
      })
      return grouped
    }
  },
  
  actions: {
    /**
     * 获取样品列表
     * @param {Object} params - 查询参数
     */
    async fetchSamples(params = {}) {
      this.loading = true
      this.error = null
      
      try {
        const response = await samplesService.getSamples({
          skip: ((params.page || 1) - 1) * (params.limit || 10),
          limit: params.limit || 10,
          ...params
        })
        
        this.samples = response.data
        this.pagination = response.pagination
        
        return response
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 获取单个样品详情
     * @param {number} id - 样品ID
     */
    async fetchSampleById(id) {
      this.loading = true
      this.error = null
      
      try {
        const sample = await samplesService.getSample(id)
        this.currentSample = sample
        
        // 更新本地samples数组中的数据
        const index = this.samples.findIndex(s => s.id === id)
        if (index !== -1) {
          this.samples[index] = sample
        }
        
        return sample
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 创建新样品
     * @param {Object} sampleData - 样品数据
     */
    async createSample(sampleData) {
      this.loading = true
      this.error = null
      
      try {
        const newSample = await samplesService.createSample(sampleData)
        
        // 添加到本地数组头部
        this.samples.unshift(newSample)
        this.pagination.total++
        
        return newSample
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 更新样品
     * @param {number} id - 样品ID
     * @param {Object} sampleData - 更新的样品数据
     */
    async updateSample(id, sampleData) {
      this.loading = true
      this.error = null
      
      try {
        const updatedSample = await samplesService.updateSample(id, sampleData)
        
        // 更新本地数组
        const index = this.samples.findIndex(s => s.id === id)
        if (index !== -1) {
          this.samples[index] = updatedSample
        }
        
        // 更新当前样品
        if (this.currentSample && this.currentSample.id === id) {
          this.currentSample = updatedSample
        }
        
        return updatedSample
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 删除样品
     * @param {number} id - 样品ID
     */
    async deleteSample(id) {
      this.loading = true
      this.error = null
      
      try {
        await samplesService.deleteSample(id)
        
        // 从本地数组移除
        const index = this.samples.findIndex(s => s.id === id)
        if (index !== -1) {
          this.samples.splice(index, 1)
          this.pagination.total--
        }
        
        // 清除当前样品
        if (this.currentSample && this.currentSample.id === id) {
          this.currentSample = null
        }
        
        return true
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 恢复样品
     * @param {number} id - 样品ID
     */
    async restoreSample(id) {
      this.loading = true
      this.error = null
      
      try {
        const restoredSample = await samplesService.restoreSample(id)
        
        // 添加到本地数组
        this.samples.unshift(restoredSample)
        this.pagination.total++
        
        return restoredSample
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 搜索样品
     * @param {string} query - 搜索关键词
     * @param {Object} filters - 筛选条件
     */
    async searchSamples(query, filters = {}) {
      this.loading = true
      this.error = null
      
      try {
        const response = await samplesService.searchSamples(query, filters)
        this.samples = response.data
        this.pagination = response.pagination
        
        return response
      } catch (error) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 获取样品统计信息
     */
    async fetchSamplesStats() {
      try {
        const stats = await samplesService.getSamplesStats()
        this.stats = stats
        return stats
      } catch (error) {
        this.error = error.message
        throw error
      }
    },
    
    /**
     * 清除错误状态
     */
    clearError() {
      this.error = null
    },
    
    /**
     * 清除当前样品
     */
    clearCurrentSample() {
      this.currentSample = null
    },
    
    /**
     * 获取样品选项数据
     */
    getSampleOptions() {
      return {
        sampleTypes: samplesService.getSampleTypeOptions(),
        processingMethods: samplesService.getProcessingMethodOptions(),
        roastLevels: samplesService.getRoastLevelOptions()
      }
    }
  }
})
