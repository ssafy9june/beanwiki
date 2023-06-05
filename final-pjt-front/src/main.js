import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'

import Swiper from 'swiper/bundle'; // swiper
import 'swiper/css/bundle'; // swiper

Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')


  // init Swiper:
  const swiper = new Swiper({
    // modules: [Navigation, Pagination],
  });
