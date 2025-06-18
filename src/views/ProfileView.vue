<template>
  <div class="settings-view">
    <div class="settings-container">
      <!-- Page Header -->
      <div class="page-header">
        <h1 class="page-title">Setting</h1>
      </div>

      <!-- Tab Navigation -->
      <div class="tab-navigation">
        <button 
          v-for="tab in tabs" 
          :key="tab.key"
          class="tab-button"
          :class="{ active: activeTab === tab.key }"
          @click="activeTab = tab.key"
        >
          {{ tab.label }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="tab-content">
        <!-- Edit Profile Tab -->
        <div v-if="activeTab === 'profile'" class="tab-pane">
          <div class="profile-form">
            <!-- Left Side - Avatar Section -->
            <div class="avatar-section">
              <div class="avatar-wrapper">
                <div class="avatar">
                  <img 
                    v-if="profileData.avatar" 
                    :src="profileData.avatar" 
                    :alt="profileData.name || 'User Avatar'"
                  />
                  <div v-else class="avatar-placeholder">
                    {{ getInitials(profileData.name || user.name) }}
                  </div>
                </div>
                <button class="avatar-edit-btn" @click="changeAvatar">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
                    <circle cx="12" cy="13" r="4"/>
                  </svg>
                </button>
              </div>
              <div class="user-info">
                <h3 class="user-name">{{ profileData.name || user.name || 'User' }}</h3>
                <p class="user-role">{{ profileData.certification_level || 'Coffee Enthusiast' }}</p>
              </div>
            </div>

            <!-- Right Side - Form Fields -->
            <div class="form-section">
              <form @submit.prevent="saveProfile">
                <!-- Name Section -->
                <div class="form-row">
                  <div class="form-group">
                    <label class="form-label">First Name</label>
                    <input
                      v-model="profileData.firstName"
                      type="text"
                      class="form-input"
                      placeholder="Enter first name"
                    />
                  </div>
                  <div class="form-group">
                    <label class="form-label">Last Name</label>
                    <input
                      v-model="profileData.lastName"
                      type="text"
                      class="form-input"
                      placeholder="Enter last name"
                    />
                  </div>
                </div>

                <!-- Email -->
                <div class="form-group">
                  <label class="form-label">Email Address</label>
                  <input
                    v-model="profileData.email"
                    type="email"
                    class="form-input"
                    placeholder="Enter email address"
                  />
                </div>

                <!-- Phone -->
                <div class="form-group">
                  <label class="form-label">Phone Number</label>
                  <input
                    v-model="profileData.phone"
                    type="tel"
                    class="form-input"
                    placeholder="Enter phone number"
                  />
                </div>

                <!-- Personal Address Section -->
                <h4 class="section-title">Personal Address</h4>
                
                <div class="form-row">
                  <div class="form-group">
                    <label class="form-label">Country</label>
                    <input
                      v-model="profileData.country"
                      type="text"
                      class="form-input"
                      placeholder="Enter country"
                    />
                  </div>
                  <div class="form-group">
                    <label class="form-label">City</label>
                    <input
                      v-model="profileData.city"
                      type="text"
                      class="form-input"
                      placeholder="Enter city"
                    />
                  </div>
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label class="form-label">Address</label>
                    <input
                      v-model="profileData.address"
                      type="text"
                      class="form-input"
                      placeholder="Enter address"
                    />
                  </div>
                  <div class="form-group">
                    <label class="form-label">Zip Code</label>
                    <input
                      v-model="profileData.zipCode"
                      type="text"
                      class="form-input"
                      placeholder="Enter zip code"
                    />
                  </div>
                </div>

                <!-- Professional Info -->
                <h4 class="section-title">Professional Information</h4>
                
                <div class="form-row">
                  <div class="form-group">
                    <label class="form-label">Certification Level</label>
                    <input
                      v-model="profileData.certification_level"
                      type="text"
                      class="form-input"
                      placeholder="e.g., Q Grader, SCA Certified"
                    />
                  </div>
                  <div class="form-group">
                    <label class="form-label">Experience Years</label>
                    <input
                      v-model.number="profileData.experience_years"
                      type="number"
                      class="form-input"
                      placeholder="Years of experience"
                      min="0"
                      max="50"
                    />
                  </div>
                </div>

                <div class="form-group">
                  <label class="form-label">Bio</label>
                  <textarea
                    v-model="profileData.bio"
                    class="form-textarea"
                    placeholder="Tell us about your coffee journey..."
                    rows="4"
                  ></textarea>
                </div>

                <!-- Save Button -->
                <div class="form-actions">
                  <button 
                    type="submit" 
                    class="save-button"
                    :disabled="isLoading"
                  >
                    <span v-if="isLoading" class="loading-spinner"></span>
                    {{ isLoading ? 'Saving...' : 'Save Changes' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>

        <!-- Preferences Tab -->
        <div v-if="activeTab === 'preferences'" class="tab-pane">
          <div class="preferences-content">
            <h3>Preferences</h3>
            <p>Customize your application preferences here.</p>
            <!-- Add preferences content -->
          </div>
        </div>

        <!-- Security Tab -->
        <div v-if="activeTab === 'security'" class="tab-pane">
          <div class="security-content">
            <h3>Security Settings</h3>
            <div class="security-actions">
              <button class="action-button" @click="showChangePassword">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                  <circle cx="12" cy="16" r="1"/>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                </svg>
                <span>Change Password</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Data Privacy Tab -->
        <div v-if="activeTab === 'privacy'" class="tab-pane">
          <div class="privacy-content">
            <h3>Data Privacy</h3>
            <p>Manage your data privacy settings here.</p>
            <!-- Add privacy content -->
          </div>
        </div>
      </div>
    </div>

    <!-- Change Password Dialog -->
    <ChangePasswordDialog 
      v-model="showPasswordDialog"
      @success="onPasswordChanged"
    />
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { useUiStore } from '@/stores/ui.store'
import ChangePasswordDialog from '@/components/user/ChangePasswordDialog.vue'

const authStore = useAuthStore()
const uiStore = useUiStore()

// Tab management
const activeTab = ref('profile')
const tabs = [
  { key: 'profile', label: 'Edit Profile' },
  { key: 'preferences', label: 'Preferences' },
  { key: 'security', label: 'Security' },
  { key: 'privacy', label: 'Data Privacy' }
]

// Form state
const isLoading = ref(false)
const showPasswordDialog = ref(false)

// User data
const user = computed(() => authStore.user)
const profileData = reactive({
  firstName: '',
  lastName: '',
  name: '',
  username: '',
  email: '',
  phone: '',
  country: '',
  city: '',
  address: '',
  zipCode: '',
  certification_level: '',
  experience_years: null,
  bio: '',
  avatar: ''
})

// Initialize data on mount
onMounted(() => {
  loadUserProfile()
})

/**
 * Load user profile data
 */
const loadUserProfile = async () => {
  try {
    await authStore.refreshUserInfo()
    
    // Split name into first and last name
    const fullName = user.value.name || ''
    const nameParts = fullName.split(' ')
    
    // Fill form data
    Object.assign(profileData, {
      firstName: nameParts[0] || '',
      lastName: nameParts.slice(1).join(' ') || '',
      name: user.value.name || '',
      username: user.value.username || '',
      email: user.value.email || '',
      phone: user.value.phone || '',
      country: user.value.country || '',
      city: user.value.city || '',
      address: user.value.address || '',
      zipCode: user.value.zipCode || '',
      certification_level: user.value.certification_level || '',
      experience_years: user.value.experience_years || null,
      bio: user.value.bio || '',
      avatar: user.value.avatar || ''
    })
  } catch (error) {
    uiStore.showNotification({
      type: 'error',
      message: 'Failed to load user information'
    })
  }
}

/**
 * Save profile data
 */
const saveProfile = async () => {
  isLoading.value = true
  
  try {
    // Combine first and last name
    const fullName = `${profileData.firstName} ${profileData.lastName}`.trim()
    
    const updateData = {
      ...profileData,
      name: fullName
    }
    
    await authStore.updateProfile(updateData)
    
    uiStore.showNotification({
      type: 'success',
      message: 'Profile updated successfully'
    })
  } catch (error) {
    uiStore.showNotification({
      type: 'error',
      message: error.message || 'Update failed, please try again'
    })
  } finally {
    isLoading.value = false
  }
}

/**
 * Change avatar
 */
const changeAvatar = () => {
  // TODO: Implement avatar upload
  uiStore.showNotification({
    type: 'info',
    message: 'Avatar upload feature coming soon'
  })
}

/**
 * Show change password dialog
 */
const showChangePassword = () => {
  showPasswordDialog.value = true
}

/**
 * Password change success callback
 */
const onPasswordChanged = () => {
  uiStore.showNotification({
    type: 'success',
    message: 'Password changed successfully'
  })
}

/**
 * Get user initials for avatar placeholder
 */
const getInitials = (name) => {
  if (!name) return 'U'
  return name.split(' ')
    .map(word => word.charAt(0))
    .join('')
    .toUpperCase()
    .slice(0, 2)
}
</script>

<style scoped>
.settings-view {
  background: var(--md-sys-color-surface);
  min-height: 100vh;
}

.settings-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: var(--spacing-xl);
}

.page-header {
  margin-bottom: var(--spacing-xl);
}

.page-title {
  font-size: var(--md-sys-typescale-display-small-font-size);
  font-weight: var(--md-sys-typescale-display-small-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0;
}

/* Tab Navigation */
.tab-navigation {
  display: flex;
  gap: var(--spacing-xs);
  margin-bottom: var(--spacing-xl);
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
}

.tab-button {
  padding: var(--spacing-md) var(--spacing-lg);
  background: none;
  border: none;
  border-radius: var(--md-sys-shape-corner-medium) var(--md-sys-shape-corner-medium) 0 0;
  font-size: var(--md-sys-typescale-body-large-font-size);
  font-weight: var(--md-sys-typescale-body-large-font-weight);
  color: var(--md-sys-color-on-surface-variant);
  cursor: pointer;
  transition: all var(--transition-short);
  position: relative;
}

.tab-button:hover {
  background: var(--md-sys-color-primary-container);
  color: var(--md-sys-color-on-primary-container);
}

.tab-button.active {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
}

.tab-button.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--md-sys-color-primary);
}

/* Tab Content */
.tab-content {
  background: var(--md-sys-color-surface-container-low);
  border-radius: var(--md-sys-shape-corner-large);
  overflow: hidden;
  box-shadow: var(--md-sys-elevation-level1);
}

.tab-pane {
  padding: var(--spacing-xl);
}

/* Profile Form */
.profile-form {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: var(--spacing-xl);
}

/* Avatar Section */
.avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-lg);
  padding: var(--spacing-xl);
  background: var(--md-sys-color-surface-container);
  border-radius: var(--md-sys-shape-corner-large);
}

.avatar-wrapper {
  position: relative;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  background: var(--md-sys-color-primary-container);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  font-size: 2.5rem;
  font-weight: 600;
  color: var(--md-sys-color-on-primary-container);
}

.avatar-edit-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 36px;
  height: 36px;
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-short);
  box-shadow: var(--md-sys-elevation-level2);
}

.avatar-edit-btn:hover {
  background: var(--md-sys-color-primary-container);
  color: var(--md-sys-color-on-primary-container);
  transform: scale(1.1);
}

.user-info {
  text-align: center;
}

.user-name {
  font-size: var(--md-sys-typescale-title-large-font-size);
  font-weight: var(--md-sys-typescale-title-large-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0 0 var(--spacing-sm);
}

.user-role {
  font-size: var(--md-sys-typescale-body-medium-font-size);
  color: var(--md-sys-color-on-surface-variant);
  margin: 0;
}

/* Form Section */
.form-section {
  background: var(--md-sys-color-surface-container);
  border-radius: var(--md-sys-shape-corner-large);
  padding: var(--spacing-xl);
}

.section-title {
  font-size: var(--md-sys-typescale-title-medium-font-size);
  font-weight: var(--md-sys-typescale-title-medium-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: var(--spacing-xl) 0 var(--spacing-lg);
}

.section-title:first-child {
  margin-top: 0;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-lg);
}

.form-group {
  margin-bottom: var(--spacing-lg);
}

.form-label {
  display: block;
  font-size: var(--md-sys-typescale-body-medium-font-size);
  font-weight: 500;
  color: var(--md-sys-color-on-surface);
  margin-bottom: var(--spacing-sm);
}

.form-input,
.form-textarea {
  width: 100%;
  padding: var(--spacing-md);
  border: 1px solid var(--md-sys-color-outline-variant);
  border-radius: var(--md-sys-shape-corner-medium);
  background: var(--md-sys-color-surface-container-highest);
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-body-large-font-size);
  transition: all var(--transition-short);
  box-sizing: border-box;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--md-sys-color-primary);
  box-shadow: 0 0 0 2px var(--md-sys-color-primary-container);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  margin-top: var(--spacing-xl);
  display: flex;
  justify-content: flex-end;
}

.save-button {
  padding: var(--spacing-md) var(--spacing-xl);
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  border: none;
  border-radius: var(--md-sys-shape-corner-medium);
  font-size: var(--md-sys-typescale-label-large-font-size);
  font-weight: var(--md-sys-typescale-label-large-font-weight);
  cursor: pointer;
  transition: all var(--transition-short);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  min-width: 140px;
  justify-content: center;
}

.save-button:hover:not(:disabled) {
  background: var(--md-sys-color-primary-container);
  color: var(--md-sys-color-on-primary-container);
}

.save-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Security Content */
.security-content,
.preferences-content,
.privacy-content {
  max-width: 600px;
}

.security-content h3,
.preferences-content h3,
.privacy-content h3 {
  font-size: var(--md-sys-typescale-title-large-font-size);
  font-weight: var(--md-sys-typescale-title-large-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0 0 var(--spacing-lg);
}

.security-actions {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.action-button {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  padding: var(--spacing-md) var(--spacing-lg);
  background: var(--md-sys-color-surface-container);
  border: 1px solid var(--md-sys-color-outline-variant);
  border-radius: var(--md-sys-shape-corner-medium);
  color: var(--md-sys-color-on-surface);
  text-decoration: none;
  cursor: pointer;
  transition: all var(--transition-short);
  font-size: var(--md-sys-typescale-body-large-font-size);
}

.action-button:hover {
  background: var(--md-sys-color-surface-container-high);
  border-color: var(--md-sys-color-outline);
}

.action-button span {
  flex: 1;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .settings-container {
    padding: var(--spacing-lg);
  }
  
  .profile-form {
    grid-template-columns: 1fr;
    gap: var(--spacing-lg);
  }
  
  .avatar-section {
    order: -1;
  }
  
  .form-row {
    grid-template-columns: 1fr;
    gap: var(--spacing-md);
  }
  
  .tab-navigation {
    flex-wrap: wrap;
    gap: var(--spacing-xs);
  }
  
  .tab-button {
    flex: 1;
    min-width: 120px;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .tab-button {
    padding: var(--spacing-sm);
    font-size: var(--md-sys-typescale-body-medium-font-size);
  }
  
  .avatar {
    width: 100px;
    height: 100px;
  }
  
  .avatar-placeholder {
    font-size: 2rem;
  }
}
</style>
