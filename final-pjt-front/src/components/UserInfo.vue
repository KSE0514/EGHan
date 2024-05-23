<template>
  <main id="userinfo">
      <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
              <p>사용자 이름: {{ store.userInfo.nickname }}</p>
              <p>이메일 : {{ store.userInfo.email }}</p>
            </div>
            <div class="flip-card-back">
              <p>사용자 이름: {{ store.userInfo.nickname }}</p>
              <p>이메일 : {{ store.userInfo.email }}</p>
              <p>나이: {{ store.userInfo.age }}</p>
              <p>자산: {{ store.userInfo.money }}원</p>
              <p>연봉: {{ store.userInfo.salary }}원</p>
                <RouterLink :to="{name:'userinfoupdate'}" class="nav-link">
                  <button class="button">회원정보 수정</button>
                </RouterLink>
            </div>
        </div>
    </div>
  </main>

  <div>
    <div>
      <h5>가입한 예금 상품 목록</h5>
      <ul>
        <li v-for="product in store.userInfo.product_user" :key="product.fin_prdt_cd">
          {{ product.fin_prdt_nm }}
        </li>
      </ul>
    </div>

    <div>
      <h5>가입한 적금 상품 목록</h5>
      <ul>
        <li v-for="product in store.userInfo.savingproduct_user" :key="product.fin_prdt_cd">
          {{ product.fin_prdt_nm }}
        </li>
      </ul>
    </div>

    <canvas ref="chartCanvas"></canvas>

  </div>
</template>

<script setup>
import { onMounted, ref, nextTick } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import Chart from 'chart.js';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const productOptions = ref({});
const savingProductOptions = ref({});
const chartCanvas = ref(null);
const router = useRouter()

const goToDetail = function(productCode){
      router.push(`/product/${productCode}`)
    }


async function fetchProductOptions(fin_prdt_cd) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/deposit-product-options/${fin_prdt_cd}/`);
    productOptions.value[fin_prdt_cd] = response.data;
  } catch (error) {
    console.error(`Failed to fetch product options for ${fin_prdt_cd}`, error);
    console.error('Response data:', error.response ? error.response.data : 'No response data');
  }
}

async function fetchSavingProductOptions(fin_prdt_cd) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/saving-product-options/${fin_prdt_cd}/`);
    savingProductOptions.value[fin_prdt_cd] = response.data;
  } catch (error) {
    console.error(`Failed to fetch saving product options for ${fin_prdt_cd}`, error);
    console.error('Response data:', error.response ? error.response.data : 'No response data');
  }
}

async function fetchAllProductOptions() {
  const productUsers = store.userInfo.product_user || [];
  const savingProductUsers = store.userInfo.savingproduct_user || [];
  const productPromises = productUsers.map(product => fetchProductOptions(product.fin_prdt_cd));
  const savingProductPromises = savingProductUsers.map(product => fetchSavingProductOptions(product.fin_prdt_cd));
  await Promise.all([...productPromises, ...savingProductPromises]);
}

function calculateRatesForProducts() {
  const productRates = [];

  Object.keys(productOptions.value).forEach(fin_prdt_cd => {
    const options = productOptions.value[fin_prdt_cd];
    if (options.length > 0) {
      const avgRate = options.reduce((acc, option) => acc + option.intr_rate, 0) / options.length;
      const maxRate = Math.max(...options.map(option => option.intr_rate2));
      const productName = store.userInfo.product_user.find(product => product.fin_prdt_cd === fin_prdt_cd)?.fin_prdt_nm || 'Unknown Product';
      productRates.push({ product: productName, avgRate, maxRate });
    }
  });

  Object.keys(savingProductOptions.value).forEach(fin_prdt_cd => {
    const options = savingProductOptions.value[fin_prdt_cd];
    if (options.length > 0) {
      const avgRate = options.reduce((acc, option) => acc + option.intr_rate, 0) / options.length;
      const maxRate = Math.max(...options.map(option => option.intr_rate2));
      const productName = store.userInfo.savingproduct_user.find(product => product.fin_prdt_cd === fin_prdt_cd)?.fin_prdt_nm || 'Unknown Product';
      productRates.push({ product: productName, avgRate, maxRate });
    }
    console.log('옵션',options)
  });

  return productRates;
}

function drawChart() {
  const productRates = calculateRatesForProducts();

  const labels = productRates.map(rate => rate.product);
  const avgData = productRates.map(rate => rate.avgRate);
  const maxData = productRates.map(rate => rate.maxRate);

  const ctx = chartCanvas.value.getContext('2d');
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: '평균 우대금리',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        data: avgData,
      },
      {
        label: '최고 우대금리',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        data: maxData,
      },
    ],
  };

  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true,
        min: 0,
        ticks: {
          stepSize: 1,
        },
      },
    },
  };

  new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: chartOptions,
  });
}

onMounted(async () => {
  if (store.isLogin) {
    await store.getUserInfo();
    await fetchAllProductOptions();
    await nextTick();
    drawChart();
  }
});
</script>

<style scoped>
/* 스타일 정의 */
#userinfo {
  display: flex;
  justify-content: center;
}
.flip-card {
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
