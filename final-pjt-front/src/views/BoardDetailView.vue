<template>
  <div v-if="article">
    <!-- <h1>{{ route.params.id }}번 게시글 DetailView</h1> -->
    <h1>{{ article.title }}</h1>
    <p>작성자: {{ article.username }}</p>
    <p class="p">작성일: {{ article.created_at }}</p>
    <p class="p">마지막 수정일: {{ article.updated_at }}</p>
    <div style="margin-top: 10px; border: 1px solid gray; height: 100px; padding: 10px; border-radius: 10px;">{{ article.content }}</div>
    <br>
    <RouterLink :to="{name: 'board'}" class="nav-link" style="display: inline-block;">
      <button class="back">
        <span style="color: white;"><strong>←</strong></span>
        <!-- <svg class="svg-icon" fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g stroke="#ff342b" stroke-linecap="round" stroke-width="1.5"><path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path></g></svg> -->
        <span class="lable1" style="color: white;">이전</span>
      </button>
      <!-- <button>뒤로가기</button> -->
    </RouterLink>
    <div style="display: inline-block; width: 78%;"></div>
    <RouterLink 
      :to="{name: 'board-update', params:{id: article.id}}"
    class="nav-link" style="display: inline-block;">
    <button v-if="article.user === store.userInfo.id"  @click="update_article(article.id)" class="btn">
      <!-- <svg class="svg-icon" fill="none" height="20" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g stroke="#a649da" stroke-linecap="round" stroke-width="2"><path d="m20 20h-16"></path><path clip-rule="evenodd" d="m14.5858 4.41422c.781-.78105 2.0474-.78105 2.8284 0 .7811.78105.7811 2.04738 0 2.82843l-8.28322 8.28325-3.03046.202.20203-3.0304z" fill-rule="evenodd"></path></g></svg> -->
      <span><strong>✏</strong></span> 
      <span class="lable">수정</span>
    </button></RouterLink>

    <!-- 삭제 -->
    <div class="nav-link" style="display: inline-block;">
      <button class="delete" v-if="article.user === store.userInfo.id"  @click="delete_article">
        <!-- <svg class="svg-icon" fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g stroke="#ff342b" stroke-linecap="round" stroke-width="1.5"><path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path></g></svg> -->
        <span style="color: rgb(182, 0, 0);"><strong>X</strong></span>
        <span class="lable2" style="color: rgb(182, 0, 0);">삭제</span>
      </button></div>
    <!-- <button v-if="article.user === store.userInfo.id"  @click="delete_article">삭제</button> -->
    <hr>
    <!-- 댓글 -->
    
    <!-- <p>{{ article }}</p> -->
  </div>
  <Comments />
</template>

<script setup>
import Comments from '@/components/Comments.vue'
import BoardUpdateView from '@/views/BoardUpdateView.vue'

import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
const store = useCounterStore()
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
const API_URL = store.API_URL
const id = route.params.id
import { ref } from 'vue'

const article = ref(null)

const detail = function() {
  console.log(`${API_URL}/boards/detail/${id}/`)
  axios({
    method: 'get',
    url: `${API_URL}/boards/detail/${id}/`
  })
    .then((res) => {
      console.log(res)
      article.value = res.data
    })
}

import { onMounted } from 'vue'

onMounted(() => {
  detail()
  store.getUserInfo()
})

const delete_article = function() {
  axios({
    method: 'delete',
    url: `${API_URL}/boards/detail/${id}/`
  })
  .then((res) =>{
    console.log('삭제 완료')
    router.push({name: 'board'})
  })
}

// const update_article = function (article_id) {
//   axios({
//     method: 'put',
//     url: `${API_URL}/boards/detail/${id}`
//   })
//   .then((res) =>{
//     console.log('수정 완료')
//     router.push({name: 'board-detail', params: {id: article_id}})
//   })
// }

</script>

<style scoped>
p{
  font-family:'S-CoreDream-3Light' ;
}
  .p {
    margin: 5px 0; /* 위아래 여백을 5px로 설정 */
    color: gray;
  }


  @font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}




.btn {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 12px;
  gap: 2px;
  height: 30px;
  width: 85px;
  border: none;
  background: #a549da3d;
  border-radius: 20px;
  cursor: pointer;
}

.lable {
  line-height: 22px;
  font-size: 15px;
  color: #A649DA;
  font-family: sans-serif;
  letter-spacing: 1px;
}

.button:hover {
  background: #a549da62;
}

.button:hover .svg-icon {
  animation: lr 1s linear infinite;
}

@keyframes lr {
  0% {
    transform: translateX(0);
  }

  25% {
    transform: translateX(-1px);
  }

  75% {
    transform: translateX(1px);
  }

  100% {
    transform: translateX(0);
  }
}

/* 뒤로가기 버튼 */
.back {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 6px 12px;
  gap: 8px;
  height: 30px;
  width: 90px;
  border: none;
  background: #56565634;
  border-radius: 20px;
  cursor: pointer;
}

.lable1 {
  line-height: 20px;
  font-size: 15px;
  color: #2f2f2f;
  font-family: sans-serif;
  letter-spacing: 1px;
}

.back:hover {
  background: #e1e1e152;
}

.back:hover span {
  color: black !important;
}

.back:hover .svg-icon {
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(-360deg);
  }
}


/* 삭제 */
.delete {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 6px 12px;
  gap: 8px;
  height: 30px;
  width: 90px;
  border: none;
  background: #ff000039;
  border-radius: 20px;
  cursor: pointer;
}

.lable2 {
  line-height: 20px;
  font-size: 15px;
  color: #2f2f2f;
  font-family: sans-serif;
  letter-spacing: 1px;
}

.delete:hover {
  background: #ffc7c752;
}

.delete:hover span {
  color: rgb(147, 0, 0) !important;
}

.delete:hover .svg-icon {
  animation: spin 2s linear infinite;
}

</style>