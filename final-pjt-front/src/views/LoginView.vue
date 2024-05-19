<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="login">
      <label for="username">ID:</label>
      <input type="text" v-model="username" id="username" required><br>

      <label for="password">PASSWORD:</label>
      <input type="password" v-model="password" id="password" required><br>

      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const login = function() {
  const payload ={
    username:username.value,
    password:password.value,
  }
  store.logIn(payload)
}

</script>

<style scoped>

</style>