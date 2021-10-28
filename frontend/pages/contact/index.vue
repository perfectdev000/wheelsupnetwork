<template>
  <div>
    <SearchPopup />
    <ContactModern :site="$store.state.site._data.uid" />
  </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    SearchPopup: () => import("@/components/SearchPopup"),
    ContactModern: () => import("@/components/sections/ContactModern"),
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("contact_us")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("contact_us")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("contact_us")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("contact_us")} | ${pageTitle}`, siteUid);
  },
  head() {
    const { favicon, name: siteName } = this.$store.state.site._data;

    return {
      title: ` ${this.$t("contact_us")}  | ${
        siteName
      }`,
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
