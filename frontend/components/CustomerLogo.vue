<template>
  <img
    v-if="customer && customer.logo"
    :src="getStrapiMedia(url)"
    :alt="customer.name"
    :class="addClass"
  />
 
</template>

<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  props: {
    customer: {
      type: Object,
      default() {
        return {};
      },
    },
    addClass: {
      type: String,
      default: "customer-logo-min",
    },
  },
  computed:{
      url(){
        if(this.customer.logo.formats) return this.customer.logo.formats.thumbnail.url
        else return this.customer.logo.url
      }
  },
  methods: {
    getStrapiMedia,
  },
};
</script>

<style lang="scss">
.customer-logo-min {
  max-height: 100px;
  max-width: 100px;
}
.customer-logo-medium {
  max-height: 90px;
  max-width: 140px;
}
</style>
