<template>
  <div class="chat-item"
       :class="{ user: fromUser, mollu: !fromUser }">
    <div v-if="fromUser"
         class="chat-balloon">
      {{ chatData.content }}
    </div>

    <div v-else>
      <img class="profile-image"
           src="@/assets/images/mollu_coconutcorn.png"
           alt="아로나 프로필 이미지" />

      <div class="chat-balloon-wrapper">
        <div class="profile-name">아로?나</div>
        <div class="chat-balloon">
          {{ chatData.content }}
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
}
</script>
