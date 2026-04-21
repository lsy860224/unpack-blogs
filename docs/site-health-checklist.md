# Site Health Checklist

## 점검 주기 매트릭스

| 점검 항목 | 주기 | 실행 주체 | 대응 프롬프트 |
|---|---|---|---|
| Lighthouse (LCP/CLS/TBT) | 매 PR | GitHub Actions | — |
| 번들 사이즈 | 매 PR | GitHub Actions (bundlewatch) | — |
| CLAUDE.md 200줄 초과 | 매 PR | GitHub Actions | — |
| 의존성 보안 | 주 1회 | Dependabot | — |
| 깨진 링크 | 월 1회 | GitHub Actions (cron) | — |
| CLAUDE.md 비대화 감사 | 월 1회 | Claude Code | 프롬프트 3 |
| SEO·수익 헬스 | 월 1회 | Claude Code | 프롬프트 4 |
| UX/기능 리뷰 | 분기 1회 | Claude Code | 프롬프트 2 |
| 접근성 재점검 | 분기 1회 | Claude Code | 프롬프트 5 |
| 디자인 일관성 | Figma 변경 시 | Claude Code | 프롬프트 1 |
| 접근성 초기 감사 | 런칭 전 1회 | Claude Code | 프롬프트 5 |

---

## 1. 성능 (Performance)

### Core Web Vitals 임계값

| 지표 | Good | Needs improvement | Poor |
|---|---|---|---|
| LCP | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| CLS | ≤ 0.1 | ≤ 0.25 | > 0.25 |
| INP | ≤ 200ms | ≤ 500ms | > 500ms |
| TBT | ≤ 200ms | ≤ 600ms | > 600ms |
| FCP | ≤ 1.8s | ≤ 3.0s | > 3.0s |

### 번들 예산

| 라우트 | JS (gzip) | CSS (gzip) |
|---|---|---|
| `/` (홈) | ≤ 120KB | ≤ 20KB |
| `/blog/[slug]` | ≤ 150KB | ≤ 25KB |
| 기타 | ≤ 100KB | ≤ 20KB |

- 초과 시 Lighthouse CI 가 PR fail 처리.

---

## 2. SEO

### 메타태그 (모든 라우트 필수)

- [ ] `<title>` 60자 이내
- [ ] `<meta name="description">` 150~160자
- [ ] Open Graph (og:title, og:description, og:image, og:url)
- [ ] Twitter Card (twitter:card summary_large_image, twitter:image)
- [ ] `<link rel="canonical">` 정확히 설정

### 구조화 데이터 (JSON-LD)

- [ ] 홈: `WebSite` + `SearchAction`
- [ ] 블로그 목록: `Blog`
- [ ] 블로그 상세: `Article` (author, datePublished, dateModified, image)
- [ ] FAQ 있는 글: `FAQPage`
- [ ] 모든 페이지: `BreadcrumbList`

### Sitemap & Robots

- [ ] `sitemap.xml` 에 모든 공개 라우트 포함
- [ ] `robots.txt` 에 sitemap 경로 선언
- [ ] draft/preview 페이지는 `noindex`
- [ ] Google Search Console / Naver 서치어드바이저 등록 확인

---

## 3. 접근성 (A11y)

### 필수 (WCAG 2.1 AA)

- [ ] Lighthouse a11y 90점 이상
- [ ] 모든 `<img>` 에 alt (장식용은 `alt=""`)
- [ ] heading 순서 정상 (h1 → h2 → h3, 건너뜀 금지)
- [ ] 페이지당 h1 1개
- [ ] 색 대비 비율 4.5:1 이상 (텍스트), 3:1 이상 (큰 텍스트)
- [ ] 키보드로 모든 인터랙션 가능
- [ ] `:focus-visible` 스타일 명확
- [ ] `<html lang="ko">` 또는 해당 언어 설정

### AdSense 심사 요건

- [ ] About / Privacy / Disclaimer 페이지 존재
- [ ] 연락처 정보 공개
- [ ] 콘텐츠 최소 15~20개
- [ ] 플레이스홀더 페이지 없음

---

## 4. 수익화

### AdSense

- [ ] `ca-pub-XXXX` 스크립트가 모든 페이지 `<head>` 에 로드
- [ ] `ads.txt` 배포 (`/ads.txt` 에서 접근 가능)
- [ ] 광고 슬롯 배치 일관성 (글 상단/중단/하단)
- [ ] 모바일에서 레이아웃 깨짐 없음
- [ ] CLS 유발 방지: 광고 슬롯에 `min-height` 확보

### 제휴 마케팅

- [ ] AffiliateLink 컴포넌트 사용 (직접 `<a>` 금지)
- [ ] 모든 제휴 링크 `rel="sponsored nofollow"`
- [ ] 제휴 포함 글에 Disclaimer 컴포넌트
- [ ] 쿠키 정책 페이지에 제휴 언급

---

## 5. 컨텐츠 품질

### MDX Frontmatter 필수 필드

- [ ] title
- [ ] date (ISO 형식)
- [ ] slug (kebab-case)
- [ ] description (150~160자)
- [ ] tags (배열)
- [ ] thumbnail (OG 이미지)

### 이미지

- [ ] WebP 또는 AVIF 포맷
- [ ] `next/image` 또는 동급 최적화 컴포넌트 사용
- [ ] alt 텍스트 존재
- [ ] 적절한 width/height 지정 (CLS 방지)

---

## 6. 보안 & 의존성

- [ ] `npm audit` 에서 High 이상 취약점 0건
- [ ] Dependabot 활성화
- [ ] `.env.local` 커밋 금지 (`.gitignore` 확인)
- [ ] 환경변수 값은 Vercel 대시보드에서만 관리
- [ ] 외부 이미지 로딩 시 `next.config.ts` 의 `remotePatterns` 화이트리스트만 허용

---

## 7. 모니터링

- [ ] GA4 설치 + 이벤트 발화 확인
- [ ] Vercel Analytics 활성화
- [ ] Search Console 에서 인덱싱 오류 주 1회 확인
- [ ] Giscus 댓글 정상 로딩

---

## 8. CLAUDE.md 규칙

- [ ] 200줄 이하 유지
- [ ] 디자인 토큰 값 직접 포함 금지 → `docs/design-system.md` 참조
- [ ] 상세 점검 절차 포함 금지 → 이 파일 참조
- [ ] 환경변수 값 포함 금지 → 변수명만 언급

---

## 9. 점검 로그

점검 결과는 `docs/inspection-log/YYYY-MM.md` 에 기록. 템플릿은 `_template.md`.
