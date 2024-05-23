<!-- <template>
    <div>  
      <label for="age">나이:</label>
      <input type="number" v-model="age" id="age" required><br>

      <label for="money">자산:</label>
      <input type="number" v-model="money" id="money" required><br>

      <label for="salary">연봉:</label>
      <input type="number" v-model="salary" id="salary" required><br>

      <label for="financial_products">가입한 상품 목록:</label>
      <textarea v-model="financial_products" id="financial_products"></textarea><br>
  
      <button @click="submitSignUp">회원가입</button>
    </div>
  </template> -->
  <template>
    <div class="form">
          <div class="form-field">
            <label for="signup-age"><i class="fa fa-envelope"></i></label>
            <input id="signup-age" type="number" v-model="age" placeholder="age" required>
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          <div class="form-field">
            <label for="signup-money"><i class="fa fa-user"></i></label>
            <input id="signup-money" type="number" v-model="money" placeholder="자산" required>
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          <div class="form-field">
            <label for="signup-salary"><i class="fa fa-lock"></i></label>
            <input id="signup-salary" type="number" v-model="salary" placeholder="연봉" required>
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          <div class="form-field">
            <label for="signup-product"><i class="fa fa-lock"></i></label>
            <input id="signup-product" type="text" v-model="financial_products" placeholder="가입한 상품 목록">
            <svg>
              <use href="#svg-check" />
            </svg>
          </div>
          <button type="submit" class="signup-button" @click="submitSignUp"> <!-- 변경된 부분 -->
            <div class="arrow-wrapper">
              <span class="arrow"></span>
            </div>
            <p class="button-text">SignUp</p>
          </button>
        </div>
      <!-- <p v-if="signupError" style="color: red;">Failed to sign up. Please try again.</p> -->
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router';

  const props = defineProps(['email', 'username', 'password','nickname']);
  
  const age = ref(null);
  const money = ref(null)
  const salary = ref(null)
  const financial_products = ref(null)
  
  const errorMessage = ref('')


  const store = useCounterStore()
  const router = useRouter()

  const submitSignUp = function() {
    //회원가입 처리 로직
    if (!age.value || !money.value || !salary.value){
        errorMessage.value = '모든 정보를 입력해주세요.'
        return
    } 
    console.log('회원가입 정보:', {
      email: props.email,
      username: props.username,
      password: props.password,
      nickname: props.nickname,
      age:age.value,
      money:money.value
    });
    const payload = {
        email: props.email,
        username: props.username,
        password: props.password,
        nickname: props.nickname,
        age:age.value,
        money:money.value,
        salary:salary.value,
        financial_products:financial_products.value,
    }
    store.signUp(payload)    
    // router.push('/')
  };
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
  