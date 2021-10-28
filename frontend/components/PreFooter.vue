<template>
  <footer class="page-footer pl--150 pr--150 pl_lg--30 pr_lg--30 pl_md--30 pr_md--30 pl_sm--5 pr_sm--5">
    <div class="bk-footer-inner pt--30 pb--30">
      <div class="container">
        <div class="row d-flex justify-content-center align-items-center">
          <div class="col-lg-4 col-sm-12 d-block d-md-flex w-100 justify-content-center">
            <div class="footer-widget">
              <div class="logo prefooter--border-right p-0">
                <img src="/img/logo/Logo_Global_Agents_970x520.png" alt="brand logo" />
              </div>
            </div>
          </div>
          <div class="col-lg-8 col-sm-12 d-block d-flex justify-content-center justify-content-md-center justify-content-lg-start">
            <div class="footer-widget text__color menu--about">
              <h1 class="widgettitle pl-0 pl-md-5">PART OF GLOBAL AGENTS</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      instagramPosts: [
        {
          id: 1,
          image: "/img/instagram/instagram-1.jpg",
          like: "1K",
          comment: "8",
        },
        {
          id: 2,
          image: "/img/instagram/instagram-2.jpg",
          like: "6K",
          comment: "9",
        },
        {
          id: 3,
          image: "/img/instagram/instagram-3.jpg",
          like: "3K",
          comment: "4",
        },
        {
          id: 4,
          image: "/img/instagram/instagram-4.jpg",
          like: "1K",
          comment: "3",
        },
        {
          id: 5,
          image: "/img/instagram/instagram-5.jpg",
          like: "2K",
          comment: "7",
        },
        {
          id: 6,
          image: "/img/instagram/instagram-6.jpg",
          like: "1K",
          comment: "8",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.bg_color--footer {
  background-color: $color-3;
}
.text__color{
  h1{
    color:$color-3;
    padding-left:33px;
  }
}
.prefooter--border-right {
  padding-right: 2.5rem;
  border-right: .2rem dashed #00529c;
  -ms-flex-align: end;
  align-items: flex-end;
  display: -ms-flexbox;
  display: flex;
}

@media only screen and (max-width: 990px) {
  .prefooter--border-right {
    border-right: none;
  }
}
</style>


