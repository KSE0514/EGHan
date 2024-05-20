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
import { onMounted, ref } from 'vue';

const store = useCounterStore()
const email = ref('')
const nickname = ref('')
const username = ref('')
const password = ref('')
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const financial_products = ref('')

onMounted(async () => {
  if (store.isLogin) {
    await store.getUserInfo()
    // store.getUserInfo()가 완료된 후에 값을 설정
    email.value = store.userInfo.email
    nickname.value = store.userInfo.nickname
    username.value = store.userInfo.username
    age.value = store.userInfo.age
    money.value = store.userInfo.money
    salary.value = store.userInfo.salary
    financial_products.value = store.userInfo.financial_products
  }
})

const handleSubmit = () => {
  store.updateProfile({
    email: email.value,
    username: username.value,
    password: password.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    financial_products: financial_products.value
  })
}
</script>

<style scoped>

</style>
