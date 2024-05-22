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

    <!-- <canvas ref="chartCanvas"></canvas> -->

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';

const store = useCounterStore()



// function drawChart() {
//   // 가입한 상품의 금리 정보를 가져와서 labels와 data 배열에 저장합니다.
//   const products = store.userInfo.product_user;
//   const labels = products.map(product => product.fin_prdt_nm);
//   const data = products.map(product => product.금리_정보_키); // 실제로는 해당 키를 바꿔야 합니다.

//   // 차트를 그리기 위한 데이터 설정
//   const ctx = document.getElementById('chartCanvas').getContext('2d');
//   const chartData = {
//     labels: labels,
//     datasets: [{
//       label: '금리 정보',
//       backgroundColor: 'rgba(255, 99, 132, 0.2)',
//       borderColor: 'rgba(255, 99, 132, 1)',
//       borderWidth: 1,
//       data: data,
//     }],
//   };

//   // 차트 옵션 설정
//   const chartOptions = {
//     scales: {
//       y: {
//         beginAtZero: true,
//       },
//     },
//   };

//   // 차트 객체 생성
//   new Chart(ctx, {
//     type: 'bar',
//     data: chartData,
//     options: chartOptions,
//   });
// }



onMounted(() => {
  if (store.isLogin) {
    store.getUserInfo()
    // drawChart()
  }
})

console.log('사용자 정보',store.userInfo)
</script>

<style scoped>
/* 스타일 정의 */
</style>
