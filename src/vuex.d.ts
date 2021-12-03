import { Store } from "vuex";

declare module "@vue/runtime-core" {
  interface State {
    appVersion: string,

    enableMolluImageAnimation: boolean,
    mollufyOptions: IMollufyOptions,
  }

  interface ComponentCustomProperties { $store: Store<State> }
}
