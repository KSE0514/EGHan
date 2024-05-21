import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(localStorage.getItem('token') || null)
  const userInfo = ref([])

  const isLogin = computed(() => {
    return token.value === null ? false : true
  })

  const signUp = function(payload){
    const username = payload.username
    const password1 = payload.password
    const password2 = payload.password
    const nickname = payload.nickname
    const email = payload.email
    const age = payload.age
    const money = payload.money
    const salary = payload.salary
    const financial_products = payload.financial_products

    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data:{
        username,email,password1,password2,nickname,age,money,salary,financial_products
      }
    }).then((response)=>{
      console.log('회원가입 완료')
      logIn(payload)
    }).catch((error)=>{
      console.log(error)
    })
  }


  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data:{
        username,password
      }
    }).then((response)=>{
      console.log('로그인 완료')
      console.log(response.data)
      token.value = response.data.key
      localStorage.setItem('token', response.data.key)
      router.push({name:'home'})
    }).catch((error)=>{
      console.log(error)
    })
  }

  const logout = function(){
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((response) => {
        token.value = null
        // userInfo.value = []
        localStorage.removeItem('token')
        console.log('로그아웃')
        router.push({name:'home'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getUserInfo = function() {
    axios({
      method:'get',
      url:`${API_URL}/accounts/userinfo/`,
      headers:{
        Authorization:`Token ${token.value}`
      }
    }).then((response)=>{
      userInfo.value = response.data
      console.log(response.data)
    }).catch((error)=>{
      console.log(error)
    })
    
  }

  const updateProfile = function(payload){
    const username = payload.username
    const password = payload.password
    const nickname = payload.nickname
    const email = payload.email
    const age = payload.age
    const money = payload.money
    const salary = payload.salary
    const financial_products = payload.financial_products

    axios({
      method:'patch',
      url:`${API_URL}/accounts/update/`,
      headers:{
        Authorization:`Token ${token.value}`
      },
      data:{
        username,email,password,nickname,age,money,salary,financial_products
      }
    }).then((response)=>{
      console.log('회원정보 수정 완료')
      router.push({name:'user'})
    }).catch((error)=>{
      console.log(error)
    })
  }
    
  // 게시판
    const articles = ref([])
    const board = function() {
      console.log(token.value)
      axios({
        method: 'get', 
        url: `${API_URL}/boards/`,
      })
      .then((res) => {
        console.log(res.data)
        console.log('board 함수 작동')
        articles.value = res.data
        // console.log(articles.value)
      })
    }

    const create = function(payload) {
      const { title, content } = payload
      console.log(`${API_URL}/boards/create/`)
      axios({
        method:'post',
        url: `${API_URL}/boards/create/`,
        data: {
          title,content
        },
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        console.log(res.data)
        router.push({name:'board'})
      }).catch((error)=>{
        console.log(error)
      })
    }
  
    // 댓글
    const comment_create = function(payload, article_id) {
      const { content } = payload
      console.log('확인용', article_id)
      // const id = article_id
      // console.log(id)
      axios({
        method: 'post',
        url:  `${API_URL}/boards/comment/create/${article_id}`,
        data: {
          content
        },
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        // console.log('확인용 url', url)
        console.log(res)
      })
      .catch((error) => {
        console.error(error);
      })
    }

    // 댓글 리스트
    const comments = ref([])
    const comments_lst = function (article_id) {
      axios({
        method: 'get',
        url:  `${API_URL}/boards/comment/create/${article_id}`,
      })
      .then((res) => {
        console.log('댓글 리스트 확인용', res.data)
        comments.value = res.data
      })
    }
    


    // 예금 상품 리스트 가져오기
    const products = ref([])
    const get_products = function(){
      axios({
        method:'get',
        url:`${API_URL}/api/v1/deposit-products/`
      }).then((response)=>{
        products.value = response.data
      }).catch((error)=>{
        console.log(error)
      })
    }

  return { signUp,logIn,isLogin,logout,getUserInfo,userInfo,updateProfile, board, articles, API_URL, comment_create, create, token, products,get_products, comments, comments_lst  }
})
