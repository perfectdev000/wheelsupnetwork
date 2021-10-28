<template>
  <div class="team team__style--3">
    <n-link to="/">
      <div class="thumb">
        <img :src="teamMember.image" alt="team Images">
          <div class="overlay" :style="{ backgroundImage: `url(${teamMember.image})` }"></div>
        </div>
    </n-link>
    <div class="team-info text-center">
      <div class="info">
        <h5>{{ teamMember.name }}</h5>
        <span>{{ teamMember.position }}</span>
      </div>
    </div>
    </div>
</template>

<script>
    export default {
      props: ["teamMember"]
    };
</script>
