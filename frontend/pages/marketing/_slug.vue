<template>
  <div class="brook-portfolio-details bg_color--1">
    <div class="container">
      <BreadcrumbSlug
        path="/marketing"
        slag
        :crumb="$t('resources')"
        :title="customer.name"
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
                    >
                      {{ customer.excerpt }}
                    </h5>
                  </div>
                </blockquote>
              </div>

              <div
                v-if="customer.gallery.length"
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
                    :sliders="customer.gallery"
                  />
                </div>
              </div>
              <div class="portfolio-content text-justify mt--40">
                <div class="desc mt--20">
                  <ContentArticle :content="customer.description" />
                </div>
              </div>
              <ListGroup :item="customer.files" />
              <!-- <PaginateNextPreviuos
                category-slug="customers"
                :article="customer"
              /> -->
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
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    BreadcrumbSlug: () => import("@/components/BreadcrumbSlug"),
    FlexibleSlider: () => import("@/components/FlexibleSlider"),
    BlogPostThree: () => import("@/components/BlogPostThree"),
    ContentArticle: () => import("@/components/ContentArticle"),
    PaginateNextPreviuos: () => import("@/components/PaginateNextPreviuos"),
    ListGroup: () => import("@/components/ListGroup"),
  },

  async asyncData({ $strapi, query, params, $config: { siteUid } }) {
    const matchingArticle = await $strapi.find("customers", {
      slug: params.slug,
      "sites.uid": siteUid,
      featured:true
    });
    return {
      customer: matchingArticle[0],
    };
  },
  data() {
    return {
      apiUrl: process.env.strapiBaseUri,
    };
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.customer.name} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.customer.name} | ${pageTitle}`, siteUid);
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
      metaTitle: this.customer.name,
      metaDescription: this.customer.description,
      shareImage: this.customer.logo,
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
