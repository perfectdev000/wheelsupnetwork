<template>
  <div class="bk-accordion-area ptb--100 ptb-md--80 ptb-sm--60 bg_color--1">
    <div class="container">
      <div class="row">
        <!-- Start Single Accordion -->
        <div class="col-md-12">
          <div class="brook-section-title mb--10 mb_sm--20 mb_md--20">
            <h4 class="heading heading-h4">{{ $t("titlelegal") }}</h4>
          </div>
          <div class="content mt--10 mb--10 mb__sm--20 mb_md--20">
            <div class="bkseparator--20"></div>
            <p class="bk_pra wow move-up">
              {{ $t("bodylegal") }} <br />
              <br />
            </p>
          </div>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-1 block class="acc-btn">
                  {{ $t("title_legal_one") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-1" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("header_body_legal_one") }}
                    <br />
                    <br />
                    <div
                      class="plans-about"
                      v-html="$t('body_legal_one')"
                    ></div>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <p class="bk_pra wow move-up">{{ $t("footer_body_legal_one") }}</p>
            <br />
            <div class="plans-about">
              <div class="bk-list--2 move-up wow">
                <div class="list-header with-ckeck">
                  <div class="marker"></div>
                  <div class="title-wrap">
                    <p class="heading heading-h5">
                      <strong>Email:</strong>
                      <a style="color: black" :href="$t('addresesemail')"
                        >{{ $t("addresesemail") }}
                      </a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <h6 class="heading heading-5 theme-color pt--30 pb--10"></h6>
          <p class="bk_pra wow move-up" v-html="$t('body_legal_two')">
            <br />
            <br />
          </p>
          <h5 class="heading heading-5 theme-color pt--30 pb--10">
            {{ $t("termsofuse") }}
          </h5>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-2 block class="acc-btn">
                  {{ $t("introductionto") }} {{ $t("addresesemail") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-2" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    <div v-html="$t('introductionto_body')"></div>
                    <br />
                    <br />
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-2 block class="acc-btn">
                  {{ $t("obligationsuser") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-2" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("header_body_obligationsuser") }} <br />
                    <br />
                  </b-card-text>
                  <div
                    class="plans-about"
                    v-html="$t('obligationsuser_body')"
                  ></div>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-3 block class="acc-btn">
                  {{ $t("exclusion") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-3" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("exclusionbody") }}
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <div v-html="$t('body_legal_two')"></div>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-4 block class="acc-btn">
                  {{ $t("externallink") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-4" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('externallink_body')"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-5 block class="acc-btn">
                  {{ $t("internallink") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-5" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('internallink_body')"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-6 block class="acc-btn">
                  {{ $t("denialofaccess") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-6" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('denialofaccess_body')">
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <p class="bk_pra wow move-up" v-html="$t('text_legal')"></p>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-7 block class="acc-btn">
                  {{ $t("comments_legal") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-7" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('comments_legal_body')">
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <h5 class="heading heading-h5 pt--30 pb--30 theme-color">
            {{ $t("title_legal_three") }}
          </h5>
          <div class="plans-about" v-html="$t('body_legal_three')"></div>
          <p class="bk_pra wow move-up pt--30 pb--10">
            {{ $t("footer_three_legal") }}
          </p>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-8 block class="acc-btn">
                  {{ $t("datatreatment") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-8" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("datatreatment_body") }}
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-9 block class="acc-btn">
                  {{ $t("copyright") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-9" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('copyright_body')"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-10 block class="acc-btn">
                  {{ $t("clauses") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-10" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="$t('clauses_body')"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-11 block class="acc-btn">
                  {{ $t("acceptance") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-11" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("acceptance_body") }}
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-12 block class="acc-btn">
                  {{ $t("jurisdiction") }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-12" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text>
                    {{ $t("jurisdiction_body") }}
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <p class="heading heading-h5 theme-color pt--30 pb--30">
            {{ $t("commission") }}
            <a
              href=" https://webgate.ec.europa.eu/odr/main/index.cfm?event=main.home.chooseLanguage"
              ><strong
                >https://webgate.ec.europa.eu/odr/main/index.cfm?event=main.home.chooseLanguage</strong
              ></a
            >
          </p>
          <p class="heading heading-h5 pt--80">
            <strong> <span>Versión 1.0 – {{ $t('may')}} 2018</span></strong>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
