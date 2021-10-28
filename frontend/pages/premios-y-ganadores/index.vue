<template>
  <div>
    <div class="breadcaump-area py-2 mb--35 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row mb--20">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">{{ $t("prizewinners") }}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <FilterCustomer @changeSelected="changeCustomer" />
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="bk-blog-grid-area bg_color--1">
          <div class="container">
            <div class="row mtn--50">
              <div
                v-for="(article, index) in articles"
                :key="index"
                :class="[index < 4 ? 'mt--30' : 'mt--100', styleclass]"
              >
                <BlogPostThree
                  :category-slug="localePath({ name: 'premios-y-ganadores' })"
                  :article="article"
                  add-class="blog-standard blog-grid--modern"
                  read-more-button
                />
              </div>
            </div>
            <infinite-loading
              class="mt--50"
              spinner="waveDots"
              :identifier="customer_id"
              @infinite="infiniteHandler"
            >
            </infinite-loading>
          </div>
        </div>
      </div>
      <!-- <div class="col-lg-4 mt_md--40 mt_sm--40 mt--30">
        <BlogSidebar />
      </div> -->
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
    Paginate: () => import("@/components/Paginate"),
    FilterCustomer: () => import("@/components/FilterCustomer"),
  },
  data() {
    return {
      articles: [],
      page: 1,
      date: new Date().toISOString(),
      styleclass: "col-xl-3 col-md-4 col-sm-6 move-up wow",
      customer_id: undefined,
    };
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("prize")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("prize")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("prize")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("prize")} | ${pageTitle}`, siteUid);
  },
  mounted() {
    document.body.classList.add("template-color-1", "template-font-1");
  },
  methods: {
    infiniteHandler($state) {
      this.$strapi
        .find(
          "contests",
          qs.stringify({
            _limit: 12,
            _start: 12 * (this.page - 1),
            publishedDate_lte: this.date,
            _sort: "id:desc,publishedDate:desc",
            "customer.id": this.customer_id,
            "sites.uid": this.$config.siteUid,
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
            this.articles.push(...data);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
    },
    changeCustomer(id) {
      this.page = 1;
      this.articles = [];
      this.customer_id = id;
    },
  },
  head() {
    const { favicon, name: siteName } = this.$store.state.site._data;
    
    return {
      title: `${this.$t("prize")} | ${siteName}`,
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
