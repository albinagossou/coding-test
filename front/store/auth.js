import authService from '@/services/authService.js'

export const state = () => ({
  user: null,
})

export const mutations = {
  SET_USER_DATA(state, userData) {
    process.browser &&
      userData.accessToken &&
      window.$nuxt.$cookies.set('token', userData.accessToken)
    delete userData.accessToken
    state.user = userData
  },
  CLEAR_USER_DATA() {
    process.browser && window.$nuxt.$cookies.remove('token')
    location.reload()
  },
}

export const actions = {
  register({ commit }, credentials) {
    return authService.register(credentials).then(({ data }) => {
      return commit('SET_USER_DATA', data)
    })
  },
  login({ commit }, credentials) {
    return authService.login(credentials).then(({ data }) => {
      return commit('SET_USER_DATA', data)
    })
  },
  logout({ commit }) {
    commit('CLEAR_USER_DATA')
  },
  setUserData({ commit }, userData) {
    return commit('SET_USER_DATA', userData)
  },
}

export const getters = {
  isLoggedIn(state) {
    return !!state.user
  },
}
