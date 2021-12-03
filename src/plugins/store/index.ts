import { createStore } from "vuex";

export default createStore({
  state: {
    appVersion: "0.2.3",

    enableMolluImageAnimation: true,
    mollufyOptions: {
      ignoreNounLengthLimit: false,
      forceMollufyForPredefinedWords: true,
    },
  },
  mutations: {
    enableMolluImageAnimation(state, payload: boolean) {
      state.enableMolluImageAnimation = payload;
    },
    ignoreNounLengthLimit(state, payload: boolean) {
      state.mollufyOptions.ignoreNounLengthLimit = payload;
    },
    forceMollufyForPredefinedWords(state, payload: boolean) {
      state.mollufyOptions.forceMollufyForPredefinedWords = payload;
    },
  },
});
