<template>
  <div>
    <nav-bar />
    <v-content>
      <hello-world />
      <map-component />
    </v-content>
  </div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import NavBar from "@/components/NavBar.vue";
import MapComponent from "@/components/MapComponent.vue";


export default {
  name: "Home",
  components: {
    HelloWorld,
    NavBar,
    MapComponent,

  },
  data: () => ({
    url: "",
  }),
};
</script>
