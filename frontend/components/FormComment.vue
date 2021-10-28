<template>
  <div class="comment-form-wrapper">
    <!-- Start Contact Area -->
    <div class="contact-form wow move-up">
      <form>
        <div class="row">
          <div class="col-lg-12">
            <input class="form__color--primary" type="text" placeholder="Your Name *" required>
          </div>

          <div class="col-lg-12 mt--30">
            <input class="form__color--primary" type="text" placeholder="Your Email *" required>
          </div>

          <div class="col-lg-12 mt--30">
            <input class="form__color--primary" type="text" placeholder="Subject">
          </div>

          <div class="col-lg-12 mt--30">
            <textarea class="form__color--primary" placeholder="Your Message" />
          </div>

          <div class="col-lg-12 mt--30">
            <div class="blog-btn">
              <button class="brook-btn bk-btn-theme btn-sd-size btn-rounded space-between">
                Send
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
    <!-- End Contact Area -->
  </div>
</template>
<style lang="scss" scoped>
.form__color--primary{
  font-size: 23px;
  color: black;
  }
</style>
