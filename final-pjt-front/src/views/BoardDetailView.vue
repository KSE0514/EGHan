<template>
  <div v-if="article">
    <!-- <h1>{{ route.params.id }}번 게시글 DetailView</h1> -->
    <h1>{{ article.title }}</h1>
    <p>작성자: {{ article.username }}</p>
    <p class="p">작성일: {{ article.created_at }}</p>
    <p class="p">마지막 수정일: {{ article.updated_at }}</p>
    <div style="border: 1px solid gray; height: 100px; padding: 10px; border-radius: 10px;">{{ article.content }}</div>
    <br>
    <RouterLink :to="{name: 'board'}" class="nav-link" style="display: inline-block;">
      <button class="back">
        <svg class="svg-icon" fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g stroke="#ff342b" stroke-linecap="round" stroke-width="1.5"><path d="m3.33337 10.8333c0 3.6819 2.98477 6.6667 6.66663 6.6667 3.682 0 6.6667-2.9848 6.6667-6.6667 0-3.68188-2.9847-6.66664-6.6667-6.66664-1.29938 0-2.51191.37174-3.5371 1.01468"></path><path d="m7.69867 1.58163-1.44987 3.28435c-.18587.42104.00478.91303.42582 1.0989l3.28438 1.44986"></path></g></svg>
        <span class="lable1">뒤로가기</span>
      </button>
      <!-- <button>뒤로가기</button> -->
    </RouterLink>
    <RouterLink 
      :to="{name: 'board-update', params:{id: article.id}}"
    class="nav-link" style="display: inline-block;">
    <button v-if="article.user === store.userInfo.id"  @click="update_article(article.id)" class="btn">
      <svg class="svg-icon" fill="none" height="20" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g stroke="#a649da" stroke-linecap="round" stroke-width="2"><path d="m20 20h-16"></path><path clip-rule="evenodd" d="m14.5858 4.41422c.781-.78105 2.0474-.78105 2.8284 0 .7811.78105.7811 2.04738 0 2.82843l-8.28322 8.28325-3.03046.202.20203-3.0304z" fill-rule="evenodd"></path></g></svg>
      <span class="lable">수정</span>
    </button></RouterLink>
    <button v-if="article.user === store.userInfo.id"  @click="delete_article" class="back">
      <svg class="svg" height="512" viewBox="0 0 512 512" width="512" xmlns="http://www.w3.org/2000/svg"></svg>
      <!-- <svg class="svg-icon" fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g stroke="#ff342b" stroke-linecap="round" stroke-width="1.5"><path d="m3.33337 10.8333c0 3.6819 2.98477 6.6667 6.66663 6.6667 3.682 0 6.6667-2.9848 6.6667-6.6667 0-3.68188-2.9847-6.66664-6.6667-6.66664-1.29938 0-2.51191.37174-3.5371 1.01468"></path><path d="m7.69867 1.58163-1.44987 3.28435c-.18587.42104.00478.91303.42582 1.0989l3.28438 1.44986"></path></g></svg> -->
        <span class="lable1">삭제</span>
    </button>
    <button v-if="article.user === store.userInfo.id"  @click="delete_article">삭제</button>
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
  width: 120px;
  border: none;
  background: #ff362b34;
  border-radius: 20px;
  cursor: pointer;
}

.lable1 {
  line-height: 20px;
  font-size: 15px;
  color: #FF342B;
  font-family: sans-serif;
  letter-spacing: 1px;
}

.back:hover {
  background: #ff362b52;
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
</style>