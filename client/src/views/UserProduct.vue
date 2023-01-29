<template>

    
    <div class="column is-12">
        <div v-if="$i18n.locale === 'ru'">
        <h2 class="is-size-2 has-text-centered">{{ product.ru_name }}</h2>

        <section class="hero is-dark mb-3">
            <div class="hero-body has-text-centered">
                <p class="title mb-6">{{ product.ru_description }}</p>
            </div>
        </section>
        </div>

        <div v-else>
        <h2 class="is-size-2 has-text-centered">{{ product.en_name }}</h2>

        <section class="hero is-dark mb-3">
            <div class="hero-body has-text-centered">
                <p class="title mb-6 is-3">{{ product.en_description }}</p>
            </div>
        </section>
        </div>

        <hr>
        
        <!-- desktop player -->
        <div class="column is-hidden-mobile">
            <kinescope-player
                class="has-text-centered"
                ref="kinescope"
                :video-id="product.video_file_id"
                @ready="handleReady"
                width="80%"
                height="430px"
            ></kinescope-player>
      </div>

      <!-- mobile player -->
      <div class="1 is-hidden-desktop">
            <kinescope-player
                class="has-text-centered"
                ref="kinescope"
                :video-id="product.video_file_id"
                @ready="handleReady"
                width="90%"
            ></kinescope-player>
      </div>

    </div>
</template>

<script>
import axios from 'axios'

import { KinescopePlayer } from "@kinescope/vue-kinescope-player"

export default {
    name: "UserProduct",
    data() {
        return {
                product: {},
                quantity: 1,

                showMobileMenu: false
            }
        },
    mounted() {
        this.getProduct() 
    },
    components: {
        KinescopePlayer,
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug
            await axios
                .get(`/api/v1/products/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.ru_name + ' | БубиКопф'
                })
                .catch(error => {
                    console.log(error)
                })
                
            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>

<!-- <style scoped>

@media screen and (max-width: 600px) {
 {
visibility: hidden;
display: none;
}
}

</style> -->