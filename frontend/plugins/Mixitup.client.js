import Vue from "vue";
import mixitup from "mixitup";

Object.defineProperty(Vue.prototype, "mixitup", {
  value: mixitup,
});
