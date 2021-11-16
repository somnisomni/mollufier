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
            <div v-for="(chat, index) in chats"
                 :key="index"
                 class="chat-item"
                 :class="{ user: chat.by === 'user', mollu: chat.by === 'arona' }">
              <div v-if="chat.by === 'user'"
                   class="chat-balloon">
                {{ chat.content }}
              </div>

              <div v-else-if="chat.by === 'arona'">
                <img class="profile-image" src="@/assets/images/mollu_coconutcorn.png" />

                <div class="chat-balloon-wrapper">
                  <div class="profile-name">아로?나</div>
                  <div class="chat-balloon">
                    {{ chat.content }}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="input-container">
            <input v-model="sentenceToMollu"
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
import { Vue } from "vue-class-component";
import mollufy from "@/scripts/mollufy";

interface IChatItem {
  by: "user" | "arona",
  content: string,
}

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
