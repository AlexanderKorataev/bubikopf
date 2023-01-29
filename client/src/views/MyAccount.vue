<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{$t('PersonalAccount')}}</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">{{$t('LogOut')}}</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">Ваши курсы</h2>

            </div>

            <UserProductBox
            v-for="product in orders"
            v-bind:key="product.id"
            v-bind:product="product"
            />
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import UserProductBox from '@/components/UserProductBox.vue'
import RuProductBox from "@/components/RuProductBox";

export default {
    name: 'MyAccount',
    components: {
        UserProductBox,
        RuProductBox
    },
    data() {
        return {
            orders: [],
            latestProducts: []
        };
    },
    mounted() {
        document.title = 'My account | БубиКопф'
        this.getMyOrders()
        this.getLatestProducts()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },

        async getMyOrders() {
            this.$store.commit("setIsLoading", true);
            await axios
            .get("/api/v1/orders/")
            .then((response) => {
              this.orders = response.data;
            })
            .catch((error) => {
              console.log(error);
            });
              this.$store.commit("setIsLoading", false);
    },
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
}
</script>