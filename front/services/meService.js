let apiClient

export function setClient(
  globalApiClient,
  onRequest = null,
  onResponse = null,
  onError = null
) {
  apiClient = globalApiClient.create()
  apiClient.setBaseURL(apiClient.defaults.baseURL + '/me')
  if (onRequest) clientOnRequest(onRequest)
  if (onResponse) clientOnResponse(onResponse)
  if (onError) clientOnError(onError)
}

export function clientOnRequest(onRequest) {
  if (!apiClient) throw new Error('Api client not installed.')
  apiClient.onRequest(onRequest)
}

export function clientOnResponse(onResponse) {
  if (!apiClient) throw new Error('Api client not installed.')
  apiClient.onResponse(onResponse)
}

export function clientOnError(onError) {
  if (!apiClient) throw new Error('Api client not installed.')
  apiClient.onError(onError)
}

export default {
  getMyProfile() {
    if (!apiClient) throw new Error('Api client not installed.')
    return apiClient.get()
  },
  updateMyProfile(profileData) {
    if (!apiClient) throw new Error('Api client not installed.')
    return apiClient.post('', profileData)
  },
  getMyCompany() {
    if (!apiClient) throw new Error('Api client not installed.')
    return apiClient.get('/company')
  },
  createCompany(companyData) {
    if (!apiClient) throw new Error('Api client not installed.')
    return apiClient.post('/company', companyData)
  },
  deleteMyCompany() {
    if (!apiClient) throw new Error('Api client not installed.')
    return apiClient.delete('/company')
  },
}
