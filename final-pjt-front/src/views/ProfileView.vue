<template>
  <div class="container">
    <div class="mt-4" v-show="!user_info" >
      <h1> {{loadingornotfound}} </h1>
      <img style="width: 50vw" class="my-3" :src="require(`@/assets/${robot}`)" alt="">
    </div>
    <div v-show="user_info" class="row justify-content-center">
      <div class="col-10">
        <div
          class="infoBox px-5 py-3"
          style="background-color: #fc3c44; color: white"
        >
          <h1 class="my-5">영화 취향 보고서</h1>
          <div v-if="user_info" class="d-flex justify-content-around">
            <div>
              <h2 v-if="clicks">{{ clicks.length }}</h2>
              <h5>관심</h5>
            </div>
            <div>
              <h2>{{ user_info.likemovies.length }}</h2>
              <h5>좋아요</h5>
            </div>
            <div>
              <h2>{{ user_info.followers.length }}</h2>
              <h5>팔로워</h5>
            </div>
            <div>
              <h2>{{ user_info.followings.length }}</h2>
              <h5>팔로잉</h5>
            </div>
            <button class="btn btn-danger" @click="following">팔로잉</button>
            <button class="btn btn-warning" @click="reset">
              알고리즘 초기화
            </button>
          </div>
        </div>
        <div class="swiper space my-5" id="swiperContainer1" v-show="like_movies">
          <h3 class="mb-4" style="text-align: center">
            <strong v-if="user_info">{{ user_info.username }}</strong
            >님이 좋아한 영화에요
          </h3>
          <div class="swiper-wrapper">
            <div
              class="swiper-slide"
              v-for="(recmovie, idx) in like_movies"
              :key="idx"
            >
              <!-- {{ recmovie }} -->
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
              <p>{{ recmovie.title }}</p>
            </div>
            <div class="swiper-scrollbar"></div>
          </div>
        </div>
        <div class="swiper space my-5" id="swiperContainer2">
          <h3 class="mb-4" style="text-align: center">
            <strong v-if="user_info">{{ user_info.username }}</strong
            >님이 좋아하실 만한 영화에요
          </h3>
          <div class="swiper-wrapper">
            <div
              class="swiper-slide"
              v-for="(recmovie, idx) in recommend_movies"
              :key="idx"
            >
              <!-- {{ recmovie }} -->
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
                {{
                  parseInt(
                    (recmovie.score / recommend_movies[0].score) * 100 - 1
                  )
                }}
              </p>
            </div>
          </div>
          <div class="swiper-scrollbar"></div>
        </div>
        <div class="row justify-content-center">
          <div class="col-5 graphBox" style="min-height: 400px">
            <h2>좋아하는 장르</h2>
            <canvas ref="myGenreChart" width="100%" height="100%"></canvas>
          </div>
          <div class="col-5 graphBox" style="min-height: 400px">
            <h2>좋아하는 배우</h2>
            <canvas ref="myActorChart" width="100%" height="100%"></canvas>
          </div>
        </div>
        <div class="row justify-content-center mt-4">
          <div class="col-5 graphBox" style="min-height: 400px">
            <h2>좋아하는 감독</h2>
            <canvas ref="myCrewChart" width="100%" height="100%"></canvas>
          </div>
          <div class="col-5 graphBox" style="min-height: 400px">
            <h2>좋아하는 키워드</h2>
            <canvas ref="myKeywordChart" width="100%" height="100%"></canvas>
          </div>
        </div>
        <div class="text-end my-5 signature">
          <h1>Sincerely,</h1>
          <h1>BEANWIKI</h1>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-xl modal-dialog-scrollable">
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
                <p class="mt-3 text-truncate-container">
                  {{ detail_movie.overview }}
                </p>
                <i
                  id="movieLike"
                  class="fa-regular fa-heart fa-lg mt-3"
                  @click="movie_like(detail_movie.id)"
                >
                  {{ detail_movie.likeuser }}</i
                >
              </div>
              <img
                class=""
                style="width: 30vh; margin-left: 50px"
                :src="`https://image.tmdb.org/t/p/original/${detail_movie.poster_path}`"
                alt=""
              />
            </div>

            <hr style="background: white; height: 2px; border: 0" />

            <div class="comment"></div>
            <h2 class="text-white text-start mx-5">이런 영화는 어떠신가요?</h2>
            <div class="swiper space my-5 mx-5" id="swiperContainer3">
              <div class="swiper-wrapper">
                <div
                  class="swiper-slide"
                  v-for="(recmovie, idx11) in recmovies"
                  :key="idx11"
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
</template>
<script>
import axios from "axios";
import Chart from "chart.js/auto";
import Swiper, { Navigation } from "swiper"; // importing swiper
import _ from "lodash";

const URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      user_info: null, // 유저정보 다 있음, 좋아요 누른 영화도 있음
      clicks: [], // 지금까지 클릭한 영화들
      recommend_movies: null, // 추천 영화 리스트
      like_movies: null,
      keywords: null, // 지금까지 본 키워드 들
      genres: null, // 지금까지 본 장르들
      actors: null, // 지금까지 본 배우들
      crews: null, // 지금까지 본 감독들
      detail_movie: {
        title: 1,
        poster_path: "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
        youtube_key: "Jvurpf91omw",
        release_date: "2010-10-10",
      },
      robots : ['robot1.jpg','robot2.jpg','robot3.jpg','robot4.jpg','robot5.jpg','robot6.jpg','robot7.jpg','robot8.jpg','robot9.jpg','robot10.jpg','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png','robot11.png'],
      robot : 'robot1.jpg',
      loadingornotfound : '로딩 중 입니다 휴먼',
    };
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
    created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
  methods: {
    movie_like(movieid) {
      axios({
        method: "post",
        url: `${URL}/movies/movie_like/${movieid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          id: this.$store.state.userid,
        },
      })
        .then((res) => {
          this.detail_movie = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    tomovie(id) {
      document.querySelector("html").style.overflowY = "hidden";
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
    reset() {
      axios({
        method: "delete",
        url: `${URL}/account/reset_algorithm/${this.$route.params.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: { 'id' : this.$store.state.userid },
      })
        .then((res) => {
          this.$router.push({
              name: 'MainView',
          });
        })
        .catch((err) => {
          console.log(err.data);
          alert("본인만 초기화가 가능합니다.");
          this.$router.push({
            name: "error",
          });
        });
    },
    following() {
      axios({
        method: "post",
        url: `${URL}/account/following/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          id: this.$route.params.userid,
        },
      })
        .then((res) => {
          this.user_info = res.data;
        })
        .catch((err) => {
          alert("자추 금지");
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
    getRandomColor(){
      const saturation = 70; // 채도 값
      const lightness = 60; // 명도 값

      const hue = Math.floor(Math.random() * 360); // 색상값 (0-359 범위)

      const hslColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

      return hslColor;
    },
    makegenrechart() {
      const genre_labels = Object.keys(this.genres);
      const genre_data = Object.values(this.genres);
      const datasetSize = genre_labels.length; // 데이터 포인트 개수
      const backgroundColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const borderColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const data = {
        labels: genre_labels,
        datasets: [
          {
            label: `${this.$store.state.username}님이 좋아하는 장르`,
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            data: genre_data,
          },
        ],
      };
      const config = {
        type: "bar",
        data,
        options: {},
      };
      const myChart = new Chart(this.$refs.myGenreChart, config);
    },
    makeactorchart() {
      const actor_labels = Object.keys(this.actors);
      const actor_data = Object.values(this.actors);
      const datasetSize = actor_labels.length; // 데이터 포인트 개수
      const backgroundColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const borderColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const data = {
        labels: actor_labels,
        datasets: [
          {
            label: `${this.$store.state.username}님이 좋아하는 배우`,
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            data: actor_data,
          },
        ],
      };
      const config = {
        type: "polarArea",
        data,
        options: {},
      };
      const myChart = new Chart(this.$refs.myActorChart, config);
    },
    makecrewchart() {
      const crew_labels = Object.keys(this.crews);
      const crew_data = Object.values(this.crews);
      const datasetSize = crew_labels.length; // 데이터 포인트 개수
      const backgroundColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const borderColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const data = {
        labels: crew_labels,
        datasets: [
          {
            label: `${this.$store.state.username}님이 좋아하는 감독`,
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            data: crew_data,
          },
        ],
      };
      const config = {
        type: "line",
        data,
        options: {
          // responsive: false,
        },
      };
      const myChart = new Chart(this.$refs.myCrewChart, config);
    },
    makekeywordchart() {
      const keyword_labels = Object.keys(this.keywords);
      const keyword_data = Object.values(this.keywords);
      const datasetSize = keyword_labels.length; // 데이터 포인트 개수
      const backgroundColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const borderColors = Array.from({ length: datasetSize }, () =>
        this.getRandomColor()
      );
      const data = {
        labels: keyword_labels,
        datasets: [
          {
            label: `${this.$store.state.username}님이 좋아하는 키워드`,
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            data: keyword_data,
          },
        ],
      };
      const config = {
        type: "doughnut",
        data,
        options: {
          // responsive: false,
        },
      };
      const myChart = new Chart(this.$refs.myKeywordChart, config);
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
            resolve(); // 프라미스 객체 완료
          })
          .catch((err) => {
            console.log(err);
            reject(err); // 프라미스 객체 에러
          });
      });
    },
    get_like_movies() {
      axios({
        method: "get",
        url: `${URL}/movies/like_movies/${this.$route.params.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.like_movies = res.data;
        })
        .catch((err) => {
          console.log(err);
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
  },
  mounted() {
    this.robot = _.sample(this.robots,1)
    setTimeout(() => {
      this.loadingornotfound = '내용이 없습니다 휴먼'
    }, 3000);
    document
      .getElementById("exampleModal")
      .addEventListener("hidden.bs.modal", (event) => {
        document.querySelector("html").style.overflowY = "scroll";
      });
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
          slidesPerView: 2.7, //브라우저가 768보다 클 때
          spaceBetween: 0,
        },
        768: {
          slidesPerView: 3.2, //브라우저가 768보다 클 때
          spaceBetween: 0,
        },
        1024: {
          slidesPerView: 2.7, //브라우저가 1024보다 클 때
          spaceBetween: 0,
        },
      },
    });
    axios({
      method: "get",
      url: `${URL}/account/profile/${this.$route.params.userid}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then((res) => {
        this.user_info = res.data.profile;
        this.clicks = res.data.click;
        this.recommend_movies = JSON.parse(res.data.recommend_movies).slice(
          0,
          15
        );
        this.recommend_movies.push({
          movie: {
            poster_path: "more",
          },
        });
        console.log(this.recommend_movies);
        let keywords = {};
        let genres = {};
        let actors = {};
        let crews = {};
        this.clicks.forEach((click) => {
          click.movies.keyword.forEach((key) => {
            if (keywords[key.name]) {
              keywords[key.name]++;
            } else {
              keywords[key.name] = 1;
            }
          });
          click.movies.genre.forEach((key) => {
            if (genres[key.name]) {
              genres[key.name]++;
            } else {
              genres[key.name] = 1;
            }
          });
          click.movies.actor.forEach((key) => {
            if (actors[key.name]) {
              actors[key.name]++;
            } else {
              actors[key.name] = 1;
            }
          });
          click.movies.crew.forEach((key) => {
            if (crews[key.name]) {
              crews[key.name]++;
            } else {
              crews[key.name] = 1;
            }
          });
        });
        this.keywords = keywords;
        this.genres = genres;
        this.actors = actors;
        this.crews = crews;
        this.makegenrechart();
        this.makeactorchart();
        this.makecrewchart();
        this.makekeywordchart();
        this.get_like_movies();
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
.infoBox {
  border: 1px solid black;
  border-radius: 10px;
  margin-bottom: 30px;
  margin-top: 30px;
}

.graphBox {
  border: 1px solid black;
  border-radius: 10px;
  margin-left: 20px;
  margin-right: 20px;
}

.signature {
  font-family: "Dancing Script", cursive;
  margin-right: 50px;
}
</style>