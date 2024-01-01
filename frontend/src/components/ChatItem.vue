<template>
  <div class="chat-item"
       :class="{ user: fromUser, mollu: !fromUser }">
    <div v-if="fromUser"
         class="chat-balloon">
      <div class="chat-balloon-content">{{ chatData.content }}</div>
    </div>

    <div v-else>
      <img class="profile-image"
           src="@/assets/images/mollu_coconutcorn.png"
           alt="아로나 프로필 이미지" />

      <div class="chat-balloon-wrapper">
        <div class="profile-name">아로?나</div>
        <div class="chat-balloon">
          <div class="chat-balloon-content">{{ chatData.content }}</div>
          <button class="chat-balloon-copy-button"
                  @click="copyToClipboard(chatData.content)">
            <img src="@/assets/images/mdi-content-copy.svg"
                 alt="몰?루화된 문장 복사" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-facing-decorator";
import { IChatItem } from "@/scripts/interfaces";

@Component({})
export default class ChatItem extends Vue {
  @Prop({ required: true }) chatData!: IChatItem;

  get fromUser() {
    return this.chatData.by === "user";
  }

  async copyToClipboard(content: string) {
    try {
      await navigator.clipboard.writeText(content);
      alert("클립보드에 복사되었습니다.");
    } catch {
      alert("클립보드에 복사하는 중 오류가 발생했습니다.");
    }
  }
}
</script>
