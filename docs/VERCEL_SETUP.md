# Vercel 배포 체크리스트

> 모노레포 1개 → Vercel 프로젝트 2개 셋업 체크리스트. 각 프로젝트는 앱 디렉토리를 Root Directory로 사용합니다.
> 이 문서는 **사용자 수동 작업 목록**입니다. 저장소에는 필요한 `vercel.json`·`.env.example`이 이미 포함되어 있습니다.

## 0. 사전 준비
- [ ] GitHub 저장소 `lsy860224/unpack-blogs` 확인 (Vercel이 읽을 수 있어야 함)
- [ ] Vercel 계정(GitHub 로그인) + GitHub 앱 연결
- [ ] 도메인 `aigrit.dev` / `babipanote.com` 확보

## 1. AIGrit 프로젝트 생성
- [ ] Vercel Dashboard → **Add New → Project** → `unpack-blogs` 선택 → Import
- [ ] **Configure Project**:
  - Project Name: `aigrit`
  - Framework Preset: Next.js (자동 감지)
  - **Root Directory**: `apps/aigrit`  ← 중요
  - Build/Install/Ignore Command: `apps/aigrit/vercel.json`이 자동 주입되므로 Dashboard에서 해당 필드는 비워둬도 됩니다 (Vercel이 vercel.json 값을 우선 적용)
- [ ] **Environment Variables**:
  ```
  NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
  NEXT_PUBLIC_ADSENSE_ID=ca-pub-XXXXXXXXXXXXXXXX
  NEXT_PUBLIC_ADSENSE_IN_ARTICLE_SLOT=XXXXXXXXXX       # 선택
  NEXT_PUBLIC_GISCUS_REPO=lsy860224/aigrit-comments
  NEXT_PUBLIC_GISCUS_REPO_ID=R_XXXXXXXXXX
  NEXT_PUBLIC_GISCUS_CATEGORY=Announcements
  NEXT_PUBLIC_GISCUS_CATEGORY_ID=DIC_XXXXXXXXXX
  NEXT_PUBLIC_SITE_URL=https://aigrit.dev
  ```
  Production + Preview + Development 모두 체크
- [ ] **Deploy** 클릭 → 첫 빌드 성공 확인
- [ ] **Settings → Domains** → `aigrit.dev` + `www.aigrit.dev`(www → apex 리다이렉트) 등록
  - DNS: 외부 레지스트라면 A `76.76.21.21`, CNAME `www → cname.vercel-dns.com.` 또는 Vercel 네임서버로 위임

## 2. babipanote 프로젝트 생성 (같은 저장소)
- [ ] Vercel Dashboard → **Add New → Project** → `unpack-blogs` 선택 → Import (같은 저장소에서 두 번째 프로젝트)
- [ ] **Configure Project**:
  - Project Name: `babipanote`
  - Framework Preset: Next.js
  - **Root Directory**: `apps/babipanote`  ← 중요
- [ ] **Environment Variables** (AdSense 관련 **제외**):
  ```
  NEXT_PUBLIC_GA_ID=G-YYYYYYYYYY                        # aigrit과 별도 측정 ID
  NEXT_PUBLIC_GISCUS_REPO=lsy860224/babipanote-comments
  NEXT_PUBLIC_GISCUS_REPO_ID=R_XXXXXXXXXX
  NEXT_PUBLIC_GISCUS_CATEGORY=Announcements
  NEXT_PUBLIC_GISCUS_CATEGORY_ID=DIC_XXXXXXXXXX
  NEXT_PUBLIC_SITE_URL=https://babipanote.com
  ```
- [ ] **Deploy** → 빌드 성공 확인
- [ ] **Settings → Domains** → `babipanote.com` 등록

## 3. Giscus 설정 (두 사이트 각각)
- [ ] https://giscus.app
  - Repository: `lsy860224/aigrit-comments` (aigrit) / `lsy860224/babipanote-comments` (babipanote)
  - 각 저장소에서 **Settings → Discussions 활성화** → Giscus가 읽을 수 있는 `Announcements` 또는 `Comments` 카테고리 생성
  - 발급된 `data-repo-id` / `data-category` / `data-category-id` 값을 Vercel 환경변수에 복사
- [ ] giscus 앱(https://github.com/apps/giscus)을 저장소에 설치

## 4. GA4 (두 사이트 각각)
- [ ] https://analytics.google.com → 관리 → **속성 2개 생성** (aigrit.dev / babipanote.com)
- [ ] 각각 **데이터 스트림 → 웹** → 도메인 입력 → `G-XXXXXX` 측정 ID 발급
- [ ] 측정 ID를 각 Vercel 프로젝트의 `NEXT_PUBLIC_GA_ID`에 입력

## 5. AdSense (AIGrit만, 글 15~20편 누적 후)
- [ ] https://adsense.google.com → 사이트 추가 → `aigrit.dev`
- [ ] Publisher ID(`ca-pub-...`)를 `NEXT_PUBLIC_ADSENSE_ID`에 입력
- [ ] "글 내 광고(In-Article)" 단위 생성 → slot ID를 `NEXT_PUBLIC_ADSENSE_IN_ARTICLE_SLOT`에 입력
- [ ] ads.txt 등록: Vercel Dashboard → **Settings → Functions / Redirects** 또는 `apps/aigrit/public/ads.txt` 직접 추가
- [ ] Google Search Console에서 aigrit.dev 소유권 확인 + 사이트맵 `https://aigrit.dev/sitemap.xml` 제출

## 6. 첫 배포 검증 (두 사이트 각각)
- [ ] Production URL 접속 → 홈 렌더 확인
- [ ] `/blog`, `/blog/hello-world` (aigrit) · `/blog/hello-world` (babipanote) 렌더 확인
- [ ] `/privacy`, `/disclaimer` (aigrit) 접근 가능
- [ ] `/robots.txt`, `/sitemap.xml` 생성 확인
- [ ] 브라우저 DevTools → Console에 에러 없음
- [ ] GA4 실시간 보고서에서 방문자 카운트 확인

## 참고 문서
- 상세 배포/CI 설명: `apps/aigrit/docs/DEPLOYMENT.md`
- SEO·수익화 전략: `apps/aigrit/docs/SEO_MONETIZATION.md`
- 브랜드 규격: `apps/{aigrit,babipanote}/docs/BRAND_GUIDELINES.md`
