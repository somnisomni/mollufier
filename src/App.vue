<template>
  <div>
    <textarea v-model="sentenceToMollu"
              placeholder="몰?루화할 문장 입력" />
    <button @click="doMollufy">몰?루화!</button>
    <textarea v-model="sentenceMollufied"
              placeholder="몰?루화된 문장"
              disabled />
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import axios, { AxiosError } from "axios";

export default class App extends Vue {
  sentenceToMollu = "";
  sentenceMollufied = "";

  async doMollufy() {
    try {
      const response = await axios.post(`${process.env.VUE_APP_BACKEND_BASE_URL}/mollufy`, {
        sentence: this.sentenceToMollu,
      }, {
        responseType: "json",
      });

      this.sentenceMollufied = response.data.content;
    } catch { /* NO ACTION */ }
  }
}
</script>
