<template>
  <div v-if="article">
    <h1>게시글 수정</h1>
    <form @submit.prevent="update_article(article.id)">
      <label for="title">제목 :</label>
      <!-- <p>{{ article.title }}</p> -->
      <input id="title" type="text" placeholder="제목을 입력하세요." style="width: 600px;" v-model.trim="title">
      <br>
      <br>

      <label for="content">내용 :</label>
      <textarea name="content" id="content" cols="30" rows="10" placeholder="내용을 입력하세요." style="width: 600px;" v-model="content"></textarea>
      <input type="submit" value="수정">
    </form>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
const store = useCounterStore()
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
const API_URL = store.API_URL
import { ref } from 'vue'

const id = route.params.id

const article = ref(null)
const title = ref(null)
const content = ref(null)

const detail = function() {
  console.log(`${API_URL}/boards/detail/${id}/`)
  axios({
    method: 'get',
    url: `${API_URL}/boards/detail/${id}/`
  })
    .then((res) => {
      console.log(res)
      article.value = res.data
      title.value = article.value.title
      content.value = article.value.content
      console.log('타이틀', title)
      console.log('내용', content)
      // console.log('콘솔', article.value.title)
    })
}

const update_article = function (article_id) {
  const payload = {
    title: title.value, 
    content: content.value, 
    article_id: article_id
  }
  store.update(payload)
  // axios({
  //   method: 'put',
  //   url: `${API_URL}/boards/detail/${article_id}`
  // })
  // .then((res) =>{
  //   console.log('수정 완료')
  //   router.push({name: 'board-detail', params: {id: article_id}})
  // })
}

// import { onMounted } from 'vue'
onMounted(() =>{
  detail()
  // console.log('확인', article.value)
})
</script>

<style scoped>

</style>