import { defineStore } from "pinia";
import { version } from "@/../package.json";
import { ref } from "vue";

const useAppStore = defineStore("app", () => {
  const appVersion = version;
  const gaEnabled  = ref(false);

  return {
    appVersion,
    gaEnabled,
  };
});

export default useAppStore;
