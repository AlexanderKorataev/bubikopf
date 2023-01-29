<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Приветствуем в нашей супер онлайн школе😃👍</p>
        <p class="subtitle">Лучшие онлайн курсы по волосам</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ $t("lessons") }}</h2>
      </div>

      <template v-if="$i18n.locale === 'ru'">
        <RuProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product"
        />
      </template>

      <template v-if="$i18n.locale === 'en'">
        <EnProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product"
        />
      </template>

    </div>
  </div>

</template>

<script>
import axios from "axios";

// import { KinescopePlayer } from "@kinescope/vue-kinescope-player";

import { i18n } from "../i18n";

import EnProductBox from "@/components/EnProductBox";
import RuProductBox from "@/components/RuProductBox";

export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    RuProductBox,
    EnProductBox,
  },
  mounted() {
    this.getLatestProducts();
    document.title = "Home | БубиКопф";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>