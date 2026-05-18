# AdSense 자가점검 5 FAIL 발견 — 스크린샷 캡쳐 가이드

**대상 글:** [babipanote/wrote-adsense-guide-found-5-fails](../../apps/babipanote/content/posts/wrote-adsense-guide-found-5-fails.mdx)
**발행일:** 2026-05-18
**preflight 기준:** babipanote essay/buildlog — OG 외 본문 1장+ 권장
**primary_keyword:** AdSense 자가점검
**secondary_keywords:** 1인 빌더 buildlog, 블로그 audit, AdSense 셋업
**연계 글:** AIGrit `adsense-approval-prep-checklist` 발행 직후 메타 회고

## 발행 시점 상태

- 본문 이미지 1장 + OG 1장 모두 자동 생성 완료
- review-post: WARN 1건 (글자 2,936자 — essay 권장 상한 2,500 초과, 깊이 콘텐츠로 수용)
- 내부 3 / 외부 2 / FAQ 없음(essay 적격) / broken 0 — 그 외 PASS

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Gowun Batang·babipanote Plum+Terracotta)
- [x] `01-audit-result.png` — 18편 PASS/WARN/FAIL 3박스 다이어그램 (matplotlib + 종이 톤)

### [사용자 캡쳐] — 추후 보강 권장 (1장, 선택)

저장 경로: `apps/babipanote/public/images/wrote-adsense-guide-found-5-fails/`

- [ ] `02-review-post-output.png` — `/review-post` 슬래시 커맨드 실제 출력 캡쳐
  - 컨텐츠: 5 FAIL 항목이 보이는 터미널/Claude Code 응답
  - 도구: macOS Terminal + Claude Code CLI
  - 캡쳐 방법: `Cmd+Shift+4` 영역 (FAIL 5건 모두 보이도록)
  - 민감정보: API 키·계정 이메일 마스킹 필수

## 규격 공통

- 자동 생성 차트: matplotlib 13×7 inch × 180dpi · babipanote 종이 톤 (#F7F1E8 BG)
- 색상 토큰: Paper `#F7F1E8` · Plum `#6B2C5C` · Terracotta `#C75B3F` · Ink `#2D2419`

## 생성 스크립트

```bash
/Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
  python3 scripts/charts/generate-self-audit-chart.py
```

## 관련

- 연계 AIGrit 글: `apps/aigrit/content/posts/ko/adsense-approval-prep-checklist.mdx`
- 같은 sprint cluster: `category-mapping-debug.mdx`, `sprint-week3-review.mdx`
- `.claude/rules/post-requirements.md` — babipanote essay 기준
