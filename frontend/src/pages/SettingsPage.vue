<template>
  <div class="settings-container">
    <div class="settings-items-container">
      <h3 style="margin-block-start: 0.5em">설정은 자동으로 저장됩니다.</h3>

      <label>
        <input v-model="ignoreNounLengthLimit"
               type="checkbox">
        명사 길이 제한 무시<br>
        <small>세 글자 이상의 명사도 몰?루화합니다.</small>
      </label>

      <label>
        <input v-model="changeMolluMark"
               type="checkbox">
        삽입될 기호를 느낌표(!)로 변경<br>
        <small>몰?루 대신 아!루</small>
      </label>

      <label>
        <input v-model="forceMollufyForPredefinedWords"
               type="checkbox">
        일부 단어 강제 몰?루화<br>
        <small>문장에 "몰루"와 같이 잘 알려진 밈 단어가 발견되면 "몰?루"와 같이 무조건 치환됩니다.</small>
      </label>

      <label>
        <input v-model="enableMolluImageAnimation"
               type="checkbox">
        몰?루 배경 일러스트 애니메이션 활성화<br>
        <small>"정말 꼴받게 하네요~"</small>
      </label>
    </div>
  </div>
</template>

<script lang="ts">
import useSettingsStore from "@/plugins/store/settings";
import { Component, Vue } from "vue-facing-decorator";

@Component({})
export default class SettingsPage extends Vue {
  /* mollufyOptions.ignoreNounLengthLimit */
  get ignoreNounLengthLimit() {
    return useSettingsStore().mollufyOptions.ignoreNounLengthLimit;
  }
  set ignoreNounLengthLimit(value: boolean) {
    useSettingsStore().mollufyOptions.ignoreNounLengthLimit = value;
  }

  /* mollufyOptions.changeMolluMark */
  get changeMolluMark() {
    return useSettingsStore().mollufyOptions.changeMolluMark;
  }
  set changeMolluMark(value: boolean) {
    useSettingsStore().mollufyOptions.changeMolluMark = value;
  }

  /* mollufyOptions.forceMollufyForPredefinedWords */
  get forceMollufyForPredefinedWords() {
    return useSettingsStore().mollufyOptions.forceMollufyForPredefinedWords;
  }
  set forceMollufyForPredefinedWords(value: boolean) {
    useSettingsStore().mollufyOptions.forceMollufyForPredefinedWords = value;
  }

  /* enableMolluImageAnimation */
  get enableMolluImageAnimation() {
    return useSettingsStore().enableMolluImageAnimation;
  }
  set enableMolluImageAnimation(value: boolean) {
    useSettingsStore().enableMolluImageAnimation = value;
  }
}
</script>

<style lang="scss" scoped>
.settings-container {
  line-height: 1.25;

  .settings-items-container {
    display: flex;
    flex-direction: column;

    label {
      margin-top: 1rem;

      &:first-child { margin-top: initial; }
    }
  }
}
</style>
