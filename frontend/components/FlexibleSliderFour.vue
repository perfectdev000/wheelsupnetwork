<template>
  <div class="flexableimage__wrapper">
    <swiper :options="swiperOption">
    <div v-for="slide in sliders" :key="slide.id" class="swiper-slide">
      <div class="flexale-image">
        <div class="thumb">
          <img
            :src="getStrapiMedia(slide.url)"
            :alt="slide.name"
            />
        </div>
      </div>
    </div>
    </swiper>

    <button class="swiper-btn swiper-btn-prev">
      <i class="fas fa-angle-left"></i>
    </button>
    <button class="swiper-btn swiper-btn-next">
      <i class="fas fa-angle-right"></i>
    </button>
  </div>
</template>

<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  props: {
    sliders: {
      type: Array,
      default: () => [],
    },
  },
  data () {
    return {
      swiperOption: {
        speed: 1500,
        slidesPerView: 1,
        spaceBetween: 60,
        // loop: true,
        centeredSlides: true,
        autoplay: true,
        navigation: {
          nextEl: '.swiper-btn-next',
          prevEl: '.swiper-btn-prev'
        },
        // Responsive breakpoints
        breakpoints: {
          992:{
            slidesPerView: 2,
            centeredSlides: true,
          },

          768:{
            centeredSlides: false,
          },

          576:{
            slidesPerView : 2,
            centeredSlides: false,
          },
          300:{
            slidesPerView : 1,
            centeredSlides: false,
          }
        }
      },
    }
  },
  methods: {
    getStrapiMedia,
  },

};
</script>
