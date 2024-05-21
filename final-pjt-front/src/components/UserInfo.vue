<!-- <template>
    <div>
      <p>사용자 이름: {{  store.userInfo.nickname }}</p>
      <p>이메일 : {{ store.userInfo.email }}</p>
      <p>나이: {{ store.userInfo.age }}</p>

      <p>자산: {{ store.userInfo.money }}원</p>
      <p>연봉: {{ store.userInfo.salary }}원</p>
      <RouterLink :to="{name:'userinfoupdate'}"><button>회원정보 수정</button></RouterLink>
    </div>
    <div v-for="product in store.userInfo.financial_products">
      <h5>가입한 상품 목록</h5>
      <ul>
        <li>{{ product }}</li>
      </ul>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
const store = useCounterStore()

onMounted(()=>{
  if (store.isLogin){
    store.getUserInfo()
  }
})
</script>

<style scoped>

</style> -->


<template>
  <div>
    <p>사용자 이름: {{ store.userInfo.nickname }}</p>
    <p>이메일 : {{ store.userInfo.email }}</p>
    <p>나이: {{ store.userInfo.age }}</p>
    <p>자산: {{ store.userInfo.money }}원</p>
    <p>연봉: {{ store.userInfo.salary }}원</p>
    <RouterLink :to="{name:'userinfoupdate'}">
      <button>회원정보 수정</button>
    </RouterLink>
    
    <div>
      <h5>가입한 적금 상품 목록</h5>
      <ul>
        <li v-for="product in store.userInfo.product_user" :key="product.fin_prdt_cd">
          {{ product.fin_prdt_nm }}
        </li>
      </ul>
    </div>

    <div>
      <h5>가입한 예금 상품 목록</h5>
      <ul>
        <li v-for="product in store.userInfo.savingproduct_user" :key="product.fin_prdt_cd">
          {{ product.fin_prdt_nm }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';

const store = useCounterStore()

onMounted(() => {
  if (store.isLogin) {
    store.getUserInfo()
  }
})

console.log('사용자 정보',store.userInfo)
</script>

<style scoped>
/* 스타일 정의 */
</style>
