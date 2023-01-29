import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { i18n } from './i18n'

import axios from 'axios'

import KinescopePlayer from '@kinescope/vue-kinescope-player'


axios.defaults.baseURL = 'http://127.0.0.1:8000/'

Vue.config.productionTip = false


new Vue({
    router,
    axios,
    store,
    i18n,
    KinescopePlayer,
    render: h => h(App)
}).$mount('#app')