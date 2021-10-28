<template>
  <div>
    <WhatWeDo :about="about" />
    <div class="brook-gradation-area ptb--40 bg_color--1 basic-thine-line">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="bk-title--default text-center">
              <h2 class="heading heading-h2 theme-color">
                {{ about.title_center }}
              </h2>
              <div class="bkseparator--30"></div>
              <h4 class="heading heading-h4">
                {{ about.center_title_footer }}
              </h4>
            </div>
            <GradationOne :about="about" />
          </div>
          <div class="col-lg-12 pt--60">
            <div class="bk-title--default text-center">
              <h3 class="heading heading-h3 theme-color">
                {{ about.title_footer }}
              </h3>
              <div class="bkseparator--30"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <BrandLogoCarousel />
  </div>
</template>

<script>
 import { getStrapiMedia } from "../../utils/medias";
 import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    WhatWeDo: () => import("@/components/WhatWeDo"),
    GradationOne: () => import("@/components/GradationOne"),
    BrandLogoCarousel: () => import("@/components/BrandLogoCarousel"),
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `About Us | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `About Us | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `About Us | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `About Us | ${pageTitle}`, siteUid);
  },
  mounted() {
    document.body.classList.add("template-color-1", "template-font-1");
  },
  async asyncData({ i18n, $strapi, $config: { siteUid } }) {
    return {
      about: await $strapi.find("about-es", {
        _locale: i18n.defaultLocale,
      }),
    };
  },
  head() {
    const {
      favicon,
      name: siteName,
    } = this.$store.state.site._data;

    return {
      title: `About Us || ${ siteName }`,
      link: [
        {
          rel: "shortcut icon",
          type: "image/x-icon",
          href: getStrapiMedia(favicon.url),
        },
      ],
    };
  },
};
</script>
