# Sprint 4주차 회고 — 스크린샷 캡쳐 가이드

**대상 글:** [babipanote/sprint-week4-review](../../apps/babipanote/content/posts/sprint-week4-review.mdx)
**발행일:** 2026-05-19
**preflight 기준:** babipanote essay/buildlog — OG 외 본문 1장+ 권장
**primary_keyword:** Sprint 4주차 회고 W22
**secondary_keywords:** 13 PR sprint, AdSense 신청 직전, 1인 빌더 buildlog, fix-everything

## 발행 시점 상태

- 본문 이미지 1장 + OG 1장 모두 matplotlib 자동 생성 완료
- review-post: WARN 1건 (글자 4,198자, essay 2,500 권장 초과 — 깊이 콘텐츠 수용)
- 내부 3 / 외부 2 / FAQ 없음(essay) / broken 0 — 그 외 PASS

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Gowun Batang·babipanote Plum+Terracotta)
- [x] `01-13-prs-timeline.png` — W22 13 PR 4그룹 박스 다이어그램 (matplotlib · 종이 톤)

### [사용자 캡쳐] — 추후 보강 권장 (1장, 선택)

저장 경로: `apps/babipanote/public/images/sprint-week4-review/`

- [ ] `02-adsense-application.png` — AdSense 콘솔 사이트 추가/심사 대기 화면
  - 컨텐츠: 신청 직후 "검토 중" 상태가 보이는 콘솔 캡쳐
  - 도구: https://www.google.com/adsense/
  - 캡쳐 방법: `Cmd+Shift+4` 영역
  - 민감정보: 게시자 ID·계정 이메일 마스킹 필수

## 생성 스크립트

```bash
/Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
  python3 scripts/charts/generate-sprint-week4-chart.py
```

## 관련

- 직전 회고: `wrote-adsense-guide-found-5-fails.mdx` (2026-05-18) — W21 자가점검 시발점
- 시리즈: `sprint-week1-review`·`sprint-week2-review`·`sprint-week3-review`
- 동시 진행 AIGrit Pillar: `apps/aigrit/content/posts/ko/ai-coding-complete-guide-2026.mdx` (W22 신규)
- W22 종합 audit log: Obsidian `02. Unpack-Blogs/10. Site Health/2026-05-19 W22 sprint 완료 — 13 PR 머지 AdSense 신청 준비 완료.md`
