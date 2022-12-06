<template>
  <div class="momotalk-wrapper">
    <div class="momotalk-container">
      <div class="title-container">
        <span class="title">몰?루파이어 <small>Mollufier</small></span>

        <div class="title-icons-container">

        </div>
      </div>

      <div class="content-container">
        <div class="left-tab">
          <router-link to="/" replace class="tab active">
            <img src="@/assets/images/mdi-pencil.svg"
                 alt="메인 페이지" />
          </router-link>
          <router-link to="/settings" replace class="tab">
            <img src="@/assets/images/mdi-cog.svg"
                 alt="설정 페이지" />
          </router-link>
          <router-link to="/about" replace class="tab">
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
           :class="{ anim: $store.state.enableMolluImageAnimation }" />
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class App extends Vue { }
</script>
