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
                            <th>{{ $t('lessons') }}</th>
                            <th>{{ $t('price') }}</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>{{ order.name }}</td>
                            <td>{{ order.paid_amount }} рублей</td>
                        </tr>
                    </tbody>

                </table>

                <button class="button is-dark" @click="submitForm">{{ $t('pay') }}</button>
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

                errors: [],
                order: [],
                lesson: {}
            }
        },
    mounted() {
        this.getOrder()
        document.title = "Оформление покупки | БубиКопф";
    },
    methods: {

        async getOrder() {
            this.$store.commit('setIsLoading', true)

            const product_slug = this.$route.params.product_slug

            await axios

                .get(`/api/v1/orders/${product_slug}`)
                .then(response => {
                    this.order = response.data

                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
                this.$store.commit('setIsLoading', false)
        },
        submitForm() {
            this.errors = []

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                window.location.href = this.order.get_payment_url
            }
        },
    }
}
</script>