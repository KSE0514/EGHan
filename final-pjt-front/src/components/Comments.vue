<template>
  <div>
    <hr>
    <form @submit.prevent="store.comment_create(comment.article)">
      <label for="comment">댓글 작성</label><br>
      <textarea name="comment" id="comment" cols="30" rows="3" style="width: 100%;" v-model="comment"></textarea>
      <input type="submit" value="등록">
    </form>
    
    <!-- 댓글 리스트 출력 -->
    

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

const comment = ref(null)

</script>

<style scoped>

</style>