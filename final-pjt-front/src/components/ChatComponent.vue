<template>
  <div class="chatbox">
    <div v-for="(message, index) in chatHistory" :key="index">
      <p v-if="message.role === 'user'" id="myChat">You: {{ message.content }}</p>
      <p v-else id="chatBox">GPT: {{ message.content }}</p>
    </div>
    <div style="display: flex; justify-content: center;">
      <input style="width: 100%;" v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type a message"/>
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userMessage: '',
      chatHistory: [],
    };
  },
  methods: {
    async sendMessage() {
      if (this.userMessage.trim() !== '') {
        this.chatHistory.push({ role: 'user', content: this.userMessage });
        try {
          const response = await axios.get('http://127.0.0.1:8000/boards/api/chat/', { 
            message: this.userMessage,
            messages: this.chatHistory
          });
          this.chatHistory.push({ role: 'assistant', content: response.data.response });
        } catch (error) {
          console.error('Error:', error);
          if (error.response) {
            this.chatHistory.push({ role: 'assistant', content: "Error: " + error.response.data.error });
          }
        }
        this.userMessage = '';
      }
    },
  },
};
</script>

<style scoped>
/* 스타일링은 필요에 따라 추가 */
.chatbox {
  padding-top: 10px;
  width: 15%;
  background-color: rgb(255, 228, 228);
}

#myChat {
  margin-top: 10px;
  margin-right: 20px;
  text-align: right;
  
}

#chatBox {
  display: inline-block;
  position: relative;
  background-color: #ea5936;
  border-radius: 20px;
  color: #fff;
  padding: 7px 12px;
  margin-bottom: 10px;
  margin-right: 5px;
  max-width: 230px;
  margin-left: 5px;
}

#chatTime {
  position: absolute;
  left: -72px;
  top: 15px;
  color: #171717;
}

</style>
