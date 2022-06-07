import { createStore } from "vuex";
import { version } from "@/../package.json";

export default createStore({
  state: {
    appVersion: version,

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
