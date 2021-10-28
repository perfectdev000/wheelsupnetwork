<template>
  <div>
    <div v-show="banners" class="mb--20">
      <a target="_black" :href="slug">
        <img
          :src="path ? getStrapiMedia(path) : ''"
          alt="Wheelsupnetwork"
          class="banners mt-5 mb-2"
        />
      </a>
    </div>
  </div>
</template>
<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  data() {
    return {
      banners: false,
      path: "",
      slug: "",
    };
  },
  methods: {
    getStrapiMedia,
    setBanners() {
      let value =
        this.banners.length != 0
          ? Math.round(
              Math.floor(Math.random() * (this.banners.length - 0)) + 0
            )
          : 0;

      this.path = this.banners[value].image.url;
      this.slug = this.banners[value].slug;

      if (this.banners.length > 1) this.callback();
    },
    callback() {
      setTimeout(
        function () {
          this.setBanners();
        }.bind(this),
        3000
      );
    },
    filterBannersPublishedTrue(banners){
      const  banner = banners.filter(banner => banner.published)
      if(banner.length){
        this.banners =  banner 
        this.setBanners()
      }  
    }  
  },
  async created() {
    const site = await this.$strapi.find("banner-ads", {
      "sites.uid": this.$config.siteUid,
    });

    if (!site.length)
        return false
    else if (site[0].banners.length != 0)
        this.filterBannersPublishedTrue(site[0].banners)
  },
};
</script>
<style lang="scss" scoped>
.banners {
  display: block;
  margin: auto;
  padding: auto;
  min-height: auto;
  height: 110px;
  width: 1115px;
  min-width: auto;
}
</style>
