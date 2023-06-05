<template>
  <div class="container">
    <!-- <h1>Community</h1> -->
    <br>
    <div v-if="articles" class="">
      <div class="row justify-content-center">
        <div class="col-10">
          <div id ="articleBox" class="rounded px-3 row justify-content-center" v-for="(article,id) in articles" :key="id" style="border : 1px solid black; margin-bottom : 30px;">
            <div class="content" style="width: 80%;">
              <!-- <div class="d-flex align-items-center justify-content-between mt-3"> -->
                <h2 class="text-start text-align-center align-middle mt-3"><strong>{{ article.title }}</strong></h2>
                <h5 class="text-end">by <span class="toprofile" @click="to_profile(article.writer.id)">{{ article.writer.username }}</span>님 </h5>
              <!-- </div> -->
              <hr>
              <p class="text-start">" {{ article.content }} "</p>
              <br>
              <div class="d-flex justify-content-end">
                <i class="fa-solid fa-thumbs-up" @click='like_article(article.id,id)'> {{ article.likeuser.length }}</i>
                <i class="fa-solid fa-trash" style="margin-left: 10px" @click="article_delete(article.id,id)"></i>
              </div>
              <br>
                <hr v-if="article.comment">
                <div v-for="(comment,idx) in article.comment" :key="idx">
                    <p class="text-start"><strong>{{ comment.writer.username }}</strong> : " {{ comment.content }} " <i class="fa-solid fa-trash" style="margin-left: 10px" @click="comment_delete(comment.id, id,idx)"></i></p>
              </div>
              <hr>  
              <div class="d-flex justify-content-start">
                <label style="margin-right: 10px;" for="commentBox"><i class="fa-solid fa-comment"></i></label>
                <input class="mb-3" style="width:90%; height: 30px; border : 1px solid black;" id="commentBox" type="text" v-model="articles_model[id]" @keyup.13="create_comment(article.id,id)">
                <button style="margin-left: 10px; border: 0.5px solid black; height: 30px; width: 50px;" @click="create_comment(article.id,id)">작성</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else></div>
    <div class="row justify-content-center">
      <div class="col-10">
        <div id="articleBox" class="rounded" style="border : 1px solid black;">
          <div class="px-3">
            <h3 class="my-3">글 작성</h3>
            <input type="text" v-model="article_title" placeholder="글제목" style="border : 2px solid black; width: 80%;">
            <br>
            <br>
            <input type="text" v-model="article_content" placeholder="글내용" style="border : 2px solid black; width: 80%; height: 100px">
            <br>
            <br>
            <button class="mb-3" style="border: 1px solid black" @click="create_article">글 작성</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000'
export default {
  data() {
    return {
      articles : [],
      articles_model : [],
      article_title : null,
      article_content : null,
    }
  },
  created() {
    if (!this.$store.state.token){
      this.$router.push({ name : 'about'})
    }
  },
  methods: {
    article_delete(id,idx){
      axios({
        method : 'delete',
        url: `${URL}/articles/article/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data : {
          'id' : id
        }
      })
      .then((res) => {
        this.articles.splice(idx,1)
      }).catch((err) => {
        alert('글 작성자가 아닙니다')
      });
    }
    ,comment_delete(comment_id, id,idx){
      axios({
        method : 'delete',
        url: `${URL}/articles/comment/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data : {
          'id' : comment_id
        }
      })
      .then((res) => {
        console.log(res.data);
        this.articles[id].comment.splice(idx,1)
      }).catch((err) => {
        alert('댓글 작성자가 아닙니다')
      });
    },
    create_comment(comment_id,id){
      axios({
        method : 'post',
        url: `${URL}/articles/comment/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data : {
          content : this.articles_model[id],
          'id' : comment_id
        }
      })
      .then((res) => {
        this.articles[id].comment.push(res.data)
        this.articles_model[id] = null
      }).catch((err) => {
        console.log(err);
      });
    },
    create_article(){
      axios({
        method : 'post',
        url: `${URL}/articles/article/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data : {
          title : this.article_title,
          content : this.article_content
        }
      })
      .then((res) => {
        this.articles.push(res.data)
        this.articles_model.push(null)
        this.article_title = null
        this.article_content = null
      }).catch((err) => {
        console.log(err);
      });
      },
    like_article(id,idx) {
      axios({
        method : 'post',
        url: `${URL}/articles/like_article/${this.$store.state.userid}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data : {
          'id' : id
        }
      })
      .then((res) => {
        this.articles[idx] = res.data
        const temp = [...this.articles]
        this.articles = [...temp]
      }).catch((err) => {
        console.log(err);
      });
    },
    to_profile(userid){
      this.$router.push({ name : 'profile', params : {'userid' : userid}})
    }
  },
  mounted() {
    axios({
      method : 'get',
      url: `${URL}/articles/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.articles = res.data
      for (let i=0; i<this.articles.length; i++)
        {this.articles_model.push(null)}
    }).catch((err) => {
      console.log(err);
    });
  },
}
</script>

<style>

#articleBox {
  background-color: lightgray;
  width: 100%;
}

.toprofile:hover {
  cursor: pointer;
  color: #fc3c44;
}

</style>