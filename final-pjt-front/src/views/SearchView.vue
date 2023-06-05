<template>
    <div class="container">
      <div class="row">
        <div class="col mx-auto">
          <h3 class="mt-3" style="text-align: left"> <strong>{{ $route.params.searchText }}</strong>과 관련된 검색어는 다음과 같습니다</h3>
          <ul class="nav nav-underline">
            <li class="nav-item">
              <a class="nav-link" :class="{active: $route.params.searchContent === 'title' && this.choice != 'actor' && this.choice != 'crew'}" @click.prevent="search('title')">영화</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="{active: $route.params.searchContent === 'actor' || choice == 'actor'}" @click.prevent="search_actor()">배우</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="{active: $route.params.searchContent === 'crew' || choice == 'crew'}" @click.prevent="search_crew()">감독</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="{active: $route.params.searchContent === 'genre' && this.choice != 'actor' && this.choice != 'crew'}" @click.prevent="search('genre')">장르</a>
            </li>
          </ul>
        </div>
      </div>
        <div class="container col" v-if="choice=='title'">
          <div class="row" v-if="movies">
            <div class="col-md-4 col-lg-3" v-for="(movie, idx) in movies" :key="idx">
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="tomovie(movie.id)">
                  <img class="posterImg" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="">
                  <p>{{ movie.title }}</p>
                </button>
            </div>
          </div>
          <div v-if="movies == false">
            <h1>영화가 없습니다.</h1>
            <img style="width: 60%; height: 60%" :src="require(`@/assets/${robot}`)" alt="">
          </div>
        </div>
        <div class="container col" v-else-if="choice=='actor'">
          <div class="row" v-if="actors">
            <div class="col-md-4 col-lg-3" v-for="(actor, idx) in actors" :key="idx">
              <button class="btn" @click="search_movie_byactor(actor.name)" alt="">
                <img class="posterImg" :src="`https://image.tmdb.org/t/p/original/${actor.profile_path}`"> 
                <p>{{ actor.name }}</p>
              </button>
            </div>
          </div>
          <div v-if="actors == false">
            <h1>영화가 없습니다.</h1>
            <img style="width: 60%; height: 60%" :src="require(`@/assets/${robot}`)" alt="">
          </div>
        </div>
        <div class="container col" v-else-if="choice=='crew'">
          <div class="row" v-if="crews">
            <div class="col-md-4 col-lg-3" v-for="(crew, idx) in crews" :key="idx">
              <button class="btn" @click="search_movie_bycrew(crew.name)" alt="">
                <img class="posterImg" :src="`https://image.tmdb.org/t/p/original/${crew.profile_path}`"> 
                <p>{{ crew.name }}</p>
              </button>
            </div>
          </div>
          <div v-if="crews == false">
            <h1>영화가 없습니다.</h1>
            <img style="width: 60%; height: 60%" :src="require(`@/assets/${robot}`)" alt="">
          </div>
        </div>           
        <div class="container col" v-else-if="choice=='genre'" style="overflow: hidden">
          <div class="row" v-if="movies">
            <div class="col-md-4 col-lg-3" v-for="(movie, idx) in genres" :key="idx">
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="tomovie(movie.id)">
                  <img class="posterImg" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="">
                  <p>{{ movie.title }}</p>
                </button>
            </div>
          </div>
          <div v-if="genres == false">
            <h1>영화가 없습니다.</h1>
            <img style="width: 60%; height: 60%" :src="require(`@/assets/${robot}`)" alt="">
          </div>
        </div>   
      
    

      <!-- <div class="modaldiv mx-5 my-5">
        <div class="modalcontent">
        </div>
      </div> -->

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-xl modal-dialog-scrollable">
            <div class="modal-content">
              <!-- <div class="modal-header">
              </div> -->
              <div class="modal-body bg-black">
                <div style="height: 50vh" class='ratio ratio-16x9'>
                  <iframe v-if="youtubeKeyExists" :src="`https://www.youtube.com/embed/${detail_movie.youtube_key}?autoplay=1&amp;mute=1`" frameborder="0"></iframe>
                  <h4 v-else>트레일러 영상이 존재하지 않습니다.</h4>
                  <br>
                </div>
                <div class="d-flex mx-5 mt-5">
                  <div class="movieDetails text-start text-white">
                    <h1 class="mb-3" >{{ detail_movie.title }}</h1>
                    <p style="display: inline;" v-for="(keyword,idx) in detail_movie.keyword " :key="idx"> #{{ keyword.name }}</p>
                    <!-- <p> {{ detail_movie }} </p> -->
                    <br>
                    <div class="mt-3">
                      <p style="display: inline"> {{ releaseYear }} </p> |
                      <p id="specificItem" style="display: inline;" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="goToMovieByType(genre.name, 'genre')" v-for="genre in detail_movie.genre " :key="genre.name"> {{ genre.name }} </p>
                      <br>
                      <p style="display: inline"> 배우: </p>
                      <p id="specificItem" style="display: inline;" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="goToMovieByType(actor.name, 'actor')" v-for="actor in detail_movie.actor " :key="actor.name"> {{ actor.name }} </p>
                      <br>
                      <p style="display: inline"> 감독:  </p>
                      <p id="specificItem" style="display: inline;" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="goToMovieByType(crew.name, 'crew')" v-for="crew in detail_movie.crew" :key="crew.name"> {{ crew.name }} </p>

                    </div>
                    <p class="mt-3 text-truncate-container"> {{ detail_movie.overview }} </p>
                    <i id="movieLike" class="fa-regular fa-heart fa-lg mt-3" @click="movie_like(detail_movie.id)"> {{ detail_movie.likeuser }}</i>
                  </div>
                  <img class="" style="width: 30vh; margin-left: 50px;" :src="`https://image.tmdb.org/t/p/original/${detail_movie.poster_path}`" alt="">
                </div>


                <hr style="background: white; height:2px; border:0">

                <div class="comment">

                </div>
                  <h2 class="text-white text-start mx-5">이런 영화는 어떠신가요?</h2>
                  <div class="swiper space my-5 mx-5" id="swiperContainer">
                    <div class="swiper-wrapper">
                      <div class="swiper-slide" v-for="(recmovie, idx11) in recmovies" :key="idx11">
                        <img class="posterImg" style="width: 20vh;" :src="`https://image.tmdb.org/t/p/w500/${recmovie.movie.poster_path}`" alt="" @click="tomovie(recmovie.movie.id)">
                        <p style="color : white">{{ recmovie.movie.title }}</p>
                      </div>
                    </div>
                    <div class="swiper-scrollbar"></div>
                    </div>
                  </div>            
              </div>
          </div>
        </div>
      </div>
</template>

<script>

import axios from 'axios'
import Swiper, { Navigation } from 'swiper' // importing swiper
import 'swiper/css/bundle'
import _ from 'lodash';

const URL = 'http://127.0.0.1:8000'  // 마지막 / 뺴야함


export default {
  components: { 
    },
  data() {
    return {
      movies : null,
      crews: null,
      actors: null,
      genres: null,
      detail_movie : {
        title:1, 
        poster_path:"/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
        youtube_key:"Jvurpf91omw",
        release_date: '2010-10-10'},
      robots : ['robot1.jpg','robot2.jpg','robot3.jpg','robot4.jpg','robot5.jpg','robot6.jpg','robot7.jpg','robot8.jpg','robot9.jpg',],
      robot : 'robot1.jpg',
      show_detail : true,
      choice : 'title',
      recmovies: null,
    }
  },
  computed: {
    youtubeKeyExists() {  // youtube key 여부
      if(this.detail_movie.youtube_key==='nothing') {
        return false
      }
      return true
    },
    searchText() {
      return this.$route.params.searchText
    },
    releaseYear() {
      return this.detail_movie.release_date.substring(0,4)
    }
  },
    created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
    // ---------------------------
    
  
  methods: {   
    movie_like(movieid){
      axios({
          method: 'post',
          url: `${URL}/movies/movie_like/${movieid}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
          data : {
            id : this.$store.state.userid
          }
        })
        .then((res) => {
          this.detail_movie = res.data;
        }).catch((err) => {
          console.log(err);
        });
    },

    // enableScroll() {
    //   document.querySelector('html').style.overflowY = 'scroll';
    // },
    tomovie(id) {
      document.querySelector('html').style.overflowY = 'hidden';
      this.click(id);
      this.recommend_movie(id).then(() => {
        axios({
          method: 'get',
          url: `${URL}/movies/movie/${id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          this.detail_movie = res.data;
        }).catch((err) => {
          console.log(err);
        });
        console.log(this.recmovies);
      });
    },
    recommend_movie(id) {
      return new Promise((resolve, reject) => {
        axios({
          method: 'get',
          url: `${URL}/movies/recommend_movie/${id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then((res) => {
            this.recmovies = JSON.parse(res.data);
            resolve(); // 프라미스 객체 완료
          })
          .catch((err) => {
            console.log(err);
            reject(err); // 프라미스 객체 에러
          });
      });
},
    // Nav Link 검색 방법
    search(searchContent) {
      this.$router.push(
        {
          name : 'search', 
          params : {
            searchContent : searchContent,
            searchText : this.$route.params.searchText
        }
      })
      .catch(()=>{})
      axios({
      method: 'get',
      url : `${URL}/movies/find_movies/${searchContent}/${this.$route.params.searchText}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.movies = res.data
      this.choice = searchContent
      console.log(this.choice);
    }).catch((err) => {
      console.log(err);
    })
    },

    // ------------------------------

    // 배우, 감독 검색 후 다시 그에 관한 영화 검색하는 함수
    search_movie_bycrew(name){
      console.log(name);
      axios({
      method: 'get',
      url : `${URL}/movies/find_movies/crew/${name}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.movies = res.data
      this.choice = 'title'
    }).catch((err) => {
      console.log(err);
    });
    },
    search_movie_byactor(name){
      console.log(name);
      axios({
      method: 'get',
      url : `${URL}/movies/find_movies/actor/${name}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.movies = res.data
      this.choice = 'title'
    }).catch((err) => {
      console.log(err);
    });
    },
    // --------------------------
    // 클릭 함수
    click(movieid) {
      axios({
      method: 'post',
      url : `${URL}/movies/click/${this.$store.state.userid}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      },
      data : {
        'movieid' : movieid
      }
    })
    .then((res) => {
      console.log(res.data);
    }).catch((err) => {
      console.log(err);
    });
    },
    showSpecificGenre(genre){
      axios({
        method: 'get',
        url : `${URL}/movies/find_movies/genre/${genre}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })    
      .then((res) => {
        this.$route.params.searchText = genre
        console.log(res.data);
        this.genres = res.data
        this.choice = 'genre'
      })
      .catch((err) => {
        console.log(err);
      })
    },
    goToMovieByType(data, type){
      this.$router.push(
        {
          name : 'search', 
          params : {
            searchContent : type,
            searchText : data
        }
      })
      .catch(()=>{})
      axios({
        method: 'get',
        url : `${URL}/movies/find_movies/${type}/${data}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })    
      .then((res) => {
        this.$route.params.searchText = data
        this.$route.params.searchContent = type
        console.log(res.data);
        if(type === 'genre'){
          this.genres = res.data.sort((o1,o2) => {
        return o2.popularity - o1.popularity
      })
          // this.choice = type
        }
        else{
          this.movies = res.data.sort((o1,o2) => {
        return o2.popularity - o1.popularity
      })
          // this.choice = 'movie'
        }
      })
      .catch((err) => {
        console.log(err);
      })
    },
    search_actor(){
      axios({
      method: 'get',
      url : `${URL}/movies/search_actor/${this.$route.params.searchText}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.actors = res.data
      this.choice = 'actor'
    }).catch((err) => {
      console.log(err);
    });
    },

    search_crew(){
      axios({
      method: 'get',
      url : `${URL}/movies/search_crew/${this.$route.params.searchText}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.crews = res.data
      this.choice = 'crew'
    }).catch((err) => {
      console.log(err);
    });
    },
  },
  mounted() {
    this.robot = _.sample(this.robots,1)

    document.getElementById('exampleModal').addEventListener('hidden.bs.modal', event => {
      document.querySelector('html').style.overflowY = 'scroll';
    })

    axios({
      method: 'get',
      url : `${URL}/movies/find_movies/${this.$route.params.searchContent}/${this.$route.params.searchText}/`,
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      console.log(res.data);
      this.movies = res.data
      this.movies.sort((o1,o2) => {
        return o2.popularity - o1.popularity
      })
    }).catch((err) => {
      console.log(err);
    })
    const swiper = new Swiper('.swiper', {
      modules: [Navigation],
      speed: 400,
      spaceBetween: 0,
      slidesPerView: 1,
      scrollbar: true,
      allowTouchMove : false,
      mousewheel: {
        invert: false
      },
      scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true,
      },
      breakpoints: {
      450: {
        slidesPerView: 2,  //브라우저가 768보다 클 때
        spaceBetween: 0,
      },
      768: {
        slidesPerView: 3,  //브라우저가 768보다 클 때
        spaceBetween: 0,
      },
      // 1500: {
      //   slidesPerView: 4,  //브라우저가 1024보다 클 때
      //   spaceBetween: 0,
      // },
      // 1500: {
      //   slidesPerView: 5,  //브라우저가 1500보다 클 때
      //   spaceBetween: 0,
      // },
      }
      
    })
  },

}
</script>

<style scoped>
  
  .posterImg {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .hide {
    display: none;
  }

  .nav-link{
    color: gray;
  }

  .text-truncate-container{
    -webkit-line-clamp: 5;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    padding: 0;
  }
  #specificItem:hover {
    cursor: pointer;
    color: #FC3C44;
  }

  .nav-link:hover {
    cursor: pointer;
  }  

  .scroll::-webkit-scrollbar {
    display: none;
  }

   /* 스크롤 문제 해결 관련 */
  /* .modal-open {
  overflow: hidden;
  }
   */
  /* end */

</style>
