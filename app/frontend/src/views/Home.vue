<template>
  <div>
    <nav-bar />
    <v-content>
      <map-component />
    </v-content>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import MapComponent from "@/components/MapComponent.vue";


export default {
  name: "Home",
  components: {
    NavBar,
    MapComponent,

  },
  data: () => ({
    url: "",
  }),
};
</script>
