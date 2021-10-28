<template>
  <div class="main-container">
    <HeaderElement />
    <OffCanvasMobileMenu />
    <SearchPopup />
    <CardImage/> 
    <BannersPublicity />
      <nuxt keep-alive />
    <FooterTwo />
  </div>
</template>

<script>
export default {
  components: {
    HeaderElement: () => import("~/components/HeaderElement"),
    OffCanvasMobileMenu: () => import("~/components/OffCanvasMobileMenu"),
    SearchPopup: () => import("~/components/SearchPopup"),
    BannersPublicity: () => import("~/components/BannersPublicity"),
    FooterTwo: () => import("~/components/FooterTwo"),
    CardImage: () => import("~/components/CardImage"),
  },
};
</script>
