<template>
    <div class="breadcrumb-area bg_image--11 ptb--270 breadcrumb-title-bar breadcrumb-title-white" :style="{ backgroundImage: `url('/img/bg/bg-image-11.jpg')` }">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="breadcrumb-inner text-center">
                        <h1 class="heading heading-h1 text-white">Brook is a New York-based <br> creative agency</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {

    };
</script>

<style lang="scss" scoped>
    .ptb--270 {
        @media #{$md-layout, $sm-layout}{
            padding-top: 130px;
            padding-bottom: 130px;
        }
    }
</style>