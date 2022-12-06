import { createApp } from "vue";
import VueGtag from "vue-gtag";

import App from "@/App.vue";
import router from "@/plugins/router";
import store from "@/plugins/store";

import "@/styles/fonts.scss";
import "@/styles/transitions.scss";
import "@/styles/main.scss";

const app = createApp(App);
app.use(store);
app.use(router);

if(process.env.NODE_ENV === "production" && process.env.VUE_APP_GA_MEASUREMENT_ID) {
  app.use(VueGtag, {
    config: {
      id: process.env.VUE_APP_GA_MEASUREMENT_ID,
      params: {
        anonymize_ip: true,
      },
    },
    onReady() {
      store.commit("setGAEnabledState", true);
    },
  }, router);
}

app.mount("#app");
