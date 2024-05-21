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
    <p v-if="loginError" style="color: red;">로그인 정보가 일치하지 않습니다. 다시 시도해주세요.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const username = ref(null)
const password = ref(null)
const loginError = ref(false)

const login = function() {
  const payload ={
    username:username.value,
    password:password.value,
  }
  store.logIn(payload)
    .catch((error) => {
      loginError.value = true; // 로그인 실패 시 로그인 오류를 표시
    });
}
</script>

<style scoped>

</style>
