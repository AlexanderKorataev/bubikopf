import Vue from 'vue'
import VueI18n from 'vue-i18n'

import ru from './ru.json'
import en from './en.json'


const messages = {
    ru,
    en
}
const LocaleStorageLang = localStorage.getItem('lang')


Vue.use(VueI18n)

export const i18n = new VueI18n({
    locale: LocaleStorageLang,
    messages
})