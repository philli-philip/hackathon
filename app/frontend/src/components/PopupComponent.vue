<template>
  <v-card
    v-if="show"
    style="position: absolute; right: 2%; top:20%"
    width="325"
  >
    <v-card-text>
      <div>Updated {{ lastUpdate }} minutes ago</div>
      <p class="title text--primary">
        {{ name }}
      </p>
      <v-container class="px-0">
        <v-row>
          <v-col>
            <div class="font-weight-bold text--primary">
              ICU Low Care
            </div>
            <v-chip
              color="green lighten-3"
              class="pl-0"
              text-color="white"
            >
              <v-chip
                text-color="white"
                class="green mr-2"
              >
                {{ icuLow }}
              </v-chip>
              available
            </v-chip>
          </v-col>
          <v-col>
            <div class="font-weight-bold text--primary">
              ICU High Care
            </div>
            <v-chip
              color="red lighten-3"
              class="pl-0"
              text-color="white"
            >
              <v-chip
                text-color="white"
                class="red mr-2"
              >
                {{ icuHigh }}
              </v-chip>
              available
            </v-chip>
          </v-col>
        </v-row>
      </v-container>

      <div class="font-weight-bold text--primary">
        Contact information
      </div>
      <div class="subtitle-1 text--primary">
        {{ address }}
      </div>
      <div class="subtitle-1 text--primary">
        {{ phone }}
      </div>
    </v-card-text>
    <v-card-actions>
      <v-btn
        color="primary"
        outlined
        @click.native="show=!show"
      >
        close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
export default {
  data: () => ({
    show: false,
    lastUpdate: 7,
    name: "Universätsspital Zürich",
    icuLow: 400,
    icuHigh: 25,
    address: "Rämistrasse 100, 8091 Zürich",
    phone: "+41 61 000 00 00",

  }),

  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === "set") {
        this.show = true;
        this.name = state.properties.name;
      }
    });
  },
};
</script>
