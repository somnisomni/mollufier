<template>
  <div class="about-container">
    <h1>몰?루파이어 <small>v{{ $store.state.appVersion }}</small></h1>
    <p>명사 사이에 물음표를 넣어주어 문장을 "몰?루화"해줍니다.</p>
    <p style="color: gray"><s>코하루 최고! 코하루는 순수해!</s></p>
    <br />
    <p>Made by <a href="https://twitter.com/somni_somni" target="_blank">somni (@somni_somni)</a></p>
    <p>지능형 한국어 형태소 분석기 <a href="https://github.com/bab2min/Kiwi">Kiwi</a> 사용</p>
    <p>소스 코드 : <a href="https://github.com/somnisomni/mollufier">GitHub</a></p>
    <p><a href="https://www.pixiv.net/artworks/89423246">블루아카콘</a> by <a href="https://www.pixiv.net/users/64509815" target="_blank">coconutcorn</a></p>
    <p>배경 이미지 from 게임 "블루아카이브"<br><small>Copyright ⓒ NAT GAMES Co., Ltd.</small></p>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class AboutPage extends Vue {

}
</script>