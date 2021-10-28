<template>
  <div>
    <ArticlesCarousel :articles="articles" /> 
    <div class="bk-blog-grid-area pb--100 pb_md--80 pb_sm--80">
      <div class="container">
        <div class="container mt-5 mb-5">
          <div class="row">
            <div class="col-lg-12">
              <div class="breadcaump-inner text-center">
                <h1 class="heading heading-h2">{{ $t("newslast") }}</h1>
              </div>
            </div>
          </div>
        </div>

        <div class="row mtn--50">
          <div
            v-for="article in news"
            :key="article.id"
            class="col-lg-3 col-md-3 col-sm-6 move-up wow mt--50"
          >
            <BlogPostThree
              :article="article"
              show-date
              category-slug="/news"
              add-class="grid-simple"
            />
          </div>
        </div>
      </div>
    </div>
    <BrandLogoStyleOne />
    <AboutAuthenticStudio />
    <BrandLogoCarousel />
  </div>
</template>

<script>
import { getMetaTags } from "../utils/seo";
import { getStrapiMedia } from "../utils/medias";
import qs from "qs";

export default {
  components: {
    ArticlesCarousel: () => import("@/components/sections/ArticlesCarousel"),
    BlogPostThree: () => import("@/components/BlogPostThree"),
    BannersPublicity: () => import("~/components/BannersPublicity"),
    BrandLogoStyleOne: () => import("~/components/BrandLogoStyleOne"),
    AboutAuthenticStudio: () => import("~/components/AboutAuthenticStudio"),
    BrandLogoCarousel: () => import("~/components/BrandLogoCarousel"),
  },

  async asyncData({ $strapi, route, $config: { siteUid } }) {
    let date =   new Date().toISOString()
    let promotions = await $strapi.find(
      "promotions",
      qs.stringify({
        _limit: 4,
        _sort: "id:desc,publishedDate:desc",
        publishedDate_lte: date,
        "sites.uid": siteUid,
        status: "published",
        _where: {
          _or: [
            { expiration_date_gte: date },
            { expiration_date_null: true },
          ],
        },
      })
    );

    return {
      articles: promotions,
      news: await $strapi.find(
        "news-items",
        qs.stringify({
          "sites.uid": siteUid,
          status: "published",
          _limit: 8,
          _sort: "id:desc,publishedDate:desc",
          publishedDate_lte: date,
          _where: {
            _or: [
              { expiration_date_gte: date },
              { expiration_date_null: true },
            ],
          },
        })
      ),
      route: route.fullPath 
    };
  },

  data() {
    return {
      items: [
        {
          text: "Home",
          to: "/",
        },
        {
          text: "Travel",
          to: "/blog",
        },
        {
          text: "Home",
          active: true,
        },
      ],
    };
  },

  mounted() {
    document.body.classList.add("template-color-2", "font-varela");
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
    };

    return {
      titleTemplate: `%s | ${siteName}`,
      title: fullSeo.metaTitle,
      meta: getMetaTags(fullSeo),
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

<style scoped></style>
