<script setup>
import { RouterLink, RouterView,useRouter } from 'vue-router'
import HomeView from './views/HomeView.vue';
import { useCounterStore } from './stores/counter';
import Exchange from './components/Exchange.vue';

const store = useCounterStore()
const router = useRouter()
const gotoHome = function(){
    router.push({name:'home'})
}

</script>

<template>
    <nav id="nav" class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <img src="@/static/EGhan_logo.png" alt="" id="logo" style="height: 50px;" @click="gotoHome">
        <!-- <a class="navbar-brand" href="#" style="color: white; " @click="gotoHome">EGHan</a> -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
            <RouterLink class="nav-link" :to="{name: 'product'}">
                상품 페이지</RouterLink>
            </li>
            <li class="nav-item">
            <RouterLink class="nav-link" :to="{name: 'board'}">
                게시판</RouterLink>
            </li>
            <li class="nav-item">
            <RouterLink class="nav-link" :to="{name: 'map'}">
                지도</RouterLink>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">환율 계산기</a>
            </li>
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">환율 계산기</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <Exchange />
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
        </ul>
        <RouterLink class="nav-link" :to="{name:'signup'}" v-if="!store.isLogin">
            회원가입 |
        </RouterLink> 
        <RouterLink class="nav-link" :to="{name:'login'}" v-if="!store.isLogin">
            로그인 |
        </RouterLink> 
        <a href="#" class="nav-link" @click="store.logout" v-if="store.isLogin">로그아웃</a>
        <RouterLink class="nav-link" :to="{name:'user'}" v-if="store.isLogin">
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
#nav {
    padding: 15px;
    height: 80px; 
    border-bottom-right-radius: 5%; 
    border-bottom-left-radius: 5%; 
    border-bottom: 3px solid rgb(255, 201, 100); 
    background-color: #ffffff !important;
}
.nav-link {
    margin: 5px;
    color : rgb(153, 38, 0);
    /* font-family: 'April16th-Life'; */
    font-family: 'WavvePADO-Regular';
}
.nav-link:hover {
    font-size: 20px;
    height: 100%;
    color: rgb(255, 0, 0);
    /* border: 2px solid black; */
    /* -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgb(255, 208, 0); */
    /* background-color: rgb(255, 201, 100); */
    /* font-family: 'WavvePADO-Regular'; */
}

@font-face {
    font-family: 'April16th-Life';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404-2@1.0/April16th-Life.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}

@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
</style>
