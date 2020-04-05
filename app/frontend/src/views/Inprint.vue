<template>
  <div>
    <nav-bar style="position:relative;z-index:1" />
    <v-content>
      <div class="section">
        <div class="container">
          <article>
            <span class="meta-data">Last updated: 30. March 2020</span>
            <h1>Terms of use</h1>
            <h3>Disclaimer</h3>
            <p>
              These Terms of Use apply to www.ubs.com as well as any other affiliated sites, digital
              services, or applications on which a link to these Terms of Use appears (collectively,
              the "UBS Website") and apply to all visitors. These Terms of Use and any other terms
              that appear on the page from which you were directed to these Terms of Use govern your
              use of the UBS Website. By accessing the UBS Website, you agree to be legally bound by
              the Terms of Use then in effect. Please also refer to the relevant additional legal
              information applicable to your country.
            </p>
            <p>
              These Terms of Use as well as the
              information and materials contained in the UBS Website are subject to change at any
              time and from time to time, without notice. UBS may add features to or remove features
              from the UBS Website at any time and from time to time in our sole discretion.
              Continued access to the UBS Website following any modification in these Terms of
              Use will constitute your acceptance of the Terms of Use as modified.
            </p>
            <p>
              If you do not agree to be bound by these Terms of Use, do not use the UBS Website.
            </p>
            <h3>Access Subject to Local Restrictions</h3>
            <p>
              The UBS Website and all information and functionalities contained within them are
              not directed at or intended for use by any person resident or located in any
              jurisdiction where (1) the distribution of such information or functionality
              is contrary to the laws of such jurisdiction; or (2) such distribution is
              prohibited without obtaining the necessary licenses or authorizations by the relevant
              branch, subsidiary or affiliate office of UBS and such licenses or authorizations
              have not been obtained.
            </p>
            <h3>Services and Products</h3>
            <p>
              Products and services displayed on the UBS Website may not be eligible for sale
              or available to residents of certain countries or certain categories of investors.
              Please consult the applicable terms and conditions such as sales restrictions or
              key specific notes for further information.
            </p>
          </article>
        </div>
      </div>
    </v-content>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Home",
  components: {
    NavBar,
  },
  data: () => ({
    url: "",
  }),
};
</script>

<style scoped>
.container {
  max-width: 960px;
}

article{
  margin-bottom: 96px;
}

article h1{
  font-size: 32px;
  font-weight: 600;
}
article h3{
  margin-bottom: 1em;
  font-size: 18px;
}

article .meta-data{
  color: #90A4AE;
  font-size: 14px;
  margin-bottom: 16px;
  margin-top: 32px;
  display: block;
}
</style>
