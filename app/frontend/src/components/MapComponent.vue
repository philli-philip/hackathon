<template>
  <div>
    <span v-if="loading">Loading...</span>
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 750px; width: 100%"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-geo-json
        :geojson="geojson_border"
        :options-style="{ color: 'grey', weight: 2, fillOpacity: 0.7, opacity:0 }"
      />
      <l-geo-json
        :geojson="geojson_canton"
        :options-style="{ color: '#FF0000', weight: 1, fillOpacity: 0, opacity:1 }"
      />
      <l-geo-json
        ref="hosp"
        :geojson="geojson_hosp"
        :options="options"
      />
    </l-map>
  </div>
</template>

<script>
import L from "leaflet";
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
      zoom: 8,
      center: [46.8182, 8.2275],
      geojson_hosp: null,
      geojson_border: null,
      geojson_canton: null,
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution: "&copy; <a href=\"http://osm.org/copyright\">OpenStreetMap</a> contributors",

      options: {
        pointToLayer: function on(feature, latlng) {
          return new L.CircleMarker(latlng, {
            radius: 5,
            weight: 2,
            fillOpacity: 0.5,
            opacity: 0.5,
            color: "#1565C0",
          });
        },
        onEachFeature: function onEachFeature(feature, layer) {
          layer.bindPopup(feature.properties.name);
        },
      },
    };
  },

  updated() {
    this.$nextTick(() => {
      this.$refs.hosp.mapObject.bringToFront();
    });
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
