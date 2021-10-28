<template>
  <fixed-header>
    <header
      class="
        br_header
        header-default header__bg--color-1
        light-logo--version
        haeder-fixed-width
        headroom--sticky
        header-mega-menu
        clearfix
      "
    >
    
      <TopHeader />
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="row header__wrapper mr--0">
              <div class="col-md-2 px-0">
                <div class="header-left flex-20" v-if="!$fetchState.pending">
                  <div class="logo">
                    <n-link to="/">
                      <img
                        :src="site ? getStrapiMedia(url) : '' "
                        alt="Wheelsupnetwork"
                      />  
                    </n-link>
                  </div>
                </div>
              </div>
              <div class="col-md-9 px-0">
                <div class="mainmenu-wrapper d-none d-xl-block">
                  <NavigationBlack />
                </div>
              </div>
              <div class="col-md-1 px-0">
                <div class="header-right">
                  <div class="popup-search-wrap">
                    <a
                      class="btn-search-click"
                      href="javascript:void(0)"
                      @click="toggleClass('addClass', 'search-popup-open')"
                    >
                      <i class="fa fa-search" />
                    </a>
                  </div>

                  <div
                    class="
                      manu-hamber
                      popup-mobile-click
                      d-block
                      dark-version
                      d-block d-xl-none
                    "
                    @click="mobiletoggleClass('addClass', 'show-mobile-menu')"
                  >
                    <div>
                      <i />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  </fixed-header>
</template>

<script>
import FixedHeader from "vue-fixed-header";
import { getStrapiMedia } from "../utils/medias";
export default {
  components: {
    NavigationBlack: () => import("@/components/NavigationBlack"),
    TopHeader: () => import("@/components/TopHeader"),
    FixedHeader,
  },
  data() {
    return {
      site: [],
      url:''
    };
  },

  async fetch() {
    
    const site = await this.$strapi.find("sites", {
      uid: this.$config.siteUid,
    });
    this.site = site[0];
    this.url = this.site.defaultSeo.shareImage.url 
    this.$store.commit('site/fetch', this.site )
    this.$store.commit('site/urlLogo', this.getStrapiMedia(this.url))
  },
  methods: {
    getStrapiMedia,
    toggleClass(addRemoveClass, className) {
      const el = document.querySelector("#search-popup");
      if (addRemoveClass === "addClass") {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },

    mobiletoggleClass(addRemoveClass, className) {
      const el = document.querySelector("#offcanvas-menu");
      if (addRemoveClass === "addClass") {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.vue-fixed-header--isFixed {
  top: 0;
  left: 0;
  width: 100vw;
  z-index: 999;
  position: fixed !important;
  /* background-color: rgba($black, 0.9); */
  background: #fff;
  box-shadow: 0 0 8px 1px rgba(0, 0, 0, 0.2);
  animation: 900ms cubic-bezier(0.2, 1, 0.22, 1) 0s normal none 1 running
    fadeInDown;
}
.header__bg--color-1 {
  /* background: #003c71; */
  background: #fff;
}
.btn-search-click i {
  color: #262626;
}
</style>
