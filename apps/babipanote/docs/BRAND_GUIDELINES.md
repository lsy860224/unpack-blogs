# babipanote — Brand Guidelines

> 1인 빌더의 하루를 기록하는 저널. AIGrit의 "전문 리뷰어" 톤과 확실히 구별되는 **개인적·편집체·종이 질감**을 기본값으로 한다.

- **도메인**: babipanote.com
- **포지션**: 바비파의 빌더 저널 (개인 블로그 / 연대기)
- **타겟**: 인디해커, 1인 창업자, 사이드 프로젝트 빌더
- **수익**: 최소 (광고 OFF, 브랜드 자산 축적 목적)
- **자매 사이트**: AIGrit (aigrit.dev) — 시각·보이스 모두 구별

---

## 1. Brand Voice

### 퍼스낼리티 5축 (0-10)

| 축 | 값 | 의미 |
|---|---|---|
| Formal ↔ Casual | **2** (Casual) | 말끝을 맺지 않고 흘러가는 일기체 허용 |
| Serious ↔ Playful | **4** | 대체로 진지하되 자조적 유머 OK |
| Expert ↔ Peer | **9** (Peer) | "가르치지 않는다" — 옆자리 빌더의 말투 |
| Enthusiastic ↔ Matter-of-fact | **5** | 숫자·실패 그대로. 과장 금지 |
| Traditional ↔ Modern | **7** | 모던하지만 에디토리얼 무게감 유지 |

### 톤앤매너
- **기본 인칭**: "나" / 독자는 지칭하지 않음 (편지 아닌 일기)
- **문장 길이**: 짧게 끊어 쓰기 기본, 호흡 긴 문단은 의도적 배치
- **시제**: 현재형·과거형 혼용. 회고는 과거, 관찰은 현재
- **줄바꿈**: 단락 사이 의도적 공백 허용 (노트 느낌)

### 호칭 / 금지 표현

| 사용 | 금지 |
|---|---|
| "오늘은 ~" "어제 ~했다" | "여러분" "독자분들" "보시는 분들" |
| "그냥 기록해둔다" | "꿀팁" "필수" "무조건" "인싸" |
| "실패했다" "아직 모르겠다" | "완벽한" "정답" "혁신" (과장어) |
| 구체 수치 ("3일" "1,200원") | 모호한 규모 ("엄청난" "엄청 많은") |

### UVP
> "1인 빌더의 실패와 배움을 가감 없이 기록하는 개인 저널 — 매출·숫자·감정까지 날것으로."

### 태그라인 (3개)

1. **"오늘도 만들고, 내일 더 나은 것을 만든다"** — 메인 (홈 히어로)
2. **"빌더의 하루는 코드와 고민 사이에서"** — 서브 (OG 디스크립션)
3. **"작게 시작해, 오래 기록한다"** — 아카이브 페이지용

### 메시지 기둥 (4개)

1. **솔직함 (Honesty)** — 숫자·실패·매출까지 있는 그대로
2. **과정 중심 (Process)** — 성공 사례보다 과정의 기록
3. **장기 관점 (Longevity)** — 번뜩이는 팁 대신 지속 가능한 루틴
4. **도구보다 사람 (Human > Tool)** — AI·SaaS 위에 선택하는 사람의 관점

---

## 2. Visual Identity

### 2-1. Color Palette (5색 시스템)

**디자인 컨셉**: "잉크와 종이" — 책·저널·원고지. AIGrit(Slate+Amber, 차갑고 선명한 리뷰어)의 대척점.

#### Primary 토큰 (Light Mode 기준)

| Role | Token | HEX | RGB | HSL | 용도 |
|---|---|---|---|---|---|
| Primary | `--color-brand-primary` | `#6B2E4E` | 107,46,78 | `335° 39% 30%` | 제목, 링크, 브랜드 |
| Secondary | `--color-brand-secondary` | `#C89F7C` | 200,159,124 | `25° 38% 64%` | 배지, 태그 배경 |
| Secondary Hover | `--color-brand-secondary-hover` | `#A87F5C` | 168,127,92 | `26° 29% 51%` | 호버 상태 |
| Accent (Growth) | `--color-brand-accent-green` | `#6B8A63` | 107,138,99 | `108° 16% 46%` | "완료" "출시" 배지 |
| Accent (Alert) | `--color-brand-accent-red` | `#9C4A3E` | 156,74,62 | `7° 43% 43%` | "실패" "중단" 배지 |
| Neutral Dark | `--color-neutral-ink` | `#2B2420` | 43,36,32 | `22° 15% 15%` | 본문 텍스트 |
| Neutral Light | `--color-neutral-paper` | `#FAF7F2` | 250,247,242 | `38° 40% 96%` | 배경 |

> **AIGrit 회피 기준**: AIGrit Primary = `#1E293B` (Hue 215°, Slate), Secondary = `#F59E0B` (Hue 38°, Amber). babipanote Primary Hue **335°**, Secondary Hue **25°** — Hue 원에서 Primary 거리 120°, Secondary는 가까우나 **채도·명도가 낮아 인상 확연히 다름** (AIGrit 채도 93% vs babipanote 38%).

#### Dark Mode 쌍

| Role | Light | Dark |
|---|---|---|
| Primary | `#6B2E4E` | `#C89BAE` |
| Secondary | `#C89F7C` | `#E0BEA0` |
| Accent Green | `#6B8A63` | `#A8BFA0` |
| Accent Red | `#9C4A3E` | `#C88072` |
| Background | `#FAF7F2` | `#1A1614` |
| Foreground | `#2B2420` | `#E8E0D6` |

#### WCAG 대비율 (4.5:1 이상 AA 통과)

| 조합 | 대비율 | 판정 |
|---|---|---|
| `#2B2420` on `#FAF7F2` (본문) | **13.8:1** | ✅ AAA |
| `#6B2E4E` on `#FAF7F2` (Primary 링크) | **9.4:1** | ✅ AAA |
| `#FAF7F2` on `#6B2E4E` (Primary 버튼) | **9.4:1** | ✅ AAA |
| `#6B8A63` on `#FAF7F2` (Accent Green 텍스트) | **3.1:1** | ⚠️ AA Large 전용 (배지만) |
| `#9C4A3E` on `#FAF7F2` (Accent Red 텍스트) | **5.6:1** | ✅ AA |
| `#C89F7C` on `#FAF7F2` (Secondary) | **2.1:1** | ❌ 텍스트 금지 · 배경·구분선 전용 |
| **Dark** `#E8E0D6` on `#1A1614` | **14.1:1** | ✅ AAA |
| **Dark** `#C89BAE` on `#1A1614` | **8.2:1** | ✅ AAA |

### 2-2. Typography

**컨셉**: 편집체. 제목은 세리프로 무게감, 본문은 산세리프로 가독성. 모두 오픈소스.

| 역할 | 한글 | 영문 | 라이선스 |
|---|---|---|---|
| **Display / Heading** | **Gowun Batang** | **Lora** | SIL OFL |
| **Body** | **Pretendard Variable** | **Inter** | SIL OFL |
| **Mono** | **JetBrains Mono** | 동일 | Apache 2.0 |

> 세리프(Gowun Batang)가 "저널" 인상의 핵심. AIGrit은 전체 산세리프(Pretendard) → 시각 구분 포인트.

#### 6단계 스케일 (1rem = 16px)

| 레벨 | Size | Line Height | Weight | 용도 |
|---|---|---|---|---|
| Display | `3.5rem` / 56px | 1.1 | 700 | 홈 히어로 1회 |
| H1 | `2.25rem` / 36px | 1.2 | 700 | 포스트 제목 |
| H2 | `1.5rem` / 24px | 1.35 | 600 | 섹션 제목 |
| Body | `1rem` / 16px | 1.75 | 400 | 본문 (긴 호흡) |
| Small | `0.875rem` / 14px | 1.6 | 400 | 메타·캡션 |
| XSmall | `0.75rem` / 12px | 1.5 | 500 | 타임스탬프·배지 |

### 2-3. Logo

**유형**: 워드마크 (심볼 없음, 타이포그래피 중심)

- **형태**: `babipanote` 전부 소문자, Gowun Batang Bold
- **색상**: Primary `#6B2E4E` (다크모드에서는 `#C89BAE`)
- **선택적 장식**: 단어 끝에 잉크 점 한 개 (`·`), Secondary 색상
- **로고 와이드마크 예시**:
  ```
  babipanote·
  ```

#### 디자인 브리프

- **키워드**: 잉크, 종이, 필사, 기록, 조용한 성장, 시간의 누적
- **금지**:
  - 그라디언트 (개인 저널 인상과 충돌)
  - 기술적 아이콘 (chip, circuit, cloud)
  - 네온·형광·채도 90% 이상 컬러
  - 강한 기하 심볼 (원·삼각형 로고 금지)
- **아이콘 방향** (향후 확장 시): 만년필 닙, 원고지 모서리, 북마크 리본 중 택1

#### 사이즈 사양

| 용도 | Size | Min |
|---|---|---|
| Header 로고 | 140×28px | 100×20px |
| Favicon | 32×32 / 16×16 | 'b' 모노그램만 |
| OG 이미지 내 | 180×36px | — |
| SNS 프로필 | 400×400 (정사각 'b') | 200×200 |

---

## 3. Digital Presence

### 3-1. Open Graph (OG)

- **규격**: 1200 × 630 px, PNG, < 300KB
- **레이아웃**: 왼쪽 60% 텍스트(제목 Gowun Batang 64pt + 작성일 Pretendard 20pt) · 오른쪽 40% Paper 텍스처 + 워드마크
- **배경**: `#FAF7F2` (다크 테마 전용 OG는 `#1A1614`)
- **테두리**: 하단 4px Primary(`#6B2E4E`)

### 3-2. Meta Tags (HTML 스니펫)

```html
<!-- Primary -->
<title>글 제목 — babipanote</title>
<meta name="description" content="150자 이내 설명" />

<!-- Open Graph -->
<meta property="og:type" content="article" />
<meta property="og:site_name" content="babipanote" />
<meta property="og:title" content="글 제목" />
<meta property="og:description" content="150자 이내 설명" />
<meta property="og:url" content="https://babipanote.com/blog/slug" />
<meta property="og:image" content="https://babipanote.com/og/slug.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="ko_KR" />

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="글 제목" />
<meta name="twitter:description" content="150자 이내 설명" />
<meta name="twitter:image" content="https://babipanote.com/og/slug.png" />

<!-- Theme Color (다크/라이트) -->
<meta name="theme-color" content="#FAF7F2" media="(prefers-color-scheme: light)" />
<meta name="theme-color" content="#1A1614" media="(prefers-color-scheme: dark)" />
```

### 3-3. SNS 규격

| 플랫폼 | 프로필 | 배너 | 핸들(권장) |
|---|---|---|---|
| X (Twitter) | 400×400 | 1500×500 | `@babipanote` |
| Instagram | 320×320 | — | `@babipanote` |
| GitHub | 460×460 | — | 조직 또는 개인 계정 |
| Threads | 320×320 | — | `@babipanote` |

### 3-4. Favicon

- `favicon.ico` (32×32, 16×16 멀티)
- `icon.svg` (벡터, 'b' 모노그램 Gowun Batang)
- `apple-touch-icon.png` (180×180, Paper 배경 + Primary 'b')

---

## 4. Code Tokens

### 4-1. Tailwind v4 `@theme` 블록 (globals.css)

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@variant dark (&:where(.dark, .dark *));

@theme {
  /* Brand */
  --color-brand-primary: #6B2E4E;
  --color-brand-secondary: #C89F7C;
  --color-brand-secondary-hover: #A87F5C;
  --color-brand-accent-green: #6B8A63;
  --color-brand-accent-red: #9C4A3E;

  /* Neutrals */
  --color-neutral-ink: #2B2420;
  --color-neutral-paper: #FAF7F2;

  /* Fonts */
  --font-serif:
    var(--font-gowun-batang, "Gowun Batang"), var(--font-lora, "Lora"),
    Georgia, "Times New Roman", serif;
  --font-sans:
    var(--font-pretendard, "Pretendard Variable"), var(--font-inter, "Inter"),
    system-ui, -apple-system, sans-serif;
  --font-mono:
    var(--font-jetbrains, "JetBrains Mono"), ui-monospace, "SFMono-Regular",
    Menlo, monospace;

  /* Type Scale */
  --text-display: 3.5rem;
  --text-display--line-height: 1.1;
  --text-h1: 2.25rem;
  --text-h1--line-height: 1.2;
  --text-h2: 1.5rem;
  --text-h2--line-height: 1.35;
  --text-body: 1rem;
  --text-body--line-height: 1.75;
  --text-small: 0.875rem;
  --text-xsmall: 0.75rem;
}

:root {
  --background: #FAF7F2;
  --foreground: #2B2420;
}

.dark {
  --background: #1A1614;
  --foreground: #E8E0D6;

  --color-brand-primary: #C89BAE;
  --color-brand-secondary: #E0BEA0;
  --color-brand-accent-green: #A8BFA0;
  --color-brand-accent-red: #C88072;
}

@layer base {
  body {
    background: var(--background);
    color: var(--foreground);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }

  h1, h2, h3, .display {
    font-family: var(--font-serif);
    letter-spacing: -0.01em;
  }

  code, pre, kbd {
    font-family: var(--font-mono);
  }
}
```

### 4-2. CSS 변수만 (non-Tailwind 환경용)

```css
:root {
  --bp-primary: #6B2E4E;
  --bp-secondary: #C89F7C;
  --bp-secondary-hover: #A87F5C;
  --bp-accent-green: #6B8A63;
  --bp-accent-red: #9C4A3E;
  --bp-ink: #2B2420;
  --bp-paper: #FAF7F2;
}

.dark {
  --bp-primary: #C89BAE;
  --bp-secondary: #E0BEA0;
  --bp-accent-green: #A8BFA0;
  --bp-accent-red: #C88072;
  --bp-ink: #E8E0D6;
  --bp-paper: #1A1614;
}
```

---

## 5. 3관점 검증

### 🔴 비판적
- **Secondary `#C89F7C`의 낮은 대비**: 본문 텍스트로 쓰면 WCAG 미달. 가이드라인에 "배경·구분선 전용" 명시로 완화했으나, 실무에서 배지 텍스트에 잘못 쓰면 접근성 실패.
- **Gowun Batang 가변폰트 미지원**: 웨이트 400/700만 제공 → 중간 웨이트가 필요할 때 Lora로 대체 필요. 한글에선 가짜-볼드 렌더링 위험.
- **Primary(#6B2E4E) Hue 335°는 Pink/Rose 영역**: 일부 독자에게 "여성향 블로그" 인상을 줄 수 있음. "빌더의 저널"이라는 중성적 포지션과 충돌 가능성 — 채도를 낮춰 plum/burgundy 인상으로 방어했으나, 로고·OG 실사 시 재검토 필요.
- **세리프 본문 위험**: 저널 인상을 위해 헤딩만 세리프로 제한. 본문까지 세리프 쓰면 한국어 화면 가독성 급락.

### 🟢 긍정적
- **AIGrit과 명확히 구별**: Hue 120° 차이 + 채도 55%p 차이 + 세리프 헤딩 → 로고 없이도 즉각 식별 가능.
- **타겟 적합성**: 인디해커·1인 창업자는 "과시형 랜딩"보다 "정직한 기록"에 반응 — Paper/Ink 컨셉이 신뢰 축적 포지셔닝에 맞음.
- **확장성**: 향후 뉴스레터·PDF·프린트 매체로 확장 시 세리프+페이퍼 시스템이 그대로 이식 가능.
- **유지비 낮음**: 오픈소스 폰트 + 광고 제거 + 정적 팔레트 → 장기 운영 부담 최소.

### ⚪ 중립적
- **도메인 babipanote.com 가용성은 사용자가 확보한 것으로 전제** (재검증 권장: `dig babipanote.com`).
- **SNS 핸들 `@babipanote`는 미확인** — 공개 전 X·Instagram·Threads 3곳 선점 필요.
- **로고는 브리프 단계**: 실제 워드마크 SVG는 디자인 툴(Figma)에서 별도 제작. 본 문서는 발주 기준선.
- **OG 이미지 자동 생성 여부**: 정적 PNG vs `@vercel/og`로 런타임 생성 중 선택 필요. Phase 2에서 결정.

---

## 다음 단계

- **필수**: Phase 1-2 → `apps/babipanote/brand.config.ts`에 본 문서 토큰 반영
- **필수**: Phase 1-3 → `apps/babipanote/src/app/globals.css`에 `4-1` 블록 복사, `layout.tsx`에서 Gowun Batang + Lora `next/font` 연결
- **권장**: `/content-strategist` → 본 문서 "Voice" 섹션 기반 콘텐츠 캘린더 설계
- 💡 **판단 기준**: 컬러·폰트 실사 후 OG 샘플 1장 렌더 → 인상이 "journal"로 읽히면 확정, "여성향 라이프스타일"로 읽히면 Primary를 `#4E3B55` (deeper aubergine)로 재조정.
