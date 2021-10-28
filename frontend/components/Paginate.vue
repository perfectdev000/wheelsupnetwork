<template>
  <paginate
    v-if="pageCount > 1"
    :page-count="pageCount"
    :click-handler="clickHandler"
    :page-range="3"
    :margin-pages="2"
    :prev-text="'Prev'"
    :next-text="'Next'"
    :container-class="'brook-pagination'"
    :page-class="'page-item'"
  />
</template>

<script>
export default {
  props: {
    pageCount: {
      type: Number,
      default: 0,
    },
    clickHandler: {
      type: Function,
      default: () => {

      }
    },
  },
}
</script>
