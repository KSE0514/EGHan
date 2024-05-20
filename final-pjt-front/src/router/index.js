import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
// import App from '@/App.vue'

import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import UserView from '@/views/UserView.vue'
import UserUpdateView from '@/views/UserUpdateView.vue'
import ProductView from '@/views/ProductView.vue'
import BoardView from '@/views/BoardView.vue'
import BoardDetailView from '@/views/BoardDetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/signup',
      name:'signup',
      component: SignUpView
    },
    {
      path:'/login',
      name:'login',
      component: LoginView
    },
    {
      path:'/user',
      name:'user',
      component: UserView
    },
    {
      path:'/userinfoupdate',
      name:'userinfoupdate',
      component: UserUpdateView
    },
    {
      path:'/boards',
      name:'board',
      component: BoardView
    },
    {
      path:'/product',
      name:'product',
      component: ProductView
    },
    {
      path:'/board/:id',
      name:'board-detail',
      component: BoardDetailView,
    },
  ]
})

export default router
