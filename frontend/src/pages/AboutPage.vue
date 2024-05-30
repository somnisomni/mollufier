<template>
  <div class="about-container">
    <div>
      <h1>몰?루파이어 <small>v{{ appVersion }}</small></h1>
      <p>명사 사이에 물음표를 넣어주어 문장을 "몰?루화"해줍니다.</p>
      <p style="color: gray"><s>프라나 사랑해</s></p>
    </div>

    <hr />

    <div>
      <h2>참고 사항</h2>
      <p>
        <strong>이 웹 서비스는 팬메이드 사이트로, 수익을 얻기 위해 운영하는 사이트가 아닙니다.</strong><br />
        이 웹 서비스는 게임 "블루 아카이브"의 개발사 및 유통/운영사와 전혀 무관한 사이트이며, 그러한 기업 또는 단체로부터 어떠한 형태로든 지원이나 지시를 받은 사실이 없습니다.<br />
        사용자는 이 웹 서비스를 이용하는 순간부터, <strong>사용자가 받는 모든 불이익에 대해 개발자는 책임질 의무가 없음에 동의</strong>한 것으로 간주합니다.<br />

      </p>
    </div>

    <hr />

    <div>
      <h2>크레딧</h2>

      <p v-for="credit in CREDITS" :key="credit.description">
        <span>{{ credit.description }} : </span>

        <a v-if="credit.link" :href="credit.link" target="_blank">{{ credit.name }}</a>
        <span v-else>{{ credit.name }}</span>

        <small v-for="subtitle in credit.subtitles" :key="subtitle.text" style="display: block; color: slategray">
          <span>{{ subtitle.text }}</span>
          <a v-if="subtitle.link" :href="subtitle.link" target="_blank">{{ subtitle.link }}</a>
        </small>
      </p>
    </div>

    <hr />

    <div>
      <h2>사용한 오픈 소스 라이브러리</h2>

      <p v-for="os in OPENSOURCES" :key="os.name">
        <b>{{ os.name }}</b>
        <span v-if="os.description"> — {{ os.description }}</span>

        <small style="display: block; color: slategray">
          <span>{{ os.license }}</span>
          <span> | </span>
          <a :href="os.link.link" target="_blank">{{ os.link.name }}</a>
        </small>
      </p>
    </div>

    <div v-if="isGAEnabled">
      <hr />
      <p>이 웹 앱은 방문 통계 확인용으로 Google Analytics를 사용합니다. 사용자가 입력한 문장 및 기타 민감한 데이터는 서버에 저장하거나 Google 및 타 서비스에 공유하지 않습니다.</p>
    </div>
  </div>
</template>

<script lang="ts">
import useAppStore from "@/plugins/store/app";
import { Component, Vue } from "vue-facing-decorator";

interface ICredit {
  description: string;
  name: string;
  link?: string;
  subtitles?: {
    text: string;
    link?: string;
  }[];
}

interface IOpenSource {
  name: string;
  description?: string;
  license: "MIT License" | "GNU LGPL" | "BSD License" | "CC0";
  link: {
    name: string;
    link: string;
  };
}

@Component({})
export default class AboutPage extends Vue {
  readonly CREDITS: Array<ICredit> = [
    {
      description: "만든이",
      name: "somni (@somni_somni)",
      link: "https://twitter.com/somni_somni",
      subtitles: [
        {
          text: "MIT License | 소스 코드 : ",
          link: "https://github.com/somnisomni/mollufier",
        },
      ],
    },
    {
      description: "아로나 몰?루 일러스트",
      name: "coconutcorn",
      link: "https://www.pixiv.net/users/64509815",
      subtitles: [
        {
          text: "\"블루아카콘!\"에서 가져옴. ",
          link: "https://www.pixiv.net/artworks/90203134",
        },
      ],
    },
    {
      description: "배경 이미지",
      name: "게임 \"블루 아카이브\"",
      link: "https://bluearchive.nexon.com/",
      subtitles: [
        {
          text: "Copyright ⓒ NEXON GAMES Co., Ltd.",
        },
      ],
    },
    {
      description: "사용된 폰트",
      name: "경기도 서체 (경기천년제목)",
      link: "https://www.gg.go.kr/contents/contents.do?ciIdx=679&menuId=2457",
    },
  ];

  readonly OPENSOURCES: Array<IOpenSource> = [
    {
      name: "Kiwi",
      description: "지능형 한국어 형태소 분석기",
      license: "GNU LGPL",
      link: {
        name: "GitHub",
        link: "https://github.com/bab2min/Kiwi",
      },
    },
    {
      name: "Kiwipiepy",
      description: "Python용 Kiwi 패키지",
      license: "GNU LGPL",
      link: {
        name: "GitHub",
        link: "https://github.com/bab2min/kiwipiepy",
      },
    },
    {
      name: "Flask",
      description: "A lightweight WSGI web application framework",
      license: "BSD License",
      link: {
        name: "홈페이지",
        link: "https://flask.palletsprojects.com/",
      },
    },
    {
      name: "Flask-CORS",
      description: "A Flask extension for handling Cross Origin Resource Sharing (CORS)",
      license: "MIT License",
      link: {
        name: "GitHub",
        link: "https://github.com/corydolphin/flask-cors",
      },
    },
    {
      name: "Vue.js",
      description: "The Progressive JavaScript Framework",
      license: "MIT License",
      link: {
        name: "홈페이지",
        link: "https://vuejs.org/",
      },
    },
    {
      name: "vue-facing-decorator",
      description: "Write class components by TypeScript decorator",
      license: "MIT License",
      link: {
        name: "홈페이지",
        link: "https://facing-dev.github.io/vue-facing-decorator/",
      },
    },
    {
      name: "vue-gtag",
      description: "Global Site Tag plugin for Vue",
      license: "MIT License",
      link: {
        name: "GitHub",
        link: "https://github.com/MatteoGabriele/vue-gtag",
      },
    },
    {
      name: "vue-router",
      description: "The official router for Vue.js",
      license: "MIT License",
      link: {
        name: "GitHub",
        link: "https://github.com/vuejs/router",
      },
    },
    {
      name: "Pinia",
      description: "The intuitive store for Vue.js",
      license: "MIT License",
      link: {
        name: "홈페이지",
        link: "https://pinia.vuejs.org/",
      },
    },
    {
      name: "pinia-plugin-persistedstate",
      description: "Configurable persistence and rehydration for Pinia stores",
      license: "MIT License",
      link: {
        name: "홈페이지",
        link: "https://prazdevs.github.io/pinia-plugin-persistedstate/",
      },
    },
    {
      name: "core-js",
      description: "Standard library",
      license: "MIT License",
      link: {
        name: "GitHub",
        link: "https://github.com/zloirock/core-js",
      },
    },
    {
      name: "string-hash",
      description: "Fast string hash function for Node.JS",
      license: "CC0",
      link: {
        name: "GitHub",
        link: "https://github.com/darkskyapp/string-hash",
      },
    },
  ];

  get appVersion(): string {
    return useAppStore().appVersion;
  }

  get isGAEnabled(): boolean {
    return useAppStore().gaEnabled;
  }
}
</script>

<style lang="scss">
.about-container {
  line-height: 1.25;

  hr {
    border: none;
    border-bottom: 2px solid slategray;
  }

  a {
    display: inline-block;
    position: relative;
    color: currentColor;
    text-decoration: none;

    &::before {
      content: "";
      position: absolute;
      left: 0;
      bottom: 2px;
      right: 0;
      width: 100%;
      height: 2px;
      background-color: currentColor;
      opacity: 1;
      transition: bottom 0.25s, opacity 0.25s, height 0.25s;
    }

    &:hover {
      &::before {
        bottom: 0;
        height: 50%;
        opacity: 0.25;
      }
    }
  }
}
</style>
