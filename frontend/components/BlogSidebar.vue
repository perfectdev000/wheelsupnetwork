<template>
  <div class="blog-sidebar-container">
    <div class="blog-sidebar-wrapper">
      <!-- <div class="bl-sidebar search">
        <h5 class="widget-title">Buscar</h5>
        <form class="inner">
          <div class="search-box">
            <input type="text" placeholder="Buscar una Palabra…">
            <button><span class="fa fa-search"></span></button>
          </div>
        </form>
      </div> -->

      <div class="bl-sidebar category wow move-up">
        <h5 class="widget-title">Categorias</h5>
        <div class="inner">
          <ul class="category-list">
            <li v-for="category in categories" :key="category.id">
              <n-link :to="`/${category.slug}`">{{ category.name }}</n-link>
            </li>
          </ul>
        </div>
      </div>

      <!-- <div class="bl-sidebar archive mt--50 wow move-up">
        <h5 class="widget-title">Archivos</h5>
        <div class="inner">
          <select>
            <option>Select Month</option>
            <option>June 2021 </option>
            <option>May 2021 </option>
            <option>April 2021 </option>
            <option> March 2021 </option>
            <option> February 2021 </option>
            <option> January 2021 </option>
          </select>
        </div>
      </div> -->

      <!-- <div class="bl-sidebar tag mt--50 wow move-up">
        <h5 class="widget-title">Tags</h5>
        <div class="inner">
          <ul class="tagcloud">
            <li v-for="category in categories" :key="category.slug">
              <n-link :to="`/${category.slug}`">{{ category.name }}</n-link>
            </li>
          </ul>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
import data from '../data/blog.json';

export default {

  async fetch() {
    const categories = await this.$strapi.find("categories");
    console.log('categories', categories);
    this.categories = categories;
  },

  data () {
    return {
      data,
      categories: []
    }
  }
};
</script>
