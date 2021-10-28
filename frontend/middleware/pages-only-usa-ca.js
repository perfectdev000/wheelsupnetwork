export default function ({ route, $config }) {
  if (!$config.showFams && route.path === "/fams") {
    //redirect
    window.onNuxtReady(() => {
      window.$nuxt.$router.push("/");
    });
  }
  if (!$config.showEvergreen && route.path === "/evergreen") {
    //redirect
    window.onNuxtReady(() => {
      window.$nuxt.$router.push("/");
    });
  }
}
