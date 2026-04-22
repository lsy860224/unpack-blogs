# 네이버 블로그도 시작했다 — 스크린샷 캡쳐 가이드

**대상 글:** [apps/babipanote/content/posts/naver-dual-platform-strategy.mdx](../../apps/babipanote/content/posts/naver-dual-platform-strategy.mdx)
**발행 예정일:** 2026-04-22 23:30
**타입:** babipanote buildlog (unpack-blogs 구축기)
**preflight 기준:** 본문 이미지 1+장, 내부 링크 2~3+, 외부 링크 1+, 1,500~2,500자

## 이미지 목록 (총 3장 + OG)

### [자동 생성 필요] — Figma / Napkin

#### `og.png` — OG 썸네일 1200×630
- **경로:** `apps/babipanote/public/images/naver-dual-platform-strategy/og.png`
- **디자인:** babipanote Plum(#6B2E4E) + Terracotta(#C89F7C) 종이 질감
- **카피:** "네이버 블로그도 시작했다 — 이중 플랫폼으로 간 이유"
- **생성 방법:** Figma MCP 또는 `docs/THUMBNAIL.md` 템플릿

#### `01-revenue-structure.png` — 구글 vs 네이버 수익 구조 비교 (1600×900)
- **경로:** `apps/babipanote/public/images/naver-dual-platform-strategy/01-revenue-structure.png`
- **구성:** 2열 비교 차트 (광고 CPC / 협찬 / 공구 / 제휴링크)
- **생성 방법:** Napkin AI 비교 차트 (`mcp__napkin-ai__generate_and_save`)

#### `03-3month-dashboard.png` — 3개월 관측 대시보드 목업 (1600×900)
- **경로:** `apps/babipanote/public/images/naver-dual-platform-strategy/03-3month-dashboard.png`
- **구성:** 3개 채널 KPI 대시보드 목업 (이웃 / 방문자 / 체험단 / 에디션 발행 수)
- **생성 방법:** Figma 대시보드 템플릿

### [사용자 캡쳐 필요]

#### `02-naver-setup.png` — 네이버 블로그 개설·관리 화면
- **경로:** `apps/babipanote/public/images/naver-dual-platform-strategy/02-naver-setup.png`
- **도구:** [네이버 블로그](https://blog.naver.com) "babipa의 AIGrit"
- **캡쳐 방법**:
  1. 네이버 블로그 "관리" 페이지 접속
  2. 블로그 정보 · 카테고리 4개(AI 도구 후기 / 부업 탐구 / IT 일상 / 리포트) 설정 화면
  3. 또는 블로그 홈 화면 (상단 블로그명 + 첫 글 카드 보이게)
- **권장 영역**: 브라우저 창 전체 (가로 1,600~1,800)
- **민감정보**: 네이버 ID · 이메일 · 우측 개인정보 영역 마스킹
- **테마**: 라이트 (babipanote 잉크·종이 톤과 조화)

## 규격 공통

- PNG/WebP, 가로 1,600px 권장
- 파일당 300KB 이하 (OG 200KB 이하)
- `Cmd+Shift+4` → 스페이스 → 창 클릭 (그림자 포함)
- `sips --resampleHeightWidthMax 1600 file.png --out file.png`

## 내용 체크

- [x] 글자수 4,500+자 (1,500~2,500 권장 초과 — 빌더 저널로 길어도 OK)
- [x] 내부 링크 4개 (최소 2~3) — craft-naver-workflow, week1-sprint-two-blogs, aigrit-month1-revenue, obsidian-seo-dashboard
- [x] 외부 링크 1개 — adpost.naver.com
- [x] 첫 문단 스토리 훅 (역피라미드 금지 규칙 준수)

## 준비 상태

- [ ] 자동 생성 2장 + OG (01, 03, og)
- [ ] 사용자 캡쳐 1장 (02) — 네이버 블로그 관리 화면

**캡쳐/생성 완료 후**: 해당 경로에 PNG 드롭 → 다음 커밋 시 자동 반영. MDX는 이미 참조 경로를 포함하고 있어 수정 불필요.
