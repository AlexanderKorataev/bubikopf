<!-- has-text-centered -->
<template>
    <div v-if="$i18n.locale === 'ru'">
        <div class="page-product">
            <div class="columns is-multiline">
                <div class="column is-7">
                    <div class="column is-8">
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

                        <div class="control">
                            <a class="button is-dark">Перейти к покупке</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-else>
        <div class="page-product">
            <div class="columns is-multiline">
                <div class="column is-7">
                    <div class="column is-8">
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

                        <div class="control">
                            <a class="button is-dark">Go to purchase</a>
                        </div>
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
            quantity: 1
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
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)
            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>