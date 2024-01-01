import { defineStore } from "pinia";
import { reactive, ref } from "vue";

const useSettingsStore = defineStore("settings", () => {
  const enableMolluImageAnimation = ref(true);
  const mollufyOptions = reactive({
    ignoreNounLengthLimit: false,
    changeMolluMark: false,
    forceMollufyForPredefinedWords: true,
  });

  return {
    enableMolluImageAnimation,
    mollufyOptions,
  };
}, {
  persist: {
    storage: localStorage,
  },
});

export default useSettingsStore;
