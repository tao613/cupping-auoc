<template>
  <div class="new-sample-view">
    <div class="page-header">
      <h1>Sample Information</h1>
      <router-link to="/samples" class="back-link">
        <i class="el-icon-arrow-left"></i> Back to Samples
      </router-link>
    </div>
    
    <div class="form-container">
      <el-form @submit.prevent="saveSample" label-position="top">
        <div class="form-section">
          <h3>Sample info</h3>
          
          <div class="form-row">
            <el-form-item label="Sample name">
              <el-input 
                v-model="form.name"
                placeholder="Write sample initial here"
              />
            </el-form-item>
            
            <el-form-item label="Country">
              <el-select v-model="form.country" placeholder="Select country" filterable>
                <el-option
                  v-for="country in countries"
                  :key="country.value"
                  :label="country.label"
                  :value="country.value"
                />
              </el-select>
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Sample type">
              <el-select v-model="form.type" placeholder="Select type">
                <el-option label="Green" value="green" />
                <el-option label="Roasted" value="roasted" />
                <el-option label="Ground" value="ground" />
              </el-select>
            </el-form-item>
            
            <el-form-item label="Sample Grade">
              <el-select v-model="form.grade" placeholder="Select grade">
                <el-option label="A" value="A" />
                <el-option label="AA" value="AA" />
                <el-option label="AAA" value="AAA" />
                <el-option label="B" value="B" />
                <el-option label="C" value="C" />
              </el-select>
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Purchase Grade">
              <el-input v-model="form.purchaseGrade" placeholder="Enter purchase grade" />
            </el-form-item>
            
            <el-form-item label="Supplier/Manufacturer">
              <el-input v-model="form.supplier" placeholder="Enter supplier" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Producer name">
              <el-input v-model="form.producer" placeholder="Enter producer name" />
            </el-form-item>
            
            <el-form-item label="Purchase Contract Reference #">
              <el-input v-model="form.purchaseRef" placeholder="Enter reference number" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Strategy">
              <el-input v-model="form.strategy" placeholder="Enter strategy" />
            </el-form-item>
            
            <el-form-item label="Customer">
              <el-input v-model="form.customer" placeholder="Enter customer" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Customer Code">
              <el-input v-model="form.customerCode" placeholder="Enter customer code" />
            </el-form-item>
            
            <el-form-item label="Sales Contracts Reference #">
              <el-input v-model="form.salesRef" placeholder="Enter reference number" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Received date">
              <el-date-picker
                v-model="form.receivedDate"
                type="date"
                placeholder="Select date"
              />
            </el-form-item>
            
            <el-form-item label="Date of Dispatch">
              <el-date-picker
                v-model="form.dispatchDate"
                type="date"
                placeholder="Select date"
              />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Date of Arrival">
              <el-date-picker
                v-model="form.arrivalDate"
                type="date"
                placeholder="Select date"
              />
            </el-form-item>
            
            <el-form-item label="Date of Results">
              <el-date-picker
                v-model="form.resultsDate"
                type="date"
                placeholder="Select date"
              />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Harvest">
              <el-input v-model="form.harvest" placeholder="Enter harvest" />
            </el-form-item>
            
            <el-form-item label="External Identification">
              <el-input v-model="form.externalId" placeholder="Enter external ID" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Reference number">
              <el-input v-model="form.referenceNumber" placeholder="Enter reference number" />
            </el-form-item>
            
            <el-form-item label="Sample Reference">
              <el-input v-model="form.sampleReference" placeholder="Enter sample reference" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Coffee processing">
              <el-input v-model="form.processing" placeholder="Enter processing method" />
            </el-form-item>
            
            <el-form-item label="Certification">
              <el-input v-model="form.certification" placeholder="Enter certification" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Preferred cupping protocol">
              <el-select v-model="form.protocol" placeholder="Select protocol">
                <el-option label="Arabica" value="arabica" />
                <el-option label="Robusta" value="robusta" />
                <el-option label="SCA" value="sca" />
              </el-select>
            </el-form-item>
            
            <el-form-item label="Species">
              <el-select v-model="form.species" placeholder="Select species">
                <el-option label="Arabica" value="arabica" />
                <el-option label="Robusta" value="robusta" />
                <el-option label="Blend" value="blend" />
              </el-select>
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Varietals">
              <el-input v-model="form.varietals" placeholder="Enter varietals" />
            </el-form-item>
            
            <el-form-item label="Received weight">
              <div class="input-with-unit">
                <el-input v-model="form.receivedWeight" placeholder="Enter weight" />
                <span class="unit">gr</span>
              </div>
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Crop year">
              <el-select v-model="form.cropYear" placeholder="Select year">
                <el-option
                  v-for="year in cropYears"
                  :key="year"
                  :label="year"
                  :value="year"
                />
              </el-select>
            </el-form-item>
            
            <el-form-item label="Number of bags">
              <el-input v-model="form.bagCount" placeholder="Enter number of bags" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Bag weight">
              <div class="input-with-unit">
                <el-input v-model="form.bagWeight" placeholder="Enter weight" />
                <span class="unit">kg</span>
              </div>
            </el-form-item>
            
            <el-form-item label="Moisture">
              <div class="input-with-unit">
                <el-input v-model="form.moisture" placeholder="Enter moisture" />
                <span class="unit">%</span>
              </div>
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Water activity">
              <el-input v-model="form.waterActivity" placeholder="Enter water activity" />
            </el-form-item>
            
            <el-form-item label="Density">
              <div class="input-with-unit">
                <el-input v-model="form.density" placeholder="Enter density" />
                <span class="unit">g/L</span>
              </div>
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Temperature">
              <el-input v-model="form.temperature" placeholder="Enter temperature" />
            </el-form-item>
            
            <el-form-item label="Mass">
              <div class="input-with-unit">
                <el-input v-model="form.mass" placeholder="Enter mass" />
                <span class="unit">gr</span>
              </div>
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Volume">
              <div class="input-with-unit">
                <el-input v-model="form.volume" placeholder="Enter volume" />
                <span class="unit">mL</span>
              </div>
            </el-form-item>
            
            <el-form-item label="Warehouse">
              <el-input v-model="form.warehouse" placeholder="Enter warehouse" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Sample Location">
              <el-input v-model="form.location" placeholder="Enter location" />
            </el-form-item>
            
            <el-form-item label="Shipment Month">
              <el-date-picker
                v-model="form.shipmentMonth"
                type="month"
                placeholder="Select month"
              />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Cargo/Seal #">
              <el-input v-model="form.cargoSeal" placeholder="Enter cargo/seal number" />
            </el-form-item>
            
            <el-form-item label="Container Number">
              <el-input v-model="form.containerNumber" placeholder="Enter container number" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row">
            <el-form-item label="Lot Number/ICO Marks">
              <el-input v-model="form.lotNumber" placeholder="Enter lot number" />
            </el-form-item>
            
            <el-form-item label="Courier">
              <el-input v-model="form.courier" placeholder="Enter courier" />
            </el-form-item>
          </div>
          
          <div class="form-row">
            <el-form-item label="Tracking Number">
              <el-input v-model="form.trackingNumber" placeholder="Enter tracking number" />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-section">
          <div class="form-row full-width">
            <el-form-item label="Notes and remarks">
              <el-input
                v-model="form.notes"
                type="textarea"
                rows="4"
                placeholder="Enter notes and remarks"
              />
            </el-form-item>
          </div>
          
          <div class="form-row full-width">
            <el-form-item label="Description">
              <el-input
                v-model="form.description"
                type="textarea"
                rows="4"
                placeholder="Enter description"
              />
            </el-form-item>
          </div>
        </div>
        
        <div class="form-actions">
          <el-button type="primary" native-type="submit" :loading="loading">Save</el-button>
          <el-button @click="cancel">Discard</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useSamplesStore } from '@/stores/samples.store'
import { useUiStore } from '@/stores/ui.store'

const router = useRouter()
const samplesStore = useSamplesStore()
const uiStore = useUiStore()

const loading = ref(false)

// 国家列表
const countries = [
  { value: 'brazil', label: 'Brazil' },
  { value: 'colombia', label: 'Colombia' },
  { value: 'ethiopia', label: 'Ethiopia' },
  { value: 'guatemala', label: 'Guatemala' },
  { value: 'honduras', label: 'Honduras' },
  { value: 'indonesia', label: 'Indonesia' },
  { value: 'kenya', label: 'Kenya' },
  { value: 'mexico', label: 'Mexico' },
  { value: 'peru', label: 'Peru' },
  { value: 'vietnam', label: 'Vietnam' }
]

// 年份列表
const currentYear = new Date().getFullYear()
const cropYears = Array.from({ length: 10 }, (_, i) => (currentYear - 5 + i).toString())

const form = reactive({
  name: '',
  country: '',
  type: '',
  grade: '',
  purchaseGrade: '',
  supplier: '',
  producer: '',
  purchaseRef: '',
  strategy: '',
  customer: '',
  customerCode: '',
  salesRef: '',
  receivedDate: null,
  dispatchDate: null,
  arrivalDate: null,
  resultsDate: null,
  harvest: '',
  externalId: '',
  referenceNumber: '',
  sampleReference: '',
  processing: '',
  certification: '',
  protocol: '',
  species: '',
  varietals: '',
  receivedWeight: '',
  cropYear: currentYear.toString(),
  bagCount: '',
  bagWeight: '',
  moisture: '',
  waterActivity: '',
  density: '',
  temperature: '',
  mass: '',
  volume: '',
  warehouse: '',
  location: '',
  shipmentMonth: null,
  cargoSeal: '',
  containerNumber: '',
  lotNumber: '',
  courier: '',
  trackingNumber: '',
  notes: '',
  description: ''
})

const saveSample = async () => {
  if (!form.name) {
    uiStore.addNotification({
      type: 'error',
      message: 'Sample name is required'
    })
    return
  }
  
  loading.value = true
  
  try {
    await samplesStore.createSample(form)
    
    uiStore.addNotification({
      type: 'success',
      message: 'Sample created successfully'
    })
    
    router.push('/samples')
  } catch (error) {
    uiStore.addNotification({
      type: 'error',
      message: error.message || 'Failed to create sample'
    })
  } finally {
    loading.value = false
  }
}

const cancel = () => {
  router.push('/samples')
}
</script>

<style scoped>
.new-sample-view {
  padding: var(--spacing-md);
}

.back-link {
  display: inline-flex;
  align-items: center;
  margin-bottom: var(--spacing-md);
  color: var(--color-primary);
  
  i {
    margin-right: var(--spacing-xs);
  }
}

.form-container {
  background-color: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
}

.form-section {
  margin-bottom: var(--spacing-xl);
  
  h3 {
    font-size: 1.1rem;
    margin-bottom: var(--spacing-md);
  }
}

.form-row {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  
  @media (min-width: 768px) {
    flex-direction: row;
    
    .el-form-item {
      flex: 1;
      margin-bottom: 0;
    }
  }
  
  &.full-width {
    flex-direction: column;
    
    @media (min-width: 768px) {
      flex-direction: column;
    }
  }
}

.input-with-unit {
  display: flex;
  align-items: center;
  
  .unit {
    margin-left: var(--spacing-sm);
    color: var(--color-text-secondary);
  }
}

.form-actions {
  display: flex;
  gap: var(--spacing-md);
  margin-top: var(--spacing-xl);
}
</style>
