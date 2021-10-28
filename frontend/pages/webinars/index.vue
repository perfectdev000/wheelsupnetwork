<template>
  <div>
    <div
      v-show="articlesNew.length"
      class="breadcaump-area bg_color--1 breadcaump-title-bar "
    >
      <div class="container">
        <div class="row ">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1  ">{{ $t("upcomingwebinar") }}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="bk-blog-grid-area bg_color--1 pb--40">
          <div class="container">
            <div class="row">
              <div
                v-for="article in articlesNew"
                :key="article.title"
                class="col-xl-3 col-md-4 col-sm-6 move-up wow mt--50"
              >
                <BlogPostThree
                  category-slug="/webinars"
                  :article="article"
                  add-class="blog-standard blog-grid--modern"
                  read-more-button
                />
              </div>
            </div>
            
          </div>
        </div>
      </div>
      <!-- <div class="col-lg-4 mt_md--40 mt_sm--40 mt--30">
        <BlogSidebar />
      </div> -->
    </div>
    <div class="breadcaump-area py-2 mb--35 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">{{ $t("lastwebinar") }}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
         <FilterCustomer @changeSelected="changeCustomer"/>  
    </div>
    <div class="col-lg-12">
      <div class="bk-blog-grid-area bg_color--1 pb--40">
        <div class="container">
          <div class="row mtn--50">
            <div
              v-for="(article, index) in articlesOld"
              :key="index"
              :class="[index < 4 ? 'mt--30' : 'mt--100', styleclass]"
            >
              <BlogPostThree
                category-slug="/webinars"
                :article="article"
                add-class="blog-standard blog-grid--modern"
                read-more-button
              />
            </div>
          </div>
          <infinite-loading class="mt--50" spinner="waveDots" :identifier="customer_id"  @infinite="infiniteHandler"> </infinite-loading>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import { getStrapiMedia } from "../../utils/medias";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    BlogPostThree: () => import("@/components/BlogPostThree"),
    FilterCustomer: () => import("@/components/FilterCustomer"),
  },

  async asyncData({ $strapi, $config: { siteUid } }) {
    let articles = await $strapi.find(
      "webinars",
      qs.stringify({
        publishedDate_gte: new Date().toISOString(),
        _sort: "id:desc,publishedDate:desc",
        "sites.uid": siteUid,
        status: "published",
        _where: {
          _or: [
            { expiration_date_gte: new Date().toISOString() },
            { expiration_date_null: true },
          ],
        },
      })
    );
    return {
      articlesNew: articles,
    };
  },

  data() {
    return {
      page: 1,
      articlesOld:[],
      date: new Date().toISOString(),
      styleclass: "col-xl-3 col-md-4 col-sm-6 move-up wow",
      customer_id: undefined
    }
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `Webinars | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `Webinars | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `Webinars | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `Webinars | ${pageTitle}`, siteUid);
  },
  mounted() {
    document.body.classList.add("template-color-1", "template-font-1");
    if (typeof this.$redrawVueMasonry === "function") {
      this.$redrawVueMasonry();
    }
  },
  methods: {
    infiniteHandler($state){
      this.$strapi
        .find(
          "webinars",
          qs.stringify({
            _limit: 12,
            _start: 12 * (this.page - 1) ,
            publishedDate_lte: this.date,
            _sort: "publishedDate:desc",
            "sites.uid": this.$config.siteUid,
            'customer.id': this.customer_id,
            status: "published",
            _where: {
              _or: [
                { expiration_date_gte: this.date },
                { expiration_date_null: true },
              ],
            },
          })
        )
        .then((data) => {
          if (data.length) {
            this.page += 1;
            this.articlesOld.push(...data);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
    },
    changeCustomer(id) {
      this.page = 1;
      this.articlesOld = [];
      this.customer_id = id;
    },
  },
  head() {
    const {
      defaultSeo,
      favicon,
      name: siteName,
    } = this.$store.state.site._data;

    return {
      title: `Webinars | ${siteName}`,
       link: [
        {
          
          href: favicon ? getStrapiMedia(favicon.url) : null,
        },
      ],
    };
  },
};
</script>
