<template>
  <div class="contact-modern pt--80 pb--120 pb_md--80 pb_sm--80 bg_color--5">
    <div class="breadcrumb-area pb--60 breadcrumb-title-bar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="breadcrumb-inner text-center">
              <h1 class="heading heading-h1">
                 {{ $t('newsletter')}}  
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-lg-6 offset-lg-3">
          <div class="contact-form">
            <validation-observer ref="observer" v-slot="{ handleSubmit }">
              <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
                <div class="row">
                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      :name="$t('email')"
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
                      name="Nombre"
                      :rules="{ required: true}"
                    >
                      <b-form-input
                        id="name"
                        v-model="form.name"
                        name="name"
                        :state="getValidationState(validationContext)"
                        aria-describedby="name-feedback"
                        :placeholder="$t('name')"
                      ></b-form-input>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Apellido"
                      :rules="{ required: true}"
                    >
                      <b-form-input
                        id="last_name"
                        v-model="form.last_name"
                        name="last_name"
                        :state="getValidationState(validationContext)"
                        aria-describedby="last_name-feedback"
                        :placeholder="$t('surname')"
                      ></b-form-input>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Ciudad"
                      :rules="{ required: true}"
                    >
                      <b-form-input
                        id="city"
                        v-model="form.city"
                        name="city"
                        :state="getValidationState(validationContext)"
                        aria-describedby="city-feedback"
                        :placeholder="$t('addreses')"
                      ></b-form-input>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider
                      v-slot="validationContext"
                      name="Código Postal"
                      :rules="{ required: true}"
                    >
                      <b-form-input
                        id="zip"
                        v-model="form.zip"
                        name="zip"
                        :state="getValidationState(validationContext)"
                        aria-describedby="zip-feedback"
                        :placeholder="$t('postalcode')"
                      ></b-form-input>
                    </validation-provider>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <validation-provider v-slot="validationContext" name="Pais" :rules="{ required: true}" >
                      <b-form-input
                        id="country"
                        v-model="form.country"
                        name="country"
                        :state="getValidationState(validationContext)"
                        aria-describedby="country-feedback"
                        :placeholder="$t('country')"
                      ></b-form-input>
                    </validation-provider>
                  </div>
                  <div class="check-box col-lg-12 mt--30" >
                    <input
                      type="checkbox"
                      name="check"
                      id="check"
                      v-model="termsConditions"
                      :rules="{ required: true}"
                    />
                    <label for="check"
                      >
                        <n-link  :to="localePath({ name: 'politica-de-privacidad' })" class="conditions">
                           {{ $t('accept') }}
                        </n-link>
                    </label>
                  </div>

                  <div class="col-lg-12 mt--30">
                    <input
                      type="submit"
                      class="text-uppercase"
                      :value="$t('subscribenow')"
                    />
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
import { getUrlApi } from "../utils/app";

export default {
  props: {
    site: {
      required: true,
      type: String,
    },
  },
  data() {
    return {
      form: {
        email: null,
        name: null,
        last_name: null,
        city: null,
        zip: null,
        country: null,
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
        email: null,
        name: null,
        last_name: null,
        city: null,
        zip: null,
        country: null,
      };

      this.$nextTick(() => {
        this.$refs.observer.reset();
      });
    },
    async onSubmit() {
      const data = {
        email: this.form.email,
        firstName: this.form.name,
        lastName: this.form.last_name,
        city: this.form.city,
        postalCode: this.form.zip,
        country: this.form.country,
        site: this.site,
      };

      if (!this.termsConditions) {
        this.$toast.show("You must agree to terms and conditions");
        return;
      }

      try {
        const url = `${getUrlApi()}newsletter`;

        this.$nuxt.$loading.start();

        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify(data),
          headers: {
            'content-type': 'application/json',
          }
        }).then((res) => res.json());

        this.$nuxt.$loading.finish();

        if (response.status === 200) {
          this.$swal(this.$t('messageForm'));
          this.$nuxt.$router.replace("/");
        } else if(response.status === 400) {
          this.$toast.show(response.message);
        }else {
          this.$toast.show("Subscription error");
          this.resetForm();
        }
      } catch (e) {
        this.$toast.show("Subscription error");
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

.conditions {
  color: #A7A7A7;
}
.conditions:hover {
  color:#003C71
}
.contact-form input[type="submit"] {
  background-color: $color-1;
}
</style>
