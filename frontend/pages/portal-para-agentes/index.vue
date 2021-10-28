<template>
  <div>
    <div class="breadcaump-area py-2 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">{{ $t('partners')}}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="bk-blog-grid-area bg_color--1 pb--40">
          <div class="container">
            <div class="row  ">
              <div
                v-for="article in articles"
                :key="article.title"
                class="col-xl-3 col-md-4 col-sm-6 move-up wow mt--100">
                <BlogPostThree
                  :category-slug="localePath({ name: 'portal-para-agentes'})"
                  :article="article"
                  :showImg="false"
                  add-class="blog-standard blog-grid--modern  " 
                  read-more-button
                  withLink
                  />
              </div>
            </div>
            <infinite-loading  class="mt--50" spinner="waveDots"  @infinite="infiniteHandler"> </infinite-loading>
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
    Paginate: () => import('@/components/Paginate'),
    BlogPostThree: () => import('@/components/BlogPostThree'),
  },
//  status: "published",
  data() {
    return {
      date: new Date().toISOString(),
      page: 1,
      articles:[]
    }
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("partners")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("partners")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("partners")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("partners")} | ${pageTitle}`, siteUid);
  },
  mounted() {
    document.body.classList.add('template-color-1', 'template-font-1')
  },
  methods: {
     infiniteHandler($state){
      this.$strapi
        .find(
          "partner-programs",
          qs.stringify({
            _limit: 12,
            _start: 12 * (this.page - 1) ,
            publishedDate_lte: this.date,
            _sort: "publishedDate:desc",
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
            this.page += 1
            this.articles.push(...data)
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    },
  },
  head() {
     const { favicon, name: siteName } = this.$store.state.site._data;
     
     return {
      title: `${ this.$t('partners') } | ${ siteName }`,
      link: [
        {
          rel: "shortcut icon",
          type: "image/x-icon",
          href: favicon ? getStrapiMedia(favicon.url) : "",
        },
      ],
    }
  },
};
</script>
