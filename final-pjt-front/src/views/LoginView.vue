<template>
  <div class="login">
    <div class="form">
      <h2>Hello User</h2>
      <form @submit.prevent="login">
        <div class="form-field">
          <label for="login-mail"><i class="fa fa-user"></i></label>
          <input id="login-mail" type="text" v-model="username" placeholder="ID" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <label for="login-password"><i class="fa fa-lock"></i></label>
          <input id="login-password" type="password" v-model="password" placeholder="Password" pattern=".{6,}" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <br>
          <p style="display: flex; justify-content: center; color:#9596A2;"> 
            Don't have an account? <RouterLink :to="{name:'signup'}">Sign up here</RouterLink>
          </p>
        <button type="submit" class="button">
          <div class="arrow-wrapper">
            <span class="arrow"></span>
          </div>
          <p class="button-text">SIGN IN</p>
        </button>
      </form>
    </div>
    <div class="finished" v-if="loginSuccess">
      <svg>
        <use href="#svg-check" />
      </svg>
    </div>
    <p v-if="loginError" style="color: red;">로그인 정보가 일치하지 않습니다. 다시 시도해주세요.</p>
  </div>


  <svg style="display:none;">
  <symbol id="svg-check" viewBox="0 0 130.2 130.2">
    <path d="M100.2,40.2 51.5,88.8 29.8,67.5 "/>
  </symbol>
</svg>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const username = ref(null);
const password = ref(null);
const loginError = ref(false);
const loginSuccess = ref(false);

const login = function() {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload)
    .then(() => {
      loginError.value = false;
      loginSuccess.value = true;
    })
    .catch(() => {
      loginError.value = true; // 로그인 실패 시 로그인 오류를 표시
      loginSuccess.value = false;
    });
};


</script>

<style scoped lang="scss">
@import url(https://fonts.googleapis.com/css?family=Roboto:400,300);
$primary: #00FCD1;
$secondary: #04DFBD;
$lighter: #9596A2;
$light: #3D4256;
$dark: #1E2137;
$bg1: #333342;
$bg2: #4D4E63;
$button: rgb(255, 201, 100);
$border-radius: 12px;


body {
  background: linear-gradient(135deg, $bg2, $bg1);
  height: 100vh;
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
}

//--- ## FORM #############
.login {
  width: 50%;
  height: 55%;
  background: #ffffff;
  box-shadow: 0 20px 50px rgba(0,0,0,0.1);
  border-radius: $border-radius;
  overflow: hidden;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  &:before {
    content:"";
    position: absolute;
    background: transparent;
    bottom: 45px;
    right: 40px; 
    width: 55px;
    height: 55px;
    z-index: 5;
    transition: all .6s ease-in-out, background 0s ease;
  }
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
      color: $lighter;
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

    // .signup {
    //   // display: flex;
    //   justify-content: center; /* Horizontally center the content */
    //   // margin-bottom: 20px; /* Adjust as needed */
    //   padding-top: 30px;
    //   color: $lighter;
    // }
    .button {
      width: 100%;
      position: relative;
      cursor: pointer;
      box-sizing: border-box;
      padding: 30px 40px 45px 40px;
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
        top: 45%;
        left: 0;
        right: 0;
        padding: 0;
        margin: 0;
        color: #fff;
        line-height: 55px;
        text-align: center;
        text-transform: uppercase;
        transform: translateY(-50%);
      }
    }
  }
  .finished {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 7;
    svg {
      width: 100px;
      fill: none;
      stroke: #fff;
      stroke-width: 7;
      stroke-linecap: round;
      stroke-dasharray: 1000;
      stroke-dashoffset: -100;
      transition: all .3s ease-in-out .5s;
    }
  }
  &.loading {
    .form {
      .button {
        .arrow-wrapper {
          width: 55px;
          animation: sk-rotateplane 1.2s infinite ease-in-out .5s;
          .arrow {
            background: #fff;
            transform: translate(15px, 0);
            opacity: 0;
            transition: opacity 0.3s ease-in-out .5s;
          }
        }
        .button-text {
          color: $lighter;
        }
      }
    }
  }
  &.active {
    &:before {
      bottom: 0;
      right: 0;
      background: linear-gradient(90deg, $secondary, $primary);
      border-radius: $border-radius;
      height: 100%;
      width: 100%; 
    }
    .form {
      .button {
        .arrow-wrapper {
          animation-iteration-count: 1;
        }
      }
    }
    .finished {
      svg {
        stroke-dashoffset: 0;
      }
    }
  }
}


@-webkit-keyframes sk-rotateplane {
  0% { transform: perspective(120px) }
  50% { transform: perspective(120px) rotateY(180deg) }
  100% { transform: perspective(120px) rotateY(180deg)  rotateX(180deg) }
}
</style>

