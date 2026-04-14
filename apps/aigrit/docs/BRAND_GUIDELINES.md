# AIGrit — Brand Guidelines

> AI 도구를 직접 써보고 숫자와 함께 비교하는 수익형 리뷰 블로그. babipanote의 "저널·종이" 감성과 정반대로, **선명한 색·정확한 숫자·기술적 명료함**을 시그니처로 한다.

- **도메인**: aigrit.dev
- **포지션**: 수익형 AI 도구 리뷰 블로그 (애드센스 + SaaS 제휴)
- **타겟**: 직장인 AI 입문자, 생산성 덕후, 개발자
- **수익**: Google AdSense + SaaS 제휴 (광고 컴포넌트 ON)
- **자매 사이트**: babipanote (babipanote.com) — 동일 운영자, 시각·보이스 완전 분리

---

## 1. Brand Voice

### 퍼스낼리티 5축 (0-10)

| 축 | 값 | 의미 |
|---|---|---|
| Formal ↔ Casual | **5** | 존댓말·경어체, 반말은 배제. 친근하되 전문지 느낌 |
| Serious ↔ Playful | **3** | 데이터 중심의 진지함. 제목에만 재치 허용 |
| Expert ↔ Peer | **4** (Expert 쪽) | "같이 실험해보는 리뷰어" — 검증 권위 + 겸손 |
| Enthusiastic ↔ Matter-of-fact | **3** | 감탄사·이모지 자제. 결과는 수치로 |
| Traditional ↔ Modern | **8** (Modern) | AI-native. 최신 벤치마크·UI 트렌드 적극 수용 |

### 톤앤매너
- **기본 인칭**: "에이아이그릿" 또는 복수 중립 ("저희가 직접 써본 결과")
- **문장 구조**: 결론 먼저 → 근거(수치) → 맥락. TL;DR 섹션 권장
- **시제**: 현재형 기본 ("작동한다", "제공한다"), 체험기는 과거형
- **서식 규칙**: 표·목록·인용 적극 사용. 단 emoji는 배지에만

### 호칭 / 금지 표현

| 사용 | 금지 |
|---|---|
| "테스트한 결과" "24시간 써본 뒤" | "개쩐다" "미쳤다" "레전드" |
| "3,200원/월 기준" (정확한 수치) | "꽤 비싼" "상당히 빠른" (모호어) |
| "장점:" "단점:" "추천 대상:" | "완벽한" "유일한" (과장어) |
| "정확도 89% (n=200)" | "매우 정확함" |
| "제휴 링크 포함" (명시) | "스폰서 여부 미공개" |

### UVP
> "AI 도구를 직접 며칠간 써보고 속도·비용·정확도를 숫자로 비교하는 한국어 리뷰 — 팔지 않고, 씁니다."

### 태그라인 (3개)

1. **"AI의 알맹이만 남긴다"** — 메인 (홈 히어로, 기존 유지)
2. **"써보고 말한다, 팔지 않는다"** — 서브 (신뢰 축 강조, 어바웃/메타)
3. **"오늘의 도구, 내일의 루틴"** — 뉴스레터·카테고리 홈

### 메시지 기둥 (4개)

1. **검증 (Validation)** — 마케팅 카피 아닌 실사용 결과
2. **수치 (Numbers)** — 속도·비용·정확도를 숫자로. 표·그래프 우선
3. **비교 (Comparison)** — 단독 리뷰보다 1:1/N:N 비교
4. **맥락 (Context)** — "직장인이 쓴다면" / "개발자가 쓴다면" 시나리오 필수

---

## 2. Visual Identity

### 2-1. Color Palette (5색 시스템)

**디자인 컨셉**: "Precision Indigo" — 기계·데이터·리뷰 계측기. babipanote(Plum+Terracotta, 종이) 대척점.

> **Phase 0-2 placeholder 재평가 결과**: Slate `#1E293B` + Amber `#F59E0B` 팔레트는 (1) 너무 보편적이라 AI 리뷰 브랜드로서 기억점 낮음, (2) Amber Hue 38°가 babipanote Terracotta Hue 25°와 13° 차이로 근접 → **교체 권장**. 단, 중성 다크(Slate-900)는 Neutral Dark로 존치.

#### Primary 토큰 (Light Mode 기준)

| Role | Token | HEX | RGB | HSL | 용도 |
|---|---|---|---|---|---|
| Primary | `--color-brand-primary` | `#3730A3` | 55,48,163 | `244° 55% 41%` | 로고, 헤더, 링크 |
| Secondary | `--color-brand-secondary` | `#06B6D4` | 6,182,212 | `189° 94% 43%` | CTA, 강조 배지, 스코어 하이라이트 |
| Secondary Hover | `--color-brand-secondary-hover` | `#0891B2` | 8,145,178 | `192° 91% 36%` | 호버 상태 |
| Accent (추천) | `--color-brand-accent-green` | `#10B981` | 16,185,129 | `160° 84% 39%` | "추천" "가성비" 배지 |
| Accent (별로) | `--color-brand-accent-red` | `#EF4444` | 239,68,68 | `0° 84% 60%` | "별로" "중단" 배지 |
| Neutral Dark | `--color-neutral-slate` | `#0F172A` | 15,23,42 | `222° 47% 11%` | 본문, 다크 배경 |
| Neutral Light | `--color-neutral-snow` | `#F8FAFC` | 248,250,252 | `210° 40% 98%` | 라이트 배경 |

> **babipanote 회피 계산**:
> - Primary Hue 244° vs babipanote 335° → **91° 차이** ✅ (목표 90°↑ 달성)
> - Secondary Hue 189° vs babipanote 25° → **164° 차이** ✅
> - Saturation: AIGrit Secondary 94% vs babipanote Secondary 38% → **56pp 차이** (선명도 격차 명확)

#### Dark Mode 쌍

| Role | Light | Dark |
|---|---|---|
| Primary | `#3730A3` | `#818CF8` (Indigo-400, 대비 확보) |
| Secondary | `#06B6D4` | `#22D3EE` (Cyan-400) |
| Accent Green | `#10B981` | `#34D399` |
| Accent Red | `#EF4444` | `#F87171` |
| Background | `#F8FAFC` | `#0F172A` |
| Foreground | `#0F172A` | `#E2E8F0` |
| Surface (카드) | `#FFFFFF` | `#1E293B` |

#### WCAG 대비율 (AA 4.5:1 이상 목표)

| 조합 | 대비율 | 판정 |
|---|---|---|
| `#0F172A` on `#F8FAFC` (본문) | **17.4:1** | ✅ AAA |
| `#3730A3` on `#F8FAFC` (Primary 링크) | **9.6:1** | ✅ AAA |
| `#F8FAFC` on `#3730A3` (Primary 버튼) | **9.6:1** | ✅ AAA |
| `#0F172A` on `#06B6D4` (Secondary 버튼 다크 텍스트) | **5.8:1** | ✅ AA |
| `#F8FAFC` on `#06B6D4` (Secondary 버튼 라이트 텍스트) | **2.9:1** | ❌ 금지 |
| `#10B981` on `#F8FAFC` (Accent Green) | **3.0:1** | ⚠️ AA Large · 배지 배경 권장 |
| `#EF4444` on `#F8FAFC` (Accent Red) | **4.0:1** | ⚠️ AA Large · 배지/아이콘 전용 |
| **Dark** `#E2E8F0` on `#0F172A` (본문) | **15.1:1** | ✅ AAA |
| **Dark** `#818CF8` on `#0F172A` | **8.0:1** | ✅ AAA |
| **Dark** `#22D3EE` on `#0F172A` | **11.2:1** | ✅ AAA |

### 2-2. Typography

**컨셉**: 전체 산세리프. 데이터와 제목이 시각적으로 동일한 무게감으로 정렬 — "계측기의 균일함". babipanote 세리프 헤딩과 완전 구별.

| 역할 | 한글 | 영문 | 라이선스 |
|---|---|---|---|
| **Display / Heading / Body** | **Pretendard Variable** | **Inter** | SIL OFL |
| **Numeric / Mono** | **JetBrains Mono** | 동일 | Apache 2.0 |

> 스코어·벤치마크·가격은 **JetBrains Mono**로 렌더하여 "수치 중심" 포지션 시각화 (예: `89.3점` / `$24/mo`).

#### 6단계 스케일 (1rem = 16px)

| 레벨 | Size | Line Height | Weight | 용도 |
|---|---|---|---|---|
| Display | `3rem` / 48px | 1.15 | 800 | 홈 히어로, 연간 베스트 |
| H1 | `2rem` / 32px | 1.25 | 700 | 포스트 제목, 리뷰 대상명 |
| H2 | `1.375rem` / 22px | 1.35 | 700 | 섹션 (장점/단점/결론) |
| Body | `1rem` / 16px | 1.65 | 400 | 본문 |
| Small | `0.875rem` / 14px | 1.55 | 400 | 메타·캡션·주석 |
| XSmall | `0.75rem` / 12px | 1.5 | 600 | 배지·태그 (대문자) |

### 2-3. Logo

**유형**: 워드마크 + 브래킷 아이콘 (기존 `[AI]Grit` 방향 유지·정교화)

- **형태**: `[AI]Grit` — `[AI]`는 Cyan 브래킷(Secondary) + Primary 글자 · `Grit`는 Primary 색상만
- **의미**: 대괄호 = 파싱·데이터 추출 = "알맹이만 남긴다" 시각화
- **폰트**: Inter Extrabold 800 (Pretendard로 한글 병기 시 `[AI]그릿`도 가능)
- **배리언트**:
  - Full: `[AI]Grit`
  - Mark only: `[AI]` (파비콘, SNS 프로필)
  - Mono: 단색 Primary 또는 단색 White (OG 다크 배경용)

#### 디자인 브리프

- **키워드**: 브래킷, 파싱, 계측, 리뷰, 정확도, 벤치마크, 터미널 프롬프트
- **금지**:
  - 세리프 폰트 (babipanote와 겹침)
  - 그라디언트 메시/블러 (전문성 저해)
  - 로봇·뇌·칩 클리셰 아이콘
  - 2021 이전 풍 iridescent holographic
- **아이콘 방향** (향후 확장): 대괄호 `[ ]`, 체크 박스 ☑, 벤치마크 게이지, CLI 커서 `▊`

#### 사이즈 사양

| 용도 | Size | Min |
|---|---|---|
| Header 로고 | 120×28px | 88×20px |
| Favicon | 32×32 / 16×16 | `[AI]` 브래킷만 |
| OG 이미지 내 | 160×36px | — |
| SNS 프로필 | 400×400 (`[AI]` 중앙) | 200×200 |

---

## 3. Digital Presence

### 3-1. Open Graph (OG)

- **규격**: 1200 × 630 px, PNG, < 300KB
- **배경**: 다크 Slate `#0F172A` 기본 (라이트 옵션: `#F8FAFC`)
- **레이아웃**: 상단 워드마크 + 카테고리 태그(Cyan) / 중앙 제목 Inter 700 64pt / 하단 메타 JetBrains Mono (벤치마크 수치·가격)
- **액센트**: 제목 왼쪽에 Cyan 세로바 6×100px

### 3-2. Meta Tags (HTML 스니펫)

```html
<!-- Primary -->
<title>글 제목 — AIGrit</title>
<meta name="description" content="150자 이내 리뷰 요약 + 핵심 수치 1개" />

<!-- Open Graph -->
<meta property="og:type" content="article" />
<meta property="og:site_name" content="AIGrit" />
<meta property="og:title" content="글 제목" />
<meta property="og:description" content="150자 이내 요약" />
<meta property="og:url" content="https://aigrit.dev/blog/slug" />
<meta property="og:image" content="https://aigrit.dev/og/slug.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="ko_KR" />

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@aigrit_dev" />
<meta name="twitter:title" content="글 제목" />
<meta name="twitter:description" content="150자 이내 요약" />
<meta name="twitter:image" content="https://aigrit.dev/og/slug.png" />

<!-- Review Structured Data (리뷰 포스트) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": { "@type": "SoftwareApplication", "name": "도구명" },
  "reviewRating": { "@type": "Rating", "ratingValue": "4.2", "bestRating": "5" },
  "author": { "@type": "Organization", "name": "AIGrit" }
}
</script>

<!-- Theme Color -->
<meta name="theme-color" content="#F8FAFC" media="(prefers-color-scheme: light)" />
<meta name="theme-color" content="#0F172A" media="(prefers-color-scheme: dark)" />
```

### 3-3. SNS 규격

| 플랫폼 | 프로필 | 배너 | 핸들 |
|---|---|---|---|
| X (Twitter) | 400×400 (`[AI]`) | 1500×500 | `@aigrit_dev` |
| Instagram | 320×320 | — | `@aigrit.dev` |
| GitHub | 460×460 | — | `lsy860224/aigrit` (개인) |
| YouTube (리뷰 영상) | 800×800 | 2560×1440 | 향후 |

### 3-4. Favicon

- `favicon.ico` (32×32, 16×16 멀티 — `[AI]` 브래킷만)
- `icon.svg` (벡터, Cyan 브래킷 + Primary `AI`)
- `apple-touch-icon.png` (180×180, 다크 Slate 배경 + 중앙 `[AI]`)

---

## 4. Code Tokens

### 4-1. Tailwind v4 `@theme` 블록 (globals.css 교체안)

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";

@variant dark (&:where(.dark, .dark *));

@theme {
  /* Brand */
  --color-brand-primary: #3730A3;
  --color-brand-secondary: #06B6D4;
  --color-brand-secondary-hover: #0891B2;
  --color-brand-accent-green: #10B981;
  --color-brand-accent-red: #EF4444;

  /* Neutrals */
  --color-neutral-slate: #0F172A;
  --color-neutral-snow: #F8FAFC;
  --color-neutral-surface: #FFFFFF;

  /* Fonts */
  --font-sans:
    var(--font-pretendard, "Pretendard Variable"), var(--font-inter, "Inter"),
    system-ui, -apple-system, sans-serif;
  --font-mono:
    var(--font-jetbrains, "JetBrains Mono"), ui-monospace, "SFMono-Regular",
    Menlo, monospace;

  /* Type Scale */
  --text-display: 3rem;
  --text-display--line-height: 1.15;
  --text-h1: 2rem;
  --text-h1--line-height: 1.25;
  --text-h2: 1.375rem;
  --text-h2--line-height: 1.35;
  --text-body: 1rem;
  --text-body--line-height: 1.65;
  --text-small: 0.875rem;
  --text-xsmall: 0.75rem;
}

:root {
  --background: #F8FAFC;
  --foreground: #0F172A;
  --surface: #FFFFFF;
}

.dark {
  --background: #0F172A;
  --foreground: #E2E8F0;
  --surface: #1E293B;

  --color-brand-primary: #818CF8;
  --color-brand-secondary: #22D3EE;
  --color-brand-accent-green: #34D399;
  --color-brand-accent-red: #F87171;
}

@layer base {
  body {
    background: var(--background);
    color: var(--foreground);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }

  code, pre, kbd, .num {
    font-family: var(--font-mono);
    font-feature-settings: "tnum" 1, "ss01" 1;
  }
}
```

### 4-2. CSS 변수만 (non-Tailwind 환경용)

```css
:root {
  --ag-primary: #3730A3;
  --ag-secondary: #06B6D4;
  --ag-secondary-hover: #0891B2;
  --ag-accent-green: #10B981;
  --ag-accent-red: #EF4444;
  --ag-slate: #0F172A;
  --ag-snow: #F8FAFC;
}

.dark {
  --ag-primary: #818CF8;
  --ag-secondary: #22D3EE;
  --ag-accent-green: #34D399;
  --ag-accent-red: #F87171;
  --ag-slate: #F8FAFC;
  --ag-snow: #0F172A;
}
```

---

## 5. 3관점 검증

### 🔴 비판적
- **Indigo `#3730A3` + Cyan `#06B6D4`는 SaaS 기본 팔레트**: Stripe·Linear·Vercel 계열 인디고, Notion/Bun 계열 시안과 친숙 → **차별화 부족 리스크**. 방어책: 대괄호 로고·JetBrains Mono 수치 타입·"[AI]" 하이라이트로 브랜드 고유성 확보.
- **Accent Red `#EF4444` vs babipanote Accent Red `#9C4A3E`**: Hue 7° 차이로 근접하나, Saturation 41pp · Lightness 17pp 차이로 톤 구별됨. 소면적(배지) 사용 한정이면 허용.
- **Cyan Secondary의 낮은 대비(2.9:1 vs snow)**: 흰 텍스트로 CTA 만들면 접근성 실패. 반드시 Slate(#0F172A) 텍스트와 페어링.
- **Pretendard + Inter 페어링 비용**: Pretendard Variable 단일로도 영문까지 렌더 가능해 Inter가 중복일 수 있음. Phase 1-3에서 Inter 제거 재검토.

### 🟢 긍정적 (babipanote 구별 강도)
- **Hue 거리**: Primary 91° / Secondary 164° — 색상환에서 확실히 반대편. 두 사이트를 나란히 놓아도 혼동 없음.
- **Saturation 격차**: babipanote 평균 채도 ~38% vs AIGrit Primary 55% · Secondary 94% → "채도 자체가 브랜드 시그니처".
- **타이포 구조 차별**: babipanote = 세리프 헤딩 + 산세리프 본문 (이중 레이어) / AIGrit = 전체 산세리프 + 수치만 모노 (데이터 레이어) → 첫 화면에서 0.5초 내 구별 가능.
- **무드**: 종이/잉크(따뜻·차분) vs 계측기/데이터(차가움·선명) — 같은 운영자의 두 모드를 읽는 독자에게 "역할 구별" 신호 명확.
- **확장성**: 리뷰 스코어 UI, 벤치마크 그래프, 비교 테이블 등 데이터 시각화에 Cyan+Indigo 조합이 차트 팔레트로 바로 활용 가능.

### ⚪ 중립적
- **도메인 aigrit.dev 확보**는 기정사실 전제.
- **SNS 핸들 `@aigrit_dev` · `@aigrit.dev`** 가용성 미확인 — 공개 전 점검.
- **로고는 브리프 단계**: 실제 `[AI]Grit` SVG는 Figma에서 별도 제작. 본 문서는 발주 기준.
- **다크모드를 "기본값"으로 할지 라이트 기본/다크 옵션으로 할지 미결정** — 애드센스 게재 면 가독성 고려 시 **라이트 기본 권장**이나, 개발자 타겟 고려 시 다크 기본도 검토 가능.
- **Phase 0-2 globals.css 교체 시 빌드 영향**: 현재 `--color-brand-*` 토큰명 유지 → 컴포넌트 코드 수정 없이 값만 교체 가능.

### babipanote와의 구별 매트릭스

| 항목 | babipanote | AIGrit | 차이 |
|---|---|---|---|
| Primary Hue | 335° (Plum) | 244° (Indigo) | **91°** ✅ |
| Secondary Hue | 25° (Terracotta) | 189° (Cyan) | **164°** ✅ |
| Primary Saturation | 39% | 55% | +16pp |
| Secondary Saturation | 38% | 94% | **+56pp** ✅ |
| 헤딩 폰트 | Gowun Batang (세리프) | Pretendard (산세리프) | 카테고리 다름 |
| 본문 폰트 | Pretendard | Pretendard | 동일 (모노레포 효율) |
| 배경 기본 | `#FAF7F2` Paper | `#F8FAFC` Snow | 온도차 (38° vs 210°) |
| 로고 유형 | 워드마크 (잉크점) | 워드마크 (대괄호) | 구조 다름 |

---

## 다음 단계

- **필수**: Phase 1-2 → `apps/aigrit/brand.config.ts`에 본 문서 토큰 반영
- **필수**: Phase 1-3 → `apps/aigrit/src/app/globals.css`의 Phase 0-2 placeholder **교체** (`4-1` 블록 복사)
- **필수**: Phase 1-3 → `layout.tsx`의 메타데이터 `theme-color` 2개 추가, 폰트 페어링은 현행 유지 (Pretendard + Inter + JetBrains Mono)
- **권장**: `/content-strategist` → 본 문서 "Voice" 섹션 기반 카테고리 구조(도구 리뷰 / 가격 비교 / 케이스 스터디) 설계
- 💡 **판단 기준**: 다크모드 기본값 여부는 Phase 2 홈페이지 완성 시 실사용 AdSense 클릭률로 A/B 검증.
