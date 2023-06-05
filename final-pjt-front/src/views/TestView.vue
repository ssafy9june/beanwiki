<template>
  <div>
    <div class="container" style="margin-top: 30px">
        <div style="min-height: 300px; border : 3px solid black">
          <h1>선택한 영화 목록</h1>
          <div class="row">
          <div class="col-3 select appear" v-for="(movie,idx) in selectmovies" :key="idx">
            <img :src="`https://image.tmdb.org/t/p/original/${movie.movie.poster_path}`" alt="" class="posterimg" @click="unselectmovie(movie)">
          </div>
        </div>
        </div>

        <div style="margin-top : 30px; min-height: 1500px">
          <h1>선택 하세요</h1>
          <div class="row" style="margin-top: 30px">
          <div class="col-3 nonselect" v-for="(movie,idx) in movies" :key="idx" @click="selectmovie(idx,movie)">
            <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="" class="posterimg">
          </div>
        </div>
        </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectmovies : []
    }
  },
  mounted() {
    this.$store.dispatch('get_movies')
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    selectmovie(idx,movie){
      if (this.selectmovies.length==5) {
        alert('이미 5개를 고르셨습니다')
        return
      }
      document.querySelectorAll('.nonselect')[idx].classList.add('disappear')
      setTimeout(() => {
        document.querySelectorAll('.nonselect')[idx].classList.add('hidden')
        this.selectmovies.push({movie,idx})
        // const idx = this.selectmovies.indexOf(movie)
        // document.querySelectorAll('.select')[idx].add('appear')
        // document.querySelectorAll('.nonselect')[idx].classList.remove('hidden')
      }, 1000);
    },
    unselectmovie(movie){
      const idx = this.selectmovies.indexOf(movie)
      document.querySelectorAll('.select')[idx].classList.add('disappear')
      document.querySelectorAll('.nonselect')[movie.idx].classList.add('appear')
      document.querySelectorAll('.nonselect')[movie.idx].classList.remove('hidden','disappear')
      setTimeout(() => {
        this.selectmovies.splice(idx,1)
        if (this.selectmovies.length>idx){
          setTimeout(() => {
          document.querySelectorAll('.select')[idx].classList.remove('disappear')
          
        }, 20);
        }

      }, 1000);
      

    }
  }
}
</script>

<style>
.posterimg {
  width:100%;
  height:100%;
  object-fit:cover;
}
.appear {
  animation: fade-in 2s;
  animation-fill-mode: toward;
}
.disappear {
  animation: fade-out 1s;
  animation-fill-mode: toward;
}
@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes fade-out {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
.hidden {
  display: none;
}
</style>