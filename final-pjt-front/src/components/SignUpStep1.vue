<template>
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

</style>