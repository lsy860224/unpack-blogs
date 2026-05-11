# Sprint 3주차 회고 — 스크린샷 캡쳐 가이드

**대상 글:** [babipanote/sprint-week3-review](../../apps/babipanote/content/posts/sprint-week3-review.mdx)
**발행일:** 2026-05-12
**preflight 기준:** babipanote essay — OG 외 본문 1장+ 권장 (선택)
**primary_keyword:** Sprint 3주차 회고
**secondary_keywords:** Claude Code 슬래시 커맨드, 1인 빌더 워크플로우, 블로그 발행 자동화

## 발행 시점 상태

- 본문 이미지 0장 (마커 0 — 사용자 결정대로 추후 보강 패턴)
- review-post: WARN (글자수 상한 미세 초과 + 이미지 0장) — 모두 사용자 결정 사항
- 추후 캡쳐 보강 권장

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Gowun Batang·babipanote Plum+Terracotta, `scripts/og/generate-og-all.py`)

### [사용자 캡쳐] — 추후 보강 권장 (1~2장)

저장 경로 공통: `apps/babipanote/public/images/sprint-week3-review/`

- [ ] `01-week3-publish-summary.png` — W20 발행 7편 요약 시각화 (옵션)
  - 컨텐츠: AIGrit 3편 + babipanote 3편 + Naver 1편 = 7편, 슬래시 커맨드 4개, EN 차트 6장 등 한눈 인포그래픽
  - 도구: **NapkinAI** (https://app.napkin.ai/) `visual_query=summary` 또는 Excel/Sheets 표
  - 권장 영역: 1,600~2,000px PNG
  - 민감정보: 없음

- [ ] `02-slash-commands-diagram.png` — 슬래시 커맨드 4개 흐름 다이어그램 (옵션)
  - 컨텐츠: `/blog-review` → 데이터 분석 → `/publish-post` → commit·PR → 라이브 자동화 흐름
  - 도구: NapkinAI flowchart 또는 Mermaid Live (https://mermaid.live)
  - 권장 영역: 1,600~2,000px PNG
  - 민감정보: 없음

## 규격 공통

- 본문 이미지: 가로 1,600~2,000px PNG (60~150KB)
- 마스킹 불필요 (메타·통계 콘텐츠)

## 관련

- `.claude/rules/post-requirements.md` — babipanote 1장+ 권장
- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian) — 캡쳐 도구 비교
