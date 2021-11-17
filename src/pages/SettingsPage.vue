<template>
  <div class="settings-container">
    <div style="display: flex; flex-direction: column">
      <label>
        <input v-model="ignoreNounLengthLimit" type="checkbox" />
        명사 길이 제한 무시<br>
        <small>세 글자 이상의 명사도 몰?루화합니다.</small>
      </label>

      <label style="margin-top: 1rem">
        <input v-model="forceMollufyForPredefinedWords" type="checkbox" />
        일부 단어 강제 몰?루화<br>
        <small>문장에 "몰루"와 같이 잘 알려진 밈 단어가 발견되면 "몰?루"와 같이 무조건 치환됩니다.</small>
      </label>
    </div>

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

  get forceMollufyForPredefinedWords() {
    return this.$store.state.mollufyOptions.forceMollufyForPredefinedWords;
  }

  set forceMollufyForPredefinedWords(value: boolean) {
    this.$store.commit("forceMollufyForPredefinedWords", value);
  }
}
</script>
