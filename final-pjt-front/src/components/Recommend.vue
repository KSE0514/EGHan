<template>
  <div>
    <h1>추천 상품</h1>
    <br>
    <label for="age">
      <input type="radio" name="recommend" value="age" v-model="selectedOption" @click="recommend_age">
      <span>연령대별</span>
    </label>

    <label for="salary">
      <input type="radio" name="recommend" value="salary" v-model="selectedOption" @click="recommend_salary">
      <span>소득별</span>
    </label>


    <label for="money">
      <input type="radio" name="recommend" value="money" v-model="selectedOption" @click="recommend_money">
      <span>자산별</span>
    </label>

    <div v-if="selectedOption === 'age'">
      <br>
      <h3>추천 예금</h3>
      <div v-for="product in recommendedDeposit" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-for="product in recommendedSaving" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
    </div>

    <div v-if="selectedOption === 'salary'">
      <br>
      <h3>추천 예금</h3>
      <div v-for="product in recommendedDeposit_s" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-for="product in recommendedSaving_s" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
    </div>

    <div v-if="selectedOption === 'money'">
      <br>
      <h3>추천 예금</h3>
      <div v-for="product in recommendedDeposit_m" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-for="product in recommendedSaving_m" :key="product.id">
        <ul>
          <li @click="goToDetail(product.fin_prdt_cd)">
            {{ product.fin_prdt_nm }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<!-- <script>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue'



const recommend = function(){
  const store = useCounterStore()
  // const recommendedProducts = ref([])
  axios({
    method:'get',
    url:`${API_URL}/api/v1/recommend-age/`,
    headers:{
        Authorization:`Token ${store.token.value}`
        // Authorization: 'Token 111111'
      }
  }).then((response)=>{
    // recommendedProducts.value = response.data
    console.log('정보',response.data)
  }).catch((error)=>{
    console.log(error)
  })
}



</script> -->

<script setup>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const selectedOption = ref(null);

const store = useCounterStore();
const recommendedDeposit = ref([])
const recommendedSaving = ref([])
const recommend_age = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/recommend-age/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log('정보', response.data);
    recommendedDeposit.value = response.data.recommended_deposit_products
    recommendedSaving.value = response.data.recommended_saving_products
  }).catch((error) => {
    console.log(error);
  });
};

const recommendedDeposit_s = ref([])
const recommendedSaving_s = ref([])
const recommend_salary = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/recommend-salary/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log('정보', response.data);
    recommendedDeposit_s.value = response.data.recommended_deposit_products
    recommendedSaving_s.value = response.data.recommended_saving_products
  }).catch((error) => {
    console.log(error);
  });
};


const recommendedDeposit_m = ref([])
const recommendedSaving_m = ref([])
const recommend_money = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/recommend-money/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log('정보', response.data);
    recommendedDeposit_m.value = response.data.recommended_deposit_products
    recommendedSaving_m.value = response.data.recommended_saving_products
  }).catch((error) => {
    console.log(error);
  });
};



const router = useRouter()
const goToDetail = function(productCode){
    router.push(`/product/${productCode}`)
}



// onMounted(()=>{
//   recommend()
// })

</script>
