<template>
  <div class="bk-accordion-area ptb--150 ptb-md--80 ptb-sm--60 bg_color--1">
    <div class="container">
      <div class="row">
        <!-- Start Single Accordion -->
        <div class="col-md-12">
          <div class="brook-section-title mb--50 mb_sm--20 mb_md--20">
            <h3 class="heading heading-h3">{{ $t("whatarecookies") }}</h3>
          </div>
          <div class="brook-section-title mb--50 mb_sm--20 mb_md--20">
            <h4 class="heading heading-h4">
              {{ $t("footertitlecookie") }}
            </h4>
          </div>
          <div class="content mt--30 mb--50 mb__sm--20 mb_md--20">
            <div class="bkseparator--20"></div>
            <div v-html="$t('bodycookies')"></div>
          </div>
          <div class="content mt--30 mb--10 mb__sm--10 mb_md--10">
            <div class="bkseparator--20"></div>
            <div v-html="$t('cookieweuse')"></div>
          </div>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-1 block class="acc-btn">
                  {{ $t("cookiestechnical") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-1" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("cookiestechnicalbody") }}
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>

            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-2 block class="acc-btn">
                  {{ $t("customizationcookies") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-2" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    <div v-html="$t('customizationcookiesbody')"></div>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>

            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-3 block class="acc-btn">
                  {{ $t("Cookies Analysis") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-3" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    <div v-html="$t('cookiesanalysisbody')"></div>
                  </b-card-text>
                  <div
                    class="
                      view-more-btn
                      heding-color
                      heading-font
                      font-18 font-700
                      theme-color
                      wow
                      move-up
                    "
                  >
                    <a
                      target="_blank"
                      href="https://support.google.com/analytics/answer/6004245"
                    >
                      <span>Google analytics</span>
                      <span class="btn-arrow"></span>
                    </a>
                  </div>
                  <div
                    class="
                      view-more-btn
                      heding-color
                      heading-font
                      font-18 font-700
                      theme-color
                      wow
                      move-up
                    "
                  >
                    <a
                      target="_blank"
                      href="http://www.google.com/intl/es/policies/privacy/"
                    >
                      <span>Google policies privacy</span>
                      <span class="btn-arrow"></span>
                    </a>
                  </div>
                </b-card-body>
              </b-collapse>
            </b-card>
            <p class="bk_pra wow move-up mt--20 mb--10">
              <div v-html="$t('disablecookies')"></div>
            </p>
            <div class="plans-about">
              <div class="bk-list--2 mt--25 move-up wow">
                <div class="list-header with-ckeck">
                  <div class="marker"></div>
                  <div class="title-wrap">
                    <h6 class="heading heading-h5">
                      {{ $t('disable_des_one') }}
                    </h6>
                  </div>
                </div>
                <div class="list-header with-ckeck">
                  <div class="marker"></div>
                  <div class="title-wrap">
                    <h6 class="heading heading-h5">
                      {{ $t('disable_des_two')}}
                    </h6>
                  </div>
                </div>
                <div class="list-header with-ckeck">
                  <div class="marker"></div>
                  <div class="title-wrap">
                    <h6 class="heading heading-h5">
                        {{ $t('disable_des_three')}}
                    </h6>
                  </div>
                </div>
                <div class="list-header with-ckeck">
                  <div class="marker"></div>
                  <div class="title-wrap">
                    <h6 class="heading heading-h5">
                       {{ $t('disable_des_four') }}
                    </h6>
                  </div>
                </div>
              </div>
            </div>

            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-4 block class="acc-btn mt--20">
                  {{ $t('publicitycookies')}}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-4" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                      <div v-html="$t('publicitycookiesbody')"></div>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <div class="list-header with-ckeck">
              <div class="marker"></div>
              <div class="title-wrap">
                <h6 class="heading heading-h5">
                  DoubleClick Y GOOGLE ADWORDS – Google, Inc.,
                </h6>
                <br />
                <p class="bk_pra wow move-up" v-html="$t('infocookies')">
                 
                </p>
              </div>
            </div>
              <div v-html="$t('preefootercookies')"></div>
            <div
              class="
                view-more-btn
                heding-color
                heading-font
                font-18 font-400
                theme-color
                wow
                move-up
                mt--20
                pt--20
              "
            >
              <a target="_blank"
                href="http://support.google.com/chrome/bin/answer.py?hl=es&answer=95647"
              >
                <span>Cookies {{ $t('for') }} Google</span>
                <span class="btn-arrow"></span>
              </a>
            </div>
            <div
              class="
                view-more-btn
                heding-color
                heading-font
                font-18 font-400
                theme-color
                wow
                move-up
                mt--20
                pt--20
              "
            >
               <a target="_blank"
                 href="http://windows.microsoft.com/es-es/windows-vista/block-or-allow-cookies"
              >
                <span>Cookies {{ $t('for') }} Explorer</span>
                <span class="btn-arrow"></span>
              </a>
            </div>
            <div
              class="
                view-more-btn
                heding-color
                heading-font
                font-18 font-400
                theme-color
                wow
                move-up
                mt--20
                pt--20
              "
            >
              <a target="_blank"
                 href="http://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-que-los-sitios-we"
              >
                <span>Cookies {{ $t('for') }} Firefox</span>
                <span class="btn-arrow"></span>
              </a>
            </div>
            <div
              class="
                view-more-btn
                heding-color
                heading-font
                font-18 font-400
                theme-color
                wow
                move-up
                mt--20
                pt--20
              "
            >
               <a target="_black"  href="https://support.apple.com/kb/index?q=manage+cookies&src=globalnav_support&type=organic&page=search&locale=es_ES">
                <span>Cookies {{ $t('for') }} Safari</span>
                <span class="btn-arrow"></span>
              </a>
            </div>
            <p class="bk_pra wow move-up mt--30 mb--20 " v-html="$t('footercookies')">
            </p>
          </div>
        </div>
        <!-- End Single Accordion -->
      </div>
    </div>
  </div>
</template>
