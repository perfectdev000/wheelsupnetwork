<template>
  <div class="brook-whatdo-area ptb--100 ptb-md--80 ptb-sm--60 bg_color--1">
    <div class="container">
      <div class="row">
        <div class="col-lg-10 offset-lg-2">
          <div class="bk-title--default text-left">
            <h2 class="heading heading-h2 theme-color">{{ about.title }}</h2>
            <div class="bkseparator--30"></div>
            <h4 class="heading heading-h4">  {{ $t('about') }} {{ $config.pageTitle }} </h4>
          </div>
        </div>
      </div>
      <div class="row mt--40 mt_md--20 mt_sm--5">
        <div class="col-xl-2 col-lg-2">
          <div class="what-do mt--40 mt_md--5 mt_sm--5">
            <div class="basic-separator line-3"></div>
          </div>
        </div>
        <div class="col-xl-4 col-lg-5 col-md-6 col-sm-12">
          <div class="what-do mt--40">
            <div class="content">
              <div class="bkseparator--20"></div>
              <p class="bk_pra wow move-up" v-html="about.columna_rigth">  </p>
              <!-- <h5 class="heading heading-h5 theme-color pt--30"> Estamos orgullosos de servir a la industria de viajes en seis países, en tres continentes y en dos idiomas. </h5> -->
            </div>
          </div>
        </div>
        <div class="col-xl-4 col-lg-5 col-md-6 col-sm-12 offset-xl-1">
          <div class="what-do mt--40">
            <div class="content">
              <div class="bkseparator--20"></div>
              <p class="bk_pra wow move-up" v-html="about.columna_left" >  </p>
              <!-- <h5 class="heading heading-h5 theme-color pt--30"> ¡Estamos absolutamente donde su marca quiere estar! </h5> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  props:['about']
  
}
</script>
