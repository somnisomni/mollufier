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
              :disabled="mollufyDisabled"
              @click="clearChats">
        <img src="@/assets/images/mdi-delete.svg" />
      </button>

      <input v-model="sentenceToMollu"
             @keydown.enter.exact="doMollufy"
             @keydown.ctrl.enter.exact="doMollufy"
             :disabled="mollufyDisabled"
             type="text"
             placeholder="몰?루화할 문장 입력..."
             autofocus />
    </div>

    <button @click="doMollufy"
            :disabled="mollufyDisabled">몰?루화!</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import stringHash from "string-hash";
import ChatItem from "@/components/ChatItem.vue";
import mollufy, { checkHealth } from "@/scripts/mollufy";
import { IChatItem } from "@/scripts/interfaces";

@Options({
  components: {
    ChatItem,
  },
})
export default class MollufyPage extends Vue {
  sentenceToMollu = "블루 아카이브 정말 건전하고 건강하고 밝은 게임인데...";
  mollufyDisabled = false;

  chats: Array<IChatItem> = [];

  async created(): Promise<void> {
    /* SERVER HEALTH CHECK */
    if(!await checkHealth()) {
      this.onServerNotRespond();
    }

    /* INITIAL MOLLUFY */
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

      if(mollufied) {
        if(this.$store.state.mollufyOptions.forceMollufyForPredefinedWords) {
          ["몰루", "아루", "네루", "코하루"].forEach((word) => {
            const startWord = word.slice(0, word.length - 1);
            const endWord = word.slice(word.length - 1);

            mollufied = mollufied!.replaceAll(word, `${startWord}?${endWord}`);
          });
        }

        this.chats.push({
          by: "arona",
          content: mollufied,
          hash: stringHash(mollufied),
        });
      } else {
        this.onServerNotRespond();
      }

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

  onServerNotRespond() {
    const errorMessage = "몰?루파이어 서버에 연결할 수 없습니다. 페이지를 새로고침해보거나 나중에 다시 접속해주세요.";

    this.chats.push({
      by: "arona",
      content: errorMessage,
      hash: stringHash(errorMessage),
    });

    this.sentenceToMollu = "";
    this.mollufyDisabled = true;
  }
}
</script>
