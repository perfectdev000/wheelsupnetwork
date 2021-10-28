<template>
  <div>
    <div class="breadcaump-area py-2 mb--40 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">
                {{ $t("resources") }}
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="bk-blog-grid-area bg_color--1 pb--20">
          <div class="container">
            <div class="row  mtn--50 ">
              <div
                v-for="article in articles"
                :key="article.id"
                class="col-xl-3 col-md-4 col-sm-6 move-up wow mt--20"
              >
                <n-link
                  v-if="article.logo"
                  :to="`/${'marketing'}/${article.slug}`"
                >
                  <div class="box">
                    <LogoCustomer :isLogo="false" :alt="article.logo.url" />
                  </div>
                </n-link>
              </div>
            </div>
             <infinite-loading  class="mt--50" spinner="waveDots"  @infinite="infiniteHandler"> </infinite-loading>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import qs from "qs";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    BlogPostThree: () => import("@/components/BlogPostThree"),
    LogoCustomer: () => import("@/components/LogoCustomer"),
  },
  data() {
    return {
      articles:[],
      page:1,
      date: new Date().toISOString(),
    };
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("resources")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("resources")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("resources")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("resources")} | ${pageTitle}`, siteUid);
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
          "customers",
          qs.stringify({
            _limit: 12,
            _start: 12 * (this.page - 1) ,
            published_date_lte: this.date,
            _sort: "vip:desc,published_date:desc",
            "sites.uid": this.$config.siteUid,
            status: "published",
            featured: true,
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
            this.articles.push(...data);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
    },
  },
  head() {
    const { favicon, name: siteName } = this.$store.state.site._data;
    
    return {
      title: `${ this.$t('resources') }| ${ siteName }`,
      link: [
        {
          rel: "shortcut icon",
          type: "image/x-icon",
          href: favicon ? getStrapiMedia(favicon.url) : "",
        },
      ],
    };
  },
};
</script>
<style lang="scss" scoped>
.box {
  border: 1px solid #d1d1d1;
  background: #ffffff;
  padding: 50px;
  width: 320px;
  height: 200px;
}
</style>
