<template>
  <div class="settings-container">
    <label><input v-model="ignoreNounLengthLimit" type="checkbox" /> 명사 길이 제한 무시</label>

    <div><br><br>더 많은 설정이 구현될 예정입니다!</div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class SettingsPage extends Vue {
  get ignoreNounLengthLimit() {
    return this.$store.state.mollufyOptions.ignoreNounLengthLimit;
  }

  set ignoreNounLengthLimit(value: boolean) {
    this.$store.commit("ignoreNounLengthLimit", value);
  }
}
</script>
