<template>
  <div v-if="product_detail !== null">
    <h2>{{ product_detail.fin_prdt_nm }}</h2>
    <p>가입 방법: {{ product_detail.join_way }}</p>
    <p>은행명: {{ product_detail.kor_co_nm }}</p>
    <pre>상세 정보: {{ product_detail.etc_note }}</pre>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { defineProps, onMounted, ref, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';

const props = defineProps({
  productCode: String,
});

const store = useCounterStore();

const product_detail = ref(null);

const get_product_detail = () => {
  if (props.productCode) {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/deposit-product-detail/${props.productCode}/`,
    })
      .then((response) => {
        console.log('응답데이터', response.data);
        product_detail.value = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
};

onMounted(() => {
  get_product_detail();
});

watch(() => props.productCode, () => {
  get_product_detail();
});
</script>

<style scoped>
/* 스타일 정의 */
</style>
