<template>
    <div>  
      <label for="age">나이:</label>
      <input type="number" v-model="age" id="age" required><br>

      <label for="money">자산:</label>
      <input type="number" v-model="money" id="money" required><br>

      <label for="salary">연봉:</label>
      <input type="number" v-model="salary" id="salary" required><br>

      <label for="financial_products">가입한 상품 목록:</label>
      <textarea v-model="financial_products" id="financial_products"></textarea><br>
  
      <button @click="submitSignUp">회원가입</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router';

  const props = defineProps(['email', 'username', 'password','nickname']);
  
  const age = ref(null);
  const money = ref(null)
  const salary = ref(null)
  const financial_products = ref(null)
  
  const errorMessage = ref('')


  const store = useCounterStore()
  const router = useRouter()

  const submitSignUp = function() {
    //회원가입 처리 로직
    if (!age.value || !money.value || !salary.value){
        errorMessage.value = '모든 정보를 입력해주세요.'
        return
    } 
    console.log('회원가입 정보:', {
      email: props.email,
      username: props.username,
      password: props.password,
      nickname: props.nickname,
      age:age.value,
      money:money.value
    });
    const payload = {
        email: props.email,
        username: props.username,
        password: props.password,
        nickname: props.nickname,
        age:age.value,
        money:money.value,
        salary:salary.value,
        financial_products:financial_products.value,
    }
    store.signUp(payload)    
    // router.push('/')
  };
  </script>
  
  <style scoped>
  /* 추가 스타일 */
  </style>
  