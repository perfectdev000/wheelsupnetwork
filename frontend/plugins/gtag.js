import Vue from "vue";
import VueGtag from "vue-gtag";

export default ({ $gtag, $config: {GA} }) => { Vue.use(VueGtag, {
  config: { 
    id: GA
  },
  pageTrackerSkipSamePath: false,
  pageTrackerScreenviewEnabled: true
})}