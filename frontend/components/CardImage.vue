<template>
  <div class="main-wrapper" v-if="$route.fullPath === '/'" >
    <div class="hero-blog-grid mt--30 mb--10">
      <div class="hero-blog-grid-active swiper-arrow-hover">
         
        <swiper :options="swiperOption" v-if="banners.length ">
          <div
            v-for="(banner, index) in   banners"
            :key="index"
            class="swiper-slide"
            v-show="banner.published" 
          >
            <a target="_black" :href="banner.slug">
              <img
                height="400"
                width="500"
                :src="getStrapiMedia(banner.image.url)"
              />
            </a>
          </div>
        </swiper>

        <div
          id="ht-prev--card-image"
          class="ht-swiper-button ht-swiper-button-prev"
        >
          <i class="ion ion-ios-arrow-back" />
        </div>
        <div
          id="ht-next--card-image"
          class="ht-swiper-button ht-swiper-button-next"
        >
          <i class="ion ion-ios-arrow-forward" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  components: {},
  
   async fetch() {
     
    const data = await this.$strapi.find("banners", {
      "site.uid": this.$config.siteUid,
    });
     this.banners = data.length  ?  data[0].banners  : [];
  },
  data() {
    return {
      swiperOption: {
        autoplay: true,
        loop: true,
        speed: 1000,
        slidesPerView: 3,
        // slidesPerGroup: 3,
        spaceBetween: 10,
        centeredSlides: true,
        navigation: {
          nextEl: "#ht-next--card-image",
          prevEl: "#ht-prev--card-image",
        },
        breakpoints: {
          1024: {
            slidesPerView: 4,
            spaceBetween: 8,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 5,
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 5,
          },
          320: {
            slidesPerView: 1,
            spaceBetween: 5,
          },
        },
      },
      banners: [],
    };
  },
  methods: {
    getStrapiMedia,
    // filterBannersPublished(banners){
    //     return banners.filter(banner => banner.published ) 
    // }
  },
};
</script>

<style lang="scss" scoped>
.hero-blog-grid-item {
  width: 800px;
  height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  // res
  @media #{$sm-layout} {
    height: 400px;
  }
}
.swiper-container{
  height: 400px;
}
.hero-blog-grid-content {
  .post-inner {
    padding-top: 250px;
    @media #{$sm-layout} {
      padding-top: 150px;
    }
    .heading {
      font-size: 36px;
      margin-bottom: 20px;
      @media #{$md-layout, $sm-layout} {
        font-size: 24px;
      }
      a {
        color: $white;
        &:hover {
          color: $color-1;
        }
      }
    }
    .post-meta {
      color: $white;
      .post-date {
        color: $white;
      }
      .post-category {
        a {
          color: $white;
          &:hover {
            color: $color-1;
          }
        }
      }
    }
  }
}
.swiper-slide {
  .hero-blog-grid-content {
    opacity: 0;
    visibility: hidden;
  }
  &-active {
    .hero-blog-grid-content {
      opacity: 1;
      visibility: visible;
    }
  }
}
.ht-swiper-button-prev {
  font-size: 50px;
  left: 50px;

  @media #{$large-mobile} {
    display: none;
  }
}
.ht-swiper-button-next {
  font-size: 50px;
  right: 50px;

  @media #{$large-mobile} {
    display: none;
  }
}
</style>
