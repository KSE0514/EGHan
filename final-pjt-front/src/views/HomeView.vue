<script>
import { RouterLink, RouterView } from 'vue-router'
import ChatComponent from '@/components/ChatComponent.vue'

export default {
  name: 'App',
  components: {
    ChatComponent
  }
};
</script>

<template>
    <h1>메인페이지</h1>

    <!-- 챗봇 -->
    <div id="app">
        <ChatComponent />
    </div>
</template>

<style scoped>
#app {
    display: inline-block;
    width: 2500px;
}
</style>
