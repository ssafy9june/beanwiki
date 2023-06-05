<template>
  <div>
    <div v-if='title_movie'>
      <div class="my-4">
        <h3>금주의 최신 영화</h3>
        <h1>{{ title_movie.title }}</h1>
      </div>
      <div
        class="ratio ratio-16x9"
        style="height: 40vw; margin-left: 0px; margin-right: 0px"
      >
        <iframe
          :src="`https://www.youtube.com/embed/${this.title_movie.youtube_key}?autoplay=1&mute=1&loop=1`"
          frameborder="0" v-if="title_movie"
        ></iframe>
      </div>
    </div>
    <div class="container">
      <div v-show="personal_movie">
      <div class="swiper space my-5" id="swiperContainer">
        <h3 class="mb-4" style="text-align: left">
          {{ $store.state.username }}님을 위한 <strong>추천 영화</strong>를 준비해
          보았어요
        </h3>
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="(recmovie, idx) in personal_movie" :key="idx">
            <button
              v-if="recmovie.movie.poster_path !== 'more'"
              type="button"
              class="btn"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="tomovie(recmovie.movie.id)"
            >
              <img
                class="posterImg"
                style="width: 20vw"
                :src="`https://image.tmdb.org/t/p/w500/${recmovie.movie.poster_path}`"
                alt=""
              />
            </button>
            <button v-else @click="goToMoreView('personal', 'movie')">
              <img
                class="posterImg"
                src="@/assets/more_movies.png"
                style="width: 20vw; border: none"
                alt="HI"
              />
            </button>
            <p>{{ recmovie.movie.title }}</p>
            <p v-if="recmovie.movie.poster_path !== 'more'">
              추천도 :
              {{ parseInt((recmovie.score / personal_movie[0].score) * 100 - 1) }}
            </p>
          </div>
        </div>
        <div class="swiper-scrollbar"></div>
      </div>
      <div class="swiper space my-5" id="swiperContainer">
        <h3 class="mb-4" style="text-align: left">
          {{ $store.state.username }}님이 좋아하시는
          <strong>{{ recgenre }}</strong> 장르의 영화에요
        </h3>
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="(recmovie, idx) in genre_movie" :key="idx">
            <button
              v-if="recmovie.poster_path !== 'more'"
              type="button"
              class="btn"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="tomovie(recmovie.id)"
            >
              <img
                class="posterImg"
                style="width: 20vw"
                :src="`https://image.tmdb.org/t/p/w500/${recmovie.poster_path}`"
                alt=""
              />
            </button>
            <button v-else @click="goToMoreView('genre', recgenre)">
              <img
                class="posterImg"
                src="@/assets/more_movies.png"
                style="width: 20vw; border: none"
                alt="HI"
              />
            </button>
            <p>{{ recmovie.title }}</p>
          </div>
        </div>
        <div class="swiper-scrollbar"></div>
      </div>
      <div class="swiper space my-5" id="swiperContainer">
        <h3 class="mb-4" style="text-align: left">
          {{ $store.state.username }}님이 좋아하시는 배우 <strong>{{ recactor }}</strong
          >가 출연한 작품이에요
        </h3>
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="(recmovie, idx) in actor_movie" :key="idx">
            <button
              v-if="recmovie.poster_path !== 'more'"
              type="button"
              class="btn"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="tomovie(recmovie.id)"
            >
              <img
                class="posterImg"
                style="width: 20vw"
                :src="`https://image.tmdb.org/t/p/w500/${recmovie.poster_path}`"
                alt=""
              />
            </button>
            <button v-else @click="goToMoreView('actor', recactor)">
              <img
                class="posterImg"
                src="@/assets/more_movies.png"
                style="width: 20vw; border: none"
                alt="HI"
              />
            </button>
            <p>{{ recmovie.title }}</p>
          </div>
        </div>
        <div class="swiper-scrollbar"></div>
      </div>
      <div class="swiper space my-5" id="swiperContainer">
        <h3 class="mb-4" style="text-align: left">
          {{ $store.state.username }}님이 좋아하시는 감독 <strong>{{ reccrew }}</strong
          >의 영화에요
        </h3>
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="(recmovie, idx) in crew_movie" :key="idx">
            <button
              v-if="recmovie.poster_path !== 'more'"
              type="button"
              class="btn"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="tomovie(recmovie.id)"
            >
              <img
                class="posterImg"
                style="width: 20vw"
                :src="`https://image.tmdb.org/t/p/w500/${recmovie.poster_path}`"
                alt=""
              />
            </button>
            <button v-else @click="goToMoreView('crew', reccrew)">
              <img
                class="posterImg"
                src="@/assets/more_movies.png"
                style="width: 20vw; border: none"
                alt="HI"
              />
            </button>
            <p>{{ recmovie.title }}</p>
          </div>
        </div>
        <div class="swiper-scrollbar"></div>
      </div>
      </div>
      <div class="swiper space my-5" id="swiperContainer">
        <h3 class="mb-4" style="text-align: left">최신 트랜드 영화를 모아봤어요.</h3>
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="(recmovie, idx) in trend_movie" :key="idx">
            <button
              v-if="recmovie.poster_path !== 'more'"
              type="button"
              class="btn"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="tomovie(recmovie.id)"
            >
              <img
                class="posterImg"
                style="width: 20vw"
                :src="`https://image.tmdb.org/t/p/w500/${recmovie.poster_path}`"
                alt=""
              />
            </button>
            <button v-else @click="goToMoreView('trend', 'trend')">
              <img
                class="posterImg"
                src="@/assets/more_movies.png"
                style="width: 20vw; border: none"
                alt="HI"
              />
            </button>
            <p>{{ recmovie.title }}</p>
          </div>
        </div>
        <div class="swiper-scrollbar"></div>
      </div>
    </div>

    <div>
      <!-- Modal -->
      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-xl">
          <div class="modal-content">
            <!-- <div class="modal-header">
            </div> -->
            <div class="modal-body bg-black">
              <div style="height: 50vh" class="ratio ratio-16x9">
                <iframe
                  v-if="youtubeKeyExists"
                  :src="`https://www.youtube.com/embed/${detail_movie.youtube_key}?autoplay=1&amp;mute=1`"
                  frameborder="0"
                ></iframe>
                <h4 v-else>트레일러 영상이 존재하지 않습니다.</h4>
                <br />
              </div>
              <div class="d-flex mx-5 mt-5">
                <div class="movieDetails text-start text-white">
                  <h1 class="mb-3">{{ detail_movie.title }}</h1>
                  <p
                    style="display: inline"
                    v-for="(keyword, idx) in detail_movie.keyword"
                    :key="idx"
                  >
                    #{{ keyword.name }}
                  </p>
                  <!-- <p> {{ detail_movie }} </p> -->
                  <br />
                  <div class="mt-3">
                    <p style="display: inline">{{ releaseYear }}</p>
                    |
                    <p
                      id="specificItem"
                      style="display: inline"
                      data-bs-toggle="modal"
                      data-bs-target="#exampleModal"
                      @click="goToMovieByType(genre.name, 'genre')"
                      v-for="genre in detail_movie.genre"
                      :key="genre.name"
                    >
                      {{ genre.name }}
                    </p>
                    <br />
                    <p style="display: inline">배우:</p>
                    <p
                      id="specificItem"
                      style="display: inline"
                      data-bs-toggle="modal"
                      data-bs-target="#exampleModal"
                      @click="goToMovieByType(actor.name, 'actor')"
                      v-for="actor in detail_movie.actor"
                      :key="actor.name"
                    >
                      {{ actor.name }}
                    </p>
                    <br />
                    <p style="display: inline">감독:</p>
                    <p
                      id="specificItem"
                      style="display: inline"
                      data-bs-toggle="modal"
                      data-bs-target="#exampleModal"
                      @click="goToMovieByType(crew.name, 'crew')"
                      v-for="crew in detail_movie.crew"
                      :key="crew.name"
                    >
                      {{ crew.name }}
                    </p>
                  </div>
                  <p class="mt-3 text-truncate-container">{{ detail_movie.overview }}</p>
                  <i id="movieLike" class="fa-regular fa-heart fa-lg mt-3" @click="movie_like(detail_movie.id)"> {{ detail_movie.likeuser }}</i>
                  
                </div>
                <img
                  class="posterImg"
                  style="width: 30vh; margin-left: 50px"
                  :src="`https://image.tmdb.org/t/p/original/${detail_movie.poster_path}`"
                  alt=""
                />
              </div>

              <hr style="background: white; height: 2px; border: 0" />

              <div class="comment"></div>
              <h2 class="text-white text-start mx-5">이런 영화는 어떠신가요?</h2>
              <div class="swiper space my-5 mx-5" id="swiperContainer">
                <div class="swiper-wrapper">
                  <div
                    class="swiper-slide"
                    v-for="(recmovie, idx) in recmovies"
                    :key="idx"
                  >
                    <img
                      class="posterImg"
                      style="width: 20vh"
                      :src="`https://image.tmdb.org/t/p/w500/${recmovie.movie.poster_path}`"
                      alt=""
                      @click="tomovie(recmovie.movie.id)"
                    />
                    <p style="color: white">{{ recmovie.movie.title }}</p>
                  </div>
                </div>
                <div class="swiper-scrollbar"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Swiper, { Navigation } from "swiper"; // importing swiper
import "swiper/css/bundle";
const URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      personal_movie: null,
      title_movie : null,
      actor_movie: null,
      genre_movie: null,
      crew_movie: null,
      trend_movie: null,
      recactor: null,
      recgenre: null,
      reccrew: null,
      temp: null,
      detail_movie: {
        title: 1,
        poster_path: "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
        youtube_key: "Jvurpf91omw",
        release_date: "2010-10-10",
      },
      show_detail: true,
      recmovies: null,
    };
  },
  created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
  methods: {
    goGenre(data) {
      this.$router.push({
        name: "search",
        params: {
          searchContent: "genre",
          searchText: data,
        },
      });
    },
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
    // 영화 디테일 관련 함수
    tomovie(id) {
      this.click(id);
      this.recommend_movie(id).then(() => {
        axios({
          method: "get",
          url: `${URL}/movies/movie/${id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.detail_movie = res.data;
          })
          .catch((err) => {
            console.log(err);
          });
        console.log(this.recmovies);
      });
    },
    recommend_movie(id) {
      return new Promise((resolve, reject) => {
        axios({
          method: "get",
          url: `${URL}/movies/recommend_movie/${id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.recmovies = JSON.parse(res.data);
            console.log("awdawd");
            resolve(); // 프라미스 객체 완료
          })
          .catch((err) => {
            console.log(err);
            reject(err); // 프라미스 객체 에러
          });
      });
    },
    goToMovieByType(data, type) {
      this.$router.push({
        name: "search",
        params: {
          searchContent: type,
          searchText: data,
        },
      });
      axios({
        method: "get",
        url: `${URL}/movies/find_movies/${type}/${data}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.$route.params.searchText = data;
          this.$route.params.searchContent = type;
          console.log(res.data);
          if (type === "genre") {
            this.genres = res.data.sort((o1, o2) => {
              return o2.popularity - o1.popularity;
            });
            // this.choice = type
          } else {
            this.movies = res.data.sort((o1, o2) => {
              return o2.popularity - o1.popularity;
            });
            // this.choice = 'movie'
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    click(movieid) {
      axios({
        method: "post",
        url: `${URL}/movies/click/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          movieid: movieid,
        },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_title_movie(id){
      axios({
            method: 'get',
            url : `https://api.themoviedb.org/3/movie/${id}/videos?api_key=WRITE_YOUR_OWN_API_KEY`,
          })
          .then((res) => {
            res.data.results.forEach((movie) => {
              if (movie.type == "Trailer") {
                this.temp['youtube_key'] = movie.key
                this.title_movie = this.temp
              }
            })
            console.log(res.data.results);
          }).catch((err) => {
            console.log(err);
          });
    },
    // 여기부터 추천 영화 관련 함수
    get_personal_movie() {
      axios({
        method: "get",
        url: `${URL}/movies/recommend_main/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          if (JSON.parse(res.data).length === 0){
          } else {
            this.personal_movie = JSON.parse(res.data).slice(0, 15);
            this.personal_movie.push({
              movie: {
                poster_path: "more",
              },
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_actor_movie() {
      axios({
        method: "get",
        url: `${URL}/movies/recommend_actor/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.actor_movie = res.data.movies.slice(0, 15);
          this.actor_movie.push({ poster_path: "more" });
          this.recactor = res.data.actor;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_genre_movie() {
      axios({
        method: "get",
        url: `${URL}/movies/recommend_genre/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.genre_movie = res.data.movies.slice(0, 15);
          this.genre_movie.push({ poster_path: "more" });
          this.recgenre = res.data.genre;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_crew_movie() {
      axios({
        method: "get",
        url: `${URL}/movies/recommend_crew/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.crew_movie = res.data.movies.slice(0, 15);
          this.crew_movie.push({ poster_path: "more" });
          this.reccrew = res.data.crew;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_trend_movie() {
      axios({
        method: "get",
        url: `${URL}/movies/recommend_trend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          let trend = [];
          const result = JSON.parse(res.data);
          result.forEach((movie) => {
            movie.results.forEach((mov) => {
              trend.push({ title: mov.title, id: mov.id, poster_path: mov.poster_path });
            });
          });
          this.trend_movie = trend.slice(0, 15);
          let ran = Math.floor(Math.random() * 20)
          if (ran>=15) { ran -= 6}
          this.temp = this.trend_movie[ran]
          // this.title_movie = this.trend_movie[ran]
          this.trend_movie.push({ poster_path: "more" });
          // console.log(this.title_movie);
        })
        .then((res) => {
          // console.log(this.title_movie.id);
          this.get_title_movie(parseInt(this.temp.id))
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 여기까지 추천 영화 관련 함수임
    // 영화 장르 이동

    showSpecificGenre(genre) {
      axios({
        method: "get",
        url: `${URL}/movies/find_movies/genre/${genre}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.$route.params.searchText = genre;
          console.log(res.data);
          this.genres = res.data;
          this.choice = "genre";
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goToMoreView(type, keyword) {
      this.$router.push({
        name: "more",
        params: {
          type: type,
          keyword: keyword,
        },
      });
    },
  },
  mounted() {
    const swiper = new Swiper(".swiper", {
      modules: [Navigation],
      speed: 400,
      spaceBetween: 0,
      slidesPerView: 1,
      scrollbar: true,
      allowTouchMove : false,
      mousewheel: {
        invert: false,
      },
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
      breakpoints: {
        450: {
          slidesPerView: 3, //브라우저가 768보다 클 때
          spaceBetween: 0,
        },
        768: {
          slidesPerView: 3.5, //브라우저가 768보다 클 때
          spaceBetween: 0,
        },
        1024: {
          slidesPerView: 3.2, //브라우저가 1024보다 클 때
          spaceBetween: 0,
        },
        // 1500: {
        //   slidesPerView: 5,  //브라우저가 1500보다 클 때
        //   spaceBetween: 0,
        // },
      },
    });
    // 추천 목록 받아오기, 숫자는 user id로 바꾸기
    axios({
      method: "post",
      url: "http://127.0.0.1:8000/account/",
      data: {
        token: this.$store.state.token,
      },
    })
      .then((res) => {
        this.$store.dispatch("save_userid", JSON.parse(res.data).id);
      })
      .catch((err) => {
        console.log(err);
      })
      .then((res) => {
        this.get_personal_movie();
        this.get_actor_movie();
        this.get_crew_movie();
        this.get_genre_movie();
        this.get_trend_movie();
      })
      .catch((err) => {});
  },
  computed: {
    youtubeKeyExists() {
      // youtube key 여부
      if (this.detail_movie.youtube_key === "nothing") {
        return false;
      }
      return true;
    },
    releaseYear() {
      return this.detail_movie.release_date.substring(0, 4);
    },
  },
};
</script>

<style>
#specificGenre:hover {
  cursor: pointer;
  color: #fc3c44;
}
.mainImg {
  height: 150px;
}

.mainLabel {
  margin-right: 50px;
}

.container {
  --bs-gutter-x: 0px;
}

.swiper-slide {
  margin-bottom: 20px;
}

.swiper-slide > p {
  font-size: 20px;
  margin-top: 5px;
}
#specificItem:hover {
  cursor: pointer;
  color: #fc3c44;
}

#movieLike:hover {
  cursor: pointer;
}
</style>
