<template>
  <div>
    <div
      class="
        brook-gradation-area
        ptb--50
        ptb-md--50
        ptb-sm--30
        bg_color--1
        basic-thine-line
      "
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="bk-title--default text-center">
              <div class="bkseparator--30"></div>
              <h3 class="heading heading-h3">{{ $t("cookie") }}</h3>
            </div>
            <PoliciesCookies />
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
    PoliciesCookies: () => import("@/components/sections/PoliciesCookies"),
    BrandLogoCarousel: () => import("@/components/BrandLogoCarousel"),
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("cookie")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("cookie")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("cookie")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("cookie")} | ${pageTitle}`, siteUid);
  },

  mounted() {
    document.body.classList.add("template-color-1", "template-font-1");
  },

  head() {
    const { favicon, name: siteName } = this.$store.state.site._data;

    return {
      title: `${siteName} || ${this.$t("cookie")}`,
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
