<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="10" lg="8" xl="6">
        <v-fab-transition hide-on-leave>
          <div v-show="!createAccount">
            <v-card>
              <v-card-title>
                <h1 class="text-h4">Se connecter</h1>
              </v-card-title>
              <v-card-text class="text-right">
                <v-form>
                  <v-text-field
                    v-model="loginData.email"
                    label="E-mail"
                    type="email"
                    prepend-icon="mdi-email"
                    :error-messages="loginEmailErrors"
                    @input="$v.loginData.email.$touch()"
                    @blur="$v.loginData.email.$touch()"
                  />
                  <v-text-field
                    v-model="loginData.password"
                    :type="showPassword ? 'text' : 'password'"
                    label="Mot de passe"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    :error-messages="loginPasswordErrors"
                    @click:append="showPassword = !showPassword"
                    @input="$v.loginData.password.$touch()"
                    @blur="$v.loginData.password.$touch()"
                    @keydown.enter="login"
                  />
                </v-form>
              </v-card-text>
              <v-divider />
              <v-card-actions>
                <v-btn rounded color="info" text @click="changeCreateAccount">
                  Pas encore de compte ?
                </v-btn>
                <v-spacer />
                <v-btn
                  rounded
                  color="success"
                  :loading="loading"
                  @click="login"
                >
                  Se connecter
                </v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </v-fab-transition>
        <v-fab-transition hide-on-leave>
          <div v-show="createAccount">
            <v-card>
              <v-card-title>
                <h1 class="text-h4">Créer un compte</h1>
              </v-card-title>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="registerData.email"
                    label="E-mail"
                    type="email"
                    prepend-icon="mdi-email"
                    :error-messages="registerEmailErrors"
                    @input="$v.registerData.email.$touch()"
                    @blur="$v.registerData.email.$touch()"
                  />
                  <v-text-field
                    v-model="registerData.password"
                    :type="showPassword ? 'text' : 'password'"
                    label="Mot de passe"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    :error-messages="registerPasswordErrors"
                    @click:append="showPassword = !showPassword"
                    @input="$v.registerData.password.$touch()"
                    @blur="$v.registerData.password.$touch()"
                  />
                  <v-text-field
                    v-model="registerData.repeatPassword"
                    :type="showRepeatPassword ? 'text' : 'password'"
                    label="Répétez votre mot de passe"
                    prepend-icon="mdi-lock-outline"
                    :append-icon="
                      showRepeatPassword ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    :error-messages="registerRepeatPasswordErrors"
                    @click:append="showRepeatPassword = !showRepeatPassword"
                    @input="$v.registerData.repeatPassword.$touch()"
                    @blur="$v.registerData.repeatPassword.$touch()"
                  />
                  <v-text-field
                    v-model="registerData.firstName"
                    label="Prénom"
                    prepend-icon="mdi-account-circle"
                    :error-messages="registerFirstNameErrors"
                    @input="$v.registerData.firstName.$touch()"
                    @blur="$v.registerData.firstName.$touch()"
                  />
                  <v-text-field
                    v-model="registerData.lastName"
                    label="Nom"
                    prepend-icon="mdi-account-circle"
                    :error-messages="registerLastNameErrors"
                    @input="$v.registerData.lastName.$touch()"
                    @blur="$v.registerData.lastName.$touch()"
                  />
                </v-form>
              </v-card-text>
              <v-divider />
              <v-card-actions>
                <v-btn rounded color="info" text @click="changeCreateAccount">
                  Déjà inscrit ?
                </v-btn>
                <v-spacer />
                <v-btn
                  rounded
                  color="success"
                  :loading="loading"
                  @click="register"
                >
                  Créer mon compte
                </v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </v-fab-transition>
        <v-snackbar v-model="error" right>
          {{ errorText }}
          <v-btn color="error" text @click="error = false">Fermer</v-btn>
        </v-snackbar>
        <v-snackbar v-model="success" right>
          {{ successText }}
          <v-btn color="success" text @click="success = false">Fermer</v-btn>
        </v-snackbar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'

export default {
  layout: 'not-logged-in',
  data() {
    return {
      error: false,
      errorText: '',
      success: false,
      successText: '',

      createAccount: false,

      showPassword: false,
      showRepeatPassword: false,

      loginData: this.createFreshLoginData(),
      registerData: this.createFreshRegisterData(),

      loading: false,
    }
  },
  computed: {
    loginEmailErrors() {
      const errors = []
      if (!this.$v.loginData.email.$dirty) return errors
      !this.$v.loginData.email.email && errors.push('E-mail invalide.')
      !this.$v.loginData.email.required && errors.push('Un e-mail est requis.')
      return errors
    },
    loginPasswordErrors() {
      const errors = []
      if (!this.$v.loginData.password.$dirty) return errors
      !this.$v.loginData.password.minLength &&
        errors.push('Le mot de passe doit faire au moins 8 caractères.')
      !this.$v.loginData.password.required &&
        errors.push('Le mot de passe est requis.')
      return errors
    },
    registerEmailErrors() {
      const errors = []
      if (!this.$v.registerData.email.$dirty) return errors
      !this.$v.registerData.email.email && errors.push('E-mail invalide.')
      !this.$v.registerData.email.required &&
        errors.push('Un e-mail est requis.')
      return errors
    },
    registerPasswordErrors() {
      const errors = []
      if (!this.$v.registerData.password.$dirty) return errors
      !this.$v.registerData.password.minLength &&
        errors.push('Le mot de passe doit faire au moins 8 caractères.')
      !this.$v.registerData.password.required &&
        errors.push('Un mot de passe est requis.')
      !this.$v.registerData.password.goodPassword &&
        errors.push(
          'Le mot de passe doit être alphanumérique et comporter au moins une majuscule et un chiffre.'
        )
      return errors
    },
    registerRepeatPasswordErrors() {
      const errors = []
      if (!this.$v.registerData.repeatPassword.$dirty) return errors
      !this.$v.registerData.repeatPassword.sameAsPassword &&
        errors.push('Les deux mots de passe sont différents.')
      return errors
    },
    registerFirstNameErrors() {
      const errors = []
      if (!this.$v.registerData.firstName.$dirty) return errors
      !this.$v.registerData.firstName.required &&
        errors.push('Un prénom est requis.')
      return errors
    },
    registerLastNameErrors() {
      const errors = []
      if (!this.$v.registerData.lastName.$dirty) return errors
      !this.$v.registerData.lastName.required &&
        errors.push('Un nom de famille est requis.')
      return errors
    },
  },
  methods: {
    changeCreateAccount() {
      this.showPassword = false
      this.showRepeatPassword = false
      this.createAccount = !this.createAccount
      this.loginData = this.createFreshLoginData()
      this.registerData = this.createFreshRegisterData()
      this.$v.$reset()
    },
    createFreshLoginData() {
      return {
        email: '',
        password: '',
      }
    },
    createFreshRegisterData() {
      return {
        email: '',
        password: '',
        repeatPassword: '',
        firstName: '',
        lastName: '',
      }
    },
    login() {
      this.$v.loginData.$touch()
      if (!this.$v.loginData.$invalid) {
        this.loading = true
        this.$store
          .dispatch('auth/login', this.loginData)
          .then(() => {
            this.$router.push('/home')
            this.loading = false
            this.loginData = this.createFreshLoginData()
            this.$v.$reset()
          })
          .catch((err) => {
            this.loading = false
            this.error = true
            this.errorText =
              err.response && err.response.data && err.response.data.error
                ? err.response.data.error
                : err
          })
      }
    },
    register() {
      this.$v.registerData.$touch()
      if (!this.$v.registerData.$invalid) {
        this.loading = true
        this.$store
          .dispatch('auth/register', this.registerData)
          .then(() => {
            this.$router.push('/home')
            this.loading = false
            this.registerData = this.createFreshRegisterData()
            this.$v.$reset()
          })
          .catch((err) => {
            this.loading = false
            this.error = true
            this.errorText =
              err.response && err.response.data && err.response.data.error
                ? err.response.data.error
                : err
          })
      }
    },
  },
  head() {
    return {
      titleTemplate: '%s',
    }
  },
  validations: {
    loginData: {
      email: { required, email },
      password: {
        required,
        minLength: minLength(8),
      },
    },
    registerData: {
      email: { required, email },
      password: {
        required,
        minLength: minLength(8),
        goodPassword: (password) => {
          return (
            /[a-z]/.test(password) &&
            /[A-Z]/.test(password) &&
            /[0-9]/.test(password)
          )
        },
      },
      repeatPassword: {
        sameAsPassword: sameAs('password'),
      },
      firstName: { required },
      lastName: { required },
    },
  },
}
</script>
