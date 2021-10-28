<template>
  <div class="brook-about-area bg_color--1 ptb--40">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <div class="about-inner authenthick-about pr--30">
            <h2 class="heading headin-h2 theme-color wow move-up"> {{ $t('about_message') }}  </h2>
            <div class="bkseparator--30"></div>
            <h3 class="heading heading-h3 heading-font line-height-1-5 wow move-up">
              {{ $t('about_body') }}
            </h3>

            <div class="bkseparator--40"></div>
            <p class="bk_pra font-20 line-height-1-6 dark-2 heading-font2 wow move-up">
              {{ $t('about_footer')}}
            </p>
            <div class="bkseparator--65"></div>
            <div class="view-more-btn heding-color heading-font font-18 font-700 theme-color wow move-up">
              <n-link to="/about-us">
                <span> {{ $t('more_about_us')}} </span>
                <span class="btn-arrow"></span>
              </n-link>
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="about-thumb text-center text-lg-right mt_md--40 mt_sm--40">
            <img src="/img/about/aboutauth.jpg" alt="Multipurpose">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
