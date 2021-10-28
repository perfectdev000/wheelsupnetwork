<template>
  <div class="bk-accordion-area ptb--100 ptb-md--80 ptb-sm--60 bg_color--1">
    <div class="container">
      <div class="row">
        <!-- Start Single Accordion -->
        <div class="col-md-12">
          <div class="content mt--30 mb--10 mb__sm--20 mb_md--20">
            <div class="bkseparator--20"></div>
            <p v-html="data.content"></p>
          </div>
          <div id="accordionExampl3" class="bk-accordion-style--2">
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-1 block class="acc-btn">
                  {{ data.title_one }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-1" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_one"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>

            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-2 block class="acc-btn">
                  {{ data.title_two }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-2" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_two"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>

            <h5 class="heading heading-h5 theme-color pt--30 pb--10">
              {{ data.title_header_three }}
            </h5>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-3 block class="acc-btn">
                  {{ data.title_three }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-3" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_three"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>

            <h5 class="heading heading-h5 theme-color pt--30 pb--10">
              {{ data.title_header_four }}
            </h5>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-4 block class="acc-btn">
                  {{ data.title_four }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-4" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_four"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-5 block class="acc-btn">
                  {{ data.title_five }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-5" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_five"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <p class="heading heading-h6 pb--10 pt--30">
              {{ data.title_header_six }}
            </p>
            <h5 class="heading heading-h6 theme-color">
                {{ data.title_base_legal }}  
            </h5>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-6 block class="acc-btn">
                  {{ data.title_six }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-6" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_six">
                    <br />
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
            <h5 class="heading heading-h6 theme-color pt--30">
              {{ data.title_header_seven }}
            </h5>
            <b-card no-body>
              <b-card-header header-tag="header">
                <b-button v-b-toggle.accordion-7 block class="acc-btn">
                  {{ data.title_seven }}
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-7" visible accordion="my-accordion">
                <b-card-body>
                  <b-card-text v-html="data.content_seven"> </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <p class="bk_pra wow move-u" v-html="data.content_footer"></p>
        </div>
        <!-- End Single Accordion -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: "",
    };
  },
  async fetch() {
    const policy = await this.$strapi.find("privacy-policies", {
      _locale: this.$i18n.locale,
    });
    this.data = policy;
  },
};
</script>

<style></style>
