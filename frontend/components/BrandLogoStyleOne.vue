<template>
  <div class="bk-brand-area bg_color--1 ptb--40">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-5">
          <div class="brand-inner">
            <div class="brook-section-title text-left">
              <h3 class="heading heading-h3 font-large">
                {{ $t('ourcustomers')}}
              </h3>
              <div class="bkseparator--25"></div>
              <div class="title-separator w--80 color-red"></div>
            </div>
            <div class="bkseparator--45"></div>
            <h6
              class="
                heading heading-h6
                font-16
                line-height-1-88
                font-medium
                body-color
              "
            >
             {{ $t('body_customers')}}
            </h6>
            <div class="bkseparator--35"></div>
          </div>
        </div>
        <div class="col-lg-6 offset-lg-1 mt_sm--40 mt_md--40">
            <div class="row ">
                <div class="col-lg-12">
                    <div class="brand-wrapper">
                        <div class="brand__list brand-default brand-style--1  no-border ">
                            <swiper :options="swiperOption" >
                                <div v-for="brand in data.item"  :key="brand.id" class="swiper-slide">
                                    <a :href="brand.url" :target="`_blank`" >
                                        <img :src="brand.logo" alt="logo image" class="img-logo brand">
                                    </a>
                                </div>
                            </swiper> 
                        </div>
                    </div>
                </div>
            </div>
            <div class="row ">
                <div class="col-lg-12">
                    <div class="brand-wrapper">
                        <div class="brand__list brand-default brand-style--1">
                            <swiper :options="swiperOption" >
                                <div v-for="brand in data.Item"  :key="brand.id" class="swiper-slide">
                                    <a :href="brand.url" :target="`_blank`" >
                                        <img :src="brand.logo" alt="logo image" class="img-logo ">
                                    </a>
                                </div>
                            </swiper> 
                        </div>
                    </div>
                </div>
            </div>
            <div class="row ">
                <div class="col-lg-12">
                    <div class="brand-wrapper">
                        <div class="brand__list brand-default brand-style--1">
                            <swiper :options="swiperOption" >
                                <div v-for="brand in data.itemTwo"  :key="brand.id" class="swiper-slide">
                                    <a :href="brand.url" :target="`_blank`" >
                                        <img :src="brand.logo" alt="logo image" class="img-logo ">
                                    </a>
                                </div>
                            </swiper> 
                        </div>
                    </div>
                </div>
            </div>
            <div class="row ">
                <div class="col-lg-12">
                    <div class="brand-wrapper">
                        <div class="brand__list brand-default brand-style--1">
                            <swiper :options="swiperOption" >
                                <div v-for="brand in data.itemThree"  :key="brand.id" class="swiper-slide">
                                    <a :href="brand.url" :target="`_blank`" >
                                        <img :src="brand.logo" alt="logo image" class="img-logo ">
                                    </a>
                                </div>
                            </swiper> 
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import data from "../data/brandLogoOne.json";

export default {
  data() {
    return {
      data,
       swiperOption: {
        loop: true,
        speed: 1000,
        spaceBetween: 25,
        slidesPerView:5,
        centeredSlides: true,
        autoplay: {
          delay: 3000,
        },
        // Responsive breakpoints
        breakpoints: {
          1200: {
            slidesPerView : 7
          },
          768:{
            slidesPerView : 4
          },
        }
      }
    };
  },
};
</script>
<style lang="scss" scoped>
.swiper-wrapper .swiper-slide {
  max-height: 120px;
  align-items: center;
}
.img-logo  {
        width: 100px;
        height: 60px;
        display:block;
        margin:auto;
      }
</style>