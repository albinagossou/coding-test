<template>
  <v-app>
    <v-main>
      <v-row class="fill-height">
        <v-col cols="12" md="6" align-self="center">
          <router-view :key="$route.fullPath" />
        </v-col>
        <v-col
          cols="12"
          md="6"
          order="first"
          order-md="last"
          style="align-self: center"
        >
          <v-row class="fill-height">
            <v-col cols="1" class="hidden-sm-and-down">
              <v-divider vertical />
            </v-col>
            <v-col cols="12" md="10" align-self="center">
              <v-img
                src="/logo-text-baseline.jpg"
                alt="Heqtor, au service de la restauration!"
                max-height="700px"
                contain
              />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-main>
    <heqtor-footer />
  </v-app>
</template>

<script>
import HeqtorFooter from '@/components/HeqtorFooter.vue'

export default {
  components: {
    HeqtorFooter,
  },
}
</script>
