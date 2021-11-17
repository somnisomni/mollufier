import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import MollufyPage from "@/pages/MollufyPage.vue";
import SettingsPage from "@/pages/SettingsPage.vue";
import AboutPage from "@/pages/AboutPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "mollufy",
    component: MollufyPage,
  },
  {
    path: "/settings",
    name: "settings",
    component: SettingsPage,
  },
  {
    path: "/about",
    name: "about",
    component: AboutPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
