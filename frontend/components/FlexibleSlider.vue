<template>
  <div class="flexale-image bg_color--1" :class="addClass">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="brook-element-carousel flexable-arrow flexable-dots">
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
          </div>
        </div>
      </div>
    </div>
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
    addClass: String
  },

  data () {
    return {
      swiperOption: {
        speed: 1500,
        slidesPerView: 1,
        spaceBetween: 60,
        centeredSlides: false,
        autoplay: {
          delay: 3000,
        },
        breakpoints: {
          992:{
            slidesPerView: 2,
            centeredSlides: false,
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
      }
    }
  },
  methods: {
    getStrapiMedia,
  },
};
</script>
