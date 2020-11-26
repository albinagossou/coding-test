<template>
  <v-card>
    <v-card-title>
      Mon Entreprise
      <v-spacer />
      <v-icon color="info" large>mdi-bank</v-icon>
    </v-card-title>
    <v-divider />
    <v-card-text>
      <v-card outlined>
        <v-card-title>Mon entreprise</v-card-title>
        <v-card-text v-if="company" class="text-center">
          Infos de l'entreprise
        </v-card-text>
        <v-card-text v-else class="text-center">
          Pas encore dans une entreprise ! --> faire un formulaire de création
          ici ;)
        </v-card-text>
      </v-card>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      company: (state) => state.me.company,
    }),
  },
}
</script>
