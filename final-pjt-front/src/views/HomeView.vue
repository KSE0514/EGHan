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

<template>
  <div>
    <div class="welcome-message" ref="welcomeMessage" v-if="showWelcome">
      <h1>Welcome to Our Website!</h1>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showWelcome: false
    };
  },
  mounted() {
    this.showWelcomeMessage();
  },
  methods: {
    showWelcomeMessage() {
      this.showWelcome = true;
      this.fadeInEffect();
    },
    fadeInEffect() {
      let opacity = 0;
      const interval = setInterval(() => {
        if (opacity >= 1) {
          clearInterval(interval);
        }
        // 요소에 접근하기 위해 $refs를 사용합니다.
        if (this.$refs.welcomeMessage) {
          this.$refs.welcomeMessage.style.opacity = opacity;
        }
        opacity += 0.01;
      }, 10);
    }
  }
};
</script>

<style scoped>
.welcome-message {
  /* display: none; */
  text-align: center;
  font-size: 24px;
  margin-top: 100px;
}
</style>



