# 환경변수 가이드

> 루트 `.env.example`이 단일 소스. Vercel에서는 각 프로젝트에 별도 설정.

## AIGrit (aigrit.dev)

| 변수 | 용도 | 발급처 |
|---|---|---|
| `NEXT_PUBLIC_GA_ID` | GA4 측정 ID | analytics.google.com |
| `NEXT_PUBLIC_ADSENSE_ID` | 애드센스 게시자 ID (`ca-pub-` + 숫자 16자리, `pub-…`도 허용) — 이 값 하나로 광고 스크립트·`google-adsense-account` 메타·`/ads.txt`가 함께 생성됨 | adsense.google.com → 계정 → 계정 정보 |
| `NEXT_PUBLIC_ADSENSE_IN_ARTICLE_SLOT` | 글 내 광고 슬롯 ID (선택, 승인 후) | adsense.google.com → 광고 → 광고 단위 |
| `NEXT_PUBLIC_GISCUS_REPO` | 댓글 GitHub 저장소 | giscus.app |
| `NEXT_PUBLIC_GISCUS_REPO_ID` | Giscus 저장소 ID | giscus.app |
| `NEXT_PUBLIC_GISCUS_CATEGORY` | Giscus 카테고리명 | giscus.app |
| `NEXT_PUBLIC_GISCUS_CATEGORY_ID` | Giscus 카테고리 ID | giscus.app |
| `NEXT_PUBLIC_SITE_URL` | 사이트 URL | `https://aigrit.dev` |
| `INDEXNOW_KEY_AIGRIT` | IndexNow API 키 | Bing Webmaster Tools |

## babipanote (babipanote.com)

광고 비활성 — AdSense·IndexNow 변수 없음.

| 변수 | 용도 | 발급처 |
|---|---|---|
| `NEXT_PUBLIC_GA_ID` | GA4 측정 ID (AIGrit과 별도) | analytics.google.com |
| `NEXT_PUBLIC_GISCUS_REPO` | 댓글 GitHub 저장소 (별도) | giscus.app |
| `NEXT_PUBLIC_GISCUS_REPO_ID` | Giscus 저장소 ID | giscus.app |
| `NEXT_PUBLIC_GISCUS_CATEGORY` | Giscus 카테고리명 | giscus.app |
| `NEXT_PUBLIC_GISCUS_CATEGORY_ID` | Giscus 카테고리 ID | giscus.app |
| `NEXT_PUBLIC_SITE_URL` | 사이트 URL | `https://babipanote.com` |
| `INDEXNOW_KEY_BABIPANOTE` | IndexNow API 키 | Bing Webmaster Tools |

## 규칙

- `.env.local` 절대 커밋 금지 (.gitignore에 포함)
- `NEXT_PUBLIC_` 접두사 = 클라이언트 노출. 시크릿에 쓰지 않는다
- Vercel Environment Variables에서 Production/Preview/Development 분리 설정
- 새 변수 추가 시 반드시 `.env.example`에도 추가
