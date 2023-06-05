<template>
  <div>
    <img style="width: 30vw" class="my-3" :src="require(`@/assets/${robot}`)" alt="">
    <h2 class="mb-4">에러가 발생했습니다 휴먼.</h2>
    <router-link to="/main"> <h3 style="color: #fc3c44">메인으로 이동</h3>  </router-link>
  </div>
</template>

<script>
import _ from 'lodash';

export default {
  data() {
    return {
      robots : ['robot1.jpg','robot2.jpg','robot3.jpg','robot4.jpg','robot5.jpg','robot6.jpg','robot7.jpg','robot8.jpg','robot9.jpg','robot10.jpg','robot11.png','robot11.png'],
      robot : 'robot1.jpg',
    }
  },
  created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
  mounted() {
    this.robot = _.sample(this.robots,1)
  }

}
</script>

<style>

</style>