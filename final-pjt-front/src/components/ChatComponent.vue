<template>
  <div class="chatbox">
    <div v-for="(message, index) in chatHistory" :key="index">
      <p v-if="message.role === 'user'" id="myChat">You: {{ message.content }}</p>
      <p v-else id="chatBox">GPT: {{ message.content }}</p>
    </div>
    <div style="display: flex; justify-content: center;">
      <input class="chat-input" v-model="userMessage" @keyup.enter="sendMessage" placeholder=" 궁금한 것을 물어보세요!"/>
      <button @click="sendMessage">전송</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    const userMessage = ref('')
    const chatHistory = ref([])

    function sendMessage() {
      if (userMessage.value.trim() !== '') {
        chatHistory.value.push({ role: 'user', content: userMessage.value })
        
        axios.post('http://127.0.0.1:8000/boards/api/chat/', {
          message: userMessage.value,
          messages: chatHistory.value,
        })
        .then(response => {
          chatHistory.value.push({ role: 'assistant', content: response.data.response })
        })
        .catch(error => {
          console.error('Error:', error)
          if (error.response) {
            chatHistory.value.push({ role: 'assistant', content: "Error: " + error.response.data.error })
          }
        })
        
        userMessage.value = ''
      }
    }

    return {
      userMessage,
      chatHistory,
      sendMessage,
    }
  }
}

// export default {
//   data() {
//     return {
//       userMessage: '',
//       chatHistory: [],
//     };
//   },
//   methods: {
//     async sendMessage() {
//       if (this.userMessage.trim() !== '') {
//         this.chatHistory.push({ role: 'user', content: this.userMessage });
//         try {
//           const response = await axios.get('http://127.0.0.1:8000/boards/api/chat/', { 
//             message: this.userMessage,
//             messages: this.chatHistory
//           });
//           this.chatHistory.push({ role: 'assistant', content: response.data.response });
//         } catch (error) {
//           console.error('Error:', error);
//           if (error.response) {
//             this.chatHistory.push({ role: 'assistant', content: "Error: " + error.response.data.error });
//           }
//         }
//         this.userMessage = '';
//       }
//     },
//   },
// };
</script>

<style scoped>
/* 스타일링은 필요에 따라 추가 */
.chatbox {
  border: 1px solid rgba(214, 153, 117, 0.699);
  border-radius: 10px;
  padding-top: 5px;
  width: 15%;
  background-color: rgb(255, 244, 242);
}

#myChat {
  margin-top: 10px;
  margin-right: 20px;
  text-align: right;
  
}

#chatBox {
  display: inline-block;
  position: relative;
  background-color: #f87f61;
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

button {
 appearance: none;
 background-color: #FAFBFC;
 border: 1px solid rgba(27, 31, 35, 0.15);
 border-radius: 6px;
 box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;
 box-sizing: border-box;
 color: #24292E;
 cursor: pointer;
 display: inline-block;
 font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
 font-size: 14px;
 font-weight: 500;
 line-height: 20px;
 list-style: none;
 padding: 6px 16px;
 position: relative;
 transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
 user-select: none;
 -webkit-user-select: none;
 touch-action: manipulation;
 vertical-align: middle;
 white-space: nowrap;
 word-wrap: break-word;
}

button:hover {
 background-color: #F3F4F6;
 text-decoration: none;
 transition-duration: 0.1s;
}

button:disabled {
 background-color: #FAFBFC;
 border-color: rgba(27, 31, 35, 0.15);
 color: #959DA5;
 cursor: default;
}

button:active {
 background-color: #EDEFF2;
 box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
 transition: none 0s;
}

button:focus {
 outline: 1px transparent;
}

button:before {
 display: none;
}

button:-webkit-details-marker {
 display: none;
}

.chat-input {
  width: 100%; 
  border-radius: 10px; 
  border: 0.15em solid rgb(255, 195, 195);
}
.chat-input:focus {
  outline: none;
}
</style>
