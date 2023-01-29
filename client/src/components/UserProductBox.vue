<template>
    <div v-if="$i18n.locale === 'ru'" class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="lesson.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ lesson.ru_name }}</h3>
            <hr>
            <div class="columns is-multiline">
                <span class="icon">
                    <i class="fas fa-duotone fa-clock"></i>
                </span>
                <p>{{ lesson.video_duration }} минут</p>
            </div>

            <router-link v-bind:to="'products/' + lesson.get_absolute_url" class="button is-dark mt-4">Перейти к просмотру</router-link>
        </div>
    </div>

    <div v-else class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="lesson.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ lesson.en_name }}</h3>
            <hr>
            <div class="columns is-multiline">
                <span class="icon">
                    <i class="fas fa-duotone fa-clock"></i>
                </span>
                <p>{{ lesson.video_duration }} minutes</p>
            </div>

            <router-link v-bind:to="'my-account' + lesson.get_absolute_url" class="button is-dark mt-4">Go to the lesson</router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UserProductBox',
    data() {
        return {
            latestProducts: [],
            lesson: [],
        };
    },
    props: {
        product: Object
    },
    mounted() {
        this.getLatestProducts();
    },
    methods: {
        async getLatestProducts() {

        this.$store.commit("setIsLoading", true);
        await axios
            .get("/api/v1/latest-products/")
            .then((response) => {

            this.latestProducts = response.data;

            this.lesson = this.latestProducts.find(x => x.id === Number(this.product.product_id))
            })
            .catch((error) => {
            console.log(error);
            });
        this.$store.commit("setIsLoading", false);
        },
    },
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>