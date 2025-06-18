<template>
  <div class="mobile-settings-view">
    <!-- Header with back button -->
    <div class="settings-header">
      <button class="back-button" @click="goBack">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
      </button>
      <h1 class="page-title">Settings</h1>
    </div>

    <!-- Settings Form -->
    <div class="settings-form">
      <!-- Currency Settings -->
      <div class="form-section">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">CURRENCY STAT</label>
            <select v-model="settings.currencyStat" class="form-select">
              <option value="ETH/USD">ETH/USD</option>
              <option value="BTC/USD">BTC/USD</option>
              <option value="EUR/USD">EUR/USD</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">SELECT EXCHANGE</label>
            <select v-model="settings.exchange" class="form-select">
              <option value="">Select</option>
              <option value="binance">Binance</option>
              <option value="coinbase">Coinbase</option>
              <option value="kraken">Kraken</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Trade Date -->
      <div class="form-section">
        <div class="form-group">
          <label class="form-label">TRADE DATE</label>
          <select v-model="settings.tradeDate" class="form-select">
            <option value="">Select</option>
            <option value="today">Today</option>
            <option value="yesterday">Yesterday</option>
            <option value="this-week">This Week</option>
            <option value="this-month">This Month</option>
          </select>
        </div>
      </div>

      <!-- Trade Price and Quantity -->
      <div class="form-section">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">TRADE PRICE</label>
            <select v-model="settings.tradePrice" class="form-select">
              <option value="">Select</option>
              <option value="market">Market Price</option>
              <option value="limit">Limit Price</option>
              <option value="stop">Stop Price</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">QUANTITY</label>
            <select v-model="settings.quantity" class="form-select">
              <option value="1">1</option>
              <option value="5">5</option>
              <option value="10">10</option>
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Current Price and Total -->
      <div class="form-section">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">CURRENT PRICE</label>
            <input 
              v-model="settings.currentPrice" 
              type="number" 
              step="0.01" 
              class="form-input"
              placeholder="435.90"
            />
          </div>
          <div class="form-group">
            <label class="form-label">TOTAL PRICE</label>
            <input 
              v-model="totalPrice" 
              type="number" 
              step="0.01" 
              class="form-input"
              readonly
            />
          </div>
        </div>
      </div>

      <!-- Toggle Settings -->
      <div class="form-section">
        <div class="toggle-item">
          <span class="toggle-label">PRIMARY SETTING</span>
          <label class="toggle-switch">
            <input type="checkbox" v-model="settings.primarySetting">
            <span class="toggle-slider"></span>
          </label>
        </div>
        
        <div class="toggle-item">
          <span class="toggle-label">SECONDARY SETTING</span>
          <label class="toggle-switch">
            <input type="checkbox" v-model="settings.secondarySetting">
            <span class="toggle-slider"></span>
          </label>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-buttons">
        <button class="buy-button" @click="buyCoin">
          Buy Coin
        </button>
        <button class="sell-button" @click="sellCoin">
          Sell Coin
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Settings data
const settings = ref({
  currencyStat: 'ETH/USD',
  exchange: '',
  tradeDate: '',
  tradePrice: '',
  quantity: '1',
  currentPrice: 435.90,
  primarySetting: true,
  secondarySetting: false
})

// Computed
const totalPrice = computed(() => {
  return (parseFloat(settings.value.currentPrice) * parseFloat(settings.value.quantity)).toFixed(2)
})

// Methods
const goBack = () => {
  router.go(-1)
}

const buyCoin = () => {
  console.log('Buy coin with settings:', settings.value)
  // Implement buy logic
}

const sellCoin = () => {
  console.log('Sell coin with settings:', settings.value)
  // Implement sell logic
}
</script>

<style scoped>
.mobile-settings-view {
  min-height: 100vh;
  background: var(--md-sys-color-surface);
  padding: 0 var(--spacing-lg);
}

.settings-header {
  display: flex;
  align-items: center;
  padding: var(--spacing-lg) 0 var(--spacing-md) 0;
  gap: var(--spacing-md);
}

.back-button {
  width: 40px;
  height: 40px;
  border: none;
  background: none;
  border-radius: var(--md-sys-shape-corner-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--md-sys-color-on-surface);
  transition: background-color var(--transition-short);
}

.back-button:hover {
  background-color: var(--md-sys-color-surface-container);
}

.page-title {
  font-size: var(--md-sys-typescale-headline-medium-font-size);
  font-weight: var(--md-sys-typescale-headline-medium-font-weight);
  color: var(--md-sys-color-on-surface);
  margin: 0;
}

.settings-form {
  padding-bottom: var(--spacing-xl);
}

.form-section {
  margin-bottom: var(--spacing-xl);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-md);
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: var(--md-sys-typescale-label-small-font-size);
  font-weight: var(--md-sys-typescale-label-small-font-weight);
  color: var(--md-sys-color-on-surface-variant);
  margin-bottom: var(--spacing-xs);
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.form-select,
.form-input {
  height: 56px;
  padding: 0 var(--spacing-md);
  border: 1px solid var(--md-sys-color-outline);
  border-radius: var(--md-sys-shape-corner-small);
  background: var(--md-sys-color-surface);
  color: var(--md-sys-color-on-surface);
  font-size: var(--md-sys-typescale-body-large-font-size);
  font-family: var(--md-sys-typescale-font-family);
  transition: border-color var(--transition-short);
}

.form-select:focus,
.form-input:focus {
  outline: none;
  border-color: var(--md-sys-color-primary);
  border-width: 2px;
}

.form-input[readonly] {
  background-color: var(--md-sys-color-surface-container);
  color: var(--md-sys-color-on-surface-variant);
}

.toggle-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md) 0;
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
}

.toggle-item:last-child {
  border-bottom: none;
}

.toggle-label {
  font-size: var(--md-sys-typescale-body-medium-font-size);
  color: var(--md-sys-color-on-surface-variant);
  letter-spacing: 0.5px;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 52px;
  height: 32px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--md-sys-color-surface-variant);
  border-radius: 32px;
  transition: background-color var(--transition-short);
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 24px;
  width: 24px;
  left: 4px;
  bottom: 4px;
  background-color: var(--md-sys-color-outline);
  border-radius: 50%;
  transition: transform var(--transition-short), background-color var(--transition-short);
}

input:checked + .toggle-slider {
  background-color: var(--md-sys-color-primary);
}

input:checked + .toggle-slider:before {
  transform: translateX(20px);
  background-color: var(--md-sys-color-on-primary);
}

.action-buttons {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-md);
  margin-top: var(--spacing-xl);
  padding-top: var(--spacing-lg);
}

.buy-button,
.sell-button {
  height: 56px;
  border: none;
  border-radius: var(--md-sys-shape-corner-medium);
  font-size: var(--md-sys-typescale-label-large-font-size);
  font-weight: var(--md-sys-typescale-label-large-font-weight);
  cursor: pointer;
  transition: background-color var(--transition-short);
}

.buy-button {
  background-color: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
}

.buy-button:hover {
  background-color: var(--md-sys-color-primary-container);
}

.sell-button {
  background-color: transparent;
  color: var(--md-sys-color-primary);
  border: 1px solid var(--md-sys-color-primary);
}

.sell-button:hover {
  background-color: var(--md-sys-color-primary-container);
}
</style> 