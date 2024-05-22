<template>
  <div>
    <hr>
    <form @submit.prevent="comment_cr">
      <label for="comment">댓글 작성</label><br>
      <textarea name="comment" id="comment" cols="30" rows="3" style="width: 100%;" v-model="comment"></textarea>
      <input type="submit" value="등록">
    </form>
    <br>
    <!-- 댓글 리스트 출력 -->
    <div v-if="store.comments">
      <div class="card" v-for="comment in store.comments">
        <div class="card-body" style="display: flex; flex-wrap: wrap; justify-content: space-between;">
        <div>{{ comment.content }} - {{ comment.username }}</div>
        <div v-if="comment.user === store.userInfo.id" href="#" style="color: red;" @click="comment_del(comment.id)">x</div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
const route = useRoute()
const store = useCounterStore()

const comment = ref(null)

const comment_cr = function() {
  console.log('확인용1', route.params.id)
  console.log('유저 확인용', store.userInfo)
  const payload = {
    'content': comment.value
  }
  store.comment_create(payload, route.params.id)
  comment.value = ''
}

const comment_del = function (comment_id) {
  console.log('댓글 삭제 확인용', comment_id)
  store.comment_delete(route.params.id, comment_id)
}

onMounted(() => {
  store.comments_lst(route.params.id)
  store.getUserInfo()
})


</script>

<style scoped>
#comment_list {
  background-color: rgba(255, 249, 224, 0.897);
  border: 1px solid black;
}
</style>