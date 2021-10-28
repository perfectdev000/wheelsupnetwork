<template>
  <client-only>
    <NewsletterForm :site="this.$store.state.site._data.uid" />
  </client-only>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components: {
    NewsletterForm: () => import("@/components/NewsletterForm"),
  },
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `Subscribe to Newsletter | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `Subscribe to Newsletter | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `Subscribe to Newsletter | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `Subscribe to Newsletter | ${pageTitle}`, siteUid);
  },
  
  head() {
    const {
      favicon,
      name: siteName,
    } = this.$store.state.site._data;

    return {
      title: `Contact | ${siteName }`,
      link: [
        {
          rel: "shortcut icon",
          type: "image/x-icon",
          href: favicon ? getStrapiMedia(favicon.url) : null,
        },
      ],
    };
  },
};
</script>
