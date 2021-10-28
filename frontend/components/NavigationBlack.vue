<template>
  <div class="nav nav--font-1">
    <ul class="nav__list">
      <li class="nav__menu mega--title lavel-1">
        <n-link class="nav__menu--title" :to="localePath('promotions')">
          {{ $t("win") }}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-chevron-down ml--5"
            viewBox="0 0 16 16"
          >
            <path
              fill-rule="evenodd"
              d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"
            />
          </svg>
        </n-link>
        <ul class="nav__menu-lists nav__menu--1-lists">
          <div class="mega__list">
            <li class="nav__menu-items">
              <nuxt-link to="/promotions">
                <span> {{ $t("promotions") }} </span>
              </nuxt-link>
            </li>
            <li class="nav__menu-items">
              <nuxt-link :to="localePath({ name: 'premios-y-ganadores' })">
                <span>{{ $t("prize") }}</span>
              </nuxt-link>
            </li>
            <li class="nav__menu-items">
              <nuxt-link :to="localePath({ name: 'portal-para-agentes' })">
                <span>{{ $t("partners") }}</span>
              </nuxt-link>
            </li>
            <!-- <li class="nav__menu-items">
              <nuxt-link to="/entradas">
                <span>Entradas Eventos y Espectaculos</span>
              </nuxt-link>
            </li> -->
          </div>
        </ul>
      </li>
      <li class="nav__menu mega--title lavel-1">
        <n-link class="nav__menu--title" to="/marketing">
          {{ $t("learn") }}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-chevron-down ml--5"
            viewBox="0 0 16 16"
          >
            <path
              fill-rule="evenodd"
              d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"
            />
          </svg>
        </n-link>
        <ul class="nav__menu-lists nav__menu--2-lists">
          <li class="nav__menu-items" v-if="$config.showEvergreen">
            <nuxt-link to="/evergreen">
              <span> Selling & Travel Tips </span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items" v-if="$config.showFams">
            <nuxt-link to="/fams">
              <span> FAM Trips </span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items">
            <nuxt-link to="/webinars">
              <span>{{ $t("webinars") }}</span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items">
            <nuxt-link to="/marketing">
              <span> {{ $t("marketing") }} </span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items">
            <nuxt-link :to="localePath({ name: 'destinos' })">
              <span>{{ $t("destinations") }}</span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items">
            <nuxt-link  :to="localePath({ name: 'proximos-eventos' })">
              <span>{{ $t("event") }}</span>
            </nuxt-link>
          </li>
        </ul>
      </li>
      <li class="nav__menu mega--title lavel-1">
        <n-link class="nav__menu--title" to="/specials">
          {{ $t("save") }}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-chevron-down ml--5"
            viewBox="0 0 16 16"
          >
            <path
              fill-rule="evenodd"
              d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"
            />
          </svg>
        </n-link>
        <ul class="nav__menu-lists nav__menu--1-lists">
          <li class="nav__menu-items">
            <nuxt-link to="/specials">
              <span>{{ $t("specials") }}</span>
            </nuxt-link>
          </li>
          <li class="nav__menu-items">
            <nuxt-link to="/industry">
              <span> {{ $t("industry") }} </span>
            </nuxt-link>
          </li>
        </ul>
      </li>
      <li class="nav__menu mega--title lavel-1">
        <n-link class="nav__menu--title" to="/news"> {{ $t("new") }} </n-link>
      </li>
      <li class="nav__menu">
        <n-link class="nav__menu--title" :to="localePath({ name: 'empleos' })">
          <span>{{ $t("jobs") }} </span>
        </n-link>
      </li>
      <li class="nav__menu">
        <n-link :to="localePath({ name: 'suscribete-a-nuestra-newsletter' })">
          <button type="button" class="btn btn-primary">
            {{ $t("subscribe") }}
          </button>
        </n-link>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
ul {
  list-style-type: none;
}

.nav__menu--title {
  color: #262626;
  font-weight: bold;
}

.nav__menu--title:hover {
  background: rgba(134, 134, 134, 0.1);
}

.nav {
  margin-top: 30px;
  text-align: center;
  width: 100%;
}

.nav__list {
  display: inline-block;
}

.nav__menu {
  float: left;
  width: 130px;
  height: 65px;
  line-height: 60px;
  text-transform: uppercase;
  background-color: transparent;
  cursor: pointer;
  border-radius: 12px;
  font-size: 14px;
  li {
    span {
      color: #fff;
    }
  }
}

.nav__menu:hover {
  background-color: transparent;
}

.nav__menu:hover > .nav__menu-lists li {
  display: block;
}

.nav__menu-lists {
  perspective: 5000px;
}

.nav__menu-items {
  display: none;
  /* height: 80px; */
  width: 250px;
  min-height: 50px;
  background-color: #003c71;
  font-size: 13px;
  padding: 5px;
}

.nav__menu-items > a {
  line-height: 35px;
}

.nav__menu-items:hover {
  background-color: #009cde;
}

.nav__menu:nth-child(1) {
  border-top-left-radius: 10px;
}

.nav__menu:last-child {
  border-top-right-radius: 10px;
}

li > a {
  display: block;
}
</style>
