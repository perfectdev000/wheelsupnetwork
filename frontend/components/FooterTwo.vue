<template>
  <div>
    <CallToAction />
    <PreFooter />
    <footer
      class="
        page-footer
        bg_color--footer
        pl--150
        pr--150
        pl_lg--30
        pr_lg--30
        pl_md--30
        pr_md--30
        pl_sm--5
        pr_sm--5
      "
    >
      <div class="bk-footer-inner pt--100 pb--30 pt_sm--100">
        <div class="container">
          <div class="row">
            <div class="col-lg-4 col-sm-8 mt_mobile--40">
              <div class="footer-widget text-var--2 menu--about">
                <h2 class="widgettitle">{{ $t("information") }}</h2>
                <div class="footer-menu">
                  <ul class="ft-menu-list bk-hover">
                    <li>
                      <n-link to="/about-us">
                        {{ $t("about") }} {{ $t("site") }}</n-link
                      >
                    </li>
                    <li>
                      <n-link
                        :to="localePath({ name: 'politica-de-privacidad' })"
                      >
                        {{ $t("privacy") }}
                      </n-link>
                    </li>
                    <li>
                      <n-link :to="localePath({ name: 'politica-de-cookies' })">
                        {{ $t("cookie") }}
                      </n-link>
                    </li>
                    <li>
                      <n-link :to="localePath({ name: 'nota-legal' })">
                        {{ $t("legalnote") }}
                      </n-link>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-sm-8 mt_md--40 mt_sm--40">
              <div class="footer-widget text-var--2 menu--contact">
                <h2 class="widgettitle">{{ $t("contact") }}</h2>
                <div class="footer-address">
                  <div class="bk-hover">
                    <p>
                      <a
                        class="text-white"
                        href="mailto:hola@SoloParaAgentes.com"
                        ><i class="fas fa-envelope mr-2"></i>
                        {{ $t("addresesemail") }}
                      </a>
                    </p>
                    <p>
                      <!-- <a class="text-white" href="tel:0123456789"><i class="fas fa-phone mr-2" />0123456789</a> -->
                    </p>
                  </div>
                  <div class="social-share social--transparent text-white mt-2">
                    <a
                      class="text-white"
                      :href="$t('facebook')"
                      target="_blank"
                      rel="nofollow"
                    >
                      <i class="fab fa-facebook" />
                    </a>
                    <a
                      class="text-white"
                      :href="$t('twitter')"
                      target="_blank"
                      rel="nofollow"
                    >
                      <i class="fab fa-twitter" />
                    </a>
                    <a
                      class="text-white"
                      :href="$t('linkedin')"
                      target="_blank"
                      rel="nofollow"
                    >
                      <i class="fab fa-linkedin" />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Start Footer Top Area -->
      <cookie-law
        :buttonText="$t('buttonTextCookie')"
         buttonClass="btn btn-primary text-white"
        :buttonLink="localePath({ name: 'politica-de-cookies' })"
        :buttonLinkText="$t('moreinfocookies')"
      >
        <div slot="message" class="text-black">
          <p>
              {{ $t("cookie_body") }}
          </p>
        </div>
      </cookie-law>
      <!-- Start Copyright Area -->
      <div class="copyright ptb--30 text-var-2">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-md-7">
              <div class="copyright-left text-md-left text-center">
                <ul
                  class="
                    bk-copyright-menu
                    d-flex
                    bk-hover
                    justify-content-center justify-content-md-start
                    flex-wrap flex-sm-nowrap
                  "
                >
                  <li>
                    <n-link to="/contact"> {{ $t("contact_us") }} </n-link>
                  </li>
                  <li>
                    <n-link to="/news"> {{ $t("new") }} </n-link>
                  </li>
                  <li>
                    <n-link :to="localePath({ name: 'empleos' })">
                      {{ $t("jobs") }}
                    </n-link>
                  </li>
                  <li>
                    <n-link
                      :to="
                        localePath({ name: 'suscribete-a-nuestra-newsletter' })
                      "
                    >
                      Newsletters
                    </n-link>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-md-5">
              <div class="copyright-right text-md-right text-center">
                <p>
                  &copy; 2021 Made with
                  <i class="fa fa-heart text-danger" /> by
                  <a href="#"><b>josesalinero.es</b></a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import CookieLaw from "vue-cookie-law";
export default {
  components: {
    PreFooter: () => import("@/components/PreFooter"),
    CallToAction: () => import("@/components/CallToAction"),
    CookieLaw,
  },
};
</script>
<style lang="scss" scoped>
.bg_color--footer {
  background-color: $color-3;
}
.text__color {
  h1 {
    color: $color-3;
    padding-left: 33px;
  }
}
</style>
