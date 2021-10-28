<template>
    <div class="brook-portfolio-details bg_color--1">
      <div class="container">
        <BreadcrumbSlug
          :path="localePath({ name: 'empleos'})"
          slag
          :crumb="$t('jobs')"
          :title="job.name"
        />
        <div class="row pb--40">
          <div id="is_stuck_inner" class="col-12 order-2 order-lg-1 mt_md--40 mt_sm--40">
            <div class="portfolio-left bk-portfolio-details">
              <div class="portfolio-main-info">
                <div class="portfolio-content text-justify mt--40">
                  <div class="desc mt--20">
                    <div class="bk_pra preserve-line-break" >
                        <ContentArticle :content="job.description" />
                    </div>
                  </div>
                </div>

                <div class="spacing"></div>
                <div class="call-btn text-center wow move-up">
                  <a :href="job.link" target="_blank" class="brook-btn bk-btn-theme text-white btn-sd-size btn-rounded text-uppercase">
                    {{ $t('gotooffer') }}
                  </a>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- <div class="container">
        <div class="row">
          <div class="col-lg-12">
            [>Portfolio Nav List<]
            <div class="portfolio-nav-list pt--50 pb--150 pb_md--80 pb_sm--60 pt_md--5 pt_sm--5">
              <div class="portfolio-page prev">
                <div class="inner">
                  <n-link to="/">
                    <p>Prev</p>
                  </n-link>
                </div>
              </div>
              <div class="portfolio-page next mt_sm--30">
                <div class="inner">
                  <n-link to="/">
                    <p>Next</p>
                  </n-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div> -->
    </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";
import { getMetaTags } from "../../utils/seo";
import qs from "qs";
import { pageTrackGAV4, screenViewGAV4 } from "../../utils/analytics";

export default {
  components:{
    BreadcrumbSlug: () => import('@/components/BreadcrumbSlug'),
    ContentArticle: () => import('@/components/ContentArticle'),
  },
  async asyncData({ $strapi, params, $config: { siteUid } }) {
    const matchingJobs = await $strapi.find("jobs", 
      qs.stringify({
        slug: params.slug,
        "sites.uid": siteUid,
        status: "published",
        _where: {
              _or: [
                { expiration_date_gte: new Date().toISOString() },
                { expiration_date_null: true },
              ],
            },
      })
    );
    return {
      job: matchingJobs[0],
      
    };
  },

  data() {
    return {
      apiUrl: process.env.strapiBaseUri,
    }
  },
  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.job.name} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.job.name} | ${pageTitle}`, siteUid);
  },

  mounted() {
    document.body.classList.add('template-color-1', 'template-font-1')
  },

  methods: {
    getStrapiMedia,
  },

  head() {
    const { defaultSeo, favicon, name: siteName } = this.$store.state.site._data;

    // Merge default and article-specific SEO data
    const fullSeo = {
      ...defaultSeo,
      metaTitle: this.job.name,
      metaDescription: this.job.description,
      // shareImage: this.article.image,
    };

    return {
      titleTemplate: `%s | ${ siteName }`,
      title: fullSeo.metaTitle,
      meta: getMetaTags(fullSeo),
      link: [
        {
          rel: "shortcut icon",
          type: "image/x-icon",
          href: favicon ? getStrapiMedia(favicon.url) : '',
        },
      ],
    };
  },
}
</script>

<style lang="scss" scoped>
.portfolio-content > * {
  padding: 5px 0;
}

.portfolio-content > img {
  text-align: center;
}

 
a.text-white {
  color: white !important;
}
.preserve-line-break {
  white-space: pre-wrap;
}
</style>
