<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-7">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-7 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>{{ product.ru_name }}</td>
                            <td>{{ product.ru_price }} рублей</td>
                        </tr>
                    </tbody>

                </table>
            </div>

            <div class="column is-7 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>
                    </div>
                </div>

                <div id="card-element" class="mb-5"></div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <template>
                    <hr>
                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Checkout",
    data() {
        return {
                product: {},
                quantity: 1,

                stripe: {},
                card: {},
                first_name: '',
                last_name: '',
                email: '',
                product_id: '',
                errors: []
            }
        },
    mounted() {
        this.getProduct()

        // this.id = this.product.get_absolute_url
        
        this.stripe = Stripe('pk_test_51MUE81BHtvU8rNSs1hBPJMz0WZTVYNrQ2ToADpc3dqIjcm3UYz0ZJUT2vEcogmHHmYsHLoEbJ9cuPxhLqrcujgQR00sRqpCeat')
        const elements = this.stripe.elements();
        this.card = elements.create('card', { hidePostalCode: true })
        this.card.mount('#card-element')
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
        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('The first name field is missing!')
            }
            if (this.last_name === '') {
                this.errors.push('The last name field is missing!')
            }
            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {

            const data = {
                'product_id': this.product.id,
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'items': [],
                'stripe_token': token.id
            }
            await axios
                .post('/api/v1/checkout/', data)
                // .then(response => {
                //     this.$store.commit('clearCart')
                    // this.$router.push('/cart/success')
                // })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
                this.$store.commit('setIsLoading', false)
        }
    }
}
</script>