<!-- <script>
import { RouterLink, RouterView } from 'vue-router'
import ChatComponent from '@/components/ChatComponent.vue'

export default {
  name: 'App',
  components: {
    ChatComponent
  }
};
</script> -->

<!-- HomeView.vue -->
<!-- HomeView.vue -->
<template>
  <div class="home-view">
    <div class="welcome-message" :class="{ 'fade-in': showWelcome }">
      <h1>Welcome to Our Financial Services!</h1>
      <p>Discover the best financial products tailored for you.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const showWelcome = ref(false);

onMounted(() => {
  setTimeout(() => {
    showWelcome.value = true;
  }, 100); // 시간 지연 추가
});
</script>

<style scoped>
.home-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.welcome-message {
  text-align: center;
  opacity: 0;
  font-family: 'WavvePADO-Regular';
  /* font-size: x-large; */
  animation: fade-in 4s infinite; /* 애니메이션 반복 */
}


@font-face {
  font-family: 'WavvePADO-Regular';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}


@keyframes fade-in {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>


