<template>
  <div
    class="breadcrumb-area pt--400 pt_lg--300 pt_md--250 pt_sm--200 pb--100 bg_image--8 breadcrumb-title-bar breadcrumb-title-white"
    :style="{ backgroundImage: `url('/img/bg/image-1920x600.jpg')` }"
  >
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="breadcrumb-inner text-center">
            <h2 class="heading">
              {{ title }}
            </h2>
            <div class="breadcrumb-insite">
              <b-breadcrumb class="core-breadcrumb" :items="items" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default() {
        return [];
      },
    },
    title: {
      type: String,
      default: "",
    },
  },
};
</script>
