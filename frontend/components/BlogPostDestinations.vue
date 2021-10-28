<template>
  <div class="blog-grid blog-standard" :class="addClass">
    <div class="post-thumb">
      <n-link
        :to="`${categorySlug}/${
          item.id
        }`"
      >
      <img
        class="blog__post--img"
        :src="item.logo ? getStrapiMedia(item.logo.url) : '/img/service/service-3/service-1.jpg'"
        :alt="item.title"
      />
      </n-link>
    </div>
  </div>
</template>

<script>
import { getStrapiMedia } from "../utils/medias";

export default {
  props: {
    item: {
      type: Object,
      default() {
        return {};
      },
    },
    categorySlug: {
      type: String,
      default: "",
      required:false
    },
    addClass: {
      type: String,
      default: "",
      required: false,
    },
    readMoreButton: Boolean,
  },
  methods: {
    getStrapiMedia,
  },
};
</script>

<style lang="scss" scoped>
.blog__post--img {
  height: 250px;
}
.blog-grid--modern.blog-standard {
  min-height: 200px;
}

.heading {
  margin-top: 9px;
}
 
</style>
