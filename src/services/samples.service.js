import apiClient from './api.js'

class SamplesService {
  /**
   * 获取样品列表
   * @param {Object} params - 查询参数
   * @returns {Promise} API响应
   */
  async getSamples(params = {}) {
    try {
      const response = await apiClient.get('/samples/', { params })
      return response.data
    } catch (error) {
      console.error('Error fetching samples:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 获取单个样品详情
   * @param {number} id - 样品ID
   * @returns {Promise} API响应
   */
  async getSample(id) {
    try {
      const response = await apiClient.get(`/samples/${id}`)
      return response.data
    } catch (error) {
      console.error('Error fetching sample:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 创建新样品
   * @param {Object} sampleData - 样品数据
   * @returns {Promise} API响应
   */
  async createSample(sampleData) {
    try {
      const response = await apiClient.post('/samples/', sampleData)
      return response.data
    } catch (error) {
      console.error('Error creating sample:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 更新样品
   * @param {number} id - 样品ID
   * @param {Object} sampleData - 更新的样品数据
   * @returns {Promise} API响应
   */
  async updateSample(id, sampleData) {
    try {
      const response = await apiClient.put(`/samples/${id}`, sampleData)
      return response.data
    } catch (error) {
      console.error('Error updating sample:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 删除样品
   * @param {number} id - 样品ID
   * @returns {Promise} API响应
   */
  async deleteSample(id) {
    try {
      const response = await apiClient.delete(`/samples/${id}`)
      return response.data
    } catch (error) {
      console.error('Error deleting sample:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 恢复样品
   * @param {number} id - 样品ID
   * @returns {Promise} API响应
   */
  async restoreSample(id) {
    try {
      const response = await apiClient.patch(`/samples/${id}/restore`)
      return response.data
    } catch (error) {
      console.error('Error restoring sample:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 获取样品统计信息
   * @returns {Promise} API响应
   */
  async getSamplesStats() {
    try {
      const response = await apiClient.get('/samples/stats/overview')
      return response.data
    } catch (error) {
      console.error('Error fetching samples stats:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 搜索样品
   * @param {string} query - 搜索关键词
   * @param {Object} filters - 筛选条件
   * @returns {Promise} API响应
   */
  async searchSamples(query, filters = {}) {
    try {
      const params = {
        search: query,
        ...filters
      }
      const response = await apiClient.get('/samples/', { params })
      return response.data
    } catch (error) {
      console.error('Error searching samples:', error)
      throw this.handleError(error)
    }
  }

  /**
   * 获取样品类型选项
   * @returns {Array} 样品类型选项
   */
  getSampleTypeOptions() {
    return [
      { value: 'arabica', label: 'Arabica', description: '阿拉比卡' },
      { value: 'robusta', label: 'Robusta', description: '罗布斯塔' },
      { value: 'blend', label: 'Blend', description: '拼配' }
    ]
  }

  /**
   * 获取处理方式选项
   * @returns {Array} 处理方式选项
   */
  getProcessingMethodOptions() {
    return [
      { value: 'washed', label: 'Washed', description: '水洗' },
      { value: 'natural', label: 'Natural', description: '日晒' },
      { value: 'honey', label: 'Honey', description: '蜜处理' },
      { value: 'semi_washed', label: 'Semi-Washed', description: '半水洗' }
    ]
  }

  /**
   * 获取烘焙程度选项
   * @returns {Array} 烘焙程度选项
   */
  getRoastLevelOptions() {
    return [
      { value: 'light', label: 'Light', description: '浅烘' },
      { value: 'medium_light', label: 'Medium Light', description: '中浅烘' },
      { value: 'medium', label: 'Medium', description: '中烘' },
      { value: 'medium_dark', label: 'Medium Dark', description: '中深烘' },
      { value: 'dark', label: 'Dark', description: '深烘' }
    ]
  }

  /**
   * 错误处理
   * @param {Error} error - 错误对象
   * @returns {Error} 处理后的错误
   */
  handleError(error) {
    if (error.response) {
      // 服务器响应的错误
      const { data, status } = error.response
      
      switch (status) {
        case 400:
          return new Error(data.detail || '请求参数错误')
        case 401:
          return new Error('认证失败，请重新登录')
        case 403:
          return new Error('权限不足')
        case 404:
          return new Error('样品不存在')
        case 409:
          return new Error('样品编号已存在')
        case 422:
          return new Error('数据验证失败')
        case 500:
          return new Error('服务器内部错误')
        default:
          return new Error(data.detail || '请求失败')
      }
    } else if (error.request) {
      // 网络错误
      return new Error('网络连接失败，请检查网络设置')
    } else {
      // 其他错误
      return new Error(error.message || '未知错误')
    }
  }
}

export default new SamplesService() 