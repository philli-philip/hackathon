import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    properties: null,
    show: false,
  },
  mutations: {
    show(state) {
      state.show = true;
    },
    set(state, payload) {
      state.properties = payload.properties;
    },
  },
  actions: {
    show(context) {
      context.commit("show");
    },
    set({ commit }, payload) {
      commit("show", payload);
    },
  },
});
