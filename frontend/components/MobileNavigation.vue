<template>
  <div class="mobile-navigation">
    <nav id="offcanvas-navigation" class="offcanvas-navigation">
      <ul>
        <li class="menu-item-has-children">
          <n-link to="/promotions" > {{ $t("win") }} </n-link>
          <ul class="sub-menu">
            <li class="mega--title menu-item-has-children " @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/promotions"   >
                <span>  {{ $t("promotions") }}   </span>
              </nuxt-link>
            </li>

            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link :to="localePath({ name: 'premios-y-ganadores' })" >
                <span> {{ $t("prize") }} </span>
              </nuxt-link>
            </li>

            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link :to="localePath({ name: 'portal-para-agentes' })">
                <span> {{ $t("partners") }} </span>
              </nuxt-link>
            </li>

            <!-- <li class="mega--title menu-item-has-children">
              <nuxt-link to="/entradas">
                <span>Entradas Eventos y Espectaculos</span>
              </nuxt-link>
            </li> -->
          </ul>
        </li>

        <li class="menu-item-has-children" >
          <n-link to="/marketing" > {{ $t("learn") }} </n-link>
          <ul class="sub-menu">
             <li class="nav__menu-items menu-item-has-children " v-show="$config.showEvergreen "  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')">
              <nuxt-link to="/evergreen">
                <span> Selling & Travel Tips </span>
              </nuxt-link>
            </li>
            <li class="nav__menu-items menu-item-has-children " v-show="$config.showFams"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/fams">
                <span> FAM Trips </span>
              </nuxt-link>
            </li>
             <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/webinars">
                <span> {{ $t("webinars") }} </span>
              </nuxt-link>
            </li>
            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/marketing">
                <span> {{ $t("marketing") }} </span>
              </nuxt-link>
            </li>
            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link :to="localePath({ name: 'destinos' })">
                <span> {{ $t("destinations") }} </span>
              </nuxt-link>
            </li>
           <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link :to="localePath({ name: 'proximos-eventos' })">
                <span> {{ $t("events") }} </span>
              </nuxt-link>
            </li>
          </ul>
        </li>

        <li class="menu-item-has-children">
          <n-link to="/specials"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')"  > {{ $t("save") }} </n-link>
          <ul class="sub-menu">
            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/specials">
                <span>{{ $t("specials") }} </span>
              </nuxt-link>
            </li>

            <li class="mega--title menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
              <nuxt-link to="/industry">
                <span> {{ $t("industry") }} </span>
              </nuxt-link>
            </li>
          </ul>
        </li>

        <li class="menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
          <n-link to="/news/"> {{ $t("new") }} </n-link>
        </li>

        <li class="menu-item-has-children"  @click="mobiletoggleClass('removeClass', 'show-mobile-menu')" >
          <n-link :to="localePath({ name: 'empleos' })">
            <span> {{ $t("jobs") }} </span>
          </n-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  
  name: "MobileNavMenu",
  methods: {
    // offcanvas menu close
    mobiletoggleClass(addRemoveClass, className) {
      const el = document.querySelector("#offcanvas-menu");
      if (addRemoveClass === "addClass") {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },
  },
  mounted() {
    const offCanvasNav = document.querySelector("#offcanvas-navigation");
    const offCanvasNavSubMenu = offCanvasNav.querySelectorAll(".sub-menu");
    const anchorLinks = offCanvasNav.querySelectorAll("a");

    for (let i = 0; i < offCanvasNavSubMenu.length; i++) {
      offCanvasNavSubMenu[i].insertAdjacentHTML(
        "beforebegin",
        "<span class='menu-expand'><i></i></span>"
      );
    }

    const menuExpand = offCanvasNav.querySelectorAll(".menu-expand");
    const numMenuExpand = menuExpand.length;

    for (let i = 0; i < numMenuExpand; i++) {
      menuExpand[i].addEventListener("click", (e) => {
        sideMenuExpand(e);
      });
    }

    for (let i = 0; i < anchorLinks.length; i++) {
      anchorLinks[i].addEventListener("click", () => {
        closeMobileMenu();
      });
    }

    const sideMenuExpand = (e) => {
      e.currentTarget.parentElement.classList.toggle("active");
    };
    const closeMobileMenu = () => {
      const offcanvasMobileMenu = document.querySelector(
        "#offcanvas-mobile-menu"
      );
      offcanvasMobileMenu.classList.remove("active");
    };
  },
};
</script>

<style lang="scss">
.offcanvas-navigation {
  ul {
    li {
      &.menu-item-has-children {
        &.mega--title > {
          a {
            font-weight: 500;
          }
        }

        .sub-menu {
          height: 0;
          opacity: 0;
          transition: 0.3s;
          visibility: hidden;
        }

        &.active > {
          .sub-menu {
            height: 100%;
            opacity: 1;
            visibility: visible;
          }
        }
      }

      a {
        color: $white;
        font-size: 14px;
        font-weight: 600;
        padding: 10px 0;
        display: block;

        &:hover {
          color: $theme-color;
        }
      }
    }
  }

  ul {
    &.sub-menu {
      margin-left: 15px;
      transition: 0.4s;

      li {
        a {
          color: $white;
          font-weight: 400;

          &:hover {
            color: $theme-color;
          }
        }

        .sub-menu {
          li {
            a {
              font-size: 13px;
              padding: 5px 0;
            }
          }
        }
      }
    }

    li {
      &.menu-item-has-children {
        position: relative;
        display: block;

        a {
          display: block;
        }

        &.active > {
          .menu-expand {
            background-color: rgba($white, 0.2);

            i {
              &:before {
                transform: rotate(0);
              }
            }
          }
        }

        .menu-expand {
          top: 5px;
          right: 0;
          width: 35px;
          height: 35px;
          cursor: pointer;
          line-height: 35px;
          position: absolute;
          text-align: center;
          background-color: rgba($white, 0.1);

          &:hover {
            background-color: rgba($white, 0.2);
          }

          i {
            display: block;
            border-bottom: 1px solid #ffffff;
            position: relative;
            width: 10px;
            text-align: center;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);

            &:before {
              width: 100%;
              content: "";
              border-bottom: 1px solid $white;
              display: block;
              position: absolute;
              top: 0;
              transform: rotate(90deg);
              transition: 0.4s;
            }
          }
        }
      }
    }
  }
}

.offcanvas-navigation ul.sub-menu li a {
  text-transform: capitalize;
}

.offcanvas-navigation ul li a:hover {
  color: #009cde;
}

.offcanvas-navigation ul.sub-menu li a:hover {
  color: #009cde;
}
</style>
