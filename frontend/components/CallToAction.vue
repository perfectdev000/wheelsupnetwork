<template>
    <div class="brook-call-to-action bg_color--2 ptb--40 ptb-md--40 ptb-sm--60">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-12 col-12">
            <div class="call-content vertical-call-toaction text-center">
              <h3 class="heading heading-h3 text-white wow move-up">{{ $t('newsletter')}}</h3>
              <div class="spacing"></div>
              <div class="call-btn text-center wow move-up">
                <n-link :to="localePath({ name: 'suscribete-a-nuestra-newsletter'})" class="brook-btn bk-btn-white text-theme btn-sd-size btn-rounded text-uppercase"> {{ $t('subscribenow')}} </n-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
