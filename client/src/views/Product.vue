<template>
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

                    <hr style="background-color:#242424">

                    <p class="is-size-4"><strong></strong>{{ product.ru_price }} рублей</p>
                    <div class="field has-addons mt-6">

                        <button class="button is-dark" @click="createOrder">Перейти к покупке</button>
                    </div>
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

                    <hr style="background-color:#242424">

                    <p class="is-size-4"><strong></strong>${{ product.en_price }}</p>
                    <div class="field has-addons mt-6">
                        <button class="button is-dark" @click="createOrder">Go to purchase</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
        }
    },

    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug
            await axios
                .get(`/api/v1/products/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' | БубиКопф'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        async createOrder() {

            var randomID = Math.random().toString(36).slice(-10);

            const data = {
                'name': this.product.ru_name,
                'product_id': this.product.id,
                'paid_amount': this.product.ru_price,
                'randomID': randomID
            }
            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$router.push('/my-account/checkout/' + randomID)
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
                this.$store.commit('setIsLoading', false)
        },
    }
}
</script>