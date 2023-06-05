<template>
  <div id="app">
    <div class="row">
      <div class="col-10 mx-auto">
        <nav class="navbar navbar-black bg-black" v-if="isLoggedIn">
            <!-- <p style="color: white; margin-right: 12px; margin-left: 20px; display: inline">BEANWIKI</p> -->
            <router-link class="mx-3" to="/" style="color: #FC3C44;">BEANWIKI</router-link>
            <router-link to="/main">Home</router-link> | 
            <router-link to="/community">Community</router-link> | 
            <router-link to="/findthatmovie">FindThatMovie</router-link> |
            <!-- <router-link to="/test">Test</router-link> | -->
            <input type="text" placeholder="검색" v-model="searchText" @keyup.enter="search(searchText)" style="color: white; border: solid 1px white; width: 300px; border-radius:5px">
            <a href="" @click.prevent="logOut">Log Out</a>
            <router-link class="mx-3" :to="{name : 'profile', params: { userid : this.$store.state.userid}}">마이페이지</router-link>
            <!-- <p style="color: white;">안녕하세요, JUNE님</p> -->
          </nav>
          <nav class="navbar navbar-black bg-black" v-if="!isLoggedIn">
            <router-link class="mx-3" to="/" style="color: #FC3C44;">BEANWIKI</router-link>
            <a href="#" class="text-white" @click.prevent="alertLogin">Home</a> | 
            <a href="#" class="text-white" @click.prevent="alertLogin">Community</a> | 
            <a href="#" class="text-white" @click.prevent="alertLogin">FindThatMovie</a> |
            <input type="text" placeholder="검색" @keyup.enter="alertLogin" style="color: white; border: solid 1px white; width: 300px; border-radius:5px">
            <router-link style="margin-right: 20px;" to="/" data-bs-toggle="modal" data-bs-target="#exampleModal" @click.native="LoginOrSignup(true)">Login</router-link>
            <router-link style="margin-right: 20px;" to="/" data-bs-toggle="modal" data-bs-target="#exampleModal" @click.native="LoginOrSignup(false)">Sign Up</router-link>
          </nav>
          <!-- <h1>{{ user }}</h1> -->
      </div>
    </div>
    <router-view :key="$route.fullPath"/>
  </div>
  
</template>
<script>

export default {
  data(){
    return{
      searchText: null,
    }
  },
  methods: {
    search(searchText) {
      this.searchText = ''
      this.$router.push({ name: 'search'  , params: {searchContent: 'title', searchText} }).catch(()=>{})
    },
    logOut() {
      this.$store.dispatch('logOut')
      this.$router.replace({
        name: 'about'
      })
      .catch((err) => {
      console.log(err);
    })
    },
    alertLogin() {
      alert('로그인이 필요한 서비스 입니다.')
    },
    LoginOrSignup(check) {
      this.$store.dispatch('isLoginOrSignup',check)
    }
  },
  computed: {
    isLoggedIn() {
      if(this.$store.state.token){
        return true
      }
      else{
        return false
      }
    }
    
  }
}
</script>
<style>
#app {
  font-family: 'IBM Plex Sans KR', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

}
p {
  margin-top: 0;
  margin-bottom: 0;

}
.navbar {
  padding: 10px;
}
a {
  color: white;
  text-decoration: none;
}
.row {
  --bs-gutter-x: 0rem
}
.card {
  min-width: 200px;
}
body, html {scroll-behavior:smooth;}

.posterImg {
  aspect-ratio: 2 / 3;
  border: 1px solid black;
  border-radius: 5px;
}
</style>