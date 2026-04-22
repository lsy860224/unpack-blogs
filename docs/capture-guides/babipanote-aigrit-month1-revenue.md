# AIGrit 첫 달 중간 리포트 (1주차) — 스크린샷 캡쳐 가이드

**대상 글:** [apps/babipanote/content/posts/aigrit-month1-revenue.mdx](../../apps/babipanote/content/posts/aigrit-month1-revenue.mdx)
**발행 예정일:** 2026-04-22 16:40
**타입:** babipanote revenue-report
**preflight 기준:** 본문 이미지 1+, 내부 링크 2~3, 외부 링크 1+

## 이미지 목록

### [자동 생성 완료] — Claude 렌더
- [x] `og.png` — OG 썸네일 1200×630 (크림 + Plum)
- [x] `02-revenue-vs-cost.png` — 1주차 수익(₩0) vs 비용(₩59,000) 비교 인포그래픽

### [사용자 캡쳐 필요]

#### `01-ga4-month1.png` — GA4 Reports snapshot (1주차 실측)

- **경로**: `apps/babipanote/public/images/aigrit-month1-revenue/01-ga4-month1.png`
- **도구**: [Google Analytics 4](https://analytics.google.com) — AIGrit 속성
- **캡쳐 방법**:
  1. GA4 접속 → 좌상단 속성 선택 → `aigrit.dev` 선택
  2. 좌측 메뉴 → Reports → Reports snapshot
  3. 우상단 날짜 범위 → **2026-04-15 ~ 04-22** (1주차 정확히)
  4. 상단 4개 카드 (Users, New users, Average engagement time, Events) + 아래 꺾은선 그래프까지 한 화면에 보이게 스크롤
  5. `Cmd+Shift+4` 드래그로 카드 + 그래프 영역 캡쳐
- **권장 영역**: 가로 1,800~2,000
- **민감정보**:
  - 좌상단 프로필 아이콘 마스킹
  - 계정 이메일 (상단) 마스킹
  - 인기 페이지 목록에 나오는 URL 은 그대로 OK (이미 공개 사이트)
- **테마**: GA4 라이트 모드 (babipanote 크림 톤 조화)

### [선택 추가 이미지]

#### `03-gsc-index-status.png` — GSC 색인 상태 (선택)

- **도구**: [Google Search Console](https://search.google.com/search-console)
- **메뉴**: 색인생성 → 페이지 → "왜 페이지가 색인 생성되지 않는지"
- **컨텐츠**: 현재 "발견됨 - 색인 미생성" 상태의 URL 목록 (투명성 강화)

## 규격 공통

- PNG, 가로 1,800~2,000px
- macOS `Cmd+Shift+4` 드래그
- Preview.app 사각형 도구로 민감정보 마스킹

## Obsidian Pipeline 메타

- **primary_keyword:** `블로그 수익 리포트 1달차`
- **content_type:** revenue-report
- **featured_snippet_target:** none (본문 내부 테이블 위주)
- **internal_links:** `sprint-week1-review`, `adsense-prep-checklist`, `craft-naver-workflow`, `time-management-solo-builder`, + AIGrit `solo-developer-automation-stack` (교차)

## 준비 상태

- [x] 자동 생성 2장
- [ ] 사용자 캡쳐 1장 (GA4)
- [ ] 선택 1장 (GSC)

**캡쳐 완료 후**: 해당 경로에 PNG 드롭 → 다음 커밋 시 자동 반영. MDX 는 이미 참조 경로를 포함.

## 데이터 업데이트 주의

이 글은 "1주차 중간" 리포트. **2026-05-15 전후** 별도 글 `aigrit-month1-final-revenue` 에서 첫 달 완전 데이터 업데이트 예정. 숫자가 누적되는 시점에 **새 글로** 발행 (기존 글 `updated` 필드는 손대지 않음 — babipanote revenue-report 관행).
