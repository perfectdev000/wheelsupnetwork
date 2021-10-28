<template>
  <div class="brook-portfolio-details bg_color--1">
    <div class="container">
      <BreadcrumbSlug
        :path="localePath({ name: 'destinos' })"
        slag
        :crumb="$t('destinations')"
        :title="destionations.excerpt"
      />

      <div class="row pb--40">
        <div
          id="is_stuck_inner"
          class="col-12 order-2 order-lg-1 mt_md--40 mt_sm--40"
        >
          <div class="portfolio-left bk-portfolio-details">
            <div class="portfolio-main-info">
              <div class="bk-quote-content">
                <blockquote class="brook-quote move-up wow">
                  <div class="quote-text">
                    <h5
                      class="
                        heading heading-h5
                        line-height-1-42
                        text-muted text-justify
                      "
                    ></h5>
                  </div>
                </blockquote>
              </div>
              <div
                v-if="destionations.gallery.length"
                class="portfolio-content mt--10"
              >
                <div
                  class="
                    flexale-image
                    bg_color--1
                    swiper-custom-arrow swiper-custom-dots
                    move-up
                    wow
                  "
                >
                  <FlexibleSlider
                    add-class="ptb-md--30 ptb-sm--20"
                    :sliders="destionations.gallery"
                  />
                </div>
              </div>
              <div class="portfolio-content text-justify mt--40">
                <h6 class="heading heading-h6">{{ destionations.name }}</h6>
                <div class="desc mt--20">
                  <ContentArticle :content="destionations.description" />
                </div>
              </div>
              <ListGroup :item="destionations.files" />
               
              <PaginateNextPreviuos
                category-slug="destinations"
                :article="destionations"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import { getMetaTags } from "../../utils/seo";
import qs from "qs";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    FlexibleSlider: () => import("@/components/FlexibleSlider"),
    BlogPostThree: () => import("@/components/BlogPostThree"),
    BreadcrumbSlug: () => import("@/components/BreadcrumbSlug"),
    ContentArticle: () => import("@/components/ContentArticle"),
    ListGroup: () => import("@/components/ListGroup"),
    PaginateNextPreviuos: () => import("@/components/PaginateNextPreviuos"),
  },

  async asyncData({ $strapi, params, query, $config: { siteUid } }) {

    const destionation = await $strapi.find("destinations",{
        id:params.slug
    })
    return {
      destionations: destionation[0] 
    };
  },

  data() {
    return {
      apiUrl: process.env.strapiBaseUri,
    };
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.destionations.name} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.destionations.name} | ${pageTitle}`, siteUid);
  },
  mounted() {
    document.body.classList.add("template-color-1", "template-font-1");
  },
  methods: {
    getStrapiMedia,
  },

  head() {
    const {
      defaultSeo,
      favicon,
      name: siteName,
    } = this.$store.state.site._data;

    // Merge default and article-specific SEO data
    const fullSeo = {
      ...defaultSeo,
      metaTitle: this.destionations.name,
      metaDescription: this.destionations.description,
      shareImage: this.destionations.logo,
    };

    return {
      titleTemplate: `%s | ${siteName}`,
      title: fullSeo.metaTitle,
      meta: getMetaTags(fullSeo),
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
