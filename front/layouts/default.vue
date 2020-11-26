<template>
  <v-app>
    <nav-bar />
    <v-main>
      <v-fade-transition mode="out-in" appear>
        <router-view :key="$route.fullPath" />
      </v-fade-transition>
    </v-main>
    <heqtor-footer />
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import HeqtorFooter from '@/components/HeqtorFooter.vue'

export default {
  components: {
    NavBar,
    HeqtorFooter,
  },
}
</script>
