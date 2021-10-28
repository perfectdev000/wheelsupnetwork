<template>
  <!-- <p class="bk_pra" v-html="formattingContent | marked"></p> -->
  <p
    :class="[
      'bk_pra mb-2',
      $config.siteUid == 'wheels-up-network-usa' ||
      $config.siteUid == 'wheels-up-network-canada'
        ? 'content-wheel'
        : 'content-latam',
    ]"
    v-html="markedown"
  ></p>
</template>

<script>
// import marked from "marked";
export default {
  props: {
    content: {
      required: true,
      type: String,
    },
  },
  computed: {
    markedown() {
      let value = this.content.replace( new RegExp('<oembed', 'g'), '<iframe')
      value =  value.replace(new RegExp('</oembed>','g'), '</iframe>')
      value =  value.replace(new RegExp('<a','g'), "<a target='_blank' ")
      value =  value.replace(new RegExp('url', 'g'), ` width="700" height="400"" src`)
      return this.$md.render(value)
    },
     
  },
};
</script>
<style lang="postcss">
 .image , .aligncenter{
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>