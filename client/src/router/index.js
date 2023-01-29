import Vue from 'vue'
import VueRouter from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'

import UserProduct from '../views/UserProduct.vue'
import Checkout from '../views/Checkout.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/search',
        name: 'Search',
        component: Search
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn
    },
    {
        path: '/my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/my-account/checkout/:product_slug',
        name: 'Checkout',
        component: Checkout
    },
    {
        path: '/products/:product_slug',
        name: 'Product',
        component: Product
    },
    {
        path: '/my-account/:product_slug',
        name: 'UserProduct',
        component: UserProduct
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next({ name: 'LogIn', query: { to: to.path } });
    } else {
        next()
    }
})

export default router