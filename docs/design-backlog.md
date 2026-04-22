# Design System Backlog

> 디자인 시스템 관련 **Nice-to-have** 개선 항목 모음. Must/Should 수준의 긴급도 아님.
> 처리 시 `docs/inspection-log/YYYY-MM.md`에 기록 + 이 파일의 해당 항목 ☑️ 체크.
>
> 관련 문서: `docs/design-system.md` (마스터 계약) · `docs/site-health-checklist.md`

---

## NTH-1. 인라인 `style={{ fontFamily|color|background }}` → Tailwind 유틸리티 치환

- **현황:** 31건 (2026-04-22 점검 기준)
  - `apps/aigrit/src/app/[locale]/**` 12건 (`fontFamily: var(--font-mono)`)
  - `apps/aigrit/src/app/[locale]/**` 3건 (`background: var(--color-brand-secondary)`)
  - `apps/aigrit/src/components/layout/**` 4건 (font-mono)
  - `apps/babipanote/src/app/**` 9건 (font-serif·mono)
  - `packages/blog-core/components/**` 3건 (font-mono·accent)
- **배경:** 값은 CSS 변수 경유라 drift는 없지만 `docs/design-system.md` §21 "인라인 style 금지" 위반. ESLint 자동 탐지를 도입하려면 먼저 정리 필요.
- **작업:**
  - `style={{ fontFamily: "var(--font-mono)" }}` → `className="font-mono"` (Tailwind v4가 `--font-mono`를 자동 유틸리티로 변환)
  - `style={{ background: "var(--color-brand-secondary)" }}` → `className="bg-[color:var(--color-brand-secondary)]"` 또는 `bg-brand-secondary` (v4 `@theme` 자동 생성 유틸)
  - 동적 값(Callout.tsx `s.bar`·`s.bg` 같은 타입별 분기)은 inline 유지 허용 — 별도 예외 목록화
- **수용 기준:** `rg 'style=\{\{.*(fontFamily|background|color):' apps packages` 결과 ≤ 5건 (동적 분기만)
- **리스크:** prose 영역의 `font-serif` 자동 적용이 inline `font-sans`와 충돌할 수 있음 — 테스트 필요

## NTH-2. `--tracking-*` 토큰 정의

- **현황:** Figma Variables에 `tracking/logo`, `tracking/heading`, `tracking/body` 있음 (AIGrit은 `-3%/-1%/0`, babipanote는 `-2%/0/0` + `tracking/mark: -4`). globals.css에 전혀 없음
- **배경:** 로고·헤딩 letter-spacing 일관성 보호. 현재 `letter-spacing: -0.01em` 같은 값이 컴포넌트에 흩어져 있음
- **작업:** 양쪽 globals.css `@theme`에 `--tracking-logo`, `--tracking-heading`, `--tracking-body` 추가 (babipanote는 `--tracking-mark`도). Header/로고/PostHeader 등에서 사용
- **수용 기준:** `rg 'letter-spacing: -0?\.0[0-9]+' apps packages` 결과 0건 (토큰 경유만)

## NTH-3. `--weight-*` 토큰 정의

- **현황:** Figma Variables에 `weight/display|heading|body|meta`(Extra Bold/Bold/Regular/Medium) 있음. globals.css에 없음
- **배경:** Tailwind `font-bold`/`font-medium` 등으로 대체 가능하나 Figma 이름과 매핑 유지 시 drift 감지 쉬워짐
- **작업:** `@theme`에 `--font-weight-display`, `--font-weight-heading`, `--font-weight-body`, `--font-weight-meta` 추가. (Tailwind v4는 `--font-weight-*`를 자동으로 `font-display`/`font-heading` 등으로 매핑)
- **수용 기준:** 헤딩 컴포넌트에서 `font-bold` 대신 `font-heading`(토큰 기반) 사용

## NTH-4. `--font-display` 분리 (AIGrit 로고 전용)

- **현황:** AIGrit 로고는 **Inter Extra Bold · tracking -3%** 전용이지만 globals.css에 `--font-display` 없음. 현재 `--font-sans`가 `Pretendard → Inter` 순으로 섞임
- **배경:** 로고는 Inter가 primary, 본문은 Pretendard가 primary. 스택 순서가 반대여야 함
- **작업:**
  - AIGrit: `--font-display: var(--font-inter), var(--font-pretendard), system-ui, sans-serif;` 추가
  - Header 로고 `[AI]Grit` 렌더에 `font-display` 클래스 적용
  - babipanote는 `--font-display: var(--font-serif)` 또는 `Gowun Batang + Lora` 스택 (Lora 폰트는 이미 제거됨 → Gowun만)
- **수용 기준:** AIGrit 로고가 Inter로 먼저 렌더 (네트워크 인스펙터 확인)

## NTH-5. `--space-0-5` (hair line) 실제 활용

- **현황:** 2026-04 Should-fix에서 `--space-0-5: 0.125rem` 토큰은 globals.css에 추가했으나 사용처 없음. `apps/aigrit/src/components/layout/Header.tsx` 100/105/110 라인의 `h-[2px]` 3곳이 잠재 대체 대상
- **배경:** 햄버거 메뉴 라인 2px는 hair line 용도. 토큰 경유로 바꾸면 다크모드·brand 변경 시 일관 유지
- **작업:**
  - `h-[2px]` → `h-0.5` (Tailwind 기본) 또는 `h-[var(--space-0-5)]` (토큰 경유)
  - Tailwind 기본 `h-0.5 = 0.125rem`이 우연히 일치하므로 `h-0.5`로 충분
- **수용 기준:** `rg 'h-\[2px\]|w-\[2px\]' apps packages` 결과 0건

---

## 처리 기록

| 날짜 | 항목 | 커밋 |
|---|---|---|
| — | (아직 없음) | — |

---

## 참조

- 원 점검 로그: `docs/inspection-log/2026-04.md` (§8 Nice-to-have)
- 디자인 계약: `docs/design-system.md`
- 체크리스트: `docs/site-health-checklist.md`
