<template>
  <div class="post-nav-lisnt mb--45 wow move-up">
    <div class="nav-item previous">
      <a @click="handlePaginate(false)" class="" v-if="buttonPrevious">
        <div class="link-text">
          <span class="fa fa-arrow-left"></span>
          <p>{{ $t("previous") }}</p>
        </div>
      </a>
    </div>
    <div class="nav-item next mt_sm--30" v-if="buttonNext">
      <a @click="handlePaginate(true)" class="">
        <div class="link-text">
          <p>{{ $t("next") }}</p>
          <span class="fa fa-arrow-right"></span>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
import qs from "qs";

export default {
  props: {
    article: {
      type: Object,
      require: true,
    },
    categorySlug: {
      type: String,
    },
  },
  data() {
    return {
      dateCurrency: new Date().toISOString(),
      buttonNext: true,
      buttonPrevious: true,
    };
  },
  methods: {
    _queryNextArticle() {
      return this.$strapi.find(
        this.categorySlug,
        qs.stringify({
          _limit: 1,
          "sites.uid": this.$store.state.site._data.uid,
           status: "published",
          _sort: "id:desc,publishedDate:desc",
           publishedDate_lte: this.article.publishedDate,
           id_lt: this.article.id,
          _where: {
            _or: [
                { expiration_date_gte: this.dateCurrency },
                { expiration_date_null: true },
            ],
          },
        })
      );
    },
    _queryPreviousArticle() {
      return this.$strapi.find(
        this.categorySlug,
        qs.stringify({
          _limit: 1,
          _sort: "id:asc,publishedDate:asc",
          id_ne: this.article.id,
          publishedDate_gte: this.article.publishedDate,
          id_gt: this.article.id,
          "sites.uid": this.$store.state.site._data.uid,
          status: "published",
          _where: {
            _or: [
              { expiration_date_gte: this.dateCurrency },
              { expiration_date_null: true },
            ],
          },
        })
      );
    },
    _queryPreviousDestinations() {
      return this.$strapi.find(
        this.categorySlug,
        qs.stringify({
          _limit: 1,
          _sort: "id:asc,published_date:asc",
          id_ne: this.article.id,
          published_date_gte: this.article.published_date,
          id_gt: this.article.id,
          "sites.uid": this.$store.state.site._data.uid,
          status: "published",
          _where: {
            _or: [
              { expiration_date_gte: this.dateCurrency },
              { expiration_date_null: true },
            ],
          },
        })
      );
    },
    _queryNextDestinations() { 
      return this.$strapi.find(
        this.categorySlug,
        qs.stringify({
          _limit: 1,
          _sort: "id:desc,published_date:desc",
          id_ne: this.article.id,
          published_date_lte: this.article.published_date,
          id_lt: this.article.id,
          "sites.uid": this.$store.state.site._data.uid,
          status: "published",
          _where: {
            _or: [
              { expiration_date_gte: this.dateCurrency },
              { expiration_date_null: true },
            ],
          },
        })
      );
    },
    _queryCustomerNext() {

      let published_date = this.article.vip ? undefined : this.article.published_date 
      
      return this.$strapi.find(this.categorySlug, qs.stringify({
        _limit: 1,
        _sort: "published_date:asc",
         published_date_gte: published_date,
         id_ne:this.article.id,
        "sites.uid": this.$store.state.site._data.uid,
        status: "published",
        featured: true,
        _where: {
          _or: [
            { expiration_date_gte: this.dateCurrency },
            { expiration_date_null: true },
          ],
        },
      }));
    },
    disabledButtons(action, articles) {
      if (action) this.buttonNext = articles ? true : false;
      else this.buttonPrevious = articles ? true : false;
    },
    async handlePaginate(action) {
      const articles = await this.ToCallQuery(action);
      this.disabledButtons(action, articles.length);

      if (articles.length) {
        this.scrollTop();
        const tmp = articles[0];
        let path = this.$nuxt.$route.path;
        const tmpSlug = tmp.slug ? tmp.slug : tmp.id;
        const articleSlug = this.article.slug
          ? this.article.slug
          : this.article.id;
        path = path.replace(articleSlug, tmpSlug);
        this.$router.replace(`${path}`);
      }
    },
    async ToCallQuery(action) {
      if (!action && this.categorySlug == "destinations")
        return this._queryPreviousDestinations();
      else if(action && this.categorySlug == "destinations")
        return this._queryNextDestinations();
      else if (action && this.categorySlug == "customers")
        return this._queryCustomerNext();
      else if (!action && this.categorySlug == "customers")
        return this._queryCustomerNext();
      else if (action) return await this._queryNextArticle();
      else return await this._queryPreviousArticle();
    },
    scrollTop() {
      window.scrollTo({
        left: 0,
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>

<style></style>
