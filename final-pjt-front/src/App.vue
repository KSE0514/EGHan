<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue';
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
    <nav>
        <RouterLink :to="{name:'signup'}">
            회원가입
        </RouterLink> |
        <RouterLink :to="{name:'login'}">
            로그인
        </RouterLink> |
        <a @click="store.logout">로그아웃</a>
    </nav>

<RouterView />
    <!-- <HomeView /> -->
</template>

<style scoped>

</style>
