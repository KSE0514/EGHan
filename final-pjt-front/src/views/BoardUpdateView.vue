<template>
  <div v-if="article">
    <h1>게시글 수정</h1>
    <form @submit.prevent="update_article(article.id)">
      <div style="display: flex; flex-wrap: wrap; justify-content: center;">
        <p>제목</p>
        <!-- <p>{{ article.title }}</p> -->
        <input id="title1" type="text" placeholder="제목을 입력하세요." style="width: 600px;" v-model.trim="title">
      </div>
      <br>
      <br>

      <div style="display: flex; flex-wrap: wrap; justify-content: center;">
        <p>내용</p>
        <textarea name="content" id="content" cols="30" rows="10" placeholder="내용을 입력하세요." style="width: 600px;" v-model="content"></textarea>
      </div>


      <div style="display: inline-block; width: 50px;"></div>
      <RouterLink :to="{name: 'board-detail', params: {id: $route.params.id}}" class="nav-link" style="margin-top: 20px; display: inline-block;">
      <button class="back-btn">
        <svg height="16" width="16" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 1024 1024"><path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path></svg>
        <span>이전</span>
      </button>
      </RouterLink>
      <div style="display: inline-block; width: 350px; margin-right: 250px;"></div>
      <!-- 수정 버튼 -->
      <button class="back-btn" type="submit" style="display: inline-block;">
        <span>수정</span>
        <svg style="transform: scaleX(-1);" height="16" width="16" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 1024 1024"><path d="M874.690416 495.52477c0 11.2973-9.168824 20.466124-20.466124 20.466124l-604.773963 0 188.083679 188.083679c7.992021 7.992021 7.992021 20.947078 0 28.939099-4.001127 3.990894-9.240455 5.996574-14.46955 5.996574-5.239328 0-10.478655-1.995447-14.479783-5.996574l-223.00912-223.00912c-3.837398-3.837398-5.996574-9.046027-5.996574-14.46955 0-5.433756 2.159176-10.632151 5.996574-14.46955l223.019353-223.029586c7.992021-7.992021 20.957311-7.992021 28.949332 0 7.992021 8.002254 7.992021 20.957311 0 28.949332l-188.073446 188.073446 604.753497 0C865.521592 475.058646 874.690416 484.217237 874.690416 495.52477z"></path></svg>
      </button>



      <!-- <input type="submit" value="수정"> -->
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
p {
  font-family: 'WavvePADO-Regular';
  margin-right: 10px; 
  margin-top: 10px;
}

h1 {
  text-align: center;
}
form {
  margin-top: 30px;
  text-align: center;
}

#title1{
  padding: 10px;
  border-radius: 10px;
  border: 1px solid black;
}

#title1:focus {
  outline: none;
}

#content {
  padding: 10px;
  border-radius: 10px;
}

#content:focus {
  outline: none;
}

/* back 버튼 */
.back-btn {
 display: flex;
 height: 3em;
 width: 100px;
 align-items: center;
 justify-content: center;
 background-color: #eeeeee4b;
 border-radius: 3px;
 letter-spacing: 1px;
 transition: all 0.2s linear;
 cursor: pointer;
 border: none;
 background: #fff;
}

.back-btn > svg {
 margin-right: 5px;
 margin-left: 5px;
 font-size: 20px;
 transition: all 0.4s ease-in;
}

.back-btn:hover > svg {
 font-size: 1.2em;
 transform: translateX(-5px);
}

.back-btn:hover {
 box-shadow: 9px 9px 33px #d1d1d1, -9px -9px 33px #ffffff;
 transform: translateY(-2px);
}

span {
  font-family: 'S-CoreDream-3Light';
}

@font-face {
  font-family: 'WavvePADO-Regular';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

@font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}
</style>