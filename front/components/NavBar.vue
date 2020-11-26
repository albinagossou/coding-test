<template>
  <div>
    <v-app-bar app color="white" elevate-on-scroll height="96">
      <v-toolbar-title class="my-auto mx-4">
        <nuxt-link to="/home">
          <v-img
            src="/logo-full.png"
            alt="Heqtor"
            contain
            max-height="72"
            max-width="120"
          />
        </nuxt-link>
      </v-toolbar-title>

      <v-spacer />

      <v-btn
        v-for="link in links.filter((link) => link.toolbar)"
        :key="`${link.name}-toolbar`"
        rounded
        :color="link.color || 'primary'"
        :to="link.to && link"
        :nuxt="link.to"
        :disabled="link.disabled"
        active-class="background-color: success"
        class="hidden-xs-only my-auto mx-4"
        style="text-transform: none"
        :fab="$vuetify.breakpoint.mdAndDown"
        :small="$vuetify.breakpoint.mdAndDown"
      >
        <v-icon :left="$vuetify.breakpoint.lgAndUp">
          {{ link.icon }}
        </v-icon>
        {{ $vuetify.breakpoint.lgAndUp ? link.label : '' }}
      </v-btn>

      <v-btn icon class="my-auto mx-4" @click="drawer = !drawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" fixed right temporary>
      <v-list-item two-line>
        <v-list-item-avatar color="primary">
          <v-icon class="white--text" v-text="'mdi-account'"></v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>
            {{ isLoggedIn ? user.firstName : 'Prénom' }}
            {{ isLoggedIn ? user.lastName : 'Nom' }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ isLoggedIn ? user.username : '' }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-list flat>
        <v-list-item
          v-for="link in links"
          :key="`${link.name}-drawer`"
          link
          :color="link.disabled ? '' : link.color || 'primary'"
          :to="link.to && link"
          :nuxt="link.to"
          :input-value="!link.to"
          :disabled="link.disabled"
          @click="navDrawerItemClickHandler(link.onClick)"
        >
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ link.label }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  data() {
    return {
      drawer: false,
      links: [
        {
          name: 'home',
          label: 'Accueil',
          icon: 'mdi-home',
          to: true,
        },
        {
          name: 'profile',
          label: 'Mon profil',
          icon: 'mdi-account',
          toolbar: true,
          to: true,
        },
        {
          name: 'other',
          label: 'Autre onglet',
          icon: 'mdi-clipboard-text-outline',
          toolbar: true,
          to: true,
          disabled: true,
        },
        {
          name: 'logout',
          label: 'Se déconnecter',
          icon: 'mdi-logout-variant',
          color: 'error',
          onClick: this.logout,
        },
      ],
    }
  },
  computed: {
    ...mapState({
      user: (state) => state.auth.user,
    }),
    ...mapGetters({
      isLoggedIn: 'auth/isLoggedIn',
    }),
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout')
      this.$router.push({ name: 'auth' })
    },
    navDrawerItemClickHandler(onClickFunc) {
      if (!onClickFunc) return
      return onClickFunc()
    },
  },
}
</script>
