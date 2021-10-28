export default function ( { route, $config }) {
    
    if($config.isMaintenance){
        window.onNuxtReady(() => { window.$nuxt.$router.push('/maintenance') })
    }
    if($config.isMaintenance === false && route.path === '/maintenance'){
        window.onNuxtReady(() => { window.$nuxt.$router.push('/') })
    }

   }