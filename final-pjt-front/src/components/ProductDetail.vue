<!-- <template>
  <div v-if="product_detail !== null">
    <h2>{{ product_detail.fin_prdt_nm }}</h2>
    <p>가입 방법: {{ product_detail.join_way }}</p>
    <p>은행명: {{ product_detail.kor_co_nm }}</p>
    <pre>상세 정보: {{ product_detail.etc_note }}</pre>
    <button v-if="show" @click="signDeposit">가입 취소</button>
    <button v-else @click="signDeposit">가입 신청</button>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { defineProps, onMounted, ref, vModelCheckbox, watch } from 'vue';
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
        check()
      })
      .catch((error) => {
        console.log(error);
      });
  }
};

const show = ref(false)

const check = function(){
  store.getUserInfo()
  if (product_detail.value.user.includes(store.userInfo.pk)){
    show.value = true
  }
}

const signDeposit = function() {
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/deposit-product-detail/${props.productCode}/${store.userInfo.pk}/`
  }).then((response)=>{
    console.log('가입 완료 or 취소')
    const result = get_product_detail()
    product_detail.value = result.value
    show.value = !show.value
    console.log('show',show.value)
  }).catch((error)=>{
    console.log(error)
  })
}

console.log(show)
onMounted(() => {
  get_product_detail();
  // check()
  console.log('새로고침',product_detail.value)
});

watch(() => show.value, (newValue) => {
  console.log('show 변경:', newValue);
});

watch(() => props.productCode, () => {
  get_product_detail();
});
</script>

<style scoped>
/* 스타일 정의 */
</style> -->


<template>
  <div v-if="product_detail !== null">
    <h2>{{ product_detail.fin_prdt_nm }}</h2>
    <p>가입 방법: {{ product_detail.join_way }}</p>
    <p>은행명: {{ product_detail.kor_co_nm }}</p>
    <pre>상세 정보: {{ product_detail.etc_note }}</pre>
    <button v-if="show" @click="signDeposit">가입 취소</button>
    <button v-else @click="signDeposit">가입 신청</button>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { defineProps, onMounted, ref, vModelCheckbox, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';

const props = defineProps({
  productCode: String,
});

const store = useCounterStore();

const product_detail = ref(null);

const get_product_detail = () => {
  if (props.productCode) {
    return axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/deposit-product-detail/${props.productCode}/`,
    })
      .then((response) => {
        console.log('응답데이터', response.data);
        product_detail.value = response.data;
        check()
        return response.data; // Return the response data
      })
      .catch((error) => {
        console.log(error);
      });
  }
};

const show = ref(false)

const check = function(){
  store.getUserInfo()
  if (product_detail.value.user.includes(store.userInfo.pk)){
    show.value = true
  }else{
    show.value = false
  }
  return show.value
}

const signDeposit = function() {
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/deposit-product-detail/${props.productCode}/${store.userInfo.pk}/`
  }).then((response)=>{
    console.log('가입 완료 or 취소')
    get_product_detail().then((result) => { // Use the returned value here
      product_detail.value = result;
      check()
      console.log('show', show.value);
      console.log(product_detail.value)
    });
  }).catch((error)=>{
    console.log(error)
  })
}

console.log(show)
onMounted(() => {
  get_product_detail();
  // check()
});

watch(() => show.value, (newValue) => {
  console.log('show 변경:', newValue);
});

watch(() => props.productCode, () => {
  get_product_detail();
});
</script>

<style scoped>
/* 스타일 정의 */
</style>
