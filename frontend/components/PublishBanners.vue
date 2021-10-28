<template>
  <div class="container-fluid p-0">
    <div class="row no-gutters">
      <div class="col-12">
        <h2 class="mb--30 mt--30 text-center">{{ title }}</h2>
        <div class="brook-element-carousel swiper-custom-arrow swiper-arrow-hover">
          <swiper :options="swiperOption">
            <div
              v-for="teamMember in data.teamMembers.slice(4, 7)"
              :key="teamMember.id "
              class="swiper-slide"
            >
              <TeamMemberThree :teamMember="teamMember" />
            </div>
          </swiper>

          <!-- slider arrow navigation -->
          <button class="swiper-btn swiper-btn-prev">
            <i class="ion ion-ios-arrow-back"></i>
          </button>
          <button class="swiper-btn swiper-btn-next">
            <i class="ion ion-ios-arrow-forward"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import data from '../data/team.json';
export default {
  components: {
    TeamMemberThree: () => import('../components/TeamMemberThree'),
  },
  props: {
    title: {
      type: String,
      default: "",
    }
  },
  data () {
    return {
      data,
      swiperOption: {
        spaceBetween: 60,
        loop: true,
        speed: 1000,
        navigation: {
          nextEl: '.swiper-btn-next',
          prevEl: '.swiper-btn-prev'
        },
        // Responsive breakpoints
        breakpoints: {
          1499:{
              slidesPerView : 5
          },

          768:{
              slidesPerView : 3

          },

          480:{
              slidesPerView : 2
          }
        }
      }
    }
  }
};
</script>

