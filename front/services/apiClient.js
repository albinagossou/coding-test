import { keysToCamelCase, keysToSnakeCase } from './helpers'
import { setClient as setAuthClient } from './authService'
import MeService, { setClient as setMeClient } from './meService'

let apiClient
const onRequestSnakeCase = (config) => {
  if (config.data) {
    config.data = keysToSnakeCase(config.data)
  }
}
const onResponseCamelCase = (response) => {
  if (response.data) {
    response.data = keysToCamelCase(response.data, response.config.responseType)
  }
  return response
}
const onErrorUnauthorized = (error) => {
  if (error.response && error.response.status === 401) {
    if (process.browser) {
      window.$nuxt.store.dispatch('auth/logout')
    }
  }
}

function setAllApiClients() {
  setMeClient(
    apiClient,
    onRequestSnakeCase,
    onResponseCamelCase,
    onErrorUnauthorized
  )
}

export function setClient(axiosInstance, token = null) {
  apiClient = axiosInstance.create({
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
  })
  apiClient.setBaseURL(apiClient.defaults.baseURL + '/api')
  setAuthClient(axiosInstance, onRequestSnakeCase, onResponseCamelCase)
  token ? setToken(token) : setAllApiClients()
}

export function setToken(token) {
  if (!apiClient) throw new Error('Api client not installed')
  apiClient.defaults.headers.common.Authorization = `Bearer ${token}`
  setAllApiClients()
}

export function unsetToken() {
  if (!apiClient) return
  apiClient.defaults.headers.common.Authorization = ''
  setAllApiClients()
}

export function checkToken(token) {
  setToken(token)
  return MeService.getMyProfile()
}
