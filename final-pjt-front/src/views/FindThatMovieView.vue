<template>
  <div class="container">
    <h1 class="my-3">FindThatMovie</h1>
    <p class="mb-5">그 영화 뭐더라...?</p>
    <div class="input-group mb-5">
      <button
        class="btn btn-outline-secondary btn-warning"
        type="button"
        id="button-addon1"
        @click="resetButton"
      >
        <p>검색내용</p>
        <p>초기화</p>
      </button>
      <textarea
        class="form-control"
        type="text"
        name="search"
        v-model="search_text"
        @keyup.13="search_bard"
        aria-label="With textarea"
        style="width: 80%"
        placeholder="예시 : 레오나르도 디카프리오 주연의 액션 영화로 꿈과 꿈에 들어가는 내용의 영화"
      ></textarea>
      <button
        class="btn btn-outline-secondary btn-danger text-white"
        type="button"
        id="button-addon1"
        @click="search_bard"
      >
        검색
      </button>
    </div>
    <div>
      <h1 class="mb-4">Bard says..</h1>
      <div
        class="mx-auto"
        style="border-radius: 5px; border: 1px solid black; min-height: 200px"
      >
        <h3 class="m-5 text-center" v-if="answer">
          {{ answer.response.content }}
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      search_text: null,
      answer: null,
    };
  },
  created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
  methods: {
    resetButton() {
      return (this.search_text = null);
    },
    search_bard() {
      axios({
        method: "post",
        url: `${URL}/movies/find_movie_by_bard/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          input: `나는 내가 입력한 내용과 가장 관련성이 높은 영화를 검색하고자 합니다.
                  반드시 지켜야 하는 조건은 아래와 같습니다.

                  1. 가장 관련성이 높은 영화 제목을 1개부터 최대 3개까지 출력
                  2. 영화 제목만 출력
                  3. 영화 제목 외에 다른 어떠한 정보도 출력 금지
                  4. '네, 알겠습니다' 와 같은 대답 출력 금지
                  5. 영화 제목 앞에 숫자나, 뒤에 출시년도와 같은 정보 출력 금지
                  6. 대답 언어는 반드시 한글로 출력
                  7. 영화 줄거리 및 내용 출력 금지


                  검색 내용: ${this.search_text}`,
        },
      })
        .then((res) => {
          this.answer = res.data;
          this.search_text = null;
          console.log(answer);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>