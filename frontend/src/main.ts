import { createApp } from "vue";
import VueGtag from "vue-gtag";
import { createPinia } from "pinia";
import piniaPluginPersistedState from "pinia-plugin-persistedstate";

import App from "@/App.vue";
import router from "@/plugins/router";
import useAppStore from "@/plugins/store/app";

import "@/styles/fonts.scss";
import "@/styles/transitions.scss";
import "@/styles/main.scss";

const app = createApp(App);
app.use(router);

const pinia = createPinia();
pinia.use(piniaPluginPersistedState);
app.use(pinia);

if(process.env.NODE_ENV === "production" && process.env.VUE_APP_GA_MEASUREMENT_ID) {
  app.use(VueGtag, {
    config: {
      id: process.env.VUE_APP_GA_MEASUREMENT_ID,
      params: {
        anonymize_ip: true,
      },
    },
    onReady() {
      useAppStore().gaEnabled = true;
    },
  }, router);
}

app.mount("#app");
