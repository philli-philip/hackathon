<template>
  <v-app-bar
    color="grey lighten-5"
    shrink-on-scroll
    prominent
  >
    <h2 class="blue--text text--darken-3">
      ICU-CH
    </h2>
    <v-spacer />
    <v-app-bar-nav-icon />
  </v-app-bar>
</template>


<script>
export default {
  data: () => ({
    drawer: false,
  }),
};
</script>
