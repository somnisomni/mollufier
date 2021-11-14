<template>
  <div class="momotalk-wrapper">
    <div class="momotalk-container">
      <div class="title-container">
        <span class="title">몰루파이어 <small>Mollufier</small></span>
      </div>

      <div class="content-container">
        <h4>한국어 형태소 분석기 <a href="https://github.com/bab2min/Kiwi" target="_blank">Kiwi</a>를 이용해 문장을 몰?루화해줍니다.</h4>
        <h4>사이트 디자인은 추후 작업 예정입니다... ㅠ</h4>

        <div class="content">
          <textarea v-model="sentenceToMollu"
                    placeholder="몰?루화할 문장 입력" />
          <button @click="doMollufy">몰?루화!</button>
          <label><input v-model="ignoreNounLengthLimit" type="checkbox" />명사 단어 길이 제한 무시</label>
          <textarea v-model="sentenceMollufied"
                    placeholder="몰?루화된 문장"
                    disabled />
        </div>

        <div>Made by <a href="https://twitter.com/somni_somni">somni (@somni_somni)</a></div>
      </div>

      <img class="container-background-image"
           src="@/assets/images/mollu_coconattsu_corn.png" />
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import mollufy from "@/scripts/mollufy";

export default class App extends Vue {
  sentenceToMollu = "장비를 정지합니다";
  sentenceMollufied = "";
  ignoreNounLengthLimit = false;

  created(): void {
    this.doMollufy();
  }

  async doMollufy() {
    this.sentenceMollufied = await mollufy({
      sentence: this.sentenceToMollu,
      options: {
        ignoreNounLengthLimit: this.ignoreNounLengthLimit,
      },
    });
  }
}
</script>

<style lang="scss" scoped>
textarea {
  min-width: 300px;
  min-height: 200px;
}

.content {
  display: flex;
  flex-direction: row;
  max-width: 500px;
  padding: 0 2vw;
}

.content > * {
  margin: 0.5rem 0;
}
</style>
