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
    <p style="margin: 0px;">상세 정보:</p>
    <pre><strong>{{ product_detail.etc_note }}</strong></pre>
    <button id="btn-id" v-if="show" @click="signDeposit">가입 취소</button>
    <button id="btn-id" v-else @click="signDeposit">가입 신청</button>
  </div>
  <!-- <div v-else>
    <p>Loading...</p>
  </div> -->
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
      url: `${store.API_URL}/api/v1/saving-product-detail/${props.productCode}/`,
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
  store.get_user_info()
  if (product_detail.value.user.includes(store.profile.pk)){
    show.value = true
  }else{
    show.value = false
  }
  return show.value
}

const signDeposit = function() {
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/saving-product-detail/${props.productCode}/${store.profile.pk}/`
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
h2 {
  /* color: rgb(236, 0, 0); */
  font-family: 'WavvePADO-Regular';
}

h5{
  font-family: 'S-CoreDream-3Light';
  font-weight: bolder;
}
p{
  font-weight: bolder;
  font-family: 'S-CoreDream-3Light';
}
@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}


#btn-id {
  height: 40px;
  padding: 5px 15px;
 /* padding: 15px 25px; */
 border: unset;
 border-radius: 15px;
 color: #212121;
 z-index: 1;
 background: #fffaf4;
 position: relative;
 font-weight: 1000;
 font-size: 15px;
 -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 transition: all 250ms;
 overflow: hidden;
}

#btn-id::before {
 content: "";
 position: absolute;
 top: 0;
 left: 0;
 height: 100%;
 width: 0;
 border-radius: 15px;
 background-color: #ffb89e;
 z-index: -1;
 -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 transition: all 250ms
}

#btn-id:hover {
 color: #ffffff;
}

#btn-id:hover::before {
 width: 100%;
}
</style>
