<template>
  <img :class="[isLogo ?'img-logo' : 'img-card']" :alt="alt" :src="getStrapiMedia(alt)" />
</template>

<script>
 import { getStrapiMedia } from "../utils/medias";

export default {
  props: {
    isLogo:{
      required:false,
      type: Boolean,
      default:true
    },
    alt: {
      required: true,
    },
  },
  methods:{
    getStrapiMedia
  }
};
</script>

<style lang="scss" scoped>
     .img-logo  {
        width: 100px;
        height: 60px;
        display:block;
        margin:auto;
      }
      .img-card  {
        max-height: 300px;
        max-width: 180px;
        display:block;
        margin:auto;
      }
      
 
</style>
