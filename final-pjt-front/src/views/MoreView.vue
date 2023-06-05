<template>
  <div class="container">
        <h1>{{ $route.params.text }} </h1>
        <div class="row" v-if="movies && $route.params.type == 'personal'">
            <div class="col-md-4 col-lg-3" v-for="movie in movies" :key="movie.movie.id">
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="tomovie(movie.movie.id)">
                    <img :src="`https://image.tmdb.org/t/p/original/${movie.movie.poster_path}`" alt="">
                </button>
            </div>
        </div>
        <div class="row" v-else-if="movies && $route.params.type != 'personal'">
            <div class="col-md-4 col-lg-3" v-for="movie in movies" :key="movie.title">
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="tomovie(movie.id)">
                    <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="">
                </button>
            </div>
        </div>
        <div v-if="movies == false">
        <h1>영화가 없습니다.</h1>
        <img src="http://jjal.today/data/file/gallery/1028612757_lM5AsgeU_59f9b0985577f3793835e964fb58dd7d0252122b.jpeg" alt="">
        </div>


        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg modal-dialog-scrollable">
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
                    <p style="display: inline;" v-for="keyword in detail_movie.keyword " :key="keyword.name"> #{{ keyword.name }}</p>
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
                  <img class="" style="width: 20vh; margin-left: 50px;" :src="`https://image.tmdb.org/t/p/original/${detail_movie.poster_path}`" alt="">
                </div>


                <hr style="background: white; height:2px; border:0">

                <div class="comment">

                </div>
                  <h2 class="text-white text-start mx-5">이런 영화는 어떠신가요?</h2>
                  <div class="swiper space my-5 mx-5" id="swiperContainer">
                    <div class="swiper-wrapper">
                      <div class="swiper-slide" v-for="(recmovie, idx) in recmovies" :key="idx">
                        <img style="width: 20vh;" :src="`https://image.tmdb.org/t/p/w500/${recmovie.movie.poster_path}`" alt="" @click="tomovie(recmovie.movie.id)">
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
const URL = 'http://127.0.0.1:8000'  // 마지막 / 뺴야함

export default {
    data() {
        return {
            movies : null,
            detail_movie : {
                title:1, 
                poster_path:"/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
                youtube_key:"Jvurpf91omw",
                release_date: '2010-10-10'
            },
            recmovies : null,
            }  
    },
    created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
    computed: {
    youtubeKeyExists() {  // youtube key 여부
      if(this.detail_movie.youtube_key==='nothing') {
        return false
      }
      return true
    },
    releaseYear() {
      return this.detail_movie.release_date.substring(0,4)
    }
  
  },
  mounted() {
    if (this.$route.params.type == 'personal'){
        this.get_personal_movie()
    } else if (this.$route.params.type == 'actor'){
        this.get_more_movie()
    } else if (this.$route.params.type == 'genre'){
        this.get_more_movie()
    } else if (this.$route.params.type == 'crew'){
        this.get_more_movie()
    } else if (this.$route.params.type == 'trend'){
        this.get_trend_movie()
    }

    document.getElementById('exampleModal').addEventListener('hidden.bs.modal', event => {
      document.querySelector('html').style.overflowY = 'scroll';
    })
    const swiper = new Swiper('.swiper', {
      modules: [Navigation],
      speed: 400,
      spaceBetween: 0,
      slidesPerView: 1,
      scrollbar: true,
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
      }
      
    })
  },
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
    goGenre(data){
      this.$router.push(
        {
          name : 'search', 
          params : {
            searchContent : 'genre',
            searchText : data
        }
      })
      
    },
    // 영화 디테일 관련 함수
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
    // 여기부터 추천 영화 관련 함수
    get_personal_movie() {
      axios({
        method: 'get',
        url : `${URL}/movies/recommend_main/${this.$store.state.userid}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movies = JSON.parse(res.data)
      }).catch((err) => {
        console.log(err);
      });
      },
    get_more_movie(){
      axios({
        method: 'get',
        url : `${URL}/movies/more_movies/${this.$route.params.type}/${this.$route.params.keyword}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movies = res.data
        console.log(111111111);
        console.log(this.movies);
      }).catch((err) => {
        console.log(err);
      });
    },
    get_trend_movie(){
      axios({
        method: 'get',
        url : `${URL}/movies/recommend_trend/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        let trend = []
        const result = JSON.parse(res.data)
        result.forEach((movie) => {
          movie.results.forEach((mov) => {
            trend.push({title : mov.title, id : mov.id, poster_path : mov.poster_path})
          })
        })
        this.movies = trend
      }).catch((err) => {
        console.log(err);
      });
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
    }
    
  },

  
}
</script>

<style scoped>
  
  img {
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
  .scroll::-webkit-scrollbar {
    display: none;
  }
</style>