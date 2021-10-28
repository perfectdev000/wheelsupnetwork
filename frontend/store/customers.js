export const state = () => ({
    data:[],
})
export const mutations = {
    SET_CUSTOMERS(state, customers) {
        state.data = customers
    },
}