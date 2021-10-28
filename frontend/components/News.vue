<template>
<div class="min_sidebar">
  <div class="primary text-light titleUp">
    TRENDING
  </div>
  <div class="news">
    <div 
      v-for="post in posts"
      :key="post.title"
      class="contentComent"
    >
      <h1> {{ post.title  }}</h1>
      <p> {{ post.content }} </p>
    </div>
  </div>
  <div class="titleDown">
     <a href="#4">Click here to subscribre</a>
   </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      posts: [
        {
          title: 'Free 1 All: Extra AMResorts Perks for Everyone!',
          content: 'In the spirit of travel, AMResorts is treating their guests ...'
        },
        {
          title: 'Free 2 All: Extra AMResorts Perks for Everyone!',
          content: 'In the spirit of travel, AMResorts is treating their guests ...'
        },
        {
          title: 'Free 3 All: Extra AMResorts Perks for Everyone!',
          content: 'In the spirit of travel, AMResorts is treating their guests ...'
        },
        {
          title: 'Free 4 All: Extra AMResorts Perks for Everyone!',
          content: 'In the spirit of travel, AMResorts is treating their guests ...'
        }
      ],
    }
  }
}
</script>

<style scoped>
  
.min_sidebar .titleUp {
  position:absolute;
  background-color: #1daeeb;
  color: #ffffff;
  right:0px;
  left: 0px;
  text-align: center;
  line-height: 40px;
  font-size: 25px;
}
.news {
  position:absolute;
  top: 50px;
  bottom: 42px;
  overflow: auto;
}
.news h1 {
  color:#ec168b;
  font-size: 20px;
  font-weight: bold;
  line-height: 22px;
}
.titleDown{
  position:absolute;
  bottom: 0px;
  left: 0px;
  right: 0px;
  display: block;
  background-color: #1daeeb;
  color: #ffffff;
  text-align: center;
  line-height: 40px;
  font-size: 20px;
  cursor: pointer;
}
</style>
