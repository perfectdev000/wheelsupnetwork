<template>
    <div class="bk-brand-area bg_color--1 ptb--60">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="brand-wrapper">
                        <div class="brand__list brand-default brand-style--1 ">
                            <swiper :options="swiperOption">
                                <div v-for="brand in data" :key="brand.id" class="swiper-slide">
                                    <a :href="brand.url" target="_blank"  >
                                        <img :src="brand.logo" alt="logo image" >
                                    </a>
                                </div>
                            </swiper>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import data from '../data/brandLogo.json';
export default {
  data () {
    return {
      data,
      swiperOption: {
        loop: true,
        speed: 1000,
        spaceBetween: 60,
        slidesPerView: 4,
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
    }
  }
};
</script>

<style lang="scss" scoped>
.swiper-wrapper .swiper-slide {
  height: auto !important;
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 128px;
  max-height: 90px;
}
 
</style>
