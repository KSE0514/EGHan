<template>
  <div>
    <h1>BoardView</h1>
    <div v-if="store.articles">
      <ul v-for="article in store.articles" :key="article.id">
        <RouterLink class="nav-link" 
          :to="{name:'board-detail', params: {id: article.id } }">
        <h5>제목: {{ article.title }}</h5>
        <p>작성자: {{ article.username }}</p>
        <p>내용: {{ article.content }}</p>
      </RouterLink>
        <hr>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

import { onMounted } from 'vue'

onMounted(() =>{
  store.board()
  // console.log()
  console.log('확인용', store.articles)
})

</script>

<style scoped>

</style>