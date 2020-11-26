import { setClient } from '~/services/apiClient'

export default function ({ $axios, app }) {
  setClient($axios, app.$cookies.get('token'))
}
