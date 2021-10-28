<template>
  <div>
    <div class="breadcaump-area py-2 bg_color--1 breadcaump-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcaump-inner text-center">
              <h1 class="heading heading-h1">{{ $t('ticket') }}</h1>
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
              <p class="pt-5 text-justify" v-html="$t('bodyticket')">
                 <h4 class="py-3 d-block">
                  <a :style="$config.siteUid == 'wheels-up-network-canada' ||
                      $config.siteUid == 'wheels-up-network-usa'  ? 'color: #08a6ca !important' : 'color: #ca3c08 !important;' " src="../../static/img/others/teatro-700x355.jpg" target="_blank" rel="noopener">{{ $t('buyticket')}}</a>
                </h4> 
              </p>
              <p class="d-block w-100">
                <img class="alignleft size-large wp-image-7798" src="http://www.soloparaagentes.com/wp-content/uploads/2018/08/teatro-700x355.jpg" alt="" srcset="http://www.soloparaagentes.com/wp-content/uploads/2018/08/teatro-700x355.jpg 700w, http://www.soloparaagentes.com/wp-content/uploads/2018/08/teatro-330x167.jpg 330w, http://www.soloparaagentes.com/wp-content/uploads/2018/08/teatro-314x160.jpg 314w, http://www.soloparaagentes.com/wp-content/uploads/2018/08/teatro.jpg 765w" sizes="(max-width: 620px) 100vw, 620px" width="620" height="314">
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  watch: {
    '$route'() {
      const { pageTitle, siteUid } = this.$config;
      pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("ticket")} | ${pageTitle}`, window.location.href);
      screenViewGAV4(this.$gtag, `${this.$t("ticket")} | ${pageTitle}`, siteUid);

    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.$t("ticket")} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.$t("ticket")} | ${pageTitle}`, siteUid);
  },
  mounted () {
    document.body.classList.add('template-color-1', 'template-font-1')

    if (typeof this.$redrawVueMasonry === 'function') {
      this.$redrawVueMasonry()
    }

    this.onLoad()
  },

  methods:{
    async onLoad(){
      await this.sleep(950)
      this.$redrawVueMasonry()
    },
    sleep(ms){
      return new Promise(resolve => setTimeout(resolve, ms))
    }
  },

  head() {
    const { favicon, name: siteName } = this.$store.state.site._data;

    return {
      title: `${ this.$t('ticket')} | ${ siteName }`,
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
