import { setToken } from '@/services/apiClient'

let authClient

export function setClient(axiosInstance, onRequest = null, onResponse = null) {
  authClient = axiosInstance.create({
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    withCredentials: false,
  })
  authClient.setBaseURL(authClient.defaults.baseURL + '/auth')
  if (onRequest) clientOnRequest(onRequest)
  if (onResponse) clientOnResponse(onResponse)
}

export function clientOnRequest(onRequest) {
  if (!authClient) throw new Error('Auth client not installed.')
  authClient.onRequest(onRequest)
}

export function clientOnResponse(onResponse) {
  if (!authClient) throw new Error('Auth client not installed.')
  authClient.onResponse(onResponse)
}

export default {
  register(credentials) {
    if (!authClient) throw new Error('Auth client not installed.')
    return authClient.post('/register', credentials).then((response) => {
      setToken(response.data.accessToken)
      return response
    })
  },
  login(credentials) {
    if (!authClient) throw new Error('Auth client not installed.')
    return authClient.post('/login', credentials).then((response) => {
      setToken(response.data.accessToken)
      return response
    })
  },
}
