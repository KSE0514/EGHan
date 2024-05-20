<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue';
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
    <nav id="nav" class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: rgb(109, 185, 255) !important;">
    <div class="container-fluid">
        <a class="navbar-brand" href="#" style="color: white; ">EGHan</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
            <RouterLink class="nav-link" :to="{name: 'product'}" style="color: white; ">
                상품 페이지</RouterLink>
            </li>
            <li class="nav-item">
            <RouterLink class="nav-link" :to="{name: 'board'}" style="color: white; ">
                게시판</RouterLink>
            </li>
            <li class="nav-item">
            <!-- <RouterLink class="nav-link" :to="{name: 'calculator'}"  style="color: white; ">
                환율 계산기</RouterLink> -->
            </li>
        </ul>
        <RouterLink class="nav-link" :to="{name:'signup'}" v-if="!store.isLogin">
            회원가입 |
        </RouterLink> 
        <RouterLink class="nav-link" :to="{name:'login'}" v-if="!store.isLogin">
            로그인 |
        </RouterLink> 
        <a href="#" class="nav-link" @click="store.logout" v-if="store.isLogin">로그아웃</a>
        <RouterLink :to="{name:'user'}" v-if="store.isLogin">
            내정보
        </RouterLink>
    <!-- 내정보 -->
        </div>
    </div>
    </nav>
<main class="container">
    <div style="margin: 20px;">
    <RouterView />
    </div>
</main>
    <!-- <HomeView /> -->
</template>

<style scoped>

</style>
