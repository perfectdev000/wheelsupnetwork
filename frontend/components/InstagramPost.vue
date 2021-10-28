<template>
    <div class="instagram-grid-wrap" :class="addClass">
        <div class="item-grid grid-style--1" v-for="instagram in data" :key="instagram.id" >
            <div class="thumb">
                <n-link to="/">
                    <img :src="instagram.image" alt="instagram images">
                </n-link>
                <div class="item-info">
                    <div class="inner">
                        <n-link to=""><i class="fas fa-heart"></i>{{ instagram.like }}</n-link>
                        <n-link to=""><i class="fas fa-comment-dots"></i>{{ instagram.comment }}</n-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import data from '../data/instagram.json';
    export default {
        props: ['addClass'],

        data () {
            return {
                data
            }
        },
    };
</script>