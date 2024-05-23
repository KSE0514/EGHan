<script setup>
import { RouterLink, RouterView,useRouter } from 'vue-router'
import HomeView from './views/HomeView.vue';
import { useCounterStore } from './stores/counter';
import Exchange from './components/Exchange.vue';
import ChatComponent from '@/components/ChatComponent.vue'
import { ref } from 'vue'

const isclick = ref(false)

const buttonclick = function() {
    isclick.value = !isclick.value
}


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

        <!-- 챗봇 -->
    <button v-if="isclick" @click="buttonclick" style="width: 53px; height: 30px; background-color: rgb(253, 253, 253) !important; position: fixed; left: 96%; top: 870px; border: 1px solid rgb(209, 209, 209); border-radius: 5px;">닫기</button>
    <ChatComponent v-if="isclick" class="fixedchat"/>
    <button v-else class="button" @click="buttonclick" style="position: fixed;">
        <p class="svgIcon" style="color: white; font-size: 20px;">?</p>
    </button>
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
    color : rgb(0, 0, 0);
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

ul, li {
    list-style: none;
}

li.on{
    color: red;
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


.fixedchat {
    position: fixed;
    left: 84%;
    bottom: 50px;
    max-height: 500px;
    overflow-y: auto;
}

/* -----chat gpt 버튼 스타일 ----- */
.button {

    left: 88%;
    top: 830px;
    /* bottom: 5px; */
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: rgb(255, 201, 51);
  border: none;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 0px 0px 4px rgba(255, 183, 76, 0.253);
  cursor: pointer;
  transition-duration: 0.3s;
  overflow: hidden;
  position: relative;
}

.svgIcon {
  width: 12px;
  transition-duration: 0.3s;
}

.svgIcon path {
  fill: white;
}

.button:hover {
  width: 170px;
  border-radius: 50px;
  transition-duration: 0.3s;
  background-color: rgb(255, 192, 156);
  align-items: center;
}

.button:hover .svgIcon {
  /* width: 20px; */
  transition-duration: 0.3s;
  transform: translateY(-200%);
}

.button::before {
  position: absolute;
  bottom: -20px;
  content: "궁금한 게 있으신가요?";
  color: white;
  /* transition-duration: .3s; */
  font-size: 0px;
}

.button:hover::before {
    padding: 10px;
  font-size: 13px;
  opacity: 1;
  bottom: unset;
  /* transform: translateY(-30px); */
  transition-duration: 0.3s;
}
/* --------------------------------- */
</style>
