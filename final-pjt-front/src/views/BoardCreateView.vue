<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 :</label>
      <input id="title" type="text" placeholder="제목을 입력하세요." style="width: 600px;" v-model.trim="title">
      <br>
      <br>

      <label for="content">내용 :</label>
      <textarea name="content" id="content" cols="30" rows="10" placeholder="내용을 입력하세요." style="width: 600px;" v-model="content"></textarea>
      <input type="submit" value="등록">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const store = useCounterStore()
const title = ref(null)
const content = ref(null)

const createArticle = function() {
  const payload = {
    title: title.value,
    content: content.value
  }
  store.create(payload)
  // ,console.log('확인용')
  // console.log(store.token.value)
  // console.log('확인용', `${store.API_URL}/boards/create/`)
  // axios({
  //   method: 'post',
  //   url: `${store.API_URL}/boards/create/`,
  //   headers: {
  //         Authorization: `Token ${store.token.value}`
  //       },
  //   data: {
  //     title: title.value,
  //     content: content.value
  //   },
  // }).then((res) => {
  //   router.push({name: 'board'})
  // }).catch(err => console.log(err))

}




</script>

<style scoped>

</style>