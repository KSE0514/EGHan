<template>
  <div>
    <a href="#" @click="showDeposit" class="nav-link">예금</a> |
    <a href="#" @click="showSaving" class="nav-link">적금</a>

    <!-- 하위 컴포넌트를 조건부 렌더링하는 부분 -->
    <div v-if="showingDeposit">
      <ProductList />
    </div>
    <div v-else>
      <SavingProductList />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import ProductList from '@/components/ProductList.vue';
import SavingProductList from '@/components/SavingProductList.vue';

export default {
  components: {
    ProductList,
    SavingProductList
  },
  setup() {
    const showingDeposit = ref(true); // 예금을 표시하는지 여부를 저장하는 변수

    // 예금을 표시하는 함수
    const showDeposit = () => {
      showingDeposit.value = true;
    };

    // 적금을 표시하는 함수
    const showSaving = () => {
      showingDeposit.value = false;
    };

    return {
      showingDeposit,
      showDeposit,
      showSaving
    };
  }
};
</script>

<style scoped>
/* 스타일 정의 */
a{
  font-family:'S-CoreDream-3Light' ;
  text-decoration: none;
  display: inline;
  color: rgba(94, 13, 13, 0.781);
  font-weight: bold;
}

@font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}
</style>
