<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue';
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
    <nav>
        <RouterLink :to="{name:'signup'}" v-if="!store.isLogin">
            회원가입 |
        </RouterLink> 
        <RouterLink :to="{name:'login'}" v-if="!store.isLogin">
            로그인 |
        </RouterLink> 
        <a href="#" @click="store.logout" v-if="store.isLogin">로그아웃</a>
        <RouterLink :to="{name:'user'}" v-if="store.isLogin">
            내정보
        </RouterLink>
    </nav>

<RouterView />
    <!-- <HomeView /> -->
</template>

<style scoped>

</style>
