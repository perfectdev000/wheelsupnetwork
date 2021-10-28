<template>
  <div
    class="
      bk-about-area
      pt--45
      pt_md--8
      pt_sm--6
      bg-svg--1
      swiper-arrow-hover
       
    "
  >
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="brook-section-title text-center">
            <h1 class="heading heading-h2 heading-font">
              {{ $t('trending')   }}
            </h1>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="bk-blog-grid-area bg_color--1 pb--40">
          <div class="container">
            <div class="row mtn--50">
              <div
                v-for="article in articles"
                :key="article.title"
                class="col-lg-3 col-md-4 col-sm-6 move-up wow mt--100"
              >
                <BlogPostThree
                  
                  :article="article"
                  add-class="blog-standard blog-grid--modern"
                  read-more-button
                  category-slug="/promotions"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../../utils/medias";

export default {
  components: {
    BlogPostThree: () => import("@/components/BlogPostThree"),
  },
  props: {
    articles: {
      type: Array,
      default() {
        return [];
      },
    },
    addClass: {
      type: String,
      default: "",
    },
    readMoreButton: Boolean,
  },
  data() {
    return {
      swiperOption: {
        spaceBetween: 10,
        autoplay: false,
        loop: true,
        speed: 1000,
        navigation: {
          nextEl: ".ht-swiper-button-next",
          prevEl: ".ht-swiper-button-prev",
        },
        // Responsive breakpoints
        breakpoints: {
          1024: {
            slidesPerView: 4,
            spaceBetween: 10,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 10,
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 10,
          },
          320: {
            slidesPerView: 1,
            spaceBetween: 10,
          },
        },
      },
    };
  },
  methods: {
    getStrapiMedia,
  },
};
</script>

<style lang="scss" scoped>
.blog__post--img {
  max-width: 600px;
  height: auto;
}
.blog-grid--modern.blog-standard {
  min-height: 200px;
}
/* body.template-color-1 .service.service--3 .thumb a img {
    transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
    max-height: 230px;
    width: 100%;
    height: 100%;
} */
</style>
