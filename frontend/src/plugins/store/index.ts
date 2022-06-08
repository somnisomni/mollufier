import { createStore } from "vuex";
import { version } from "@/../package.json";

export default createStore({
  state: {
    appVersion: version,

    enableMolluImageAnimation: true,
    mollufyOptions: {
      ignoreNounLengthLimit: false,
      changeMolluMark: false,
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
    changeMolluMark(state, payload: boolean) {
      state.mollufyOptions.changeMolluMark = payload;
    },
    forceMollufyForPredefinedWords(state, payload: boolean) {
      state.mollufyOptions.forceMollufyForPredefinedWords = payload;
    },
  },
});
