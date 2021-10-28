<template>
  <div class="blog-grid blog-standard" :class="addClass">
    <div class="post-thumb" v-if="showImg">
      <n-link v-if="!article.link" :to="buildUrl(article)">
        <img
          class="blog__post--img"
          :src="
            article.featured_image
              ? getStrapiMedia(article.featured_image.url)
              : '/img/service/service-3/service-1.jpg'
          "
          :alt="article.title"
        />
      </n-link>
      <a v-else-if="article.link" target="_blank" :href="article.link">
        <img
          class="blog__post--img"
          :src="
            article.featured_image
              ? getStrapiMedia(article.featured_image.url)
              : '/img/service/service-3/service-1.jpg'
          "
          :alt="article.title"
        />
      </a>
    </div>
    <div class="post-content text-center">
      <div class="post-inner">
        <div v-if="showDate || showCategory" class="post-meta mb--10">
          <div v-if="showDate" class="post-date">
            {{ article.publishedDate | formateDate($i18n.locale) }}  
          </div>
          <div v-if="showCategory" class="post-category">
            <n-link v-if="!article.link" :to="`/${article.slug}`">
              {{ categorySlug }}
            </n-link>
            <a v-else-if="article.link" target="_blank" :href="article.link">
              {{ categorySlug }}
            </a>
          </div>
        </div>

        <div v-if="article.customer">
          <LogoCustomer
            v-if="showLogo && article.customer.logo "
            :isLogo="showImg"
            :alt="article.customer.logo.url"
          />
        </div>

        <h5 class="heading heading-h5  text-capitalize ">
          <n-link v-if="!withLink" :to="buildUrl(article)">
            {{ article.title | truncate(40) }}
            <!-- FRHI Hotels & Resorts -->
          </n-link>
          <a v-else-if="withLink" target="_blank" :href="article.link">
            {{ article.title | truncate(40) }}
            <!-- FRHI Hotels & Resorts -->
          </a>
        </h5>
        <n-link
          v-if="!article.link"
          v-show="readMoreButton"
          class="post-read-more"
          :to="buildUrl(article)"
        />
        <a
          v-else-if="article.link"
          v-show="readMoreButton"
          target="_blank"
          :href="article.link"
          class="post-read-more"
        >
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  components: {
    LogoCustomer: () => import("@/components/LogoCustomer"),
  },
  props: {
    article: {
      type: Object,
      default() {
        return {};
      },
    },
    showLogo: {
      type: Boolean,
      default: true,
    },
    categorySlug: {
      type: String,
      default: "",
    },
    showDate: {
      type: Boolean,
      default: false,
    },
    showCategory: {
      type: Boolean,
      default: false,
    },
    addClass: {
      type: String,
      default: "",
      required: false,
    },
    readMoreButton: Boolean,
    withLink: Boolean,
    page: {
      type: Number,
      default: 1,
      required: false,
    },
    showImg: {
      default: true,
      required: false,
      type: Boolean,
    },
  },
  methods: {
    getStrapiMedia,
    buildUrl(article) {
      let url = `${
        this.categorySlug ? this.categorySlug : article.slug
      }/${article.slug}`;
      return url;
    },
  },
};
</script>

<style lang="scss" scoped>
.blog__post--img {
  height: 190px;
}
.blog-grid--modern.blog-standard {
  min-height: 200px;
}

.heading {
  margin-top: 9px;
}

/* body.template-color-1 .service.service--3 .thumb a img {
    transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
    max-height: 230px;
    width: 100%;
    height: 100%;
} */
</style>
