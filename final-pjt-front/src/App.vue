<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue';
</script>

<template>
    <nav>
        <RouterLink :to="{name:'signup'}">
            회원가입
        </RouterLink> |
        <RouterLink :to="{name:'login'}">
            로그인
        </RouterLink> |
        <a href="#">로그아웃</a>
    </nav>

<RouterView />
    <!-- <HomeView /> -->
</template>

<style scoped>

</style>
