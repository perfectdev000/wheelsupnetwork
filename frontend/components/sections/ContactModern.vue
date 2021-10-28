<template>
  <div class="contact-modern pt--80 pb--120 pb_md--80 pb_sm--80">
    <div class="container">
      <div class="row align-items-end">
        <div class="col-lg-6 col-12 pr--50 ptb-md--80 ptb-sm--80">
          <div
            class="
              contact-modern
              bg_color--primary
              space_dec--100
              pt--120
              pb--120
              pl--60
              pr--60
            "
          >
            <div class="inner">
              <h2 class="heading heading-h2 text-white">
                {{ $t("moreinfo") }}
              </h2>

              <div class="classic-address text-left mt--60">
                <h4 class="heading heading-h4 text-white">{{ $t('contact_us')}}</h4>
                <div class="desc mt--15 mb--30">
                  <p class="bk_pra line-height-2-22 text-white">
                    {{ $t("addresesemail") }} <br />
                  </p>
                </div>
                <div class="social-share social--transparent text-white">
                  <a :href="$t('facebook')" target="_blank">
                    <i class="fab fa-facebook" />
                  </a>
                  <a :href="$t('linkedin')" target="_blank">
                    <i class="fab fa-linkedin" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-6 col-12 pl--50">
          <div class="contact-form">
            <validation-observer ref="observer" v-slot="{ handleSubmit }">
              <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
                <div class="row">
                  <div class="col-lg-12">
                    <validation-provider
                      v-slot="validationContext"
                      name="Nombre"
                      :rules="{ required: true, min: 3 }"
                    >
                      <b-form-input
                        id="name"
                        v-model="form.name"
                        name="name"
                        :state="getValidationState(validationContext)"
                        aria-describedby="name-feedback"
                        :placeholder="$t('name')"
                      ></b-form-input>

                      <b-form-invalid-feedback id="name-feedback">{{
                        validationContext.errors[0]
                      }}</b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Correo Electrónico"
                      :rules="{ required: true, email: true }"
                    >
                      <b-form-input
                        id="email"
                        v-model="form.email"
                        name="email"
                        :state="getValidationState(validationContext)"
                        aria-describedby="email-feedback"
                        :placeholder="$t('email')"
                      ></b-form-input>
                      <b-form-invalid-feedback id="email-feedback">{{
                        validationContext.errors[0]
                      }}</b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Número de teléfono"
                    >
                      <b-form-input
                        id="phone"
                        v-model="form.phone"
                        name="phone"
                        :state="getValidationState(validationContext)"
                        aria-describedby="phone-feedback"
                        :placeholder="$t('phone')"
                      ></b-form-input>

                      <b-form-invalid-feedback id="phone-feedback">{{
                        validationContext.errors[0]
                      }}</b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Tu mensaje..."
                    >
                      <b-form-textarea
                        id="message"
                        v-model="form.message"
                        name="message"
                        :state="getValidationState(validationContext)"
                        aria-describedby="message-feedback"
                        :placeholder="$t('yourmessage')"
                      ></b-form-textarea>

                      <b-form-invalid-feedback id="message-feedback">{{
                        validationContext.errors[0]
                      }}</b-form-invalid-feedback>
                    </validation-provider>
                  </div>
                  <div class="col-12 mt--30">
                    <div class="check-box">
                      <input
                        id="check"
                        v-model="termsConditions"
                        type="checkbox"
                        name="check"
                      />
                      <label for="check">{{ $t("accept") }}</label>
                    </div>
                  </div>
                  <div class="col-lg-12 mt--30">
                    <input type="submit" :value="$t('submit')" />
                    <p class="form-messege" />
                  </div>
                </div>
              </b-form>
            </validation-observer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getUrlApi } from "../../utils/app";

export default {
  props: {
    site: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      form: {
        name: null,
        email: null,
        phone: null,
        message: null,
      },
      termsConditions: false,
    };
  },
  methods: {
    getValidationState({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null;
    },
    resetForm() {
      this.termsConditions = false;
      this.form = {
        name: null,
        email: null,
        phone: null,
        message: null,
      };

      this.$nextTick(() => {
        this.$refs.observer.reset();
      });
    },
    async onSubmit() {
      const data = {
        name: this.form.name,
        email: this.form.email,
        phone: this.form.phone,
        body: this.form.message,
        site: this.site,
      };

      if (!this.termsConditions) {
        this.$toast.show("You must agree to terms and conditions");
        return;
      }

      try {
        const url = `${getUrlApi()}contact`;

        this.$nuxt.$loading.start();

        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify(data),
          headers: {
            "content-type": "application/json",
          },
        }).then((res) => res.json());

        this.$nuxt.$loading.finish();

        if (response.status === 200) {
          this.$swal(
            this.$t('successcontact')
          );
          this.resetForm();
        } else if (response.status === 400) {
          this.$toast.show(response.message);
        } else {
          this.$toast.show("Error contact");
          this.resetForm();
        }
      } catch (e) {
        this.$toast.show("Error contact");
        this.resetForm();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.bg_color--primary {
  background-color: $color-1;
}

.contact-form input[type="submit"] {
  background-color: $color-1;
}
</style>
