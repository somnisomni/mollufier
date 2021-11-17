import { Store } from "vuex";

declare module "@vue/runtime-core" {
  interface State {
    appVersion: string,

    mollufyOptions: IMollufyOptions,
  }

  interface ComponentCustomProperties { $store: Store<State> }
}
