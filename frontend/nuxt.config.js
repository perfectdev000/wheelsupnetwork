const strapiBaseUri = process.env.API_URL || "https://admin.globalagents.net/";

export default {
  target: "static",
  
  ssr: false,

  server: {
    host: "0.0.0.0", // default: localhost,
    port: 3000,
  },

  generate: {
    fallback: true,
  },

  env: {
    strapiBaseUri,
  },

  
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.PAGE_TITLE || "Wheels Up Network  ",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: process.env.npm_package_description || "",
      },
      {
        name: "msapplication-square70x70logo",
        content: "/smalltile.png",
      },
      {
        name: "msapplication-square150x150logo",
        content: "/mediumtile.png",
      },
      {
        name: "msapplication-wide310x150logo",
        content: "/widetile.png",
      },
      {
        name: "msapplication-square310x310logo",
        content: "/largetile.png",
      },
    ],
    link: [
      // { rel: "shortcut icon", type: "image/x-icon", href: process.env.LANGUAGE === 'es' ?  `favicon-wheels-up-network.png`: 'faviddcon.ico'  },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "57x57",s
      //   href: "/apple-touch-icon-57x57.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "60x60",
      //   href: "/apple-touch-icon-60x60.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "72x72",
      //   href: "/apple-touch-icon-72x72.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "76x76",
      //   href: "/apple-touch-icon-76x76.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "114x114",
      //   href: "/apple-touch-icon-114x114.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "120x120",
      //   href: "/apple-touch-icon-120x120.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "144x144",
      //   href: "/apple-touch-icon-144x144.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "152x152",
      //   href: "/apple-touch-icon-152x152.png",
      // },
      // {
      //   rel: "apple-touch-icon",
      //   sizes: "180x180",
      //   href: "/apple-touch-icon-180x180.png",
      // },
      // {
      //   rel: "icon",
      //   type: "image/png",
      //   sizes: "16x16",
      //   href: "/favicon-16x16.png",
      // },
      // {
      //   rel: "icon",
      //   type: "image/png",
      //   sizes: "32x32",
      //   href: "/favicon-32x32.png",
      // },
      // {
      //   rel: "icon",
      //   type: "image/png",
      //   sizes: "96x96",
      //   href: "/favicon-96x96.png",
      // },
      // {
      //   rel: "icon",
      //   type: "image/png",
      //   sizes: "192x192",
      //   href: "/android-chrome-192x192.png",
      // },
    ],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: "#fff" },

  pageTransition: "fade",
  /*
   ** Global CSS
   */
  css: ["assets/scss/style.scss", "assets/css/main.css"],

  router: {
    linkExactActiveClass: "active-link",
    // middleware:['pages-only-usa-ca', 'site', 'maintenance',  ],
    middleware:['pages-only-usa-ca', 'maintenance' ],
  },
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    "~/plugins/filters.js",
    "~/plugins/vue-awesome-swiper.js",
    "~/plugins/vuejs-paginate.js",
    "~/plugins/vue2-google-maps.js",
    "~/plugins/vue-infinity-loading.js",
    "~/plugins/vue-masonry-css.js",
    "~/plugins/Mixitup.client.js",
    "~/plugins/silentbox.js",
    "~/plugins/vue-select.js",
    "~/plugins/vuejs-sweetalert2.js",
    // "~/plugins/vue-analitycs.js",
    { src: "~/plugins/vee-validate.js", ssr: false },
    { src: "~/plugins/vue-masonry", ssr: false },
    // { src: "~/plugins/ga.js", ssr: false }
    { src: "~/plugins/gtag.js", ssr: false }
  ],

  serverMiddleware: [
    "~/server-middleware/log.js",
    "~/server-middleware/sitemap",
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    "bootstrap-vue/nuxt",
    "@nuxtjs/style-resources",
    "@nuxtjs/markdownit",
    "@nuxtjs/strapi",
    "@nuxtjs/toast",
    // [
    //   "@nuxtjs/google-analytics",
    //   {
    //     id: process.env.GA || 'UA-54729729-1',
    //     autoTracking: { screenview: false, page: false },
    //     debug: { enabled: false, sendHitTask: true },
    //     checkDuplicatedScript: true
    //   },
    // ],
    // ["@nuxtjs/google-tag-manager", 
    //   { pageTracking: true, id: process.env.GOOGLE_TAG_MANAGER_ID },
    // ],    
    [
      "nuxt-i18n",
      {
        lazy: true,
        langDir: "lang/",
        defaultLocale: process.env.LANGUAGE || "es" ,
        seo: false,
        detectBrowserLanguage: false,
        parsePages: false,
        pages: {
          'empleos/index': {
            es: '/empleos',
            en: '/jobs',
          },
          'empleos/_slug': {
            es: '/empleos/:slug',
            en: '/jobs/:slug',
          },
          'suscribete-a-nuestra-newsletter/index':{
            es:'/suscribete-a-nuestra-newsletter',
            en: '/subscribe-to-our-newsletter'
          },
          'proximos-eventos/index':{
            es:'/proximos-eventos',
            en:'/upcoming-events'
          },
          'proximos-eventos/_slug': {
            es: '/proximos-eventos/:slug',
            en: '/upcoming-events/:slug',
          },
          'destinos/index': {
            es: '/destinos',
            en: '/destinations',
          },
          'destinos/_slug':{
            es: '/destinos/:slug',
            en: '/destinations/:slug',
          },
          'premios-y-ganadores/index': {
            es: '/premios-y-ganadores',
            en: '/contests-and-winners',
          },
          'premios-y-ganadores/_slug': {
            es: '/premios-y-ganadores/:slug',
            en: '/contests-and-winners/:slug',
          },
          'politica-de-privacidad/index': {
            es: '/politica-de-privacidad',
            en: '/privacy',
          },
          'politica-de-cookies/index': {
            es: '/politica-de-cookies',
            en: '/cookies',
          },
          'nota-legal/index': {
            es: '/nota-legal',
            en: '/legal',
          },
          'entradas/index':{
            es: '/entradas',
            en: '/tickets',
          },
          'portal-para-agentes/index':{
            es: '/portal-para-agentes',
            en: '/agent-portals',
          },
        },
        locales: [
          {
            code: "en",
            name: "English",
            file: "en.js",
          },
          {
            code: "es",
            name: "Spain",
            file: "es.js",
          },
        ],
      },
    ],
  ],
  extensions: [".webpack.js", ".web.js", ".mjs", ".js", ".json"],
  toast: {
    position: "bottom-right",
    duration: 4000,
  },

  strapi: {
    url: strapiBaseUri,
    entities: [
      {
        name: "articles",
        type: "collection",
      },
      {
        name: "categories",
        type: "collection",
      },
      {
        name: "sites",
        type: "collection",
      },
      {
        name: "global",
        type: "single",
      },
    ],
  },
  markdownit: {
    preset: "default",
    linkify: true,
    breaks: true,
    injected: true,
    html: true,
  },

  styleResources: {
    scss: ["assets/scss/default/_variables.scss"],
  },

  /*
   ** Build configuration
   */
  build: {
    extractCSS: true,
    /*
     ** You can extend webpack config here
     */
    /* eslint-disable */
    extend(config, ctx) {},
    /* eslint-enable */
    babel: { compact: true },
    transpile: [/^vue2-google-maps($|\/)/],
  },

  publicRuntimeConfig: {
    apiUrl: process.env.API_URL || "https://admin.globalagents.net/",
    pageTitle: process.env.PAGE_TITLE || "Wheels Up Network USA",
    siteUid: process.env.SITE || "wheels-up-network-usa", 
    ipstack:process.env.ACCESS_KEY_IPSTACK || "ceb74d8b542477b5845881f9a4a5d3f5",
    isMaintenance:process.env.IS_MAINTENANCE  || false,
    showEvergreen: process.env.SHOW_EVERGREEN || false,
    showFams:process.env.SHOW_FAM || false,
    GA: process.env.GA || 'UA-54729729-1'
  },
  mode: 'universal'
  /* privateRuntimeConfig: {
    apiUrl: process.env.API_URL
  } */
};
