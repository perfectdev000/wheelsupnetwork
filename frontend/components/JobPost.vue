<template>
  <div class="blog-grid blog-standard" :class="addClass">
    <div class="post-content">
      <div class="post-inner">
        <h3>
          <n-link
            class="btn-link"
            :to="`${localePath({ name: 'empleos' })}/${job.slug}`"
            >{{ job.name }}</n-link
          >
        </h3>
        <div class="wrap">
          <div class="event-excerpt">
            <p>
              <strong>{{ job.company }}</strong> &nbsp; | &nbsp;
              <small>{{ job.city }}</small>
            </p>
          </div>
        </div>
        <n-link
          class="btn-link btn btn-primary text-white"
          :to="`${localePath({ name: 'empleos' })}/${job.slug}`"
        >
          {{ $t("moreinfojobs") }}</n-link
        >
        <a
          class="btn-link btn btn-outline-primary outline"
          :href="job.link"
          target="_blank"
        >
          {{ $t("gotooffer") }} </a
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    job: {
      type: Object,
      default() {
        return {};
      },
    },
    addClass: {
      type: String,
      default: "",
    },
  },
};
</script>

<style lang="scss" scoped>
.post-content {
  padding: 1rem !important;
}
a:hover {
  text-decoration: none;
}
a.outline:hover {
  color: white !important;
}
</style>
