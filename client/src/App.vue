<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>БубиКопф</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template>
                <button class="button is-light" @click="switchLang">{{$t('language')}}</button>
              </template>

              <template>
                <router-link to="/about" class="button is-light">{{$t('aboutBtn')}}</router-link>
              </template>

              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">{{$t('PersonalAccount')}}</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">{{$t('LogIn')}}</router-link>
              </template>

            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer" role="contentinfo">
      <div class="content has-text-centered">
        <p>pochta@gmail.com</p>
        <p>Договор оферты</p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

import { i18n } from './i18n'


export default {

  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },

  // mounted() {
  //   this.cart = this.$store.state.cart
  // },
  // computed: {
  //     cartTotalLength() {
  //         let totalLength = 0
  //         for (let i = 0; i < this.cart.items.length; i++) {
  //             totalLength += this.cart.items[i].quantity
  //         }
  //         return totalLength
  //     }
  // },
  methods: {
    switchLang() {
      i18n.locale === "ru" ? i18n.locale = "en" : i18n.locale = "ru"
      localStorage.setItem('lang', i18n.locale)
    }
  } 
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

body {
  font-family: MontserratRegular;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

@font-face {
  font-family: MontserratRegular;
  font-style: normal;
  src: url(./assets/fonts/MontserratRegular.woff); 
}

// vars
$dark: #242424;
$lite: #fff;

#wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
}

footer {
  margin-top: auto;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid $dark;
  border-color: $dark transparent $dark transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>