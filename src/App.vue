<template>
  <div class="momotalk-wrapper">
    <div class="momotalk-container">
      <div class="title-container">
        <span class="title">몰루파이어 <small>Mollufier</small></span>

        <div class="title-icons-container">

        </div>
      </div>

      <div class="content-container">
        <div class="left-tab">
          <div class="tab active"><img src="@/assets/images/mdi-pencil.svg" /></div>
          <div class="tab"><img src="@/assets/images/mdi-cog.svg" /></div>
          <div class="tab"><img src="@/assets/images/mdi-info.svg" /></div>
        </div>

        <div class="content-wrapper">
          <div class="chat-container"
               ref="chatContainer">
            <transition-group name="slide-up">
              <chat-item v-for="chat in chats"
                         :key="chat.hash"
                         :chatData="chat" />
            </transition-group>
          </div>

          <div class="input-container">
            <input v-model="sentenceToMollu"
                   @keypress.ctrl.enter="doMollufy"
                   type="text"
                   placeholder="몰?루화할 문장 입력..."
                   autofocus />

            <button @click="doMollufy">몰?루화!</button>
          </div>
        </div>
      </div>

      <img class="container-background-image"
           src="@/assets/images/mollu_coconutcorn.png" />
    </div>
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
export default class App extends Vue {
  sentenceToMollu = "장비를 정지합니다";
  ignoreNounLengthLimit = false;

  chats: Array<IChatItem> = [];

  created(): void {
    this.doMollufy();
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
      const mollufied = await mollufy({
        sentence,
        options: {
          ignoreNounLengthLimit: this.ignoreNounLengthLimit,
        },
      });

      this.chats.push({
        by: "arona",
        content: mollufied,
        hash: stringHash(mollufied),
      });

      /* SCROLL CHAT CONTAINER TO BOTTOM */
      setTimeout(() => {
        const chatContainer = this.$refs.chatContainer as HTMLElement;
        chatContainer.scrollTo({
          top: chatContainer.scrollHeight,
          behavior: "smooth",
        });
      }, 50);
    }
  }
}
</script>
