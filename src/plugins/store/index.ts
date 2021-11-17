import { createStore } from "vuex";

export default createStore({
  state: {
    appVersion: "0.2.2",

    mollufyOptions: {
      ignoreNounLengthLimit: false,
      forceMollufyForPredefinedWords: true,
    },
  },
  mutations: {
    ignoreNounLengthLimit(state, payload: boolean) {
      state.mollufyOptions.ignoreNounLengthLimit = payload;
    },
    forceMollufyForPredefinedWords(state, payload: boolean) {
      state.mollufyOptions.forceMollufyForPredefinedWords = payload;
    },
  },
});
