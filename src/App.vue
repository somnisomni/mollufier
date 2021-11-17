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
          <router-link to="/"
                       class="tab active">
            <img src="@/assets/images/mdi-pencil.svg" />
          </router-link>
          <router-link to="/settings"
                       class="tab">
            <img src="@/assets/images/mdi-cog.svg" />
          </router-link>
          <router-link to="/about"
                       class="tab">
            <img src="@/assets/images/mdi-info.svg" />
          </router-link>
        </div>

        <div class="content-wrapper">
          <keep-alive>
            <router-view />
          </keep-alive>
        </div>
      </div>

      <img class="container-background-image"
           src="@/assets/images/mollu_coconutcorn.png" />
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class App extends Vue { }
</script>
