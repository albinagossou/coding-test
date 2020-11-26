import { checkToken } from '@/services/apiClient.js'

export default async function ({ store, app, redirect, route }) {
  if (route.name === 'auth') return
  if (store.getters['auth/isLoggedIn']) return
  try {
    const storedToken = app.$cookies.get('token')
    const user = await checkToken(storedToken).then((response) => response.data)
    user.accessToken = storedToken
    await store.dispatch('auth/setUserData', user)
  } catch {
    app.$cookies.remove('token')
    return redirect('/auth')
  }
}
