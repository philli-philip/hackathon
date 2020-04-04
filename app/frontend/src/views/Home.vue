<template>
  <div>
    <nav-bar />
    <v-content>
      <informationPanel />
      <map-component />
    </v-content>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import MapComponent from "@/components/MapComponent.vue";
import informationPanel from "@/components/informationPanel.vue";


export default {
  name: "Home",
  components: {
    NavBar,
    MapComponent,
    informationPanel,

  },
  data: () => ({
    url: "",
  }),
};
</script>
