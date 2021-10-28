export const state = () => ({
    _data:'',
    pathLogo:''
})
  
export const mutations = {
    fetch(state, site) {
        state._data = site
    },
    urlLogo(state, path) {
        state.pathLogo = path
    }
}
