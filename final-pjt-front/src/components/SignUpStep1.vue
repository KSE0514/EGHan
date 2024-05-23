<!-- <template>
  <div class="signup-container">
    <form @submit.prevent="goToStep2" class="signup-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required>
      </div>

      <div class="form-group">
        <label for="username">ID:</label>
        <input type="text" v-model="username" id="username" required>
      </div>

      <div class="form-group">
        <label for="password1">Password:</label>
        <input type="password" v-model="password1" id="password1" required>
      </div>

      <div class="form-group">
        <label for="password2">Confirm Password:</label>
        <input type="password" v-model="password2" id="password2" required>
      </div>

      <div class="form-group">
        <label for="nickname">Name:</label>
        <input type="text" v-model="nickname" id="nickname" required>
      </div>

      <button type="submit" v-if="!showStep2" class="submit-button">Next</button>
    </form>
  </div>
  <div v-if="showStep2">
      <SignUpStep2 :email="email" :username="username" :password="password1" :nickname="nickname"/>
  </div>
</template>
<script setup>
import { useRoute,useRouter } from 'vue-router'
import { ref } from 'vue'
import SignUpStep2 from './SignUpStep2.vue';
const router = useRouter()
const username =ref(null)
const email =ref(null)
const password1 =ref(null)
const password2 = ref(null)
const nickname = ref(null)

const showStep2 = ref(false)

const goToStep2 = function(){
    if (password1.value != password2.value){
        window.alert('비밀번호가 일치하지 않습니다.')
        return
    }
    showStep2.value = true
}
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.signup-form {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button.submit-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button.submit-button:hover {
  background-color: #0056b3;
}
</style> -->


<template>
  <div class="signup">
    <div class="form">
      <h2 style="color:#9596A2;">Create an Account</h2>
      <form @submit.prevent="goToStep2">
        <div class="form-field">
          <label for="signup-mail"><i class="fa fa-envelope"></i></label>
          <input id="signup-mail" type="email" v-model="email" placeholder="Email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <label for="signup-username"><i class="fa fa-user"></i></label>
          <input id="signup-username" type="text" v-model="username" placeholder="ID" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <label for="signup-password"><i class="fa fa-lock"></i></label>
          <input id="signup-password" type="password" v-model="password1" placeholder="Password" pattern=".{6,}" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <label for="signup-confirm-password"><i class="fa fa-lock"></i></label>
          <input id="signup-confirm-password" type="password" v-model="password2" placeholder="Confirm Password" pattern=".{6,}" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <label for="signup-nickname"><i class="fa fa-lock"></i></label>
          <input id="signup-nickname" type="text" v-model="nickname" placeholder="이름" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <button type="submit" v-if="!showStep2" class="signup-button"> <!-- 변경된 부분 -->
          <div class="arrow-wrapper">
            <span class="arrow"></span>
          </div>
          <p class="button-text">Next</p>
        </button>
      </form>
    </div>
    <div v-if="showStep2">
      <SignUpStep2 :email="email" :username="username" :password="password1" :nickname="nickname"/>
  </div>
    <!-- <p v-if="signupError" style="color: red;">Failed to sign up. Please try again.</p> -->
  </div>
</template>

<script setup>
import { useRoute,useRouter } from 'vue-router'
import { ref } from 'vue'
import SignUpStep2 from './SignUpStep2.vue';
const router = useRouter()
const username =ref(null)
const email =ref(null)
const password1 =ref(null)
const password2 = ref(null)
const nickname = ref(null)

const showStep2 = ref(false)

const goToStep2 = function(){
    if (password1.value != password2.value){
        window.alert('비밀번호가 일치하지 않습니다.')
        return
    }
    showStep2.value = true
}
</script>

<style lang="scss">
// Import Google Font
@import url(https://fonts.googleapis.com/css?family=Roboto:400,300);

// Define theme colors and variables
$primary: #00FCD1;
$lighter: #9596A2;
$bg1: #333342;
$button: rgb(255, 201, 100);
$border-radius: 12px;

// Apply styling

.signup {
  width: 50%;
  height: auto;
  background: #ffffff;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);
  border-radius: $border-radius;
  overflow: hidden;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  .form {
    display: block;
    position: relative;
    h2 {
      background: rgb(253, 238, 224);
      display: block;
      box-sizing: border-box;
      width: 100%;
      margin: 0 0 50px 0;
      padding: 40px;
      font-weight: 200;
      color: #fff;
      font-size: 19px;
    }
    .form-field {
      display: flex;
      align-items: center;
      height: 55px;
      margin: 0 40px 40px 40px;
      border-bottom: 1px solid $lighter;
      label {
        width: 10px;
        padding: 0 15px 0 0;
        color: $lighter;
      }
      input {
        width: 100%;
        background: transparent;
        color: $lighter;
        padding: 15px;
        border: 0;
        margin: 0;
        &+svg {
          width: 35px;
          fill: none;
          stroke: $primary;
          stroke-width: 7;
          stroke-linecap: round;
          stroke-dasharray: 1000;
          stroke-dashoffset: -100;
          transition: all .3s ease-in-out;
        }
        &:valid + svg {
          stroke-dashoffset: 0;
        }
        &:focus {
          outline: none;
        }
      }
      *::placeholder {
        color: $lighter;
      }
    }
  }
}

.signup-button {
  width: 100%;
  position: relative;
  cursor: pointer;
  box-sizing: border-box;
  padding: 20px 40px;
  margin: 0;
  border: 0;
  background: transparent;
  outline: none;
  .arrow-wrapper {
    transition: all 0.45s ease-in-out;
    position: relative;
    margin: 0;
    width: 100%;
    height: 55px;
    right: 0;
    float: right;
    background: linear-gradient(90deg, $button, $button);
    box-shadow: 0 3px 20px rgba($button, 0.4);
    border-radius: $border-radius;
    .arrow {
      position: absolute;
      top: 50%;
      margin: auto;
      transition: all 0.45s ease-in-out;
      right: 35px;
      width: 15px;
      height: 2px;
      background: none;
      transform: translateY(-50%);
      &:before {
        position: absolute;
        content: '';
        top: -4px;
        right: 0;
        width: 8px;
        height: 8px;
        border-top: 2px solid #fff;
        border-right: 2px solid #fff;
        transform: rotate(45deg);
      }
    }
  }
  .button-text {
    transition: all 0.45s ease-in-out;
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    padding: 0;
    margin: 0;
    color: #fff;
    line-height: 1;
    text-align: center;
    text-transform: uppercase;
    transform: translateY(-50%);
  }
}
</style>
