<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <label for="email">email:</label>
      <input type="email" v-model="email" id="email" required><br>

      <label for="username">ID:</label>
      <input type="text" v-model="username" id="username" required><br>

      <label for="password">password:</label>
      <input type="password" v-model="password" id="password" required><br>

      <label for="nickname">이름:</label>
      <input type="text" v-model="nickname" id="nickname" required><br>

      <label for="age">나이:</label>
      <input type="number" v-model="age" id="age" required><br>

      <label for="money">자산:</label>
      <input type="number" v-model="money" id="money" required><br>

      <label for="salary">연봉:</label>
      <input type="number" v-model="salary" id="salary" required><br>

      <label for="financial_products">가입한 상품 목록:</label>
      <textarea v-model="financial_products" id="financial_products"></textarea>
      <br>
      <button>회원 정보 수정</button>
    </form>
  </div>

</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted,ref } from 'vue';

const store = useCounterStore()
const email = store.userInfo.email
const nickname = store.userInfo.nickname
const username = store.userInfo.username
const password = ref(null)
const age = store.userInfo.age
const money = store.userInfo.money
const salary = store.userInfo.salary
const financial_products = store.userInfo.financial_products

onMounted(()=>{
  if (store.isLogin){
    store.getUserInfo()
  }
})

const handleSubmit = () => {
  store.updateProfile({ email, username, password, nickname,age,money,salary,financial_products })
}
</script>

<style scoped>

</style>