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
  <main id="userinfo">
      <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
              <p>사용자 이름: {{ store.userInfo.nickname }}</p>
              <p>이메일 : {{ store.userInfo.email }}</p>
                <!-- <p class="title">FLIP CARD</p> -->
                <!-- <p>Hover Me</p> -->
            </div>
            <div class="flip-card-back">
              <p>사용자 이름: {{ store.userInfo.nickname }}</p>
              <p>이메일 : {{ store.userInfo.email }}</p>
              <p>나이: {{ store.userInfo.age }}</p>
              <p>자산: {{ store.userInfo.money }}원</p>
              <p>연봉: {{ store.userInfo.salary }}원</p>
                <!-- <p class="title">BACK</p> -->
                <!-- <p>Leave Me</p> -->
                <RouterLink :to="{name:'userinfoupdate'}" class="nav-link">
                  <button class="button">
                    <!-- <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 24"> -->
                      <!-- <path d="m18 0 8 12 10-8-4 20H4L0 4l10 8 8-12z"></path> -->
                    <!-- </svg> -->
                    회원정보 수정
                  </button>
                  <!-- <button>회원정보 수정</button> -->
                </RouterLink>
            </div>
        </div>
    </div>
  </main>

  <div>
    <!-- <p>사용자 이름: {{ store.userInfo.nickname }}</p>
    <p>이메일 : {{ store.userInfo.email }}</p>
    <p>나이: {{ store.userInfo.age }}</p>
    <p>자산: {{ store.userInfo.money }}원</p>
    <p>연봉: {{ store.userInfo.salary }}원</p> -->
    <!-- <RouterLink :to="{name:'userinfoupdate'}">
      <button>회원정보 수정</button>
    </RouterLink> -->
    
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
#userinfo {
  display: flex;
  justify-content: center;
}
.flip-card {
  /* position: absolute; */
  background-color: transparent;
  width: 380px;
  height: 508px;
  perspective: 1000px;
  font-family: sans-serif;
  font-size: 20px;
}

.title {
  font-size: 1.5em;
  font-weight: 900;
  text-align: center;
  margin: 0;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  box-shadow: 0 8px 14px 0 rgba(0,0,0,0.2);
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border: 1px solid coral;
  border-radius: 1rem;
}

.flip-card-front {
  background: linear-gradient(120deg, bisque 60%, rgb(255, 231, 222) 88%,
     rgb(255, 211, 195) 40%, rgba(255, 127, 80, 0.603) 48%);
  color: coral;
}

.flip-card-back {
  background: linear-gradient(120deg, rgb(255, 174, 145) 30%, coral 88%,
     bisque 40%, rgb(255, 185, 160) 78%);
  color: white;
  transform: rotateY(180deg);
}

.button {
  font-size: 17px;
  position: absolute;
  bottom: 20px;
  right: 10px;
  left: 10px;
  width: fit-content;
  display: flex;
  margin: auto;
  padding: 0.8em 1.1em;
  gap: 0.4rem;
  border: none;
  font-weight: bold;
  border-radius: 30px;
  cursor: pointer;
  text-shadow: 2px 2px 3px rgb(136 0 136 / 50%);
  background: linear-gradient(
      15deg,
      #880088,
      #aa2068,
      #cc3f47,
      #de6f3d,
      #f09f33,
      #de6f3d,
      #cc3f47,
      #aa2068,
      #880088
    )
    no-repeat;
  background-size: 300%;
  background-position: left center;
  transition: background 0.3s ease;
  color: #fff;
}

.button:hover {
  background-size: 320%;
  background-position: right center;
}

.button:hover svg {
  fill: #fff;
}

.button svg {
  width: 23px;
  fill: #f09f33;
  transition: 0.3s ease;
}
</style>
