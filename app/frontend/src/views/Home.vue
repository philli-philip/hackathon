<template>
  <div>
    <nav-bar style="position:relative;z-index:1" />
    <v-content>
      <map-component />
      <popup-component />
    </v-content>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import MapComponent from "@/components/MapComponent.vue";
import PopupComponent from "@/components/PopupComponent.vue";


export default {
  name: "Home",
  components: {
    NavBar,
    MapComponent,
    PopupComponent,

  },
  data: () => ({
    url: "",
  }),
};
</script>
