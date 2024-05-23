<template>
  <!-- <div>
    <form @submit.prevent="handleSubmit">
      <label for="email">email:</label>
      <input type="email" v-model="email" id="email" required><br>

      <label for="username">ID:</label>
      <input type="text" v-model="username" id="username" required><br>

      <label for="password">password:</label>
      <input type="password" v-model="password" id="password" required><br>

      <label for="nickname">이름:</label>
      <input type="text" v-model="nickname" id="nickname" required><br>

      <label for="age">나이:</label>
      <input type="number" v-model="age" id="age" required><br>

      <label for="money">자산:</label>
      <input type="number" v-model="money" id="money" required><br>

      <label for="salary">연봉:</label>
      <input type="number" v-model="salary" id="salary" required><br>

      <button>회원 정보 수정</button>
    </form>
  </div> -->
  <div class="update">
  <div class="form">
    <h2 style="color:#9596A2;">Update Profile</h2>
    <form @submit.prevent="handleSubmit">
    <div class="form-field">
      <span>email</span>
          <label for="update-mail"><i class="fa fa-envelope"></i></label>
          <input id="update-mail" type="email" v-model="email" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <span>ID</span>
          <label for="update-username"><i class="fa fa-user"></i></label>
          <input id="update-username" type="text" v-model="username" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
        <div class="form-field">
          <span>password</span>
          <label for="update-password"><i class="fa fa-lock"></i></label>
          <input id="update-password" type="password" v-model="password1" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>

        <div class="form-field">
          <span>name</span>
          <label for="update-nickname"><i class="fa fa-lock"></i></label>
          <input id="update-nickname" type="text" v-model="nickname" required>
          <svg>
            <use href="#svg-check" />
          </svg>
        </div>
          <div class="form-field">
            <span>money</span>
            <label for="update-money"><i class="fa fa-user"></i></label>
            <input id="update-money" type="number" v-model="money"  required>
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          <div class="form-field">
            <span>salary</span>
            <label for="update-salary"><i class="fa fa-lock"></i></label>
            <input id="update-salary" type="number" v-model="salary"  required>
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          
          <button type="submit" class="update-button"> <!-- 변경된 부분 -->
            <div class="arrow-wrapper">
              <span class="arrow"></span>
            </div>
            <p class="button-text">update</p>
          </button>
        </form>
        </div>
      </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
const store = useCounterStore()
const email = ref('')
const nickname = ref('')
const username = ref('')
const password = ref('')
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const financial_products = ref('')

onMounted(async () => {
  if (store.isLogin) {
    await store.getUserInfo()
    // store.getUserInfo()가 완료된 후에 값을 설정
    email.value = store.userInfo.email
    nickname.value = store.userInfo.nickname
    username.value = store.userInfo.username
    age.value = store.userInfo.age
    money.value = store.userInfo.money
    salary.value = store.userInfo.salary
    financial_products.value = store.userInfo.financial_products
  }
})

const handleSubmit = () => {
  store.updateProfile({
    email: email.value,
    username: username.value,
    password: password.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    financial_products: financial_products.value
  })
  router.push({name:'user'})
}
</script>

<style lang="scss">
@import url(https://fonts.googleapis.com/css?family=Roboto:400,300);
  
  // Define theme colors and variables
  $primary: #00FCD1;
  $lighter: #9596A2;
  $bg1: #333342;
  $button: rgb(255, 201, 100);
  $border-radius: 12px;
  
  // Apply styling
  
  .update {
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
  
  .update-button {
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
