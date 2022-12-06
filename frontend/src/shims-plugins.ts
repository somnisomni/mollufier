import { Store } from "vuex";
import { IStoreState } from "@/scripts/interfaces";

declare module "@vue/runtime-core" {
  interface ComponentCustomProperties {
    $store: Store<IStoreState>,
  }
}
