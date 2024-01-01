<!-- eslint-disable vuejs-accessibility/form-control-has-label vuejs-accessibility/no-autofocus -->

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
        <img src="@/assets/images/mdi-delete.svg"
             alt="몰?루화 내역 삭제" />
      </button>

      <input v-model="sentenceToMollu"
             @keydown.enter.exact="doMollufy"
             @keydown.ctrl.enter.exact="doMollufy"
             :disabled="mollufyDisabled"
             type="text"
             :placeholder="'몰?루화할 문장 입력... (최대 ' + TEXT_LENGTH_LIMIT.toLocaleString() + '자)'"
             :maxlength="TEXT_LENGTH_LIMIT"
             autofocus />
    </div>

    <button @click="doMollufy"
            :disabled="mollufyDisabled">몰?루화!</button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-facing-decorator";
import stringHash from "string-hash";
import { event } from "vue-gtag";
import ChatItem from "@/components/ChatItem.vue";
import mollufy, { checkHealth } from "@/scripts/mollufy";
import { IChatItem } from "@/scripts/interfaces";
import useSettingsStore from "@/plugins/store/settings";
import useAppStore from "@/plugins/store/app";

@Component({
  components: {
    ChatItem,
  },
})
export default class MollufyPage extends Vue {
  readonly TEXT_LENGTH_LIMIT = 1000;

  sentenceToMollu = "블루 아카이브 정말 건전하고 건강하고 밝은 게임인데...";
  mollufyDisabled = false;
  mollufiable = true; // abuse guard

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
    if(!this.mollufiable) {
      alert("너무 빠르게 몰?루화하면 아로?나가 아파해요!");
      return;
    }

    const sentence = this.sentenceToMollu.trim().substring(0, this.TEXT_LENGTH_LIMIT);

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
          ignoreNounLengthLimit: useSettingsStore().mollufyOptions.ignoreNounLengthLimit,
          changeMolluMark: useSettingsStore().mollufyOptions.changeMolluMark,
        },
      });

      if(mollufied) {
        if(useSettingsStore().mollufyOptions.forceMollufyForPredefinedWords) {
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

        /* Send GA event */
        if(useAppStore().gaEnabled) {
          event("do_mollufy", {
            event_category: "engagement",
            event_label: "Mollufy success",
            description: useAppStore().appVersion,
          });
        }
      } else {
        this.onServerNotRespond();
      }

      /* SCROLL CHAT CONTAINER TO BOTTOM */
      setTimeout(this.chatContainerScrollToEnd, 50);

      /* ABUSE GUARD */
      this.mollufiable = false;
      setTimeout(() => { this.mollufiable = true; }, 500);
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

    /* Send GA event */
    if(useAppStore().gaEnabled) {
      event("do_mollufy", {
        event_category: "engagement",
        event_label: "Mollufy failed (server error)",
        description: useAppStore().appVersion,
      });
    }
  }
}
</script>
