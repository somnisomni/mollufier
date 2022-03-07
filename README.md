<figure>
  <p align="center"><img src="docs/images/Screenshot-Mollufy-v0.2.3.png" style="width: 100%; max-width: 988px"></p>
  <figcaption><p align="center" style="color: gray"><s>" 내가 몰?루가 될께... "</s></p></figcaption>
</figure>

몰?루파이어
===========
소개
----
 몰?루파이어 <span style="color: gray">*(Mollufier, **몰↗?루↘파이어**처럼 발음합니다)*</span>는 사용자가 입력한 문장에서 형태소 분석기([Kiwi](https://github.com/bab2min/Kiwi))가 인식한 명사 사이에 물음표를 삽입해주는, 재미로 만든 토이 프로젝트입니다.

사용해보기
----------
 몰?루파이어는 현재 제 개인 서버에서 배포하고 있습니다. [**여기를 클릭해 사용해보세요!**](https://app.somni.one/mollufier)

아이디어
--------
<figure>
  <p align="center"><img src="docs/images/Idea-Tweet-SDSK.png" style="width: 80%; max-width: 826px"></p>
  <figcaption><p align="center" style="color: gray"><s>그런거 없으면 만들면 된다!</s></p></figcaption>
</figure>

Docker로 배포하기
-----------------
 [6d54e64](https://github.com/somnisomni/mollufier/commit/6d54e64defad66ab4af868b2003a83c17b5e8403) 커밋 이후로 Docker를 통해 간편히 앱을 배포(실행)할 수 있게 되었습니다.
 Docker Hub 등 컨테이너 이미지 저장소에 업로드하지 않기 때문에 이미지를 직접 빌드하여 배포해야 합니다.

  1. 몰?루파이어의 git 리포지토리를 clone 한 후, 리포지토리 루트에서 Docker 이미지를 빌드합니다.
   ```sh
   $ docker build -t mollufier:latest \
     --build-arg FE_PUBLIC_PATH="<public path>" \
     --build-arg FE_BACKEND_BASE_URL="<backend base url>"
     --build-arg FE_GA_MEASUREMENT_ID="<measurement id>" \ .
   ```
   - **빌드 인수 `FE_PUBLIC_PATH`** : *(선택적 인수, 기본값 `/`)* 앱의 프론트엔드가 배포되는 URL 주소의 루트 경로입니다.  
     프론트엔드 URL 루트가 도메인의 루트라면 기본값을 사용하면 됩니다. (ex. `https://example.com/`에 배포하는 경우)  
     하위 디렉토리에서 프론트엔드를 배포할 경우 도메인 루트부터 시작한 값으로 설정합니다. (ex. `https://example.com/mollufier`에 배포하는 경우 `/mollufier`로 인수 값 설정)
   - **빌드 인수 `FE_BACKEND_BASE_URL`** : *(선택적 인수, 기본값 `/api`)* 앱의 백엔드가 배포되는 URL입니다.  
     백엔드를 다른 URL 상에서 배포를 할 경우, 절대 또는 상대 경로의 URL을 값으로 설정합니다. (ex. `https://api.example.com/mollufier`에 배포하는 경우 그 URL을 그대로 인수 값 설정)
   - **빌드 인수 `FE_GA_MEASUREMENT_ID`** : *(선택적 인수, 기본값 공란)* Google Analytics 측정 ID입니다.  
     값을 지정하지 않거나 비어 있는 값을 지정할 경우 Google Analytics가 탑재되지 않습니다.
  2. 이미지 빌드가 완료되면 컨테이너를 생성하여 실행합니다.
   ```sh
   $ docker run -d \
     -p <host (frontend)>:8080 \
     -p <host (backend)>:8081 \
     mollufier:latest
   ```
   컨테이너 내부에서 프론트엔드는 포트 **8080**, 백엔드는 포트 **8081**로 실행됩니다. 포트 바인딩을 할 경우 이에 맞추어 바인딩하면 됩니다.
   
   > ※ **주의!** 이 리포지토리의 Dockerfile로 빌드하는 경우, 몰?루파이어의 프론트엔드와 백엔드는 각각 간단한 웹 서버([http-server](https://www.npmjs.com/package/http-server) 및 [Flask](https://flask.palletsprojects.com/))를 통해 실행됩니다.  
   > 프로덕션으로 배포하기에는 보안에 취약할 가능성이 크기 때문에, [nginx](http://nginx.org/) 등 고급 웹 서버 소프트웨어에서 제공하는 [리버스 프록시](https://www.cloudflare.com/ko-kr/learning/cdn/glossary/reverse-proxy/)를 이용한 배포가 권장됩니다.

라이선스
--------
 몰?루파이어는 [MIT 라이선스](LICENSE.md) 하에 오픈 소스로 공개하고 있습니다.

만든이 및 주의사항
------
 **솜니 (somni)** / [트위터](https://twitter.com/somni_somni), [GitHub](https://github.com/somnisomni)

  > ※ 본 서비스의 개발자 **솜니 (somni)** 는 사용자가 이 서비스를 이용함으로 인해 발생하는 모든 불이익과 분쟁에 대해 책임을 질 의무를 일절 갖지 않습니다.
  >
  > ※ 사용자가 본 서비스에 입력한 문장 등은 서버에 따로 <u>명시적으로 저장하고 있진 않습니다.</u> 단, 경찰 등 공공기관으로부터 수사 협조 요청이 발생할 경우 본 서비스 관련 로그 파일의 내용이 제공될 수 있습니다.
