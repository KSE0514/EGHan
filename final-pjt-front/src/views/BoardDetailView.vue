<template>
  <div v-if="article">
    <!-- <h1>{{ route.params.id }}번 게시글 DetailView</h1> -->
    <h1>{{ article.title }}</h1>
    <p>작성자: {{ article.username }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>마지막 수정일: {{ article.updated_at }}</p>
    <div style="border: 1px solid gray; height: 100px; padding: 10px;">{{ article.content }}</div>
    <br>
    <RouterLink :to="{name: 'board'}"><button>뒤로가기</button></RouterLink>
    <RouterLink 
      :to="{name: 'board-update', params:{id: article.id}}"
    ><button v-if="article.user === store.userInfo.pk"  @click="update_article(article.id)">수정</button></RouterLink>
    <button v-if="article.user === store.userInfo.pk"  @click="delete_article">삭제</button>
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
    url: `${API_URL}/boards/detail/${id}`
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
    url: `${API_URL}/boards/detail/${id}`
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

</style>