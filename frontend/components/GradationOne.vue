<template>
    <div class="bk-gradation mt--30 mt_sm--5">
        <div v-for="gradation in gradations" :key="gradation.id" class="item-grid mt--40 move-up-x wow" data-wow-delay=".13s">
            <div class="line"></div>
            <div class="dot-wrap">
                <div class="dot">
                    <div class="count">{{ gradation.count }}</div>
                </div>
            </div>
            <div :class="gradation.id === 2 ? 'pb--100 content' : 'content'">
              <a :href="gradation.url">
                <h5 class="heading heading-h5 text-center theme-color">
                  {{ gradation.url }}
                </h5>
                <p class="bk_pra">{{ gradation.desc }}</p>
              </a>
            </div>
        </div>
    </div>
</template>

<script>
    import data from '../data/gradation.json';

    export default {
        props:['about'],
        data () {
            return {
                data
            }
        },
        computed:{
          gradations(){
              return [
                      {
                        "id": 1,
                        "count": "1",
                        "desc": this.about.dedicatedSiteOne,
                        "url": this.about.urlSiteOne
                      },
                      {
                        "id": 2,
                        "count": "2",
                        "desc": this.about.dedicatedSiteTwo,
                        "url": this.about.urlSiteTwo
                      },
                      {
                        "id": 3,
                        "count": "3",
                        "desc": this.about.dedicatedSiteThree,
                        "url": this.about.urlSiteThree
                      }
                    ]
          }
        }
    };
</script>

<style lang="scss" scoped>
.pb--100 {
  padding-bottom: 100px !important;
}
p.bk_pra {
  color: #333333 !important;
}
</style>
