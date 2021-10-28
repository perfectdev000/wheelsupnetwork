<template>
  <h2 class="pt--50 whelesup-light-blue">
    <n-link
      :to="path"
      :class="[
        $config.siteUid == 'wheels-up-network-canada' ||
        $config.siteUid == 'wheels-up-network-usa'
          ? 'wheels-color'
          : 'latam-color',
      ]"
    >
      <span class="category">{{ crumb }} {{ slag ? "/" : "" }}  </span>
    </n-link>
    {{ title }}  
  </h2>
</template>

<script>
export default {
  props: {
    crumb: {
      type: String,
    },
    path: {
      type: String,
    },
    title: {
      type: String,
      required: false,
      default: "",
    },
    slag: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>

.wheels-color {
  color: #08a6ca !important;
}
.latam-color {
  color: #cc5d34 !important;
}
</style>
