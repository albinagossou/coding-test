import { camelCase, snakeCase } from 'lodash'

export function keysToCamelCase(obj, responseType = '') {
  if (Array.isArray(obj)) {
    return obj.map((v) => keysToCamelCase(v))
  } else if (
    obj &&
    (obj.constructor === Object || typeof obj === 'object') &&
    responseType !== 'blob'
  ) {
    return Object.keys(obj).reduce((result, key) => {
      return {
        ...result,
        [camelCase(key)]: keysToCamelCase(obj[key]),
      }
    }, {})
  }
  return obj
}

export function keysToSnakeCase(obj) {
  if (Array.isArray(obj)) {
    return obj.map((v) => keysToSnakeCase(v))
  } else if (obj && obj.constructor === Object) {
    return Object.keys(obj).reduce(
      (result, key) => ({
        ...result,
        [snakeCase(key)]: keysToSnakeCase(obj[key]),
      }),
      {}
    )
  }
  return obj
}
