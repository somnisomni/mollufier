<template>
  <div class="settings-container">
    <div class="settings-items-container">
      <label for="ignoreNounLengthLimit">
        <input v-model="ignoreNounLengthLimit"
               type="checkbox"
               name="ignoreNounLengthLimit" />
        명사 길이 제한 무시<br>
        <small>세 글자 이상의 명사도 몰?루화합니다.</small>
      </label>

      <label for="changeMolluMark">
        <input v-model="changeMolluMark"
               type="checkbox"
               name="changeMolluMark" />
        삽입될 기호를 느낌표(!)로 변경<br>
        <small>몰?루 대신 아!루</small>
      </label>

      <label for="forceMollufyForPredefinedWords">
        <input v-model="forceMollufyForPredefinedWords"
               type="checkbox"
               name="forceMollufyForPredefinedWords" />
        일부 단어 강제 몰?루화<br>
        <small>문장에 "몰루"와 같이 잘 알려진 밈 단어가 발견되면 "몰?루"와 같이 무조건 치환됩니다.</small>
      </label>

      <label for="enableMolluImageAnimation">
        <input v-model="enableMolluImageAnimation"
               type="checkbox"
               name="enableMolluImageAnimation" />
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
  get ignoreNounLengthLimit() {
    return useSettingsStore().mollufyOptions.ignoreNounLengthLimit;
  }

  set ignoreNounLengthLimit(value: boolean) {
    useSettingsStore().mollufyOptions.ignoreNounLengthLimit = value;
  }

  get changeMolluMark() {
    return useSettingsStore().mollufyOptions.changeMolluMark;
  }

  set changeMolluMark(value: boolean) {
    useSettingsStore().mollufyOptions.changeMolluMark = value;
  }

  get forceMollufyForPredefinedWords() {
    return useSettingsStore().mollufyOptions.forceMollufyForPredefinedWords;
  }

  set forceMollufyForPredefinedWords(value: boolean) {
    useSettingsStore().mollufyOptions.forceMollufyForPredefinedWords = value;
  }

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
