<template>
  <div>
    <div class="breadcaump-area py-2 mb--35 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">{{ $t('destinations')}}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="bk-blog-grid-area bg_color--1 pb--40">
          <div class="container">
            <div class="row mtn--50">
              <div
                v-for="destination in destinations"
                :key="destination.title"
                class="col-xl-4 col-md-4 col-sm-6 move-up wow mt--100"
              >
                <BlogPostDestinations 
                  :item="destination" 
                  :category-slug="localePath({ name: 'destinos'})"
                  add-class="blog-standard blog-grid--modern" 
                  read-more-button 
                 />
              </div>
            </div>
             <infinite-loading class="mt--50" spinner="waveDots"  @infinite="infiniteHandler"> </infinite-loading>
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
    BlogPostDestinations: () => import("@/components/BlogPostDestinations"),
  },
  data() {
    return {
      page: 1,
      destinations:[],
      date: new Date().toISOString(),
    }
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("destinations")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("destinations")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("destinations")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("destinations")} | ${pageTitle}`, siteUid);
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
          "destinations",
          qs.stringify({
            _limit: 12,
            _start: 12 * (this.page - 1) ,
            published_date_lte: this.date,
            _sort: "id:desc, published_date:desc",
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
            this.destinations.push(...data);
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
      title: `${ this.$t('destinations') } | ${ siteName }`,
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
