import { createStore } from "vuex";

export default createStore({
  state: {
    appVersion: "0.2.0",

    mollufyOptions: {
      ignoreNounLengthLimit: false,
    },
  },
  mutations: {
    ignoreNounLengthLimit(state, payload: boolean) {
      state.mollufyOptions.ignoreNounLengthLimit = payload;
    },
  },
});
