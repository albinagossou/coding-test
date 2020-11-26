<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="6">
        <profile-card
          class="fill-height"
          @update-profile-success="
            successText = 'Informations bien mises à jour !'
            success = true
          "
          @update-profile-fail="
            errorText =
              $event.response &&
              $event.response.data &&
              $event.response.data.error
                ? $event.response.data.error
                : $event
            error = true
          "
        />
      </v-col>
      <v-col cols="12" sm="6">
        <company-card />
      </v-col>
    </v-row>
    <v-snackbar v-model="error" right>
      {{ errorText }}
      <v-btn color="error" text @click="error = false">Fermer</v-btn>
    </v-snackbar>
    <v-snackbar v-model="success" right>
      {{ successText }}
      <v-btn color="success" text @click="success = false">Fermer</v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
import ProfileCard from '@/components/ProfileCard.vue'
import CompanyCard from '@/components/CompanyCard.vue'

export default {
  components: {
    ProfileCard,
    CompanyCard,
  },
  async fetch({ store }) {
    !store.state.auth.user && (await store.dispatch('me/getProfile'))
    !store.state.me.company && (await store.dispatch('me/fetchMyCompany'))
  },
  data() {
    return {
      success: false,
      successText: '',
      error: false,
      errorText: '',
    }
  },
}
</script>
