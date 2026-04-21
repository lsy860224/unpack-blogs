# CLAUDE.md — UnpackBlogs Monorepo

## 프로젝트 개요

Turborepo 모노레포 1개로 블로그 2개 + 네이버 에디션을 운영한다.

| | AIGrit (aigrit.dev) | babipanote (babipanote.com) | 네이버 (babipa의 AIGrit) |
|---|---|---|---|
| 포지션 | AI 도구 리뷰 | 빌더 저널 | AIGrit 리프레이밍 + 협찬 |
| 톤 | 전문적·비판적 | 솔직·일기체 | 생활·재테크 프레임 |
| 수익 | AdSense + 제휴 | 없음 | 애드포스트 + 협찬 |

## 기술 스택

Turborepo + pnpm · Next.js 16 (App Router, TS) · MDX · Tailwind CSS v4 · Vercel · GA4 · Giscus

## 핵심 구조

```
unpack-blogs/
├── packages/blog-core/     ← 공유 엔진
├── apps/aigrit/             ← brand.config.ts (광고 ON)
├── apps/babipanote/         ← brand.config.ts (광고 OFF)
├── docs/                    ← 분리 문서
└── .claude/                 ← hooks/ + rules/ + commands/
```

## 명령어

```bash
pnpm turbo run build                     # 전체 빌드
pnpm turbo run dev                        # 전체 dev
pnpm --filter @unpack/aigrit dev          # aigrit만
pnpm --filter @unpack/babipanote dev      # babipanote만
npx --no-install tsc --noEmit -p .        # 타입 체크
```

## 검증 — 커밋 전 반드시

1. `pnpm turbo run build` — 양쪽 빌드 통과
2. `npx --no-install tsc --noEmit` — 타입 에러 0
3. blog-core 수정 시 양쪽 사이트 로컬 확인

## 자동화 (.claude/)

단일 진실 공급원 — 실제 동작 명세는 아래 canonical 파일만 참조.

- Hooks — `.claude/hooks/` (스크립트) + `.claude/settings.json` (트리거)
- Rules — `.claude/rules/*.md` (파일 작업 시 자동 주입)
- Commands — `.claude/commands/` (`/publish-post` 등)

상세 설명과 디버깅 가이드는 `docs/HOOKS_RULES.md` 한 곳에서만 관리. 이 문서는 목차·진입점 역할만 한다.

---

## 🖊️ 글쓰기 워크플로우 — "글쓰기 시작" 시 이 순서를 따른다

### Step 1: 대상 확인

어느 블로그? (aigrit / babipanote) + 어떤 글? (slug 또는 번호)
→ 해당 글쓰기 가이드 읽기:
- AIGrit → `docs/POST_AIGRIT.md` + `docs/CONTENT_RULES.md`
- babipanote → `docs/POST_BABIPANOTE.md`
- 네이버 에디션 → `docs/POST_NAVER.md`

### Step 2: 초안 존재 확인

MDX 파일 체크:
- AIGrit: `apps/aigrit/content/posts/ko/{slug}.mdx`
- babipanote: `apps/babipanote/content/posts/{slug}.mdx`

있으면 → "수정 발행?" 확인. 없으면 → Step 3.

### Step 3: Craft 초안 확인

Craft `05. Blog Pipeline/01. In Progress/{AIGrit or babipanote}/` 확인.
- 있으면 → Step 4로
- 없으면 → Claude Desktop 프롬프트 제안 (`docs/PUBLISH_CHECKLIST.md` 참조)

### Step 4: OG 썸네일 + 에셋 점검

**4-1. OG 썸네일 자동 생성 — `docs/THUMBNAIL.md` 필독**

1. `docs/THUMBNAIL.md` 읽기 (사이트별 템플릿 스펙)
2. Figma MCP (`use_figma`)로 OG 프레임 생성 (1200×630)
3. `get_screenshot`으로 캡처 → `apps/{app}/public/images/{slug}/og.png` 저장
4. 실패 시 수동 Export 안내

**4-2. 본문 이미지 점검**

초안의 `{IMG:}` 마커 카운트 → 필요 이미지 목록 → 부족분 체크리스트:
```
📋 에셋 체크리스트 — {slug}
경로: apps/{app}/public/images/{slug}/
✅ og.png — Figma 자동 생성 완료
❌ 본문 이미지:
  - [ ] 01-name.png — "alt 설명" (스크린샷)
  - [ ] 02-name.png — "alt 설명" (스크린샷)
💡 준비 후 "에셋 준비됐어"라고 말해주세요.
```

### Step 5: MDX 변환 + 발행

Craft 초안 → frontmatter 생성 → 마커 치환 → slug 검증 → git push → IndexNow

### Step 6: 발행 후 안내

```
✅ 발행 완료: https://{domain}/blog/{slug}
📌 수동 작업: GSC 색인 · 네이버 수집 · Obsidian 상태 · Craft 아카이브
```

상세: `docs/PUBLISH_CHECKLIST.md`

---

## 문서 가이드

### 📝 글 작성

| 문서 | 언제 읽나 |
|---|---|
| `docs/POST_AIGRIT.md` | AIGrit 글 작성 시 |
| `docs/POST_BABIPANOTE.md` | babipanote 글 작성 시 |
| `docs/POST_NAVER.md` | 네이버 에디션 작성 시 |
| `docs/CONTENT_RULES.md` | 마커·내부 링크·금지어 |
| **`docs/THUMBNAIL.md`** | **OG 썸네일 Figma 자동 생성** |
| `docs/WORKFLOW.md` | 파이프라인 전체 흐름 |
| `docs/PUBLISH_CHECKLIST.md` | 발행 전 점검·프롬프트 템플릿 |

### 🔧 개발

| 문서 | 언제 읽나 |
|---|---|
| `docs/STRUCTURE.md` | 파일 트리 확인 |
| `docs/ENV.md` | 환경변수 설정 |
| `docs/HOOKS_RULES.md` | Hook 추가·디버깅 |
| `DESIGN.md` | 디자인 작업 |

### 📊 Obsidian SEO 관제

| 문서 | 용도 |
|---|---|
| `02. Blog SEO/10. Pipeline/AIGrit/_README.md` | AIGrit 마스터 넘버링 |
| `02. Blog SEO/10. Pipeline/babipanote/_README.md` | babipanote 마스터 넘버링 |
| `02. Blog SEO/02. AIGrit 글쓰기 지침서.md` | 카테고리 표·수익화 |
| `02. Blog SEO/03. babipanote 글쓰기 지침서.md` | babipanote 상세 |
| `02. Blog SEO/07. Sprint 실행 계획.md` | 발행 일정 |

## 점검·헬스체크

- 디자인 토큰: `docs/design-system.md`
- 점검 기준: `docs/site-health-checklist.md`
- 점검 로그: `docs/inspection-log/YYYY-MM.md`
- 실행 프롬프트: Obsidian vault `02. Blog SEO/10. Site Health/`
