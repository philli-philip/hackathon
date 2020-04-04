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
      style="height: 700px; width: 100%"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-geo-json
        v-if="show"
        :geojson="geojson_hosp"
        :options="options"
      />
      <l-geo-json
        v-if="show"
        :geojson="geojson_border"
        :options-style="{ color: 'grey', weight: 2, fillOpacity: 0.6, opacity:0 }"
      />
      <l-geo-json
        v-if="show"
        :geojson="geojson_canton"
        :options-style="{ color: '#FF0000', weight: 1, fillOpacity: 0, opacity:1 }"
      />
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
  },
  data() {
    return {
      loading: false,
      show: true,
      enableTooltip: true,
      zoom: 8,
      center: [46.8182, 8.2275],
      geojson_hosp: null,
      geojson_border: null,
      geojson_canton: null,
      fillColor: "#e4ce7f",
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        "&copy; <a href=\"http://osm.org/copyright\">OpenStreetMap</a> contributors",
    };
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
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
    let response = await fetch(
      "https://raw.githubusercontent.com/uversusvirus/swiss-hospital-data/master/data/openstreetmap_exports/Swiss_Healthcare_Facilities_OSM-2020-03-22.geojson",
    );
    let data = await response.json();
    this.geojson_hosp = data;

    response = await fetch(
      "https://raw.githubusercontent.com/ZHB/switzerland-geojson/master/country/switzerland.geojson",
    );
    data = await response.json();

    data.features[0].geometry.coordinates[0].unshift(
      [0, 90],
      [180, 90],
      [180, -90],
      [0, -90],
      [-180, -90],
      [-180, 0],
      [-180, 90],
      [0, 90],
    );
    this.geojson_border = data;

    response = await fetch(
      "https://raw.githubusercontent.com/rsandstroem/IPythonNotebooks/master/GeoMapsFoliumDemo/switzerland.geojson",
    );
    data = await response.json();
    this.geojson_canton = data;

    this.loading = false;
  },
};
</script>
