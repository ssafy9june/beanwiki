import Vue from 'vue'
import VueRouter from 'vue-router'

import MainView from '../views/MainView.vue'
import AboutView from '../views/AboutView.vue';
import CommunityView from '../views/CommunityView.vue'
import FindThatMovieView from '../views/FindThatMovieView.vue'
import TestView from '../views/TestView.vue';
import SearchView from '../views/SearchView.vue'
import ProfileView from '../views/ProfileView.vue';
import MoreView from '../views/MoreView.vue';
import ErrorView from '../views/ErrorView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'about',
    component: AboutView
  },
  {
    path: '/main',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/findthatmovie',
    name: 'findthatmovie',
    component: FindThatMovieView
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/search/:searchContent/:searchText',
    name: 'search',
    component: SearchView
  },
  {
    path: '/more/:type/:keyword',
    name: 'more',
    component: MoreView
  },
  {
    path: '/profile/:userid',
    name : 'profile',
    component : ProfileView
  },
  {
    path: '/*',
    name : 'error',
    component : ErrorView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
