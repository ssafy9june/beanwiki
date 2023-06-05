import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies : null,
    token : null,
    userid : null,
    username : null,
    isLoginOrSignup : true,
    searchType: '',
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies = movies
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      setTimeout(() => {
        router.push({
          name: 'MainView'
        })  
      }, 3000);
    },
    SAVE_USERNAME(state, name){
      state.username = name
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.userid = null
      state.username = null
    },
    SAVE_USERID(state, userid){
      state.userid = userid
    },
    ISLOGINORSIGNUP(state,check){
      state.isLoginOrSignup = check ? true : false;
    }
  },
  actions: {
    get_movies (context) {
      console.log(TMDB_API);
      axios({
        method: 'get',
        // url : `https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API}&language=ko-KR&page=1`
        url : `https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&language=ko-KR&page=1&sort_by=popularity.desc&api_key=${TMDB_API}`
      })
      .then((res) => {
        context.commit('GET_MOVIES', res.data.results)
        console.log(res.data);
      }).catch((err) => {
        console.log(err);
      });
    },
    signUp(context, payload) {
      const username = payload.susername
      const password1 = payload.spassword1
      const password2 = payload.spassword2
      
      console.log(username, password1, password2);

      axios({
        url:'http://127.0.0.1:8000/user/signup/',
        method: 'POST',
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
      })
      .catch((err) => {
        if (password1 != password2) {
          alert('패스워드가 서로 다릅니다!')
        } else {
          alert('이미 존재하는 회원입니다!')
        }
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      axios ({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
      })
      .catch((err) => {
        alert('회원 정보가 잘못 되었습니다!')
      })
    },
    logOut(context){
      context.commit('DELETE_TOKEN')
    },
    save_userid(context,userid){
      context.commit('SAVE_USERID', userid)
    },
    isLoginOrSignup(context,check){
      context.commit('ISLOGINORSIGNUP', check)
    }
  },
  modules: {
  }
})
