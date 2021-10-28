<template>
  <div class="container-fluid p-0 bg-top-header">
    <div class="row">
      <div class="col-12 text-center">
        <p class="slogan w-100 text-center m-0">
          <span>{{ $t("topHeader") }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .slogan {
    padding-top: 10px;
    padding-bottom: 10px;
  }
  .slogan > span {
    /* color: #f1592a; */
    /* color: #f4792b; */
    color: #fff;
    font-weight: bold;
  }
  .bg-top-header {
    /* background-color: #003c71; */
    background-color: #00aeef;
  }
</style>

