<template>
  <nav class="page_nav menu">
    <ul class="mainmenu">
      <li class="lavel-1 with--drop slide--megamenu">
        <n-link to="/promotions">
          <span>GANA MÁS</span>
        </n-link>
        <ul class="mega__width--fullscreen">
          <div class="container">
            <div class="mega__list">
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/promotions">
                      <span>Incentivos, Comisiones y FAMs</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link :to="localePath({ name: 'premios-y-ganadores'})" >
                      <span>Premios y Ganadores</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link :to="localePath({ name: 'portal-para-agentes'})"  >
                      <span>Reserva con nuestros partners</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <!-- <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/entradas">
                      <span>Entradas Eventos y Espectaculos</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li> -->
            </div>
          </div>
        </ul>
      </li>

      <li class="lavel-1 with--drop slide--megamenu">
        <n-link to="/marketing">
          <span>APRENDE MÁS</span>
        </n-link>
        <ul class="mega__width--fullscreen">
          <div class="container">
            <div class="mega__list">
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/marketing">
                      <span>Información del Cliente y Herramientas de Venta</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/webinars">
                      <span>Webinars</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/webinars-pasados">
                      <span>Webinars pasados</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link :to="localePath({name: 'proximos-eventos'})" >
                      <span>Eventos</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link   :to="localePath({ name: 'destinos'})" >
                      <span>Destinos</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
            </div>
          </div>
        </ul>
      </li>

      <li class="lavel-1 with--drop slide--megamenu">
        <n-link to="/specials">
          <span>AHORRA MÁS</span>
        </n-link>
        <ul class="mega__width--fullscreen">
          <div class="container">
            <div class="mega__list">
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/specials">
                      <span>Ofertas Consumidor Final</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
              <li class="mega--title">
                <ul>
                  <li>
                    <nuxt-link to="/industry">
                      <span>Tarifas para Agentes</span>
                    </nuxt-link>
                  </li>
                </ul>
              </li>
            </div>
          </div>
        </ul>
      </li>

      <li class="lavel-1 slide--megamenu">
        <n-link to="/news">
          <span>Noticias</span>
        </n-link>
      </li>
      <li class="lavel-1 slide--megamenu">
        <n-link :to="localePath({ name: 'empleos'})" >
          <span>Empleos</span>
        </n-link>
      </li>
      <!--
      Esta seccion destruye el grid por defecto del nav. Una opcion es buscar donde poner
      esta opcion O Reconstruir el nav desde los main-Style, Cosa que no quiero hacer
      :sad. La mejor opcion es reubicar Book Now en algun parte o anidarla en un
      menu ya creado!
      Mientras lo agregare a una de las opciones del footer!.
      -->
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
.mega__list {
  display: flex;

  li {
    flex-basis: 100%;
    text-align: center;
  }
}
</style>
