<template>
  <div class="chat-container"
        ref="chatContainer">
    <div v-if="chats.length === 0"
         style="margin-top: 1rem; text-align: center; opacity: 0.5;">몰?루화한 문장 내역이 여기에 표시됩니다.</div>

    <transition-group name="slide-up">
      <chat-item v-for="chat in chats"
                 :key="chat.hash"
                 :chatData="chat" />
    </transition-group>
  </div>

  <div class="input-container">
    <div class="input-area-wrapper">
      <button title="채팅 내역 비우기"
              @click="clearChats">
        <img src="@/assets/images/mdi-delete.svg" />
      </button>

      <input v-model="sentenceToMollu"
             @keydown.enter.exact="doMollufy"
             @keydown.ctrl.enter.exact="doMollufy"
             type="text"
             placeholder="몰?루화할 문장 입력..."
             autofocus />
    </div>

    <button @click="doMollufy">몰?루화!</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import stringHash from "string-hash";
import ChatItem from "@/components/ChatItem.vue";
import mollufy from "@/scripts/mollufy";
import { IChatItem } from "@/scripts/interfaces";

@Options({
  components: {
    ChatItem,
  },
})
export default class MollufyPage extends Vue {
  sentenceToMollu = "장비를 정지합니다";

  chats: Array<IChatItem> = [];

  created(): void {
    this.doMollufy();
  }

  activated(): void {
    this.chatContainerScrollToEnd();
  }

  async doMollufy() {
    const sentence = this.sentenceToMollu.trim();

    if(sentence.length > 0) {
      /* USER CHAT */
      this.chats.push({
        by: "user",
        content: this.sentenceToMollu,
        hash: stringHash(this.sentenceToMollu),
      });

      this.sentenceToMollu = "";

      /* ARONA(MOLLU) CHAT */
      let mollufied = await mollufy({
        sentence,
        options: {
          ignoreNounLengthLimit: this.$store.state.mollufyOptions.ignoreNounLengthLimit,
        },
      });

      if(this.$store.state.mollufyOptions.forceMollufyForPredefinedWords) {
        ["몰루", "아루", "네루", "코하루"].forEach((word) => {
          const startWord = word.slice(0, word.length - 1);
          const endWord = word.slice(word.length - 1);

          mollufied = mollufied.replaceAll(word, `${startWord}?${endWord}`);
        });
      }

      this.chats.push({
        by: "arona",
        content: mollufied,
        hash: stringHash(mollufied),
      });

      /* SCROLL CHAT CONTAINER TO BOTTOM */
      setTimeout(this.chatContainerScrollToEnd, 50);
    }
  }

  clearChats(): void {
    this.chats = [];
  }

  chatContainerScrollToEnd(): void {
    const chatContainer = this.$refs.chatContainer as HTMLElement;

    chatContainer.scrollTo({
      top: chatContainer.scrollHeight,
      behavior: "smooth",
    });
  }
}
</script>