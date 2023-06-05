<template>
  <div class="aboutContainer" v-scroll="handleScroll">
    <img src="@/assets/imnotarobot.jpeg" alt="" style="width : 50%; height : 80%" v-if="imrobot" class="imrobot">
    <div class="logo showimg"></div>
    <p id="test"></p>
    <div class="title">
      <h1 class="aboutTitle textAni1 fw-bold" id="w1">
        영화를 만나는 새로운 방법
      </h1>
      <button
        class="btn btn-danger aboutStartBtn"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
        @click="LoginOrSignup(true)"
        v-if="!isLoggedIn"
      >
        Start
      </button>
    </div>

    <div class="aboutFunction">
      <div style="display: flex; justify-content: space-evenly">
        <div class="funcReview">
          <p id="" class="text-danger fs-4 fw-bold textAni1">REVIEW</p>
          <h1 id="" class="text-white fw-bold mb-4 textAni1">
            당신의 취향을
          </h1>
          <h1 id="" class="text-white fw-bold mb-4 textAni1">
            분석해 드립니다
          </h1>
          <h4 class="text-white textAni1">
            관심가는 영화를 바탕으로
          </h4>
          <h4 class="text-white textAni1">
            당신의 취향을 분석합니다
          </h4>
            
        </div>
        <div class="funcReviewImg"></div>
      </div>

      <div style="display: flex; justify-content: space-evenly">
        <div class="recommendImg"></div>
        <div class="funcReview">
          <p id="w1" class="text-danger fs-4 fw-bold textAni1 ani1">RECOMMENDATION</p>
          <h1 id="w2" class="text-white fw-bold textAni1 ani1">
            고민하고 있는
          </h1>
          <h1 id="w3" class="text-white fw-bold  textAni1 ani1">
            나를 위한
          </h1>
          <h1 class="text-white fw-bold mb-4 textAni1 ani1">
            맞춤형 추천
          </h1>
          <h4 class="text-white textAni1 ani1">
            코사인 유사도 알고리즘을 활용해
          </h4>
          <h4 class="text-white textAni1 ani1">
            당신에게 가장 적절한 영화를 추천합니다
          </h4>

        </div>
      </div>
      
      <div
        style="
          display: flex;
          justify-content: space-around;
          align-items: center;
        "
        class="mt-5"
      >
        <div
          class="aboutFunctionLeft d-flex flex-column justify-content-center"
        >
          <div class="leftViewImg"></div>
        </div>
        <div class="aboutFunctionMiddle text-white">
          <p id="" class="text-danger fs-4 fw-bold textAni1 ani2">FROM THE NEW PERSPECTIVE</p>
          <h1 id="" class="text-white fw-bold textAni1 ani2">
            영화를
          </h1>
          <h1 class="text-white fw-bold  textAni1 ani2">
            다양한
          </h1>
          <h1 class="text-white fw-bold mb-4 textAni1 ani2">
            시각으로
          </h1>
          <h1 class="text-white fw-bold textAni1 ani2">
            다시보기
          </h1>
        </div>
        <div
          class="aboutFunctionRight d-flex flex-column justify-content-center"
        >
          <div class="rightViewImg"></div>
        </div>
      </div>
    </div>
    <div class="aboutDatacon" style="height: 2500px">
      <div class="aboutData">
        <div class="title">
          <p class="text-danger fs-5 fw-bold ani3">WHAT WE UTILIZE</p>
          <h1 class="ani3">
            다양한 <strong>기술</strong>과 함께 <strong>당신</strong>을
            알아갑니다
          </h1>
        </div>
        <div class="mx-auto dataList d-flex aboutDataContainer">
          <div class="d-flex align-items-center card">
            <img
              class="card-img-top"
              src="../assets/tmdb_logo.png"
              alt="Card image cap"
              style=""
            />
            <h5 class="card-title mb-5"><strong>The Movie Database</strong></h5>
          </div>
          <div class="card" style="">
            <img
              class="card-img-top"
              src="../assets/tmdb_logo.png"
              alt="Card image cap"
            />
            <h5 class="card-title mb-5"><strong>The Drama D</strong></h5>
          </div>
          <div class="card" style="">
            <img
              class="card-img-top"
              src="../assets/tmdb_logo.png"
              alt="Card image cap"
            />
            <h5 class="card-title mb-5"><strong>The Music Database</strong></h5>
          </div>
          <div class="card">
            <img
              class="card-img-top"
              src="../assets/tmdb_logo.png"
              alt="Card image cap"
            />
            <h5 class="card-title mb-5">
              <strong></strong>
            </h5>
          </div>
          <div class="card">
            <img
              class="card-img-top  my-auto"
              src="../assets/skillset/django.png"
              alt="Card image cap"
              id="django"
            />
            <label for="django" style="margin-bottom : 20px"> <strong>Django</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top  my-auto"
              style="width: 25vw"
              src="../assets/skillset/vue.png"
              alt="Card image cap"
              id="vuetify"
            />
            <label for="vuetify" style="margin-bottom : 20px"> <strong>Vuetify</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top  my-auto"
              style="width: 25vw"
              src="../assets/tmdb_logo.png"
              alt="Card image cap"
              id="tmdb"
            />
            <label for="tmbd" style="margin-bottom : 20px"> <strong>The Movie Database</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top  my-auto"
              style="width: 25vw"
              src="../assets/skillset/bard.png"
              alt="Card image cap"
              id="bard"
            />
            <label for="bard" style="margin-bottom : 20px"> <strong>Google Bard AI</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top  my-auto"
              style="width: 25vw"
              src="../assets/skillset/swiper.png"
              alt="Card image cap"
              id="swiper"
            />
            <label for="swiper" style="margin-bottom : 20px"> <strong>Swiper</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top my-auto"
              style="width: 25vw"
              src="../assets/skillset/vuetify.svg"
              alt="Card image cap"
              id="vuetify"
            />
            <label for="vuetify" style="margin-bottom : 20px"> <strong>Vuetify</strong> </label>
          </div>
          <div class="card">
            <img
              class="card-img-top my-auto"
              style="width: 25vw"
              src="../assets/skillset/chatGPT.png"
              alt="Card image cap"
              id="chatgpt"
            />
            <label for="chatgpt" style="margin-bottom : 20px"> <strong>chatGPT</strong> </label>
          </div>
        </div>
      </div>
    </div>
    <p class="text-danger fs-5 fw-bold">LET US DO THE THINKING</p>
    <h1 class="mb-3">생각나지 않는 영화 <strong>고민</strong>은 그만!</h1>
    <h4 class="mb-5">최신 대화형 Bard AI와 함께 기억나지 않는 영화를 찾아보세요! </h4>
    <div class="bardImg"></div>

    <div class="aboutPeople">
      <p class="text-danger fs-5 fw-bold">WE LOVE MOVIE AND RECOMMENDATION</p>
      <h1 class="mb-5">영화를 <strong>사랑</strong>하는 사람들이 만들었습니다.</h1>
      <div class="people d-flex justify-content-around">
        <figure>
          <img src="../assets/profile/bean.png" width="400px" height="500px" />
          <div class="caption fs-3 fw-bold">팀원 현빈</div>
        </figure>
        <figure>
          <img src="../assets/profile/june.png" width="400px" height="500px" />
          <div class="caption fs-3 fw-bold">팀원 준홍</div>
        </figure>
      </div>

    </div>
    <div class="aboutQna mb-5">
      <p class="text-danger fs-5 fw-bold mt-5">QUESTIONS AND ANSWER</p>
      <h1>아래의 <strong>내용</strong>도 함께 살펴보세요</h1>
        <div class="accordion my-5 accordion-flush" id="accordionFlushExample" style="width: 50vw">
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                <h3><span style="color: #fc3c44"> BEANWIKI </span> 는 어떻게 영화를 추천하나요?</h3>
              </button>
            </h2>
            <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div class="accordion-body">
                <p class="fs-4"><span style="color: #fc3c44"> BEANWIKI </span>는 코사인 유사도 알고리즘을 활용해 영화를 추천합니다.</p>
                <p class="fs-4"> 이때, 사용자가 눌러본 영화를 목록에 자동으로 저장해 이와 관련된 영화를 추천해드립니다! </p>
                <p class="fs-4"> 관심이 가는 다양한 영화를 눌러서 정보를 확인해보세요. </p>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                <h3><span style="color: #fc3c44"> BEANWIKI </span>에서 FindThatMovie는 어떤 기능인가요?</h3>
              </button>
            </h2>
            <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div class="accordion-body">
                <p class="fs-4"> <span style="color: #fc3c44"> BEANWIKI </span>의 FindThatMovie는 입력창에 영화에 대해 기억나는 정보를 입력하면, </p>
                <p class="fs-4"> 그 영화의 제목을 찾아주는 기능입니다! </p>
                <p class="fs-4"> Google Bard AI를 활용하여 사용자가 찾고있는 영화의 제목을 유추합니다! </p>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                <h3><span style="color: #fc3c44"> BEANWIKI </span>에서 검색은 어떻게 가능한가요</h3>
              </button>
            </h2>
            <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div class="accordion-body">
                <p class="fs-4"><span style="color: #fc3c44"> BEANWIKI </span>에서는 영화, 배우, 감독, 장르의 검색이 가능합니다!</p>
                <p class="fs-4">특히, 배우 및 감독을 검색하고 해당 배우 및 감독이 등장하는 영화도 검색이 가능합니다!</p>
              </div>
            </div>
          </div>
        </div>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      style="margin-top: 15vh"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      ref="Modal"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <!-- <div class="modal-header text-center"> -->
          <!-- <i class="fas fa-envelope prefix grey-text"></i> -->
          <h1 class="modal-title fs-5" id="exampleModalLabel"></h1>
          <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
          <!-- </div> -->
          <div class="modal-body">
            <!-- login start -->
            <div class="loginForm" :class="{'hidden': !isLoginOrSignup}" style="padding : 20px">
              <h3 class="" >Log In</h3>
              <form action="#" class="signin-form" @submit.prevent="login">
                <div class="form-group mb-3" style="text-align: left;">
                  <label class="label text-left" for="name" style="margin-left : 8px; margin-bottom : 3px">아이디</label>
                  <input type="text" class="form-control" placeholder="아이디" required id="username" v-model="username">
                </div>
                <div class="form-group mb-3" style="text-align: left">
                  <label class="label text-left" for="password" style="margin-left : 8px; margin-bottom : 3px">비밀번호</label>
                  <input type="password" class="form-control" placeholder="비밀번호" required id="password" v-model="password">
                </div>
                <div class="form-group">
                  <button
                    style="background-color: #fc3c44"
                    type="submit"
                    value="Log In"
                    data-bs-dismiss="modal"
                    class="form-control btn rounded submit px-3 text-white"
                  >
                    로그인
                  </button>
                </div>
                <p class="text-center">
                  멤버가 아니시라면
                  <a
                    href="#signup"
                    style="color: #fc3c44"
                    @click.prevent="LoginOrSignup(false)"
                    >회원가입</a
                  >
                </p>
              </form>
            </div>
            <div class="signupForm" :class="{'hidden': isLoginOrSignup}" style="padding : 20px">
              <h3>Sign UP</h3>
              <form class="signin-form" @submit.prevent="signUp" style="text-align: left;">
                <label for="susername" style="margin-left : 8px; margin-bottom : 3px">아이디</label>
                <input type="text" class="form-control" id="susername" required placeholder="아이디" v-model="susername"><br>

                <label for="spassword1" style="margin-left : 8px; margin-bottom : 3px"> 비밀번호</label>
                <input type="password" class="form-control" id="spassword1" required placeholder="비밀번호" v-model="spassword1"><br>

                <label for="spassword2" style="margin-left : 8px; margin-bottom : 3px"> 비밀번호 재입력</label>
                <input type="password" class="form-control" id="spassword2" required placeholder="비밀번호 재입력" v-model="spassword2">
                <br>
                <div class="form-group">
                  <button
                    style="background-color: #fc3c44"
                    type="submit"
                    value="Sign UP"
                    data-bs-dismiss="modal"
                    class="form-control btn rounded submit px-3 text-white"
                  >
                    Sign UP
                  </button>
                </div>
                <p class="text-center">
                  아이디가 있으시다면
                  <a
                    href="#"
                    style="color: #fc3c44"
                    @click.prevent="LoginOrSignup(true)"
                    >로그인</a
                  >
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const URL = "http://127.0.0.1:8000";
// const Token = ''

export default {
  data() {
    return {
      cardbottom: null,
      card: 30,
      scrollPostion: 0,
      // 로그인 관련 data start
      username: null,
      password: null,
      // 로그인 관련 data end

      // 회원가입 관련 data start
      susername: null,
      spassword1: null,
      spassword2: null,
      //회원가입 관련 data end
      imrobot : false,
    };
  },
  methods: {
    LoginOrSignup(check) {
      this.$store.dispatch("isLoginOrSignup", check);
    },
    move() {
      console.log(1);
      if (this.card > 120) {
        this.card = 0;
      } else {
        this.card += 30;
      }
      document.querySelector(
        ".aboutDataContainer"
      ).style.transform = `translateX(-${this.card}vw)`;
    },
    handleScroll() {
      this.scrollPostion = window.pageYOffset;

      if (2500 <= this.scrollPostion && this.scrollPostion < 6000) {
        document.querySelector(
          ".aboutDataContainer"
        ).style.transform = `translateX(-${
          (this.scrollPostion - 2500) / 10
        }vw)`;
      } else {
        console.log(1);
      }
    },
    login() {
      // 로그인 함수
      const username = this.username;
      const password = this.password;
      const payload = { username, password };

      this.$store.dispatch("login", payload);
      this.username = null;
      this.password = null;
      this.imrobot = true;
      setTimeout(() => {
        this.imrobot = false;
      }, 3000);

    },
    signUp() {
      // 회원가입 함수
      const susername = this.susername;
      const spassword1 = this.spassword1;
      const spassword2 = this.spassword2;

      const payload = {
        susername,
        spassword1,
        spassword2,
      };
      this.$store.dispatch("signUp", payload);
      this.susername = null;
      this.spassword1 = null;
      this.spassword2 = null;
      this.imrobot = true;
      setTimeout(() => {
        this.imrobot = false;
      }, 3000);

    },
  },
  mounted() {
    // var touch = [false,false,false,false,false]
    // document.querySelector('html').style.overflowY = 'hidden';
    document.querySelector('html').style.overflowY = 'hidden'
    const a = document.querySelector(".dataList");
    var divtop = a.getBoundingClientRect().bottom;
    this.cardbottom = divtop;

    setTimeout(() => {
      document.querySelector('html').style.overflowY = 'scroll'     
    }, 2100);
    // var waypoint1 = new Waypoint({
    //   element: document.getElementById('w1'),
    //   handler: function() {
    //     if (!touch[0]){
    //       touch[0] = true
    //       for(let i = 0; i < 6; i++){
    //       var textWrapper = document.querySelectorAll(".ani1")[i];
    //       textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    //       anime.timeline({loop: false})
    //         .add({
    //           targets: '.ani1 .letter',
    //           opacity: [0,1],
    //           easing: "easeInOutQuad",
    //           duration: 2250,
    //           // delay: (el, j) => 150 * (j+1)
    //           delay: (el, j) => 50 * (j+1)
    //         })
    //       }
    //   }
    // }})
    // var waypoint2 = new Waypoint({
    //   element: document.getElementById('w2'),
    //   handler: function() {
    //     if (!touch[1]){
    //       touch[1] = true
    //       for(let i = 0; i < 5; i++){
    //       var textWrapper = document.querySelectorAll(".ani2")[i];
    //       textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    //       anime.timeline({loop: false})
    //         .add({
    //           targets: '.ani2 .letter',
    //           opacity: [0,1],
    //           easing: "easeInOutQuad",
    //           duration: 2250,
    //           // delay: (el, j) => 150 * (j+1)
    //           delay: (el, j) => 50 * (j+1)
    //         })
    //       }
    //   }
    // }})
    // var waypoint3 = new Waypoint({
    //   element: document.getElementById('w3'),
    //   handler: function() {
    //     if (!touch[2]){
    //       touch[2] = true
    //       for(let i = 0; i < 2; i++){
    //       var textWrapper = document.querySelectorAll(".ani3")[i];
    //       textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    //       anime.timeline({loop: false})
    //         .add({
    //           targets: '.ani3 .letter',
    //           opacity: [0,1],
    //           easing: "easeInOutQuad",
    //           duration: 2250,
    //           // delay: (el, j) => 150 * (j+1)
    //           delay: (el, j) => 50 * (j+1)
    //         })
    //       }
    //   }
    // }})                        
    // // animation1
    // for(let i = 0; i < 6; i++){
    //   var textWrapper = document.querySelectorAll(".textAni1")[i];
    //   textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    //   anime.timeline({loop: false})
    //     .add({
    //       targets: '.textAni1 .letter',
    //       opacity: [0,1],
    //       easing: "easeInOutQuad",
    //       duration: 2250,
    //       // delay: (el, j) => 150 * (j+1)
    //       delay: (el, j) => 50 * (j+1)
    //     })
    // }


  },
  computed: {
    isLoginOrSignup() {
      return this.$store.state.isLoginOrSignup;
    },
    isLoggedIn() {
      if(this.$store.state.userid) {
        return true
      }
      else{
        return false
      }
    }
  },
};
</script>

<style>
.aboutStartBtn {
  width: 400px;
  height: 50px;
  margin-top: 20px;
}

.aboutTitle {
  font-family: "IBM Plex Sans KR", sans-serif;
}

.aboutContainer {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  /* overflow: hidden; */
}

.aboutData {
  margin-top: 100px;
  margin-bottom: 100px;
  position: sticky;
  top: 100px;
}

.title {
  margin: 30px 0px;
}
.logo {
  margin: 30px 0px;
  background-image: url("../assets/logo-color.png");
  width: 150px;
  height: 150px;
  background-repeat: no-repeat;
  background-size: cover;
}

.funcReviewImg {
  margin: 30px 0px;
  background-image: url("../assets/review_img.png");
  width: 500px;
  height: 500px;
  background-repeat: no-repeat;
  background-size: cover;
}

.aboutFunction {
  background-color: black;
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: 100px;
}

.funcReview {
  width: 500px;
  height: 500px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.recommendImg {
  margin: 30px 0px;
  background-image: url("../assets/movie_rec.png");
  width: 500px;
  height: 500px;
  background-repeat: no-repeat;
  background-size: cover;
}
.showimg {
  -webkit-animation-name: prop-600;
  animation-duration: 2s;
  animation-fill-mode: both;
  animation-timing-function: linear;
}
.dataList {
  white-space: nowrap;
}
.dataList > .card {
  margin: 10px;
  height: 500px;
  width: 30vw;
}

.aboutDataContainer {
  width: 300vw;
  transition: all 1s;
}

.personBeanImg{
  margin: 30px 0px;
  background-image: url('../assets/profile/bean.png');
  background-repeat: no-repeat;
  background-size: cover;
}

.personJuneImg{
  margin: 30px 0px;
  background-image: url('../assets/profile/june.png');
  background-repeat: no-repeat;
  background-size: cover;
}

.aboutPeople {
  background-color: lightgray;
  width: 100%;
  padding: 60px;
}

.leftViewImg {
  margin: 30px 0px;
  background-image: url("../assets/numerous_view.png");
  width: 400px;
  height: 400px;
  background-repeat: no-repeat;
  background-size: cover;
}

.rightViewImg {
  margin: 30px 0px;
  background-image: url("../assets/carousel_view.png");
  width: 400px;
  height: 400px;
  background-repeat: no-repeat;
  background-size: cover;
}

.bardImg {
  margin: 30px 0px;
  background-image: url("../assets/bard_search.png");
  width: 900px;
  height: 350px;
  background-repeat: no-repeat;
  background-size: cover;
}

@keyframes prop-600 {
  0% {
    width: 500px;
    height: 500px;
  }
  1% {
    width: 500px;
    height: 500px;
  }
  100% {
    width: 150px;
    height: 150px;
  }
}
.imrobot {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 5;
}
</style>
