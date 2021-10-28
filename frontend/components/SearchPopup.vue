<template>
  <div id="search-popup" class="brook-search-popup popup-mobile-menu">
    <div
      class="search-overlay"
      @click="toggleClass('removeClass', 'search-popup-open')"
    />
    <div class="inner">
      <div class="search-header">
        <div class="logo">
          <n-link to="/">
            <img :src="$store.state.site.pathLogo" alt="Wheelsup Agentes" />
          </n-link>
        </div>
        <a
          id="search-close-trigger"
          href="javascript:void(0)"
          class="search-close"
          @click="toggleClass('removeClass', 'search-popup-open')"
        />
      </div>
      <div class="search-content">
        <form>
          <label>
            <input
              v-model="query"
              type="search"
              :placeholder="$t('search')"
            />
          </label>

          <button class="search-submit"  @click.prevent="onSearch">
            <i class="fa fa-search" />
          </button>
        </form>
      </div>
 
      <div class="search-results">
        <ul>
          <li
            v-for="(record, i) in results"
            :key="i"
            style="padding: 0 0 10px 20px"
          >
     
            <a href="#" @click.prevent="goTo(record.slug)">{{
              record.title
            }}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>

import qs from "qs";

export default {
  data() {
    return {
      query: "",
      results: [],
      date: new Date().toISOString()
    };
  },
  methods: {
    // offcanvas search close
    toggleClass(addRemoveClass, className) {
      const el = document.querySelector("#search-popup");
      if (addRemoveClass === "addClass") {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },
    async onSearch() {
      this.$nuxt.$loading.start();
      const { results } = await this.$strapi.find("search", 
        qs.stringify({
          _q: this.query,
          status: "published",
          "sites.uid": this.$config.siteUid,
          _sort: "publishedDate:desc",
          publishedDate_lte: this.date,
          _where: {
              _or: [
                { expiration_date_gte: this.date  },
                { expiration_date_null: true },
              ],
            },
        })
      );
      this.$nuxt.$loading.finish();
      this.results = results;
    },
    goTo(slug) {
      this.$nuxt.$router.push(`/news/${slug}`);
    },
  },
};
</script>

<style lang="scss" scoped>
.search-results a {
  color: white;
}
</style>
