<template>
  <div>
    <div>
      <span v-if="loading">Loading...</span>
      <label for="checkbox">Visibility</label>
      <input
        id="checkbox"
        v-model="show"
        type="checkbox"
      >
      <label for="checkboxTooltip">Tooltip</label>
      <input
        id="checkboxTooltip"
        v-model="enableTooltip"
        type="checkbox"
      >
      <br>
    </div>
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 600px; width: 600px"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-geo-json
        v-if="show"
        :geojson="geojson"
        :options="options"
        :options-style="styleFunction"
      />
      <l-marker :lat-lng="marker" />
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";

import {
  LMap, LTileLayer, LMarker, LGeoJson,
} from "vue2-leaflet";

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
    LMarker,
  },
  data() {
    return {
      loading: false,
      show: true,
      enableTooltip: true,
      zoom: 7,
      center: [46.8182, 8.2275],
      geojson: null,
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        "&copy; <a href=\"http://osm.org/copyright\">OpenStreetMap</a> contributors",
      marker: latLng(47.3769, 8.54172),
    };
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },
    styleFunction() {
      const { fillColor } = this;
      return () => ({
        weight: 2,
        color: "#ECEFF1",
        opacity: 1,
        fillColor,
        fillOpacity: 1,
      });
    },
    onEachFeatureFunction() {
      if (!this.enableTooltip) {
        return () => {};
      }
      return (feature, layer) => {
        layer.bindTooltip(
          `<div>name:${feature.properties.name}</div><div>phone: ${feature.properties.phone}</div>`,
          { permanent: false, sticky: true },
        );
      };
    },
  },
  async created() {
    this.loading = true;
    const response = await fetch(
      "https://raw.githubusercontent.com/uversusvirus/swiss-hospital-data/master/data/openstreetmap_exports/Swiss_Healthcare_Facilities_OSM-2020-03-22.geojson",
    );
    const data = await response.json();
    this.geojson = data;
    this.loading = false;
  },
};
</script>
