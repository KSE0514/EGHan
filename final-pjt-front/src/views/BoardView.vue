<template>
  <div>
    <h1>BoardView</h1>
    <RouterLink :to="{name: 'board-create'}">
      <button>작성하기</button>
      <!-- <input type="submit" value="작성하기"> -->
    </RouterLink>
    <hr style="margin-bottom: 0px;">
    <div v-if="store.articles">
      <ul v-for="article in store.articles" :key="article.id" id="article">
        <RouterLink class="nav-link" 
          :to="{name:'board-detail', params: {id: article.id } }">
        <h5 style="margin-top: 10px;">제목: {{ article.title }}</h5>
        <p>작성자: {{ article.username }}</p>
        <p>내용: {{ article.content }}</p>
      </RouterLink>
        <hr style="margin: 0px;">
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
button {
  height: 40px;
  padding: 5px 15px;
 /* padding: 15px 25px; */
 border: unset;
 border-radius: 15px;
 color: #212121;
 z-index: 1;
 background: #fffaf4;
 position: relative;
 font-weight: 1000;
 font-size: 15px;
 -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 transition: all 250ms;
 overflow: hidden;
}

button::before {
 content: "";
 position: absolute;
 top: 0;
 left: 0;
 height: 100%;
 width: 0;
 border-radius: 15px;
 background-color: #ffb89e;
 z-index: -1;
 -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
 transition: all 250ms
}

button:hover {
 color: #ffffff;
}

button:hover::before {
 width: 100%;
}

h1 {
  font-family: 'WavvePADO-Regular';
}

@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

#article {
  margin: 0px;
}

#article:hover {
  background-color: #fff5ea;
}

</style>