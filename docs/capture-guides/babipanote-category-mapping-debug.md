# 카테고리 매핑 디버그 — 스크린샷 캡쳐 가이드

**대상 글:** [babipanote/category-mapping-debug](../../apps/babipanote/content/posts/category-mapping-debug.mdx)
**발행일:** 2026-05-14
**preflight 기준:** babipanote essay/buildlog — OG 외 본문 1장+ 권장
**primary_keyword:** 카테고리 매핑 디버그
**secondary_keywords:** Next.js 카테고리 라우팅, fallback slug, 1인 빌더 디버깅

## 발행 시점 상태

- 본문 이미지 0장 (#14~#16 패턴, 추후 캡쳐 보강 예정)
- review-post: WARN (이미지 0장) — 사용자 결정

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Gowun Batang·babipanote Plum+Terracotta)

### [사용자 캡쳐] — 추후 보강 권장 (1~2장, 선택)

저장 경로 공통: `apps/babipanote/public/images/category-mapping-debug/`

- [ ] `01-category-500-error.png` — `/ko/category/수익화` HTTP 500 에러 화면 (브라우저 캡쳐)
  - 컨텐츠: Next.js dev 콘솔 또는 Vercel error overlay
  - 도구: 로컬 dev (`pnpm dev`) 후 한글 카테고리 URL 직접 접근
  - 캡쳐 방법: `Cmd+Shift+4` 영역
  - 민감정보: 없음

- [ ] `02-categories-ts-diff.png` — categories.ts 한 줄 추가 diff (Before/After)
  - 컨텐츠: CATEGORY_META 객체 안 수익화 매핑 추가
  - 도구: VS Code Diff 또는 **Carbon** (https://carbon.now.sh)
  - 권장 영역: 1,400~1,600px PNG
  - 민감정보: 없음

## 규격 공통

- 본문 이미지: 가로 1,600~2,000px PNG (60~150KB)

## 관련

- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian)
- 같은 sprint 회고: `babipanote-sprint-week3-review.md`
