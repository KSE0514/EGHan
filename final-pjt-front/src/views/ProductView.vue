<template>
  <div>
    <a href="#" @click="showDeposit">예금</a> |
    <a href="#" @click="showSaving">적금</a>

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
</style>
