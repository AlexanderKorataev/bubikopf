<template>
    <div v-if="acquisitionStatus===true">

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

        <hr>
        
        <div v-if="$i18n.locale === 'ru'">
        <div class="page-product">
            <div class="columns is-multiline">
                <div class="column is-7">
                    <div class="column is-9">
                    <figure class="image mb-6">
                        <img v-bind:src="product.get_image">
                    </figure>
                    </div>
                </div>

                <div class="column is-4">
                    <h1 class="title">{{ product.ru_name }}</h1>
                    <p>{{ product.ru_description }}</p>
                </div>
            </div>
        </div>
    </div>

    <div v-else>
        <div class="page-product">
            <div class="columns is-multiline">
                <div class="column is-7">
                    <div class="column is-9">
                    <figure class="image mb-6">
                        <img v-bind:src="product.get_image">
                    </figure>
                    </div>

                </div>

                <div class="column is-4">
              
                    <h1 class="title">{{ product.en_name }}</h1>
                    <p>{{ product.en_description }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-else>

        <!-- <p>{{ lesson }}</p>

        <p>{{ lesson.find(x => x.get_payment_status === "succeeded").randomID }}</p> -->
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
                lesson: [],

                orders: [],

                acquisitionStatus: false,

                showMobileMenu: false
            }
        },
    mounted() {
        this.getProduct()
        this.getMyOrders() 
    },
    beforeMount(){
        this.getProduct()
        this.getMyOrders() 
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
        async getMyOrders() {
            this.$store.commit("setIsLoading", true);

            await axios
            .get("/api/v1/user_orders/")
            .then((response) => {
              this.orders = response.data;
            
              this.lesson = this.orders.filter(x => x.product_id === this.product.id.toString());

              this.payment_status = this.lesson.find(x => x.get_payment_status === "succeeded").get_payment_status;

              if (this.payment_status === "succeeded") {
                this.acquisitionStatus = true;
              }
            })
            .catch((error) => {
              console.log(error);
            });
              this.$store.commit("setIsLoading", false);
        },
    }
}
</script>