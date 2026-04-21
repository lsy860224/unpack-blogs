# Design System (unpack-blogs)

> **소스 오브 트루스:** `apps/{app}/src/app/globals.css` 의 `@theme` 블록.
> 스택: **Next.js 16 + Tailwind v4 (`@theme` in `globals.css`)** — `tailwind.config.ts` 없음.
> Figma → 이 문서 → `globals.css` 동기화.

---

## 0. Figma 파일 현황 (2026-04-22 실측 v2)

**업데이트:** 이전 스캔의 `childCount: 0` 은 페이지 로드 누락 때문이었습니다. `page.loadAsync()` 후 재스캔한 결과:

| 파일 | Style Guide | Logo | Avatar | Social Header | OG Image | Watermark | Favicon | Variables |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AIGrit | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ 0개 |
| babipanote | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ 0개 |

**상황 업데이트:**
- 브랜드 가이드라인은 **디자인으로는 완전히 정의됨** (Light/Dark 모두, 모든 에셋 변형)
- **Figma Variables 만 정의되지 않음** — 이 문서가 그 "변환층" 역할을 함
- 동기화 흐름: **Figma 디자인 → 이 문서 → `globals.css`** (Variables 없이도 동기화 가능)
- Figma Variables 정의는 섹션 23 의 부트스트랩으로 해결 (선택사항)

---

## 1. 기존 문서와의 관계

| 파일 | 역할 | 이 문서와 관계 |
|---|---|---|
| `DESIGN.md` (루트) | 디자인 작업 시작점 / Figma MCP 연동 | 이 문서가 토큰 마스터, DESIGN.md 는 워크플로우 |
| `docs/DESIGN_CHECKLIST.md` | 디자인 작업 체크리스트 | 별개. 실무 체크리스트 |
| `apps/*/docs/BRAND_GUIDELINES.md` | 브랜드 스토리·보이스·메시징 | 별개. 이 문서는 토큰·규약만 |
| `apps/*/src/app/globals.css` | 실제 토큰 값 (단일 소스) | 이 문서 ≡ 그 값의 서술 + Figma 상호 참조 |

## 2. Figma 파일 키

| 사이트 | 파일 키 | Brand Guidelines URL |
|---|---|---|
| AIGrit | `njkSF5MinT8kK7kaoYpp12` | [AIGrit — Brand Guidelines](https://www.figma.com/design/njkSF5MinT8kK7kaoYpp12/AIGrit-—-Brand-Guidelines) |
| babipanote | `Vgv4MaHqiVurKEGPqTmIM9` | [babipanote — Brand Guidelines](https://www.figma.com/design/Vgv4MaHqiVurKEGPqTmIM9/babipanote-—-Brand-Guidelines) |

주요 페이지 node-id (양 파일 공통 구조):
- `0:1` Cover · `1:2` Style Guide · `1:3` Logo · `1:4` Avatar · `1:5` Social Header · `1:6` OG Image · `1:7` Watermark · `1:8` Favicon

---

## 3. 디자인 원칙

| 축 | AIGrit | babipanote |
|---|---|---|
| 은유 | 기계 · 데이터 · 계측기 | 잉크 · 종이 · 저널 |
| 시각 방향 | 정제 · 기하학적 · 고대비 | 따뜻함 · 유기적 · 부드러움 |
| 서체 방향 | Inter Extra Bold (디스플레이) + Pretendard (본문 KR) | Gowun Batang Bold (헤딩 세리프) + Pretendard (본문 KR) |
| 여백 밀도 | 밀도 있음 (정보 중심, lh 165%) | 느슨함 (호흡 중심, lh 175%) |
| Cover 처리 | **다크 인버트** — 극적 첫인상 | 정상 (Paper) |
| 수익화 UI | AdSense + AffiliateLink 렌더 | 렌더 안 됨 |
| 레이아웃 | category (사이드바 ON) | timeline (사이드바 OFF) |
| 데이터 강조 토큰 | **NUM** (JetBrains Mono Bold) 존재 | 없음 |
| 로고 장식 | `[AI]` 브래킷 (Cyan) | `·` 마침표 (Terracotta) |

---

## 4. Color System

### 4.1 네이밍 컨벤션 (Figma 라벨 그대로)

```
--color-brand.primary          # Primary
--color-brand.secondary        # Secondary
--color-brand.secondary-hover  # Secondary Hover
--color-accent.green           # Accent · Green
--color-accent.red             # Accent · Red
--color-neutral.slate / .ink   # Foreground (AIGrit=slate, baba=ink)
--color-neutral.snow  / .paper # Background base (AIGrit=snow, baba=paper)
--color-neutral.surface        # Surface (카드)
```

Figma 라벨에 `.` (점) 포함돼 있어 CSS 변수로 쓸 땐 `-` 로 치환: `--color-brand-primary`.

### 4.2 AIGrit 색상 (Figma 실측)

#### Light Mode

| 토큰 | Hex | Figma 라벨 | 비고 |
|---|---|---|---|
| `--color-brand-primary` | `#3730A3` | Primary | Deep Indigo |
| `--color-brand-secondary` | `#06B6D4` | Secondary | Cyan — **브래킷 색** |
| `--color-brand-secondary-hover` | `#0891B2` | Sec · Hover | Darker Cyan |
| `--color-accent-green` | `#10B981` | Accent · Green | Emerald |
| `--color-accent-red` | `#EF4444` | Accent · Red | Coral Red |
| `--color-neutral-slate` | `#0F172A` | Slate | **FG** (text primary) |
| `--color-neutral-snow` | `#F8FAFC` | Snow | **BG base** |
| `--color-neutral-surface` | `#FFFFFF` | Surface | Card |

#### Dark Mode

| 토큰 | Hex | 변화 |
|---|---|---|
| `--color-brand-primary` | `#818CF8` | Primary lightened (Indigo 400) |
| `--color-brand-secondary` | `#22D3EE` | Cyan lightened (Cyan 400) |
| `--color-brand-secondary-hover` | `#06B6D4` | = Light mode secondary |
| `--color-accent-green` | `#34D399` | Emerald lightened |
| `--color-accent-red` | `#F87171` | Red lightened |
| `--color-neutral-slate` | `#E2E8F0` | **FG inverted** (Slate 200) |
| `--color-neutral-snow` | `#0F172A` | **BG inverted** (원 Slate) |
| `--color-neutral-surface` | `#1E293B` | Dark card (Slate 800) |

### 4.3 babipanote 색상 (Figma 실측)

#### Light Mode

| 토큰 | Hex | Figma 라벨 | 비고 |
|---|---|---|---|
| `--color-brand-primary` | `#6B2E4E` | Primary | Plum |
| `--color-brand-secondary` | `#C89F7C` | Secondary | Terracotta — **마침표 색** |
| `--color-brand-secondary-hover` | `#A87F5C` | Secondary Hover | Darker Terracotta |
| `--color-accent-green` | `#6B8A63` | Accent · Green | Sage |
| `--color-accent-red` | `#9C4A3E` | Accent · Red | Rust |
| `--color-neutral-ink` | `#2B2420` | Ink | **FG** (text primary) |
| `--color-neutral-paper` | `#FAF7F2` | Paper | **BG base** |

#### Dark Mode

| 토큰 | Hex | 변화 |
|---|---|---|
| `--color-brand-primary` | `#C89BAE` | Dusty rose — Plum 소프트화 |
| `--color-brand-secondary` | `#E0BEA0` | Soft terracotta |
| `--color-brand-secondary-hover` | `#C89F7C` | = Light mode secondary |
| `--color-accent-green` | `#A8BFA0` | Soft sage |
| `--color-accent-red` | `#C88072` | Soft rust |
| `--color-neutral-ink` | `#E8E0D6` | **FG inverted** — 크림 (다크 위 잉크처럼) |
| `--color-neutral-paper` | `#1A1614` | **BG inverted** — 다크 페이퍼 |

> **네이밍 철학:** babipanote 의 "Ink" / "Paper" 는 역할 기반 (fg/bg) 이라 다크 모드에서 값만 뒤집힘.

### 4.4 접근성 (WCAG 대비비)

#### AIGrit Light

| 조합 | 대비비 | 판정 |
|---|---|---|
| primary `#3730A3` on snow | **10.8 : 1** | ✅ AAA |
| secondary `#06B6D4` on snow | **2.9 : 1** | ❌ Fail — 텍스트 금지 |
| accent-green `#10B981` on snow | **2.6 : 1** | ❌ Fail — 아이콘만 |
| accent-red `#EF4444` on snow | **3.8 : 1** | ⚠️ AA large only |
| slate `#0F172A` on snow | **17.3 : 1** | ✅ AAA |

#### babipanote Light

| 조합 | 대비비 | 판정 |
|---|---|---|
| primary `#6B2E4E` on paper | **9.4 : 1** | ✅ AAA |
| secondary `#C89F7C` on paper | **2.4 : 1** | ❌ Fail — 텍스트 금지 |
| accent-green `#6B8A63` on paper | **3.6 : 1** | ⚠️ AA large only |
| accent-red `#9C4A3E` on paper | **6.1 : 1** | ✅ AA |
| ink `#2B2420` on paper | **14.2 : 1** | ✅ AAA |

**운영 규칙:** `secondary`, `accent-green` 는 **텍스트 색으로 사용 금지**. 로고 장식·큰 UI·아이콘에만. 링크에 쓸 땐 밑줄로 시각 큐 보강.

### 4.5 상태 색상 매핑

| 의미 | AIGrit | babipanote |
|---|---|---|
| success | `accent-green` | `accent-green` |
| error | `accent-red` | `accent-red` |
| info | `secondary` (Cyan) | `secondary` (Terracotta) |
| warning | `#F59E0B` (Amber — 브랜드 외) | `#D97706` (Dark Amber — 브랜드 외) |

---

## 5. Typography (Figma 실측)

### 5.1 Type Scale — AIGrit

Figma 라벨에는 **"Pretendard"** 표기, Figma 실제 렌더링은 **Inter** (Figma 파일에 Pretendard 미설치로 폴백). 코드에서는 Pretendard 정상 로드됨.

| 토큰 | Figma 라벨 | 실제 속성 | 용도 |
|---|---|---|---|
| `--text-display` | Pretendard ExtraBold 48 / 55 | 48px · weight 800 · lh **115%** · tracking **-1%** | 히어로 |
| `--text-h1` | Pretendard Bold 32 / 40 | 32px · 700 · lh **125%** · -1% | 포스트 제목 |
| `--text-h2` | Pretendard Bold 22 / 30 | 22px · 700 · lh **135%** · -1% | 섹션 |
| `--text-body` | Pretendard Regular 16 / 26 | 16px · 400 · lh **165%** · -1% | 본문 |
| `--text-small` | Pretendard Regular 14 / 22 | 14px · 400 · lh **155%** · -1% | 캡션·메타 |
| `--text-num` | JetBrains Mono Bold 18 | 18px · 700 · lh **150%** · -1% | **수치 강조** (리뷰 스코어) |
| `--text-xsmall` | JetBrains Mono Bold 12 | 12px · 700 · lh **150%** · -1% | 카테고리 태그 ("CATEGORY · REVIEW #042") |

**AIGrit 고유:** 디스플레이 로고는 `Inter Extra Bold · tracking -3%` — 로고 전용.

### 5.2 Type Scale — babipanote

| 토큰 | Figma 라벨 | 실제 속성 | 용도 |
|---|---|---|---|
| `--text-display` | Gowun Batang Bold 56 / 62 | 56px · 700 · lh **110%** · 0% | 히어로 |
| `--text-h1` | Gowun Batang Bold 36 / 43 | 36px · 700 · lh **120%** · 0% | 포스트 제목 |
| `--text-h2` | Gowun Batang Bold 24 / 32 | 24px · 700 · lh **135%** · 0% | 섹션 |
| `--text-body` | Pretendard Regular 16 / 28 | 16px · 400 · lh **175%** · 0% | 본문 (여유 있게) |
| `--text-small` | Pretendard Regular 14 / 22 | 14px · 400 · lh **160%** · 0% | 캡션 |
| `--text-xsmall` | Pretendard Medium 12 / 18 | 12px · 500 · lh **150%** · 0% | 라벨·태그 |

**babipanote 고유:** H1~H3 까지 **Gowun Batang 세리프**, H4 이하 + 본문은 Pretendard 산세리프 → "저널처럼 읽히는 헤딩, 편하게 읽히는 본문".

### 5.3 공통 Tagline 토큰 (Cover·배너·OG 공통)

```
--text-tagline: Inter Medium 22~26px · tracking +5% (AIGrit) / +0% (baba, 세리프는 트래킹 넓히지 않음)
```

실측:
- AIGrit 태그라인: "AI의 알맹이만 남긴다" — Inter Bold 26px / Social Header 기준
- babipanote 태그라인: "오늘도 만들고, 내일 더 나은 것을 만든다" — Gowun Batang Bold 22px

### 5.4 Font Stacks (globals.css)

```css
/* AIGrit */
--font-display: "Inter Variable", "Pretendard Variable", system-ui, sans-serif;
--font-sans:    "Pretendard Variable", "Inter Variable", -apple-system, sans-serif;
--font-mono:    "JetBrains Mono", ui-monospace, "SF Mono", monospace;

/* babipanote */
--font-display: "Lora Variable", "Gowun Batang", Georgia, serif;
--font-serif:   "Lora Variable", "Gowun Batang", Georgia, serif; /* H1~H3 */
--font-sans:    "Pretendard Variable", "Inter Variable", -apple-system, sans-serif; /* H4+ body */
--font-mono:    "JetBrains Mono", ui-monospace, monospace;
```

**폰트 로딩:** `public/fonts/` self-host, `font-display: swap`, body 폰트 `preload`.
**중요:** Pretendard 를 반드시 로드 (Figma 에는 없지만 코드에서는 필수 — 한글 렌더링 품질 차이 큼).

---

## 6. Logo Specification

### 6.1 AIGrit 로고 (Inter Extra Bold · tracking -3%)

```
[AI]Grit  — 워드마크 (full)
[AI]      — 레터마크 (mark, 짧은 형태)
```

| 변형 | 배경 | `[` `]` 브래킷 색 | `AI Grit` 색 |
|---|---|---|---|
| Primary · Light | Snow | Cyan | Primary Indigo |
| Primary · Dark | Slate | Cyan light (`#22D3EE`) | Primary Dark (`#818CF8`) |
| Reverse · on Primary | Indigo Primary | Cyan | Snow |
| Mono · Slate | Snow (또는 임의) | Slate (모노) | Slate (모노) |

**사용 크기:**

| 컨텍스트 | 폰트 크기 |
|---|---|
| Mark (마크만, 힘 있는 로컬 사용) | 160px |
| Primary (full 워드마크 대형) | 96px |
| Social Header (X 배너) | 110px |
| OG Image | 44px |
| Watermark | 36px |
| Clear Space 예시 (실사용 추정) | 28px |
| Favicon 180 | 81px |
| Favicon 32 | 14.4px |
| Favicon 16 | 7.2px |

**규칙 (Figma 실측):**
- Clear space = `x` (**대괄호 한 칸 폭** 기준)
- Min size: **Web 88×20px, Print 20mm 폭**
- Favicon 에서는 `Grit` 제거, `[AI]` 만 사용
- 폰트: **Inter Extra Bold**, **tracking `-3%` 고정**

### 6.2 babipanote 로고 (Gowun Batang Bold · tracking -2%)

```
babipanote·   — 워드마크 (마침표 필수 포함)
b·            — 레터마크 (마크)
```

| 변형 | 배경 | "babipanote" 색 | "·" 색 |
|---|---|---|---|
| Primary · Light | Paper | Plum | Terracotta |
| Primary · Dark | Dark Paper | Dusty Rose (`#C89BAE`) | Soft Terracotta (`#E0BEA0`) |
| Reverse · on Primary | Plum | Paper | Terracotta |
| Mono · Ink | Paper (또는 임의) | Ink | Ink |

**사용 크기:**

| 컨텍스트 | 폰트 크기 |
|---|---|
| Mark (b·) | 200px |
| Primary (full) | 96px |
| Social Header (X 배너) | 140px |
| OG Image | 80px |
| Watermark | 40px |
| Favicon 180 (b 만) | 130px |
| Favicon 32 | 23px |
| Favicon 16 | 11.5px |

**규칙 (Figma 실측):**
- Clear space = `x` (**로고 높이의 0.5배**)
- Min size: **Web 100×20px, Print 25mm 폭**
- Favicon 에서는 `·` 제거, `b` 만 사용
- 폰트: **Gowun Batang Bold**, **tracking `-2%` 고정**
- **"babipanote·" 형태 필수.** "babipanote" 단독 사용 금지 (Watermark 규칙 참조)

### 6.3 공통 금지

- 로고 색상 임의 변경
- 기울임 · 왜곡 · 효과(그림자/네온)
- 두 브랜드 로고 혼합
- 장식(마침표 / 브래킷) 제거

---

## 7. Avatar (SNS 프로필 이미지)

### 7.1 AIGrit — 400×400

6종 생성: Square Light / Square Dark / Square Slate, Round Light / Round Dark / Round Slate.

- 마크 사용: `[AI]` 만 (Grit 생략 — 정사각형에서 자연스럽게 잘림)
- 마크 사이즈: **200px** (Inter Extra Bold, tracking -3%)
- Round 버전: `border-radius: 50%` (= 200px on 400 canvas)
- "Slate" 버전: Slate 배경 + 기본 색 조합 (AI Grit 부분 Snow)
- 배경 색 조합:
  - Square Light: Snow `#F8FAFC`
  - Square Dark: Slate `#0F172A` + Cyan-light/Primary-Dark 브랜드 색
  - Square Slate: Slate `#0F172A` + Snow 텍스트 (하드 대비)

### 7.2 babipanote — 400×400

5종: Square Light / Dark / Reverse (on Primary), Round Light / Dark.

- 마크 사용: `b·` (full 2-char 마크)
- 마크 사이즈: **280px** (Gowun Batang Bold, tracking -4%)
- Round: `border-radius: 50%`
- Reverse: Primary Plum 배경 + Paper 텍스트 "b" + Terracotta "·"

### 7.3 공통 규칙

- 파일 포맷: **PNG 우선** (투명 필요 시) 또는 JPG (배경 있을 때)
- 기본 추천: Round + Light (밝은 프로필 사진 느낌)
- 다크 모드 UI 용도: Square Dark 또는 Round Dark

---

## 8. Social Header (X / Twitter — 1500×500)

### 8.1 AIGrit

2 variants: **Dark (Default)** + Light.

| 요소 | 스펙 |
|---|---|
| 배경 | Dark: Slate `#0F172A` / Light: Snow `#F8FAFC` |
| 좌측 세로 액센트 바 | `8 × 200px`, Cyan, radius 4px |
| 로고 | `[AI]Grit` Inter Extra Bold **110px** |
| 태그라인 1 | "AI의 알맹이만 남긴다" Inter Bold **26px** |
| 태그라인 2 | "써보고 말한다, 팔지 않는다." Inter Regular **16px** |
| 핸들 | `@aigrit_dev` JBMono Medium **18px** Cyan, tracking +1% |
| URL | `aigrit.dev` JBMono Regular **14px** |
| 카테고리 | "REVIEWS · BENCHMARKS · COMPARISONS · 2026" JBMono Medium **11px** Cyan, tracking +2.5% |
| 배경 장식 | 1px 가로 선 15줄, `op: 0.03` (그리드 느낌) |

### 8.2 babipanote

2 variants: Light + Dark.

| 요소 | 스펙 |
|---|---|
| 배경 | Light: Paper / Dark: Dark Paper |
| 로고 | `babipanote·` Gowun Batang Bold **140px** |
| 태그라인 | "오늘도 만들고, 내일 더 나은 것을 만든다" Gowun Batang Bold **22px** |
| 핸들 | `@babipanote` JBMono Medium **18px** Plum, tracking +1% |
| URL | `babipanote.com` JBMono Regular **14px** |
| 우측 하단 액센트 바 | `160 × 4px`, Terracotta, radius 2px |
| 배경 장식 | 1px 가로 선 8줄, `op: 0.05` |

---

## 9. OG Image (1200×630)

### 9.1 AIGrit

4 variants: Default Light / Default Dark / Article Light / Article Dark.

**레이아웃 (좌→우, 상→하):**

```
[AI]Grit (44px)   "LLM · REVIEW" tag (JBMono Bold 12, Cyan 15% bg pill)
─────────────────
│ 세로 액센트 바 6×160px, Cyan, radius 3px
│
│ <HEADLINE>  Inter Regular 56px · tracking -2% · lh 118% · 최대 2줄
│
─────────────────
"REVIEWS · BENCHMARKS · 2026" (JBMono Bold 16, Cyan)
aigrit.dev (JBMono Regular 14)
```

**Default**: 헤드라인 = "AI의 알맹이만 남긴다"
**Article**: 헤드라인 = 글 제목, 하단 첨부 데이터 "$15/mo · 2.1s avg · n=200" (JBMono Bold 16, Cyan)

### 9.2 babipanote

4 variants: Default Light / Default Dark / Article Template Light / Article Template Dark.

**레이아웃:**

```
━━━━━━━━━━━━━━━━━  ← 상단 6px 가로 바, Primary color (width 1200)
LOG #042 (JBMono Medium 14, Terracotta, tracking +2.5%)
2026.04.14 · babipanote.com (JBMono Regular 13, Ink)

<HEADLINE>  Gowun Batang Bold 64px · tracking -2% · lh 115% · 최대 3줄
   "오늘도 만들고,\n내일 더 나은 것을\n만든다"

              ┌─ 우측 480×630 워시 블록 (Primary @ 5% opacity)
              │
              │   babipanote·  (80px)
              │
              └─
```

---

## 10. Watermark

### 10.1 AIGrit (400×120)

3 variants: Dark BG / Light BG / Dark Mode.

- 로고 `[AI]Grit` **36px**
- 서브 URL "aigrit.dev" JBMono Regular 11px

**사용 규칙 (Figma 실측):**
- 불투명도: **밝은 배경 55~65%, 어두운 배경 75~85%**
- 위치: 우측 하단 기본. **벤치마크 그래프는 좌측 상단 허용**
- 최소 크기: **긴 변 48px 이상**
- **대괄호 브래킷(Cyan) 색상 강조 유지 필수**
- **수치·리뷰 스코어 이미지에는 반드시 워터마크 포함**
- "aigrit.dev" 서브 URL 은 옵션 (SNS 공유 이미지 권장)

### 10.2 babipanote (400×120)

3 variants: Dark BG (light wordmark) / Light BG (primary wordmark) / Dark Mode.

- 로고 `babipanote·` **40px**
- 서브 URL "babipanote.com" JBMono Regular 11px

**사용 규칙 (Figma 실측):**
- 불투명도: **밝은 배경 50~60%, 어두운 배경 70~80%**
- 위치: 우측 하단 기본. 주제에 방해되지 않는 여백 확보
- 최소 크기: **긴 변 40px 이상**
- 영상: **정적 배치. 움직이는 워터마크 금지**
- **"babipanote·" 형태 필수. "babipanote" 단독 사용 금지**

---

## 11. Favicon

양 사이트 공통 구조:
- 3개 사이즈: **180×180 (apple-touch-icon), 32×32 (favicon.ico), 16×16 (favicon.ico)**
- Border radius: 모든 사이즈 **18%** (180 → 32.4, 32 → 5.76, 16 → 2.88)
- Next.js 16 App Router 의 `app/icon.tsx` / `app/apple-icon.tsx` 로 생성

### 11.1 AIGrit

3 variants: **Dark Slate (Default 권장)** / Light Snow / Dark Mode.

- 내용: `[AI]` (Grit 제거 — 작은 크기에서 가독)
- 폰트 크기: 180 → 81px / 32 → 14.4px / 16 → 7.2px
- **권장:** Dark Slate 배경 — 브라우저 탭에서 대비 최대

### 11.2 babipanote

2 variants: Light / Dark.

- 내용: `b` (마침표 "·" 도 제외 — favicon 사이즈에서 분간 불가)
- 폰트: Gowun Batang Bold, tracking -4%
- 폰트 크기: 180 → 129.6px / 32 → 23px / 16 → 11.5px

---

## 12. Spacing (4px 그리드 — 양 브랜드 공통)

| 토큰 | px | Figma 라벨 |
|---|---|---|
| `--space-1` | 4 | space-1 |
| `--space-2` | 8 | space-2 |
| `--space-3` | 12 | space-3 |
| `--space-4` | 16 | space-4 |
| `--space-5` | 24 | space-5 |
| `--space-6` | 32 | space-6 |
| `--space-7` | 48 | space-7 |
| `--space-8` | 64 | space-8 |

**확장 (globals.css 에서 필요 시 추가):**

| 토큰 | px | 용도 |
|---|---|---|
| `--space-0-5` | 2 | hair line |
| `--space-9` | 96 | 페이지 상하 |
| `--space-10` | 128 | 히어로 |

---

## 13. Border Radius

| 토큰 | 값 | Figma 실측 사용처 |
|---|---|---|
| `--radius-sm` | 4px | 태그 pill (OG 의 "LOG #042") |
| `--radius-md` | 8px | **AIGrit 컬러 카드** (Style Guide), 버튼, 인풋 |
| `--radius-lg` | 12px | **babipanote 컬러 카드**, 모달, 큰 카드 |
| `--radius-xl` | 16px | Logo · Avatar 프레임 래퍼 (Avatar page) |
| `--radius-2xl` | 24px | Style Guide Frame 컨테이너 |
| `--radius-avatar` | 18% (너비의) | Favicon — 180→32.4, 32→5.76, 16→2.88 |
| `--radius-full` | 9999px | Round avatar, pill button |

**브랜드 차이:**
- AIGrit 기본 카드 radius: **8px** (기계적 정돈)
- babipanote 기본 카드 radius: **12px** (종이 질감)

---

## 14. Elevation (Shadow)

Figma 파일에는 Effect 스타일이 없습니다. 코드에서 표준 적용.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--shadow-none` | `none` | 플랫 카드 |
| `--shadow-xs` | `0 1px 2px rgb(0 0 0 / 0.04)` | 인풋 |
| `--shadow-sm` | `0 1px 3px rgb(0 0 0 / 0.08), 0 1px 2px rgb(0 0 0 / 0.04)` | 카드 기본 |
| `--shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -1px rgb(0 0 0 / 0.04)` | 카드 hover |
| `--shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -2px rgb(0 0 0 / 0.04)` | 드롭다운 |
| `--shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / 0.08), 0 10px 10px -5px rgb(0 0 0 / 0.04)` | 모달 |

**다크 모드:** alpha `0.25~0.4` 로 상향.

**브랜드 기본:**
- AIGrit: `shadow-sm` 기본, hover `shadow-md`
- babipanote: `shadow-none` 또는 `shadow-xs` 기본 ("종이는 뜨지 않는다"), 필요 시 `shadow-sm`

---

## 15. Motion

Figma 에 토큰 없음. 코드 표준.

| 토큰 | 값 |
|---|---|
| `--duration-fast` | `120ms` |
| `--duration-base` | `200ms` |
| `--duration-slow` | `320ms` |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` |

**규칙:**
- `prefers-reduced-motion: reduce` 에서 duration `0ms`
- `transform` / `opacity` 만 애니메이트 (GPU 가속)
- layout shift 속성 transition 금지

---

## 16. Iconography

- 라이브러리: **`lucide-react`** (양 브랜드 공통)
- 크기: `16px` 인라인 / `20px` 버튼 / `24px` 헤딩
- stroke-width: 기본 `1.5` / 강조 `2`
- 색: `currentColor` 상속
- aria: 장식 `aria-hidden` / 인터랙티브 `aria-label` 필수
- 이모지 사용 금지

---

## 17. Component Tokens

### 17.1 Button

| variant | bg | fg | hover bg |
|---|---|---|---|
| `primary` | `brand-primary` | `#FFFFFF` | `brand-primary-hover` (별도 정의 or darken 8%) |
| `secondary` | `bg-surface` | `fg-primary` | `bg-subtle` |
| `ghost` | transparent | `fg-primary` | `bg-subtle` |
| `destructive` | `accent-red` | `#FFFFFF` | darken 8% |

| size | padding | font-size | radius |
|---|---|---|---|
| `sm` | `8px 12px` | 14px | AIGrit: 8px / baba: 12px |
| `md` | `12px 16px` | 15px | 동상 |
| `lg` | `16px 24px` | 16px | 동상 |

**포커스:** `:focus-visible { outline: 2px solid var(--color-brand-primary); outline-offset: 2px; }`

### 17.2 Callout (MDX)

| variant | bg (color-mix) | border-left | icon |
|---|---|---|---|
| `info` | `info @ 8%` | `info` (4px) | `Info` |
| `success` | `success @ 8%` | `success` (4px) | `CheckCircle` |
| `warning` | `warning @ 10%` | `warning` (4px) | `AlertTriangle` |
| `error` | `error @ 8%` | `error` (4px) | `XCircle` |

`background: color-mix(in srgb, var(--color-info) 8%, transparent);`

### 17.3 AffiliateLink

- AIGrit 텍스트 색: `brand-secondary` (Cyan)
- babipanote: 해당 없음 (`monetization.affiliateLinks === false` → no-op)
- `ExternalLink` 아이콘 14px
- **`rel="sponsored nofollow"` 강제 (props override 불가)**
- `target="_blank"` 시 `rel` 에 `noopener noreferrer` 추가
- 글 하단 `<Disclaimer />` 세트 필수

### 17.4 PostCard

| 요소 | 토큰 |
|---|---|
| bg | `bg-surface` |
| border | `border-default` 1px |
| radius | `radius-md` (AIGrit) / `radius-lg` (baba) |
| shadow | AIGrit: `sm → md` hover / baba: `xs → sm` hover |
| padding | `space-5` (24px) |
| 썸네일 비율 | `16:9` |
| 제목 | `h4` / AIGrit Inter Bold / baba Gowun Bold |
| 설명 | `small`, `fg-secondary`, `line-clamp-2` |
| 메타 | `xsmall`, `fg-muted` (AIGrit NUM 토큰 사용 가능) |

---

## 18. Prose (.prose 오버라이드)

| 항목 | AIGrit | babipanote |
|---|---|---|
| H1~H3 폰트 | Inter Bold / Pretendard | **Gowun Batang Bold** |
| H4 이하 + 본문 | Inter / Pretendard | Pretendard / Inter |
| max-width | `65ch` | `65ch` |
| line-height 본문 | **1.65 (165%)** | **1.75 (175%)** |
| 링크 색 | `brand-secondary` (Cyan) | `brand-primary` (Plum) |
| 링크 밑줄 | `underline-offset: 3px` · 1px | 동일 |
| 인용 border-left | `brand-primary` 4px | `brand-primary` 2px (얇게) |
| 인용 폰트 | italic 산세리프 | italic 세리프 (Gowun) |
| 코드블록 radius | `md` (8px) | `lg` (12px) |
| **숫자·데이터 강조** | `--text-num` 토큰 적극 활용 | 사용 안 함 |

---

## 19. Image Rules (Figma 실측 기반)

### 19.1 OG Image

- 크기: **1200 × 630**
- 포맷: PNG 또는 WebP (≤ 300KB)
- 경로: `apps/{app}/public/og/{slug}.png`
- 폴백: `apps/{app}/public/og-default.png` (Figma Default 템플릿 기반)
- 필수 요소: 로고 + 헤드라인 + 사이트 URL
- AIGrit 추가: 데이터 서브라인 (수치 강조)
- babipanote 추가: LOG #번호 태그

### 19.2 블로그 썸네일

- 종횡비: 16:9
- 최소 너비: 1280px
- 포맷: WebP (AVIF 허용)
- 경로: `apps/{app}/public/images/{slug}/thumb.webp`

### 19.3 Social Profile

- X 배너: 1500 × 500 (Figma 템플릿 활용)
- X 프로필: 400 × 400 Round (Figma Avatar Round)

### 19.4 Favicon

- Next.js 16 App Router 의 `app/icon.tsx` / `app/apple-icon.tsx` 로 생성 권장
- radius 18% 강제
- AIGrit 권장 기본: Dark Slate 버전
- babipanote 권장 기본: Light Paper 버전

---

## 20. Z-index

| 토큰 | 값 | 용도 |
|---|---|---|
| `--z-sticky` | 20 | Header sticky |
| `--z-dropdown` | 30 | 메뉴 |
| `--z-overlay` | 40 | 오버레이 |
| `--z-modal` | 50 | 모달 |
| `--z-popover` | 60 | 팝오버·툴팁 |
| `--z-toast` | 70 | 토스트 |

---

## 21. 하드코딩 금지 리스트

- ❌ Hex 문자열 직접 (`text-[#3730A3]`)
- ❌ 픽셀 임의값 (`p-[17px]`)
- ❌ 인라인 `style={{ fontFamily/color }}`
- ❌ `tailwind.config.ts` 생성 (Tailwind v4 는 CSS-first)
- ❌ `rgba()` 직접 — `color-mix(in srgb, var(--color-...) N%, transparent)` 사용
- ❌ 폰트 크기 px 직접 — `var(--text-*)` 또는 Tailwind `text-*` 클래스
- ❌ `babipanote` 로고에서 `·` 마침표 제거
- ❌ `[AI]Grit` 로고에서 브래킷 Cyan 색 변경

프롬프트 1 실행 시 자동 탐지.

---

## 22. globals.css 구현 예시 (Tailwind v4)

### 22.1 AIGrit

```css
/* apps/aigrit/src/app/globals.css */
@import "tailwindcss";

@theme {
  /* ═══ Brand Colors ═══ */
  --color-brand-primary: #3730A3;
  --color-brand-secondary: #06B6D4;
  --color-brand-secondary-hover: #0891B2;
  --color-accent-green: #10B981;
  --color-accent-red: #EF4444;

  /* ═══ Neutrals ═══ */
  --color-neutral-slate: #0F172A;      /* fg */
  --color-neutral-snow: #F8FAFC;       /* bg */
  --color-neutral-surface: #FFFFFF;    /* card */
  --color-neutral-subtle: #F1F5F9;     /* dividers */
  --color-neutral-muted: #94A3B8;      /* muted text */

  /* ═══ Semantic Aliases ═══ */
  --color-bg-base: var(--color-neutral-snow);
  --color-fg-primary: var(--color-neutral-slate);

  /* ═══ Typography ═══ */
  --font-display: "Inter Variable", "Pretendard Variable", system-ui, sans-serif;
  --font-sans: "Pretendard Variable", "Inter Variable", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;

  --text-display: 3rem;         /* 48 */
  --text-h1: 2rem;              /* 32 */
  --text-h2: 1.375rem;          /* 22 */
  --text-body: 1rem;            /* 16 */
  --text-small: 0.875rem;       /* 14 */
  --text-num: 1.125rem;         /* 18 — 수치 강조 */
  --text-xsmall: 0.75rem;       /* 12 */

  --leading-display: 1.15;
  --leading-h1: 1.25;
  --leading-h2: 1.35;
  --leading-body: 1.65;
  --leading-num: 1.5;

  --tracking-display: -0.03em;  /* 로고 */
  --tracking-heading: -0.01em;  /* h1 h2 body */

  /* ═══ Spacing, Radius, etc. ═══ */
  --radius-card: 0.5rem;        /* 8px — AIGrit 기본 */
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
  }
}
```

### 22.2 babipanote

```css
/* apps/babipanote/src/app/globals.css */
@import "tailwindcss";

@theme {
  --color-brand-primary: #6B2E4E;
  --color-brand-secondary: #C89F7C;
  --color-brand-secondary-hover: #A87F5C;
  --color-accent-green: #6B8A63;
  --color-accent-red: #9C4A3E;

  --color-neutral-ink: #2B2420;
  --color-neutral-paper: #FAF7F2;
  --color-neutral-surface: #FFFCF7;
  --color-neutral-subtle: #F2EDE4;
  --color-neutral-muted: #8B7D70;

  --color-bg-base: var(--color-neutral-paper);
  --color-fg-primary: var(--color-neutral-ink);

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
  --leading-body: 1.75;         /* 여유 있게 */

  --tracking-display: -0.02em;
  --tracking-heading: 0;         /* 세리프는 타이트하게 안 함 */

  --radius-card: 0.75rem;       /* 12px — babipanote 기본 */
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
  }
}
```

---

## 23. Figma 부트스트랩 TODO

### 23.1 즉시 (코드 동기화)

이 문서 v4 값이 globals.css 와 100% 일치하도록 PR:

- [ ] `apps/aigrit/src/app/globals.css` — Figma 실측 값으로 전면 정렬
- [ ] `apps/babipanote/src/app/globals.css` — 동일
- [ ] `brand.config.ts` 양쪽 — 비색상 토큰 (monetization, layout, social) 확인
- [ ] 코드 내 하드코딩 hex 값 탐지·교체 (프롬프트 1)

### 23.2 Figma Variables 정의 (선택, Figma MCP 자동 동기화 활성화 용)

현재 두 Figma 파일 모두 디자인은 완전하지만 **Variables 는 0개**. 다음 수동 작업으로 MCP 자동 동기화 가능:

- [ ] AIGrit 파일에서: 메뉴 → Variables → Create Collection `Color / Typography / Spacing / Radius` 4종
- [ ] Light / Dark 2 modes
- [ ] Style Guide 페이지의 각 스와치·타입 샘플을 Variable 에 바인딩
- [ ] babipanote 파일 동일
- [ ] 완료 후 프롬프트 1 으로 자동 diff 검증 루프 활성화

### 23.3 Figma 파일 정리

- [ ] AIGrit 파일에 연결된 **불필요한 커뮤니티 라이브러리 7개 해제** (Material 3, iOS 26 등 — 실사용 X)
- [ ] Figma 파일에 **Pretendard 폰트 추가 설치** (현재 Inter 로 폴백 중)

---

## 24. 변경 이력

| 날짜 | 버전 | 변경 |
|---|---|---|
| 2026-04-22 | v1 | 초안 (프로젝트 개요 기반 추정) |
| 2026-04-22 | v2 | 토큰 3계층, 대비비, 모션 등 확장 |
| 2026-04-22 | v3 | Cover 페이지 실측 반영 (로고 letter-spacing 등) |
| 2026-04-22 | **v4** | **Figma 전체 페이지 실측** (Style Guide · Logo · Avatar · Social Header · OG · Watermark · Favicon). 실제 토큰명 확정, Dark 모드 값 확정, AIGrit `NUM` 토큰 추가, 브랜드 자산 스펙 전부 추가. |
