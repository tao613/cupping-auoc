<template>
  <div v-if="modelValue" class="dialog-overlay" @click="closeDialog">
    <div class="dialog-container" @click.stop>
      <div class="dialog-header">
        <h2>修改密码</h2>
        <button class="close-button" @click="closeDialog">
          <i class="material-icons">close</i>
        </button>
      </div>

      <div class="dialog-content">
        <form @submit.prevent="changePassword" class="password-form">
          <div class="field-group">
            <label class="field-label">当前密码</label>
            <div class="password-input-wrapper">
              <input
                v-model="formData.currentPassword"
                :type="showCurrentPassword ? 'text' : 'password'"
                class="field-input"
                placeholder="请输入当前密码"
                required
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="showCurrentPassword = !showCurrentPassword"
              >
                <i class="material-icons">
                  {{ showCurrentPassword ? 'visibility_off' : 'visibility' }}
                </i>
              </button>
            </div>
          </div>

          <div class="field-group">
            <label class="field-label">新密码</label>
            <div class="password-input-wrapper">
              <input
                v-model="formData.newPassword"
                :type="showNewPassword ? 'text' : 'password'"
                class="field-input"
                placeholder="请输入新密码（至少6位）"
                minlength="6"
                required
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="showNewPassword = !showNewPassword"
              >
                <i class="material-icons">
                  {{ showNewPassword ? 'visibility_off' : 'visibility' }}
                </i>
              </button>
            </div>
            <div class="password-strength">
              <div class="strength-bar">
                <div 
                  class="strength-fill" 
                  :class="passwordStrength.level"
                  :style="{ width: passwordStrength.percentage + '%' }"
                ></div>
              </div>
              <span class="strength-text">{{ passwordStrength.text }}</span>
            </div>
          </div>

          <div class="field-group">
            <label class="field-label">确认新密码</label>
            <div class="password-input-wrapper">
              <input
                v-model="formData.confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'"
                class="field-input"
                placeholder="请再次输入新密码"
                required
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="showConfirmPassword = !showConfirmPassword"
              >
                <i class="material-icons">
                  {{ showConfirmPassword ? 'visibility_off' : 'visibility' }}
                </i>
              </button>
            </div>
            <div v-if="formData.confirmPassword && !passwordsMatch" class="error-message">
              两次输入的密码不一致
            </div>
          </div>

          <div class="password-tips">
            <h4>密码要求：</h4>
            <ul>
              <li :class="{ valid: hasMinLength }">至少6位字符</li>
              <li :class="{ valid: hasLetter }">包含字母</li>
              <li :class="{ valid: hasNumber }">包含数字</li>
              <li :class="{ valid: hasSpecialChar }">包含特殊字符（推荐）</li>
            </ul>
          </div>
        </form>
      </div>

      <div class="dialog-actions">
        <button type="button" class="cancel-button" @click="closeDialog">
          取消
        </button>
        <button 
          type="submit" 
          class="submit-button"
          :disabled="!canSubmit || isLoading"
          @click="changePassword"
        >
          <i v-if="isLoading" class="material-icons loading-icon">hourglass_empty</i>
          {{ isLoading ? '修改中...' : '确认修改' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { useUiStore } from '@/stores/ui.store'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'success'])

const authStore = useAuthStore()
const uiStore = useUiStore()

// 响应式数据
const isLoading = ref(false)
const showCurrentPassword = ref(false)
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)

const formData = reactive({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
})

// 密码强度计算
const passwordStrength = computed(() => {
  const password = formData.newPassword
  let score = 0
  let level = 'weak'
  let text = '弱'

  if (password.length >= 6) score += 1
  if (password.match(/[a-zA-Z]/)) score += 1
  if (password.match(/[0-9]/)) score += 1
  if (password.match(/[^a-zA-Z0-9]/)) score += 1
  if (password.length >= 12) score += 1

  if (score >= 4) {
    level = 'strong'
    text = '强'
  } else if (score >= 2) {
    level = 'medium'
    text = '中等'
  }

  return {
    level,
    text,
    percentage: (score / 5) * 100
  }
})

// 密码验证
const hasMinLength = computed(() => formData.newPassword.length >= 6)
const hasLetter = computed(() => /[a-zA-Z]/.test(formData.newPassword))
const hasNumber = computed(() => /[0-9]/.test(formData.newPassword))
const hasSpecialChar = computed(() => /[^a-zA-Z0-9]/.test(formData.newPassword))
const passwordsMatch = computed(() => formData.newPassword === formData.confirmPassword)

const canSubmit = computed(() => {
  return formData.currentPassword && 
         formData.newPassword && 
         formData.confirmPassword && 
         hasMinLength.value && 
         passwordsMatch.value
})

// 监听对话框状态，重置表单
watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    resetForm()
  }
})

/**
 * 重置表单
 */
const resetForm = () => {
  formData.currentPassword = ''
  formData.newPassword = ''
  formData.confirmPassword = ''
  showCurrentPassword.value = false
  showNewPassword.value = false
  showConfirmPassword.value = false
}

/**
 * 关闭对话框
 */
const closeDialog = () => {
  emit('update:modelValue', false)
}

/**
 * 修改密码
 */
const changePassword = async () => {
  if (!canSubmit.value || isLoading.value) return

  isLoading.value = true

  try {
    await authStore.changePassword({
      current_password: formData.currentPassword,
      new_password: formData.newPassword
    })

    uiStore.showNotification({
      type: 'success',
      message: '密码修改成功'
    })

    emit('success')
    closeDialog()
  } catch (error) {
    uiStore.showNotification({
      type: 'error',
      message: error.message || '密码修改失败，请重试'
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: var(--spacing-md);
}

.dialog-container {
  background: var(--md-sys-color-surface-container);
  border-radius: var(--md-sys-shape-corner-large);
  box-shadow: var(--md-sys-elevation-level3);
  width: 100%;
  max-width: 480px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.dialog-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-lg);
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
  background: var(--md-sys-color-surface-container-high);
}

.dialog-header h2 {
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--md-sys-color-on-surface);
  margin: 0;
}

.close-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: transparent;
  border: none;
  color: var(--md-sys-color-on-surface-variant);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.close-button:hover {
  background: var(--md-sys-color-surface-variant);
}

.dialog-content {
  flex: 1;
  overflow-y: auto;
  padding: var(--spacing-lg);
}

.password-form {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.field-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.field-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--md-sys-color-on-surface);
}

.password-input-wrapper {
  position: relative;
}

.field-input {
  width: 100%;
  padding: var(--spacing-md);
  padding-right: 48px;
  border: 1px solid var(--md-sys-color-outline);
  border-radius: var(--md-sys-shape-corner-small);
  font-size: 1rem;
  background: var(--md-sys-color-surface);
  color: var(--md-sys-color-on-surface);
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.field-input:focus {
  outline: none;
  border-color: var(--md-sys-color-primary);
  box-shadow: 0 0 0 1px var(--md-sys-color-primary);
}

.password-toggle {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: transparent;
  border: none;
  color: var(--md-sys-color-on-surface-variant);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.password-toggle:hover {
  background: var(--md-sys-color-surface-variant);
}

.password-strength {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  margin-top: var(--spacing-xs);
}

.strength-bar {
  flex: 1;
  height: 4px;
  background: var(--md-sys-color-surface-variant);
  border-radius: 2px;
  overflow: hidden;
}

.strength-fill {
  height: 100%;
  transition: all 0.3s ease;
  border-radius: 2px;
}

.strength-fill.weak {
  background: var(--md-sys-color-error);
}

.strength-fill.medium {
  background: #ff9800;
}

.strength-fill.strong {
  background: var(--md-sys-color-tertiary);
}

.strength-text {
  font-size: 0.75rem;
  font-weight: 500;
  min-width: 24px;
}

.error-message {
  font-size: 0.75rem;
  color: var(--md-sys-color-error);
  margin-top: var(--spacing-xs);
}

.password-tips {
  background: var(--md-sys-color-surface-variant);
  border-radius: var(--md-sys-shape-corner-small);
  padding: var(--spacing-md);
}

.password-tips h4 {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--md-sys-color-on-surface);
  margin: 0 0 var(--spacing-sm);
}

.password-tips ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.password-tips li {
  font-size: 0.75rem;
  color: var(--md-sys-color-on-surface-variant);
  margin-bottom: var(--spacing-xs);
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
}

.password-tips li:before {
  content: '○';
  color: var(--md-sys-color-outline);
}

.password-tips li.valid {
  color: var(--md-sys-color-tertiary);
}

.password-tips li.valid:before {
  content: '●';
  color: var(--md-sys-color-tertiary);
}

.dialog-actions {
  display: flex;
  gap: var(--spacing-md);
  justify-content: flex-end;
  padding: var(--spacing-lg);
  border-top: 1px solid var(--md-sys-color-outline-variant);
  background: var(--md-sys-color-surface);
}

.cancel-button,
.submit-button {
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--md-sys-shape-corner-medium);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
}

.cancel-button {
  background: transparent;
  color: var(--md-sys-color-on-surface-variant);
  border: 1px solid var(--md-sys-color-outline);
}

.cancel-button:hover {
  background: var(--md-sys-color-surface-variant);
}

.submit-button {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  border: none;
}

.submit-button:hover:not(:disabled) {
  background: var(--md-sys-color-primary-container);
  color: var(--md-sys-color-on-primary-container);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.loading-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .dialog-overlay {
    padding: var(--spacing-sm);
  }
  
  .dialog-actions {
    flex-direction: column;
  }
}
</style> 