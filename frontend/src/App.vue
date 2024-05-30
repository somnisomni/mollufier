<template>
  <div class="momotalk-wrapper">
    <div class="momotalk-container">
      <div class="title-container">
        <span class="title">몰?루파이어 <small>Mollufier</small></span>

        <div class="title-icons-container">
          <button class="menu" type="button" @click="toggleLeftTab">
            <img src="@/assets/images/bars.svg"
                 alt="메뉴" />
          </button>
        </div>
      </div>

      <div class="content-container">
        <div :class="['left-tab', { on: isLeftTabOn }]">
          <router-link to="/" replace class="tab active" @click="toggleLeftTab">
            <img src="@/assets/images/mdi-pencil.svg"
                 alt="메인 페이지" />
          </router-link>
          <router-link to="/settings" replace class="tab" @click="toggleLeftTab">
            <img src="@/assets/images/mdi-cog.svg"
                 alt="설정 페이지" />
          </router-link>
          <router-link to="/about" replace class="tab" @click="toggleLeftTab">
            <img src="@/assets/images/mdi-info.svg"
                 alt="몰?루파이어 정보 페이지" />
          </router-link>
        </div>

        <div class="content-wrapper">
          <router-view v-slot="{ Component }">
            <keep-alive>
              <component :is="Component" />
            </keep-alive>
          </router-view>
        </div>
      </div>

      <img class="container-background-image"
           src="@/assets/images/mollu_coconutcorn.png"
           alt="블루아카콘 by coconutcorn - 몰?루 이미지"
           :class="{ anim: useSettingsStore().enableMolluImageAnimation }" />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-facing-decorator";
import useAppStore from "./plugins/store/app";
import useSettingsStore from "./plugins/store/settings";

@Component({})
export default class App extends Vue {
  readonly useSettingsStore = useSettingsStore;
  isLeftTabOn: boolean = false;

  mounted(): void {
    if(useAppStore().gaEnabled) {
      console.debug("Google Analytics enabled");
    }
  }

  toggleLeftTab(): void {
    this.isLeftTabOn = !this.isLeftTabOn;
  }
}
</script>