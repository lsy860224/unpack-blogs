# Design System (unpack-blogs)

> **소스 오브 트루스 (공동 계약):**
> 1. **Figma Variables** (`njkSF5MinT8kK7kaoYpp12`, `Vgv4MaHqiVurKEGPqTmIM9`) — 디자인 정답
> 2. **`globals.css` `@theme`** — 구현 정답
> 3. **이 문서** — 두 정답 간 계약 명세 + 사용 규약
> 스택: **Next.js 16 + Tailwind v4 (`@theme` in `globals.css`)** — `tailwind.config.ts` 없음.

---

## 0. 현재 상태 (2026-04-22 기준)

| 파일 | Style Guide | Logo | Avatar | Social Header | OG Image | Watermark | Favicon | Variables |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AIGrit | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **✅ 4 컬렉션 · 55개** |
| babipanote | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **✅ 4 컬렉션 · 56개** |

**Figma Variables 부트스트랩 완료 (v5)** — 이제 Figma MCP 자동 동기화 가능.

---

## 1. 운영 규약 (READ FIRST)

### 1.1 절대 원칙

1. **Figma Variables 와 `globals.css` 는 1:1 대응을 유지한다.** 한쪽만 수정 금지.
2. **Variables 이름은 이 문서의 섹션 3 표를 정답으로 한다.** 이름이 깨지면 자동 diff 가 깨진다.
3. **새로운 토큰을 만들 때는 반드시 양쪽 + 이 문서 세 곳에 동시 추가한다.**
4. **기존 토큰의 의미(semantic)를 바꾸지 않는다.** `brand/primary` 가 "Deep Indigo" 에서 갑자기 "Cyan" 이 되면 안 됨. 의미를 바꾸고 싶으면 새 토큰을 만들거나 리네이밍 (v6 변경 이력에 기록).

### 1.2 수정 워크플로우 (디자인 변경 시)

```
[A] 색/폰트/크기 변경이 필요하다
    ↓
[B] Figma Variable 수정 (섹션 3 의 변수 이름 그대로)
    ↓
[C] globals.css @theme 에서 대응 값 수정
    ↓
[D] 이 문서의 해당 섹션 업데이트 + 변경 이력 append
    ↓
[E] 프롬프트 1 실행 → drift 없음 확인
    ↓
[F] PR 커밋 메시지 규칙: "design: {sync|add|rename} {token-name}"
```

### 1.3 금지 사항

- ❌ Figma 에서 Variable 우회 (직접 hex 입력)
- ❌ `globals.css` 에서 Variable 값 하드코딩 (`--color-brand-primary: var(--some-other);` 같은 순환 참조)
- ❌ 코드 컴포넌트에 hex 직접 사용 (`text-[#3730A3]`)
- ❌ 신규 토큰을 Figma 에만, 또는 코드에만 추가
- ❌ 이 문서 업데이트 없이 둘 중 하나만 수정

### 1.4 점검 루틴

| 주기 | 실행자 | 내용 |
|---|---|---|
| 코드 PR 시 | 사람 | Figma 변경 있었나? 있었으면 이 문서 확인 |
| 월 1회 | Claude (프롬프트 1) | Figma ↔ 이 문서 ↔ globals.css 3자 diff |
| 디자인 변경 시 | 사람 | 위 1.2 워크플로우 엄수 |

---

## 2. 기존 문서와의 관계

| 파일 | 역할 |
|---|---|
| `DESIGN.md` (루트) | 디자인 작업 시작점 / Figma MCP 연동 |
| `docs/DESIGN_CHECKLIST.md` | 디자인 작업 체크리스트 |
| `apps/*/docs/BRAND_GUIDELINES.md` | 브랜드 스토리·보이스·메시징 |
| `apps/*/src/app/globals.css` | 실제 토큰 값 (구현 정답) |
| **Figma Variables** | 디자인 정답 |
| **이 문서** | 위 3자 간 계약 + 규약 + 자산 스펙 |

---

## 3. Figma Variables — 현재 등록된 전체 목록

두 파일 모두 동일한 컬렉션 구조 (`Colors` · `Typography` · `Spacing` · `Radius`). 값만 브랜드별 다름.

### 3.1 Colors Collection (Light / Dark 2 modes)

#### Raw tokens (브랜드 색 + 액센트 + 뉴트럴)

| Variable | AIGrit Light | AIGrit Dark | babipanote Light | babipanote Dark |
|---|---|---|---|---|
| `brand/primary` | `#3730A3` | `#818CF8` | `#6B2E4E` | `#C89BAE` |
| `brand/secondary` | `#06B6D4` | `#22D3EE` | `#C89F7C` | `#E0BEA0` |
| `brand/secondary-hover` | `#0891B2` | `#06B6D4` | `#A87F5C` | `#C89F7C` |
| `accent/green` | `#10B981` | `#34D399` | `#6B8A63` | `#A8BFA0` |
| `accent/red` | `#EF4444` | `#F87171` | `#9C4A3E` | `#C88072` |
| `neutral/slate` (AIGrit) / `neutral/ink` (baba) | `#0F172A` | `#E2E8F0` | `#2B2420` | `#E8E0D6` |
| `neutral/snow` (AIGrit) / `neutral/paper` (baba) | `#F8FAFC` | `#0F172A` | `#FAF7F2` | `#1A1614` |
| `neutral/surface` | `#FFFFFF` | `#1E293B` | `#FFFCF7` | `#2B2420` |
| `neutral/subtle` | `#F1F5F9` | `#334155` | `#F2EDE4` | `#3A312C` |
| `neutral/muted` | `#94A3B8` | `#64748B` | `#8B7D70` | `#8F8275` |

> ⚠️ **이름이 다른 토큰:** `neutral/slate` (AIGrit) vs `neutral/ink` (baba), `neutral/snow` vs `neutral/paper`. 의도적 — 각 브랜드의 "잉크·종이" / "슬레이트·스노우" 은유 반영.

#### Semantic aliases (모든 파일 공통 이름, raw 토큰 참조)

| Variable | 참조 대상 (AIGrit) | 참조 대상 (baba) |
|---|---|---|
| `semantic/bg-base` | → `neutral/snow` | → `neutral/paper` |
| `semantic/bg-surface` | → `neutral/surface` | → `neutral/surface` |
| `semantic/fg-primary` | → `neutral/slate` | → `neutral/ink` |
| `semantic/border` | → `neutral/subtle` | → `neutral/subtle` |
| `semantic/info` | → `brand/secondary` | → `brand/secondary` |
| `semantic/success` | → `accent/green` | → `accent/green` |
| `semantic/error` | → `accent/red` | → `accent/red` |

> 💡 **컴포넌트는 semantic 만 참조하라.** raw 토큰 직접 참조는 피한다 (예외: 로고).

### 3.2 Typography Collection

모든 값은 FLOAT (숫자) 또는 STRING. 단위:
- `size/*`: **px**
- `leading/*`: **%** (Figma 라인 높이)
- `tracking/*`: **%** (Figma letter spacing)
- `family/*`, `weight/*`: 문자열

| Variable | AIGrit | babipanote | 비고 |
|---|---|---|---|
| `size/display` | 48 | 56 | babipanote 이 더 큼 |
| `size/h1` | 32 | 36 | |
| `size/h2` | 22 | 24 | |
| `size/body` | 16 | 16 | 동일 |
| `size/small` | 14 | 14 | 동일 |
| `size/num` | **18** | — | **AIGrit 고유** (데이터 강조) |
| `size/xsmall` | 12 | 12 | 동일 |
| `leading/display` | 115 | 110 | |
| `leading/h1` | 125 | 120 | |
| `leading/h2` | 135 | 135 | |
| `leading/body` | 165 | **175** | babipanote 이 더 여유 |
| `leading/small` | 155 | 160 | |
| `leading/num` | 150 | — | AIGrit 고유 |
| `leading/xsmall` | — | 150 | baba 고유 |
| `tracking/logo` | -3 | -2 | 로고 전용 |
| `tracking/mark` | — | **-4** | **baba 고유** (Mark "b" 전용) |
| `tracking/heading` | -1 | 0 | 세리프는 트래킹 0 |
| `tracking/body` | 0 | 0 | |
| `family/display` | Inter | Gowun Batang | |
| `family/sans` | Pretendard | Pretendard | 동일 |
| `family/serif` | — | Gowun Batang | baba 고유 |
| `family/mono` | JetBrains Mono | JetBrains Mono | 동일 |
| `weight/display` | Extra Bold | Bold | Inter vs Gowun 차이 |
| `weight/heading` | Bold | Bold | |
| `weight/body` | Regular | Regular | |
| `weight/meta` | Medium | Medium | |

### 3.3 Spacing Collection (4px 그리드, 양 브랜드 완전 동일)

| Variable | px |
|---|---|
| `space-1` | 4 |
| `space-2` | 8 |
| `space-3` | 12 |
| `space-4` | 16 |
| `space-5` | 24 |
| `space-6` | 32 |
| `space-7` | 48 |
| `space-8` | 64 |

### 3.4 Radius Collection

| Variable | px | AIGrit 사용처 | babipanote 사용처 |
|---|---|---|---|
| `radius/sm` | 4 | 태그·배지 | 태그·배지 |
| `radius/md` | 8 | 버튼·인풋 | 버튼·인풋 |
| `radius/lg` | 12 | — | 카드 (기본) |
| `radius/xl` | 16 | 큰 카드 | 큰 카드 |
| `radius/2xl` | 24 | 컨테이너 | 컨테이너 |
| `radius/card` | **8** / **12** | **AIGrit 기본** (8) | **baba 기본** (12) |
| `radius/full` | 9999 | Avatar, pill | Avatar, pill |

> 🎯 `radius/card` 는 **각 브랜드의 카드 기본 반지름** 을 가리키는 semantic token. 브랜드 차이 반영.

---

## 4. Figma Variable → CSS Variable 매핑 (구현 계약)

Figma 이름에 슬래시(`/`) 있음. CSS 변수로 쓸 땐 하이픈(`-`)으로 치환:

| Figma Variable | CSS Variable (globals.css) |
|---|---|
| `brand/primary` | `--color-brand-primary` |
| `brand/secondary` | `--color-brand-secondary` |
| `accent/green` | `--color-accent-green` |
| `neutral/slate` | `--color-neutral-slate` |
| `semantic/bg-base` | `--color-bg-base` (또는 `--color-semantic-bg-base`) |
| `size/display` | `--text-display` |
| `leading/body` | `--leading-body` |
| `tracking/logo` | `--tracking-logo` |
| `family/display` | `--font-display` |
| `space-4` | `--space-4` |
| `radius/md` | `--radius-md` |
| `radius/card` | `--radius-card` |

**변환 규칙:**
1. `/` → `-`
2. `size/` / `leading/` / `tracking/` → `text-` / `leading-` / `tracking-` (Tailwind v4 네이밍)
3. `color/` 접두사 없는 경우 → `--color-` 추가 (COLOR 타입일 때)
4. 나머지 그대로

---

## 5. 디자인 원칙 (두 브랜드 대척 구조)

| 축 | AIGrit | babipanote |
|---|---|---|
| 은유 | 기계 · 데이터 · 계측기 | 잉크 · 종이 · 저널 |
| 시각 방향 | 정제 · 기하학적 · 고대비 | 따뜻함 · 유기적 · 부드러움 |
| 서체 방향 | Inter Extra Bold (디스플레이) + Pretendard (본문) | Gowun Batang Bold (헤딩 세리프) + Pretendard (본문) |
| 여백 밀도 | 밀도 있음 (lh 165%) | 느슨함 (lh 175%) |
| Cover 처리 | 다크 인버트 (극적) | 정상 (Paper) |
| 수익화 UI | AdSense + AffiliateLink | 렌더 안 됨 |
| 레이아웃 | category (사이드바 ON) | timeline (사이드바 OFF) |
| 데이터 강조 토큰 | **`size/num`** 존재 | 없음 |
| 로고 장식 | `[AI]` 브래킷 (Cyan) | `·` 마침표 (Terracotta) |

---

## 6. 접근성 (WCAG 대비비)

### AIGrit Light

| 조합 | 대비비 | 판정 | 규칙 |
|---|---|---|---|
| primary `#3730A3` on snow | **10.8 : 1** | ✅ AAA | 전체 허용 |
| secondary `#06B6D4` on snow | **2.9 : 1** | ❌ Fail | **텍스트 금지** |
| accent/green on snow | **2.6 : 1** | ❌ Fail | 아이콘만 |
| accent/red on snow | **3.8 : 1** | ⚠️ AA large only | 18pt+ or 아이콘 |
| slate on snow | **17.3 : 1** | ✅ AAA | 본문 기본 |

### babipanote Light

| 조합 | 대비비 | 판정 | 규칙 |
|---|---|---|---|
| primary `#6B2E4E` on paper | **9.4 : 1** | ✅ AAA | 전체 허용 |
| secondary `#C89F7C` on paper | **2.4 : 1** | ❌ Fail | **텍스트 금지** |
| accent/green on paper | **3.6 : 1** | ⚠️ AA large only | 18pt+ or 아이콘 |
| accent/red on paper | **6.1 : 1** | ✅ AA | 텍스트 가능 |
| ink on paper | **14.2 : 1** | ✅ AAA | 본문 기본 |

**운영 규칙:** `brand/secondary`, `accent/green` 는 **텍스트 색으로 사용 금지** (AIGrit/baba 공통). 로고 장식·아이콘·배경용.

---

## 7. Logo Specification

### 7.1 AIGrit (Inter Extra Bold · `tracking/logo = -3`)

```
[AI]Grit  — 워드마크
[AI]      — 마크
```

| 변형 | 배경 | 브래킷 `[ ]` | `AI Grit` |
|---|---|---|---|
| Primary · Light | snow | brand/secondary | brand/primary |
| Primary · Dark | slate (bg dark) | brand/secondary (dark) | brand/primary (dark) |
| Reverse · on Primary | brand/primary | brand/secondary | snow |
| Mono · Slate | snow | slate | slate |

| 컨텍스트 | 크기 |
|---|---|
| Mark (단독) | 160px |
| Primary 대형 | 96px |
| Social Header | 110px |
| OG Image | 44px |
| Watermark | 36px |
| Favicon 180 | 81px |
| Favicon 32 | 14.4px |
| Favicon 16 | 7.2px |

**규칙:**
- Clear space = 대괄호 한 칸 폭
- Min size: Web 88×20px, Print 20mm 폭
- Favicon: `Grit` 제거, `[AI]` 만

### 7.2 babipanote (Gowun Batang Bold · `tracking/logo = -2`, Mark 는 `tracking/mark = -4`)

```
babipanote·   — 워드마크 (마침표 필수)
b·            — 마크
```

| 변형 | 배경 | "babipanote" | "·" |
|---|---|---|---|
| Primary · Light | paper | brand/primary | brand/secondary |
| Primary · Dark | paper (dark) | brand/primary (dark) | brand/secondary (dark) |
| Reverse · on Primary | brand/primary | paper | brand/secondary |
| Mono · Ink | paper | ink | ink |

| 컨텍스트 | 크기 |
|---|---|
| Mark (b·) | 200px |
| Primary | 96px |
| Social Header | 140px |
| OG Image | 80px |
| Watermark | 40px |
| Favicon 180 | 129.6px |
| Favicon 32 | 23px |
| Favicon 16 | 11.5px |

**규칙:**
- Clear space = 높이의 0.5배
- Min size: Web 100×20px, Print 25mm 폭
- Favicon: `·` 제거, `b` 만
- **"babipanote·" 형태 필수.** "babipanote" 단독 금지

### 7.3 공통 금지

- 로고 색상 임의 변경
- 기울임 · 왜곡 · 효과
- 두 브랜드 로고 혼합
- 장식(브래킷/마침표) 제거

---

## 8. Avatar (400×400)

### 8.1 AIGrit — 6종

Square Light / Dark / Slate, Round Light / Dark / Slate.

- 마크: `[AI]` 만
- 크기: 200px
- Round: `radius/full`
- 배경:
  - Square Light: snow
  - Square Dark: slate + brand 색 (lightened)
  - Square Slate: slate + snow 텍스트 (하드 대비)

### 8.2 babipanote — 5종

Square Light / Dark / Reverse (on Primary), Round Light / Dark.

- 마크: `b·`
- 크기: 280px
- Round: `radius/full`
- Reverse: brand/primary bg + paper 텍스트 "b" + brand/secondary "·"

---

## 9. Social Header (1500×500)

### 9.1 AIGrit (Dark = Default)

| 요소 | 스펙 |
|---|---|
| 배경 | Dark: slate / Light: snow |
| 좌측 액센트 바 | `8 × 200`, brand/secondary, `radius/sm` |
| 로고 | `[AI]Grit` 110px |
| 태그라인 1 | "AI의 알맹이만 남긴다" Inter Bold 26px |
| 태그라인 2 | "써보고 말한다, 팔지 않는다." Inter Regular 16px |
| 핸들 | `@aigrit_dev` JBMono Medium 18px brand/secondary, +1% |
| 카테고리 | "REVIEWS · BENCHMARKS · COMPARISONS · 2026" JBMono Medium 11px, +2.5% |
| 배경 장식 | 1px 가로 선 15줄, opacity 0.03 |

### 9.2 babipanote

| 요소 | 스펙 |
|---|---|
| 배경 | Light: paper / Dark: paper (dark) |
| 로고 | `babipanote·` Gowun Batang Bold 140px |
| 태그라인 | "오늘도 만들고, 내일 더 나은 것을 만든다" Gowun Batang Bold 22px |
| 핸들 | `@babipanote` JBMono Medium 18px brand/primary, +1% |
| 우측 액센트 바 | `160 × 4`, brand/secondary, radius 2px |
| 배경 장식 | 1px 가로 선 8줄, opacity 0.05 |

---

## 10. OG Image (1200×630)

### 10.1 AIGrit — 4 variants

Default Light / Dark / Article Light / Dark.

```
[AI]Grit (44px)       ┌─ "LLM · REVIEW" tag (JBMono Bold 12, secondary @15% bg pill)
──────────────────
│ 6×160 세로바, secondary, radius 3
│
│ <HEADLINE>  Inter Regular 56px · -2% · lh 118% · 최대 2줄
│
──────────────────
"REVIEWS · BENCHMARKS · 2026" (JBMono Bold 16, secondary)
aigrit.dev (JBMono Regular 14)
```

**Article:** 헤드라인 아래 데이터 서브라인 "$15/mo · 2.1s avg · n=200" (JBMono Bold 16, secondary)

### 10.2 babipanote — 4 variants

```
━━━━━━━━━━━━━━━━━  ← 상단 6px 가로 바 (width 1200), brand/primary
LOG #042 (JBMono Medium 14, brand/secondary, +2.5%)
2026.04.14 · babipanote.com (JBMono Regular 13, ink)

<HEADLINE>  Gowun Batang Bold 64px · -2% · lh 115% · 최대 3줄

              ┌─ 우측 480×630 워시 (brand/primary @ 5% opacity)
              │
              │   babipanote·  (80px)
              │
              └─
```

---

## 11. Watermark (400×120)

### 11.1 AIGrit — 3 variants

Dark BG / Light BG / Dark Mode.

- 로고 `[AI]Grit` 36px
- 서브 URL `aigrit.dev` JBMono Regular 11px

**사용 규칙:**
- 불투명도: 밝은 배경 55~65%, 어두운 배경 75~85%
- 위치: 우측 하단 (벤치마크 그래프는 좌상단 허용)
- 최소 크기: 긴 변 48px
- 브래킷 Cyan 색 유지 필수
- **수치·리뷰 스코어 이미지에는 반드시 워터마크 포함**

### 11.2 babipanote — 3 variants

Dark BG / Light BG / Dark Mode.

- 로고 `babipanote·` 40px
- 서브 URL `babipanote.com` JBMono Regular 11px

**사용 규칙:**
- 불투명도: 밝은 배경 50~60%, 어두운 배경 70~80%
- 위치: 우측 하단
- 최소 크기: 긴 변 40px
- **정적 배치 — 움직이는 워터마크 금지**
- **"babipanote·" 형태 필수**

---

## 12. Favicon

공통: 3 사이즈 (180×180, 32×32, 16×16), radius 18% (= `180→32.4`, `32→5.76`, `16→2.88`).

### 12.1 AIGrit — 3 variants

Dark Slate (Default 권장) / Light Snow / Dark Mode.

- 내용: `[AI]` (Grit 제거)
- 크기: 81 / 14.4 / 7.2

### 12.2 babipanote — 2 variants

Light / Dark.

- 내용: `b` (마침표 제외)
- 크기: 129.6 / 23 / 11.5

---

## 13. Prose (.prose 오버라이드)

| 항목 | AIGrit | babipanote |
|---|---|---|
| H1~H3 폰트 | `family/display` (Inter) | **`family/serif` (Gowun Batang)** |
| H4 이하 + 본문 | `family/sans` | `family/sans` |
| max-width | `65ch` | `65ch` |
| line-height 본문 | `leading/body` (1.65) | `leading/body` (1.75) |
| 링크 색 | `brand/secondary` (Cyan) | `brand/primary` (Plum) |
| 링크 밑줄 | offset 3px, 1px | 동일 |
| 인용 border-left | `brand/primary` 4px | `brand/primary` 2px (얇게) |
| 인용 폰트 | italic 산세리프 | italic 세리프 |
| 코드블록 radius | `radius/md` | `radius/lg` |
| 데이터 강조 | `size/num` 사용 | — |

---

## 14. Component Tokens

### 14.1 Button

| variant | bg | fg | hover bg |
|---|---|---|---|
| `primary` | `brand/primary` | `#FFFFFF` | `brand/secondary-hover` (또는 darken 8%) |
| `secondary` | `semantic/bg-surface` | `semantic/fg-primary` | `neutral/subtle` |
| `ghost` | transparent | `semantic/fg-primary` | `neutral/subtle` |
| `destructive` | `accent/red` | `#FFFFFF` | darken 8% |

**포커스:** `:focus-visible { outline: 2px solid var(--color-brand-primary); outline-offset: 2px; }`

### 14.2 Callout (MDX)

| variant | bg | border-left | icon |
|---|---|---|---|
| `info` | `color-mix(in srgb, var(--color-semantic-info) 8%, transparent)` | `semantic/info` 4px | Info |
| `success` | `color-mix(... success 8% ...)` | `semantic/success` 4px | CheckCircle |
| `warning` | `color-mix(... warning 10% ...)` | warning 4px | AlertTriangle |
| `error` | `color-mix(... error 8% ...)` | `semantic/error` 4px | XCircle |

### 14.3 AffiliateLink (AIGrit만)

- 색: `brand/secondary`
- `ExternalLink` 아이콘 14px
- `rel="sponsored nofollow"` 강제
- 글 하단 `<Disclaimer />` 세트 필수
- babipanote: no-op (`monetization.affiliateLinks === false`)

### 14.4 PostCard

| 요소 | 토큰 |
|---|---|
| bg | `semantic/bg-surface` |
| border | `semantic/border` 1px |
| radius | `radius/card` |
| shadow | AIGrit: `sm → md` hover / baba: `xs → sm` hover |
| padding | `space-5` (24) |
| 썸네일 | 16:9 |
| 제목 | `size/h2` |
| 설명 | `size/small`, `fg-secondary`, line-clamp-2 |
| 메타 | `size/xsmall`, `fg-muted` (AIGrit `size/num` 가능) |

---

## 15. Image Rules

### 15.1 OG Image
- 1200 × 630, PNG/WebP ≤ 300KB
- `apps/{app}/public/og/{slug}.png`
- 폴백: `public/og-default.png`

### 15.2 썸네일
- 16:9, 최소 1280px, WebP

### 15.3 Favicon
- Next.js 16 `app/icon.tsx` / `app/apple-icon.tsx`
- radius 18%

---

## 16. Motion / Z-index / Shadow (코드 전용, Figma 부재)

### Motion

| 토큰 | 값 |
|---|---|
| `--duration-fast` | 120ms |
| `--duration-base` | 200ms |
| `--duration-slow` | 320ms |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` |

### Z-index

| 토큰 | 값 |
|---|---|
| `--z-sticky` | 20 |
| `--z-dropdown` | 30 |
| `--z-overlay` | 40 |
| `--z-modal` | 50 |
| `--z-popover` | 60 |
| `--z-toast` | 70 |

### Shadow

| 토큰 | 값 |
|---|---|
| `--shadow-xs` | `0 1px 2px rgb(0 0 0 / 0.04)` |
| `--shadow-sm` | `0 1px 3px rgb(0 0 0 / 0.08), 0 1px 2px rgb(0 0 0 / 0.04)` |
| `--shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -1px rgb(0 0 0 / 0.04)` |
| `--shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -2px rgb(0 0 0 / 0.04)` |

**브랜드 차이:**
- AIGrit: sm 기본, hover md
- babipanote: none 또는 xs 기본 ("종이는 뜨지 않는다")

---

## 17. 하드코딩 금지 리스트

- ❌ Hex 문자열 직접 (`text-[#3730A3]`)
- ❌ 픽셀 임의값 (`p-[17px]`)
- ❌ 인라인 `style={{ fontFamily/color }}`
- ❌ `tailwind.config.ts` 생성
- ❌ `rgba()` 직접 — `color-mix(in srgb, var(--color-...) N%, transparent)` 사용
- ❌ 폰트 크기 px 직접 — `var(--text-*)` 또는 Tailwind `text-*` 사용
- ❌ babipanote 로고에서 `·` 제거
- ❌ `[AI]Grit` 로고에서 브래킷 Cyan 변경
- ❌ semantic 우회하여 raw 토큰 직접 참조 (로고 제외)

프롬프트 1 자동 탐지.

---

## 18. globals.css 구현 예시 (Tailwind v4)

### 18.1 AIGrit

```css
/* apps/aigrit/src/app/globals.css */
@import "tailwindcss";

@theme {
  /* ═══ Brand (Figma: brand/*) ═══ */
  --color-brand-primary: #3730A3;
  --color-brand-secondary: #06B6D4;
  --color-brand-secondary-hover: #0891B2;

  /* ═══ Accents (Figma: accent/*) ═══ */
  --color-accent-green: #10B981;
  --color-accent-red: #EF4444;

  /* ═══ Neutrals (Figma: neutral/*) ═══ */
  --color-neutral-slate: #0F172A;
  --color-neutral-snow: #F8FAFC;
  --color-neutral-surface: #FFFFFF;
  --color-neutral-subtle: #F1F5F9;
  --color-neutral-muted: #94A3B8;

  /* ═══ Semantic aliases (Figma: semantic/*) ═══ */
  --color-bg-base: var(--color-neutral-snow);
  --color-bg-surface: var(--color-neutral-surface);
  --color-fg-primary: var(--color-neutral-slate);
  --color-border: var(--color-neutral-subtle);
  --color-info: var(--color-brand-secondary);
  --color-success: var(--color-accent-green);
  --color-error: var(--color-accent-red);

  /* ═══ Typography ═══ */
  --font-display: "Inter Variable", "Pretendard Variable", system-ui, sans-serif;
  --font-sans: "Pretendard Variable", "Inter Variable", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;

  --text-display: 3rem;         /* 48 */
  --text-h1: 2rem;              /* 32 */
  --text-h2: 1.375rem;          /* 22 */
  --text-body: 1rem;            /* 16 */
  --text-small: 0.875rem;       /* 14 */
  --text-num: 1.125rem;         /* 18 — AIGrit 고유 */
  --text-xsmall: 0.75rem;       /* 12 */

  --leading-display: 1.15;
  --leading-h1: 1.25;
  --leading-h2: 1.35;
  --leading-body: 1.65;
  --leading-num: 1.5;

  --tracking-logo: -0.03em;     /* 로고 전용 */
  --tracking-heading: -0.01em;
  --tracking-body: 0;

  /* ═══ Radius ═══ */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-2xl: 1.5rem;
  --radius-card: 0.5rem;        /* AIGrit 기본 */
  --radius-full: 9999px;
}

@media (prefers-color-scheme: dark) {
  @theme {
    --color-brand-primary: #818CF8;
    --color-brand-secondary: #22D3EE;
    --color-brand-secondary-hover: #06B6D4;
    --color-accent-green: #34D399;
    --color-accent-red: #F87171;
    --color-neutral-slate: #E2E8F0;
    --color-neutral-snow: #0F172A;
    --color-neutral-surface: #1E293B;
    --color-neutral-subtle: #334155;
    --color-neutral-muted: #64748B;
  }
}
```

### 18.2 babipanote

```css
/* apps/babipanote/src/app/globals.css */
@import "tailwindcss";

@theme {
  --color-brand-primary: #6B2E4E;
  --color-brand-secondary: #C89F7C;
  --color-brand-secondary-hover: #A87F5C;
  --color-accent-green: #6B8A63;
  --color-accent-red: #9C4A3E;

  --color-neutral-ink: #2B2420;        /* AIGrit 의 slate 와 역할 동일 */
  --color-neutral-paper: #FAF7F2;      /* AIGrit 의 snow 와 역할 동일 */
  --color-neutral-surface: #FFFCF7;
  --color-neutral-subtle: #F2EDE4;
  --color-neutral-muted: #8B7D70;

  --color-bg-base: var(--color-neutral-paper);
  --color-bg-surface: var(--color-neutral-surface);
  --color-fg-primary: var(--color-neutral-ink);
  --color-border: var(--color-neutral-subtle);
  --color-info: var(--color-brand-secondary);
  --color-success: var(--color-accent-green);
  --color-error: var(--color-accent-red);

  --font-display: "Lora Variable", "Gowun Batang", Georgia, serif;
  --font-serif: "Lora Variable", "Gowun Batang", Georgia, serif;
  --font-sans: "Pretendard Variable", "Inter Variable", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;

  --text-display: 3.5rem;       /* 56 */
  --text-h1: 2.25rem;           /* 36 */
  --text-h2: 1.5rem;            /* 24 */
  --text-body: 1rem;            /* 16 */
  --text-small: 0.875rem;       /* 14 */
  --text-xsmall: 0.75rem;       /* 12 */

  --leading-display: 1.10;
  --leading-h1: 1.20;
  --leading-h2: 1.35;
  --leading-body: 1.75;
  --leading-small: 1.60;
  --leading-xsmall: 1.50;

  --tracking-logo: -0.02em;
  --tracking-mark: -0.04em;     /* babipanote 고유 — Mark "b" 전용 */
  --tracking-heading: 0;         /* 세리프는 트래킹 안 함 */
  --tracking-body: 0;

  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-2xl: 1.5rem;
  --radius-card: 0.75rem;       /* babipanote 기본 */
  --radius-full: 9999px;
}

@media (prefers-color-scheme: dark) {
  @theme {
    --color-brand-primary: #C89BAE;
    --color-brand-secondary: #E0BEA0;
    --color-brand-secondary-hover: #C89F7C;
    --color-accent-green: #A8BFA0;
    --color-accent-red: #C88072;
    --color-neutral-ink: #E8E0D6;
    --color-neutral-paper: #1A1614;
    --color-neutral-surface: #2B2420;
    --color-neutral-subtle: #3A312C;
    --color-neutral-muted: #8F8275;
  }
}
```

---

## 19. 남은 TODO

### 19.1 Figma 파일 정리 (수동)

- [ ] AIGrit: 연결된 커뮤니티 라이브러리 7개 해제 (Material 3, iOS 26, macOS 26 등)
- [ ] babipanote: 연결된 커뮤니티 라이브러리 확인·정리
- [ ] 양 파일에 Pretendard 폰트 추가 설치 (현재 Inter 로 폴백)
- [ ] Style Guide 페이지의 스와치·타입 샘플을 **Variable 에 바인딩** (수동 작업 — Figma UI 에서 각 요소 선택 후 Variable 할당)

> Style Guide 바인딩을 하면 Variable 수정 시 가이드라인 전체가 자동 갱신됨. 안 해도 Variable 은 정상 작동.

### 19.2 코드 정렬

- [ ] `apps/aigrit/src/app/globals.css` — 섹션 18.1 기준으로 정렬
- [ ] `apps/babipanote/src/app/globals.css` — 섹션 18.2 기준
- [ ] 프롬프트 1 실행 → 하드코딩 hex 탐지·교체

### 19.3 자동화 (나중)

- [ ] `docs/ci/verify-design-tokens.ts` — Figma Variable API 로 조회 + globals.css 파싱 비교 스크립트
- [ ] GitHub Actions: PR 시 실행, drift 발견 시 fail

---

## 20. 변경 이력

| 날짜 | 버전 | 변경 |
|---|---|---|
| 2026-04-22 | v1 | 초안 (프로젝트 개요 기반) |
| 2026-04-22 | v2 | 토큰 3계층·대비비·모션 확장 |
| 2026-04-22 | v3 | Cover 페이지 실측 |
| 2026-04-22 | v4 | Figma 전체 페이지 실측 (Style Guide·Logo·Avatar·Social Header·OG·Watermark·Favicon) |
| 2026-04-22 | **v5** | **Figma Variables 부트스트랩 완료** (4 컬렉션, AIGrit 55개 + babipanote 56개). 운영 규약(섹션 1) + Variable 매핑 테이블(섹션 3, 4) 추가. 소스 오브 트루스 = Figma Variables + globals.css + 이 문서 3자 계약. |
