<template>
  <div id="offcanvas-menu" class="popup-mobile-menu popup-mobile-visiable">
    <div
      class="mobile-menu-overlay"
      @click="mobiletoggleClass('removeClass', 'show-mobile-menu')"
    />
    <div class="inner">
      <div class="mobileheader">
        <div class="logo">
          <n-link to="/">
            <img  :src="$store.state.site.pathLogo" alt="Wheelsup Agentes" />
          </n-link>
        </div>
        <a
          class="mobile-close"
          href="javascript:void(0)"
          @click="mobiletoggleClass('removeClass', 'show-mobile-menu')"
        />
      </div>
      <div class="menu-content">
        <MobileNavigation />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    MobileNavigation: () => import("@/components/MobileNavigation"),
  },
  methods: {
    // offcanvas menu close
    mobiletoggleClass(addRemoveClass, className) {
      const el = document.querySelector("#offcanvas-menu");
      if (addRemoveClass === "addClass") {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },
  },
};
</script>
