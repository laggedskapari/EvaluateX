// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    content: [
        "./components/**/*.{js,vue,ts}",
        "./layouts/**/*.vue",
        "./pages/**/*.vue",
        "./plugins/**/*.{js,ts}",
        "./nuxt.config.{js,ts}",
        "./app.vue",
    ],
    css: ['~/assets/css/main.css'],
    app: {
        head: {
            link: [
                { rel: 'stylesheet', href: "https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300;400;700&display=swap" },
                { rel: 'stylesheet', href: "https://fonts.googleapis.com/css2?family=Staatliches&display=swap"}

            ],

            script: [
                { src: "https://kit.fontawesome.com/b97d7b3db5.js", crossorigin: "anonymous" }
            ]
        }
    },

})
