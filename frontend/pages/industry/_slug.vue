<template>
    <div class="brook-portfolio-details bg_color--1">
      <div class="container">
         <BreadcrumbSlug
          path="/industry"
          slag
          :crumb="$t('industry')"
          :title="article.title"
        />
 
        <div class="row pb--40">
          <div id="is_stuck_inner" class="col-12 order-2 order-lg-1 mt_md--40 mt_sm--40">
            <div class="portfolio-left bk-portfolio-details">
              <div class="portfolio-main-info">
                <div class="bk-quote-content">
                  <blockquote class="brook-quote move-up wow">
                    <CustomerLogo :customer="article.customer" />
                    <div class="quote-text">
                      <h5 class="heading heading-h5 line-height-1-42 text-muted text-justify">{{ article.description }}</h5>
                    </div>
                  </blockquote>
                </div>
                <div class="featured-image" v-if="article.featured_image">
                  <img :src="getStrapiMedia(article.featured_image.url)" :alt="article.featured_image.name"  >
                </div>
                <div class="portfolio-content text-justify mt--40">
                  <div class="desc mt--20">
                    <ContentArticle :content="article.content"/>
                  </div>
                </div>
                <div v-if="article.slider_images.length" class="portfolio-content mt--10">
                  <div class="flexale-image bg_color--1 swiper-custom-arrow swiper-custom-dots move-up wow">
                    <FlexibleSlider add-class="ptb-md--30 ptb-sm--20"  :sliders="article.slider_images" />
                  </div>
                </div>
                <ListGroup :item="article.files" />
                <h3  class="mt--50  border-top pt-4 border-muted  "> {{ $t('lastindustry')}}  </h3>
                <div class="row ">  
                  <div
                    v-for="item in news"
                    :key="item.id"
                    class="col-xl-3 col-md-4 col-sm-6 move-up wow mb--0 "
                  >
                     <BlogPostThree
                      :article="item"
                      add-class="grid-simple"
                      :showImg="false"
                      category-slug="/industry"
                    />
                  </div>
                </div>
                <PaginateNextPreviuos  category-slug="industries" :page="page" :article="article" />
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
    FlexibleSlider: () => import('@/components/FlexibleSlider'),
    BreadcrumbSlug: () => import('@/components/BreadcrumbSlug'),
    CustomerLogo: () => import('@/components/CustomerLogo'),
    BlogPostThree: () => import('@/components/BlogPostThree'),
    ContentArticle: () => import('@/components/ContentArticle'),
    PaginateNextPreviuos: () => import('@/components/PaginateNextPreviuos'),
    ListGroup: () => import('@/components/ListGroup'),
  },

  async asyncData({ $strapi, params,query, $config: { siteUid } }) {
    const matchingArticle = await $strapi.find("industries", {
      slug: params.slug,
      'sites.uid': siteUid
    });
    return {
      news: await $strapi.find("industries", 
        qs.stringify({
          _limit: 4,
          _sort: "id:desc,publishedDate:desc",
          "sites.uid": siteUid,
          status: "published",
          id_lt: matchingArticle[0].id, 
          publishedDate_lte: matchingArticle[0].publishedDate, 
          id_ne:matchingArticle[0].id,
          _where: {
            _or: [
              { expiration_date_gte: new Date().toISOString() },
              { expiration_date_null: true },
            ],
          },
        })
      ),
      article: matchingArticle[0],
      page: Number(query.page),
    };
  },

  data () {
    return {
      apiUrl: process.env.strapiBaseUri,
    }
  },

  created() {
    const { pageTitle, siteUid } = this.$config;
    pageTrackGAV4(this.$gtag, window.location.pathname, `${this.article.title} | ${pageTitle}`, window.location.href);
    screenViewGAV4(this.$gtag, `${this.article.title} | ${pageTitle}`, siteUid);
  },

  mounted () {
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
      metaTitle: this.article.title,
      metaDescription: this.article.description,
      shareImage: this.article.image,
    };

    return {
      titleTemplate: `%s | ${siteName}`,
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
};
</script>

 
