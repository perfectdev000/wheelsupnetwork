<template>
  <div class="bk-blog-grid-area pt--100 pb--100 pt_md--80 pb_md--80 pb_sm--80 pt_sm--60 bg_color--5">
    <div class="container">
      <div class="row mtn--50">
        <div
          v-for="article in articles"
          :key="article.title"
          class="col-xl-3 col-md-4 col-sm-6 move-up wow mt--100">
          <BlogPostThree
            :article="article"
            add-class="blog-standard blog-grid--modern"
            read-more-button="true"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    BlogPostThree: () => import('@/components/BlogPostThree'),
  },
  async asyncData({ $strapi, $config: { siteUid } }) {
    return {
      articles: await $strapi.find("articles", {
        _limit: 6,
        _sort: "publishedDate:desc",
        'sites.uid': siteUid
      }),
      site: await $strapi.find("sites", {
        uid: siteUid
      }),
      // homepage: await $strapi.find("homepage"),
      // global: await $strapi.find("global"),
    };
  },
  data() {
    return {}
  }
};
</script>
