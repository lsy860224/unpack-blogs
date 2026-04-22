# Design System Backlog

> 디자인 시스템 관련 **Nice-to-have** 개선 항목 모음. Must/Should 수준의 긴급도 아님.
> 처리 시 `docs/inspection-log/YYYY-MM.md`에 기록 + 이 파일의 해당 항목 ☑️ 체크.
>
> 관련 문서: `docs/design-system.md` (마스터 계약) · `docs/site-health-checklist.md`

---

## ☑️ NTH-1. 인라인 `style={{ fontFamily|color|background }}` → Tailwind 유틸리티 치환 (처리 2026-04-22)

- **처리 전:** 35건 (single-line grep) + multi-line 포함 약 40여 건
- **처리 후:** 5건 (모두 동적 분기·AdSense `<ins>` 필수 속성·런타임 계산, 수용 기준 ≤5 통과)
  - `Callout.tsx:54,59` — 타입별 분기 (`s.bar`, `s.bg`)
  - `TableOfContents.tsx:42` — `(h.depth - minDepth) * 12` 런타임 계산
  - `AdInArticle.tsx:50`, `AdBanner.tsx:48` — AdSense `<ins>` 태그 `display:block`
- **치환 매핑:**
  - `fontFamily: var(--font-mono)` → `font-mono`
  - `fontFamily: var(--font-serif)` → `font-serif`
  - `background: var(--color-brand-*)` → `bg-brand-*`
  - `color: var(--color-accent-*)` → `text-accent-*`
  - `color-mix(...)` → `bg-[color-mix(...)]` / `border-[color-mix(...)]`
- **검증 grep:** `rg 'style=\{\{.*(fontFamily|background|color):' apps packages` → 2건 (Callout.tsx 동적)

## ☑️ NTH-2. `--tracking-*` 토큰 정의 (처리 2026-04-22)

- **추가 토큰** — 양쪽 `globals.css @theme`:
  - AIGrit: `--tracking-logo: -0.03em`, `--tracking-heading: -0.01em`, `--tracking-body: 0em`
  - babipanote: `--tracking-logo: -0.02em`, `--tracking-heading: -0.01em`, `--tracking-body: 0em`, `--tracking-mark: -0.04em`
- **babipanote `--tracking-heading` 예외:** Figma는 0이나 한글 Gowun Batang 가독성 위해 `-0.01em` 유지 (`docs/BRAND_GUIDELINES.md §타이포`) — 주석으로 명시
- **하드코딩 제거:** `apps/babipanote/src/app/globals.css:112` `letter-spacing: -0.01em;` → `var(--tracking-heading)`
- **검증 grep:** `rg 'letter-spacing: -0?\.0[0-9]+' apps packages` → 0건 ✓

## ☑️ NTH-3. `--font-weight-*` 토큰 정의 (처리 2026-04-22)

- **추가 토큰** — 양쪽 `globals.css @theme`:
  - `--font-weight-display: 800` / `--font-weight-heading: 700` / `--font-weight-body: 400` / `--font-weight-meta: 500`
- **Tailwind v4 주의사항:**
  - `--font-weight-display`는 `--font-display`(family)와 같은 `.font-display` 유틸 이름을 가져 family가 우선 병합 → **weight 유틸로는 생성되지 않음**
  - 따라서 AIGrit Header 로고는 `font-display font-extrabold tracking-logo` 조합 유지 (weight 명시 필요)
- **사용처 확장:** 향후 `font-heading`/`font-body`/`font-meta` 유틸을 헤딩·본문·메타 컴포넌트에 적용 시 자동 생성됨

## ☑️ NTH-4. `--font-display` 분리 (처리 2026-04-22)

- **추가 토큰:**
  - AIGrit: `--font-display: var(--font-inter), var(--font-pretendard), system-ui, -apple-system, sans-serif;`
  - babipanote: `--font-display: var(--font-gowun-batang), Georgia, "Times New Roman", serif;`
- **AIGrit Header 로고:** `font-extrabold tracking-tight` → `font-display font-extrabold tracking-logo` (Inter 우선 + Figma `tracking/logo: -3%` 매핑)
- **검증:** 컴파일된 CSS에서 `.font-display{font-family:var(--font-display)}` + `.tracking-logo{letter-spacing:var(--tracking-logo)}` 생성 확인

## ☑️ NTH-5. `--space-0-5` (hair line) 실제 활용 (처리 2026-04-22)

- `apps/aigrit/src/components/layout/Header.tsx` 100/105/110 라인 `h-[2px]` 3곳 → `h-0.5` (Tailwind 기본 `0.125rem` = 2px, `--space-0-5` 와 동일값)
- **검증 grep:** `rg 'h-\[2px\]|w-\[2px\]' apps packages` → 0건 ✓

---

## 처리 기록

| 날짜 | 항목 | 요약 |
|---|---|---|
| 2026-04-22 | NTH-1~5 일괄 | NTH-1 (35→2건), NTH-2 tracking 토큰, NTH-3 weight 토큰, NTH-4 `--font-display`, NTH-5 hair line — 양쪽 빌드/타입체크 통과 |

---

## 참조

- 원 점검 로그: `docs/inspection-log/2026-04.md` (§8 Nice-to-have)
- 디자인 계약: `docs/design-system.md`
- 체크리스트: `docs/site-health-checklist.md`
