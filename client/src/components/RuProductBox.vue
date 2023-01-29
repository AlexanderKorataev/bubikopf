<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ product.ru_name }}</h3>

            <hr>

            <div class="columns is-multiline">
                <span class="icon">
                    <i class="fas fa-duotone fa-clock"></i>
                </span>
                <p> {{ product.video_duration }} минут</p>
            </div>

            <hr>

            <p class="is-size-6 has-text-grey">{{ product.ru_price }} рублей</p>

            <router-link v-bind:to="'products' + product.get_absolute_url" class="button is-dark mt-4">Подробнее</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RuProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>