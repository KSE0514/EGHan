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
      <div v-if="!recommendedDeposit.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedDeposit" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-if="!recommendedSaving.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedSaving" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
          </li>
        </ul>
      </div>
    </div>

    <div v-if="selectedOption === 'salary'">
      <br>
      <h3>추천 예금</h3>
      <div v-if="!recommendedDeposit_s.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedDeposit_s" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-if="!recommendedSaving_s.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedSaving_s" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
          </li>
        </ul>
      </div>
    </div>

    <div v-if="selectedOption === 'money'">
      <br>
      <h3>추천 예금</h3>
      <div v-if="!recommendedDeposit_m.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedDeposit_m" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
          </li>
        </ul>
      </div>
      <hr>
      <h3>추천 적금</h3>
      <div v-if="!recommendedSaving_m.length">
        <div class="loader"></div>
      </div>
      <div v-for="product in recommendedSaving_m" :key="product.id">
        <ul>
          <li>
            {{ product.fin_prdt_nm }}
            <span>
            <button @click="goToDetail(product.fin_prdt_cd)">가입하러가기</button></span>
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

<style>
.loader {
  display: block;
  --height-of-loader: 4px;
  --loader-color: #0071e2;
  width: 130px;
  height: var(--height-of-loader);
  border-radius: 30px;
  background-color: rgba(0,0,0,0.2);
  position: relative;
}

.loader::before {
  content: "";
  position: absolute;
  background: var(--loader-color);
  top: 0;
  left: 0;
  width: 0%;
  height: 100%;
  border-radius: 30px;
  animation: moving 1s ease-in-out infinite;
  ;
}

@keyframes moving {
  50% {
    width: 100%;
  }

  100% {
    width: 0;
    right: 0;
    left: unset;
  }
}
/* .spinner {
  font-size: 28px;
  position: relative;
  display: inline-block;
  width: 1em;
  height: 1em;
} */

/* 
.spinner.center {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
}

.spinner .spinner-blade {
  position: absolute;
  left: 0.4629em;
  bottom: 0;
  width: 0.074em;
  height: 0.2777em;
  border-radius: 0.0555em;
  background-color: transparent;
  -webkit-transform-origin: center -0.2222em;
  -ms-transform-origin: center -0.2222em;
  transform-origin: center -0.2222em;
  animation: spinner-fade9234 1s infinite linear;
}

.spinner .spinner-blade:nth-child(1) {
  -webkit-animation-delay: 0s;
  animation-delay: 0s;
  -webkit-transform: rotate(0deg);
  -ms-transform: rotate(0deg);
  transform: rotate(0deg);
}

.spinner .spinner-blade:nth-child(2) {
  -webkit-animation-delay: 0.083s;
  animation-delay: 0.083s;
  -webkit-transform: rotate(30deg);
  -ms-transform: rotate(30deg);
  transform: rotate(30deg);
}

.spinner .spinner-blade:nth-child(3) {
  -webkit-animation-delay: 0.166s;
  animation-delay: 0.166s;
  -webkit-transform: rotate(60deg);
  -ms-transform: rotate(60deg);
  transform: rotate(60deg);
}

.spinner .spinner-blade:nth-child(4) {
  -webkit-animation-delay: 0.249s;
  animation-delay: 0.249s;
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}

.spinner .spinner-blade:nth-child(5) {
  -webkit-animation-delay: 0.332s;
  animation-delay: 0.332s;
  -webkit-transform: rotate(120deg);
  -ms-transform: rotate(120deg);
  transform: rotate(120deg);
}

.spinner .spinner-blade:nth-child(6) {
  -webkit-animation-delay: 0.415s;
  animation-delay: 0.415s;
  -webkit-transform: rotate(150deg);
  -ms-transform: rotate(150deg);
  transform: rotate(150deg);
}

.spinner .spinner-blade:nth-child(7) {
  -webkit-animation-delay: 0.498s;
  animation-delay: 0.498s;
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}

.spinner .spinner-blade:nth-child(8) {
  -webkit-animation-delay: 0.581s;
  animation-delay: 0.581s;
  -webkit-transform: rotate(210deg);
  -ms-transform: rotate(210deg);
  transform: rotate(210deg);
}

.spinner .spinner-blade:nth-child(9) {
  -webkit-animation-delay: 0.664s;
  animation-delay: 0.664s;
  -webkit-transform: rotate(240deg);
  -ms-transform: rotate(240deg);
  transform: rotate(240deg);
}

.spinner .spinner-blade:nth-child(10) {
  -webkit-animation-delay: 0.747s;
  animation-delay: 0.747s;
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}

.spinner .spinner-blade:nth-child(11) {
  -webkit-animation-delay: 0.83s;
  animation-delay: 0.83s;
  -webkit-transform: rotate(300deg);
  -ms-transform: rotate(300deg);
  transform: rotate(300deg);
}

.spinner .spinner-blade:nth-child(12) {
  -webkit-animation-delay: 0.913s;
  animation-delay: 0.913s;
  -webkit-transform: rotate(330deg);
  -ms-transform: rotate(330deg);
  transform: rotate(330deg);
}

@keyframes spinner-fade9234 {
  0% {
    background-color: #69717d;
  }

  100% {
    background-color: transparent;
  }
} */

</style>