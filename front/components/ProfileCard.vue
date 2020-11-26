<template>
  <v-card>
    <v-card-title>
      Mon Profil
      <v-spacer />
      <v-icon color="info" large>mdi-card-account-details</v-icon>
    </v-card-title>
    <v-divider />
    <v-card-text>
      <v-card outlined>
        <v-card-title>Mes informations</v-card-title>
        <v-card-text class="text-center">
          <v-form>
            <v-text-field
              v-model="profileData.email"
              label="E-mail"
              type="email"
              prepend-icon="mdi-email"
              disabled
            />
            <v-text-field
              v-model="profileData.firstName"
              label="Prénom"
              prepend-icon="mdi-account-circle"
              disabled
            />
            <v-text-field
              v-model="profileData.lastName"
              label="Nom"
              prepend-icon="mdi-account-circle"
              disabled
            />
            <v-text-field
              v-model="profileData.phone"
              label="Téléphone"
              prepend-icon="mdi-phone-settings"
              :error-messages="profilePhoneErrors"
              @input="$v.profileData.phone.$touch()"
              @blur="$v.profileData.phone.$touch()"
              @keydown.enter="updateProfile"
            />
          </v-form>
          <v-btn
            rounded
            color="success"
            :loading="updateProfileLoading"
            @click="updateProfile"
          >
            Mettre à jour
          </v-btn>
        </v-card-text>
      </v-card>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'
import { minLength, maxLength, numeric } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      profileData: this.createFreshProfileData(),
      updateProfileLoading: false,
    }
  },
  computed: {
    ...mapState({
      user: (state) => state.auth.user,
    }),
    profilePhoneErrors() {
      const errors = []
      if (!this.$v.profileData.phone.$dirty) return errors
      !this.$v.profileData.phone.numeric &&
        errors.push(
          'Numéro invalide : merci de respecter le format 0033xxxxxxxxx.'
        )
      !this.$v.profileData.phone.minLength &&
        errors.push(
          'Numéro invalide : merci de respecter le format 0033xxxxxxxxx.'
        )
      !this.$v.profileData.phone.maxLength &&
        errors.push(
          'Numéro invalide : merci de respecter le format 0033xxxxxxxxx.'
        )
      return errors
    },
  },
  mounted() {
    this.profileData = this.createFreshProfileData()
  },
  methods: {
    createFreshProfileData() {
      return {
        email: this.user ? this.user.email : '',
        firstName: this.user ? this.user.firstName : '',
        lastName: this.user ? this.user.lastName : '',
        phone: this.user && this.user.phone ? this.user.phone : '',
      }
    },
    updateProfile() {
      this.$v.profileData.$touch()
      if (!this.$v.profileData.$invalid) {
        this.updateProfileLoading = true
        this.$store
          .dispatch('me/updateProfile', this.profileData)
          .then(() => {
            this.updateProfileLoading = false
            this.profileData = this.createFreshProfileData()
            this.$v.profileData.$reset()
            this.$emit('update-profile-success')
          })
          .catch((err) => {
            this.updateProfileLoading = false
            this.profileData = this.createFreshProfileData()
            this.$v.profileData.$reset()
            this.$emit('update-profile-fail', err)
          })
      }
    },
  },
  validations: {
    profileData: {
      phone: { numeric, minLength: minLength(13), maxLength: maxLength(13) },
    },
  },
}
</script>
