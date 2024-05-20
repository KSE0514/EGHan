<!-- <template>
    <div>
        <form @submit.prevent="goToStep2">
            <label for="email">email:</label>
            <input type="email" v-model="email" id="email" required><br>

            <label for="username">ID:</label>
            <input type="text" v-model="username" id="username" required><br>

            <label for="password1">password:</label>
            <input type="password" v-model="password1" id="password1" required><br>

            <label for="password2">password confirmation:</label>
            <input type="password" v-model="password2" id="password2" required><br>

            <label for="nickname">이름:</label>
            <input type="text" v-model="nickname" id="nickname" required><br>

            <button type="submit" v-if="!showStep2">다음</button>
        </form>
    </div>

    <div v-if="showStep2">
      <SignUpStep2 :email="email" :username="username" :password="password1" :nickname="nickname"/>
    </div>

</template>

<script setup>
import { useRoute,useRouter } from 'vue-router'
import { ref } from 'vue'
import SignUpStep2 from './SignUpStep2.vue';
const router = useRouter()
const username =ref(null)
const email =ref(null)
const password1 =ref(null)
const password2 = ref(null)
const nickname = ref(null)

const showStep2 = ref(false)

const goToStep2 = function(){
    if (password1.value != password2.value){
        window.alert('비밀번호가 일치하지 않습니다.')
        return
    }
    showStep2.value = true
}
</script>

<style scoped>

</style> -->


<template>
  <div class="signup-container">
    <form @submit.prevent="goToStep2" class="signup-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required>
      </div>

      <div class="form-group">
        <label for="username">ID:</label>
        <input type="text" v-model="username" id="username" required>
      </div>

      <div class="form-group">
        <label for="password1">Password:</label>
        <input type="password" v-model="password1" id="password1" required>
      </div>

      <div class="form-group">
        <label for="password2">Confirm Password:</label>
        <input type="password" v-model="password2" id="password2" required>
      </div>

      <div class="form-group">
        <label for="nickname">Name:</label>
        <input type="text" v-model="nickname" id="nickname" required>
      </div>

      <button type="submit" v-if="!showStep2" class="submit-button">Next</button>
    </form>
  </div>
</template>
<script setup>
import { useRoute,useRouter } from 'vue-router'
import { ref } from 'vue'
import SignUpStep2 from './SignUpStep2.vue';
const router = useRouter()
const username =ref(null)
const email =ref(null)
const password1 =ref(null)
const password2 = ref(null)
const nickname = ref(null)

const showStep2 = ref(false)

const goToStep2 = function(){
    if (password1.value != password2.value){
        window.alert('비밀번호가 일치하지 않습니다.')
        return
    }
    showStep2.value = true
}
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.signup-form {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button.submit-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button.submit-button:hover {
  background-color: #0056b3;
}
</style>
