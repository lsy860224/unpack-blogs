# OG 썸네일 자동 생성 가이드

> Figma MCP로 OG 이미지(1200×630)를 자동 생성한다.
> Claude Code가 글 발행 시 이 문서를 참조하여 썸네일을 만든다.

## 생성 도구

**Figma MCP** (`mcp__claude_ai_Figma__use_figma`) — JavaScript Plugin API로 Figma 파일에 OG 프레임 생성 → PNG 내보내기.

## 사이트별 템플릿

---

### AIGrit (aigrit.dev)

**디자인 컨셉:** "Precision Indigo" — 어둡고 선명한 리뷰어 톤

```
┌──────────────────────────────────────────────────┐
│ ┌─────────┐                              ┌─┐    │
│ │ 카테고리 │                              │ │    │
│ └─────────┘                              └─┘    │
│                                                  │
│  메인 타이틀 (흰색, 볼드)                         │
│  서브 타이틀 (시안, 볼드)                         │
│                                                  │
│                                                  │
│  ──────                                          │
│  [AI] Grit                          aigrit.dev   │
│  AI의 알맹이만 남긴다                              │
└──────────────────────────────────────────────────┘
```

**스펙:**

| 요소 | 값 |
|---|---|
| 프레임 | 1200×630 |
| 배경 | 그라디언트: `#0F172A` → `#1E1B4B` (좌상→우하) |
| 카테고리 뱃지 | 좌상단 (x:60, y:40), 배경 `#EF4444`, 텍스트 흰색, 라운드 20, 패딩 12×24 |
| 코너 장식 | 우상단 (x:1100, y:40), L-bracket, `#06B6D4`, 두께 3, 크기 50×50 |
| 메인 타이틀 | x:60, y:180, 흰색 `#FFFFFF`, Bold, 48px, maxWidth 1000, 1~2줄 |
| 서브 타이틀 | 메인 아래 16px, `#06B6D4`, Bold, 40px, 1줄 (키워드 요약) |
| 구분선 | x:60, y:500, 너비 60, 높이 3, `#3730A3` |
| 로고 텍스트 | x:60, y:520, "[AI] Grit", `#06B6D4`, Semi Bold, 24px |
| 태그라인 | x:60, y:552, "AI의 알맹이만 남긴다", `#94A3B8`, 14px |
| 도메인 | x:1080, y:552, "aigrit.dev", `#94A3B8`, 14px, 우측 정렬 |

**폰트:**
- 한글: Pretendard (없으면 Inter 폴백)
- 영문: Inter
- 폰트 로딩 실패 시 반드시 try/catch + Inter 폴백

**입력값 (Claude Code가 제공):**
- `title`: 메인 타이틀 (한글, 최대 2줄)
- `subtitle`: 서브 타이틀 (키워드 요약, 1줄)
- `category`: 뱃지 텍스트 (예: "코딩 도구", "LLM", "생산성")
- `slug`: 파일 저장용

---

### babipanote (babipanote.com)

**디자인 컨셉:** "잉크와 종이" — 따뜻하고 개인적인 저널 톤

```
┌──────────────────────────────────────────────────┐
│ ┌──────┐  2026.04.15                      ""     │
│ │ 유형 │                                         │
│ └──────┘                                         │
│                                                  │
│  메인 타이틀 (다크 플럼, 볼드)                     │
│  (2줄까지)                                        │
│                                                  │
│                                                  │
│  ──────                                          │
│  babipa                          babipanote·     │
│  빌더의 하루는 코드와 고민 사이에서   babipanote.com │
└──────────────────────────────────────────────────┘
```

**스펙:**

| 요소 | 값 |
|---|---|
| 프레임 | 1200×630 |
| 배경 | 그라디언트: `#FAF7F2` → `#F0EBE3` (좌상→우하) |
| 유형 뱃지 | 좌상단 (x:60, y:40), 배경 `#6B2E4E`, 텍스트 흰색, 라운드 20, 패딩 12×24 |
| 날짜 | 뱃지 우측 16px, `#A08B7A`, 16px, "YYYY.MM.DD" |
| 인용 장식 | 우상단 (x:1060, y:40), 큰따옴표 "", `#6B2E4E` 40%, 크기 60×50 |
| 메인 타이틀 | x:60, y:200, `#2B2420`, Bold, 48px, maxWidth 1000, 1~2줄 |
| 서브 타이틀 | **없음** (babipanote는 타이틀만) |
| 구분선 | x:60, y:500, 너비 60, 높이 3, `#C89F7C` |
| 저자명 | x:60, y:520, "babipa", `#2B2420`, Semi Bold, 22px |
| 태그라인 | x:60, y:550, "빌더의 하루는 코드와 고민 사이에서", `#A08B7A`, 14px |
| 브랜드 | x:1060, y:520, "babipanote·", `#6B2E4E`, Semi Bold, 20px, 우측 정렬 |
| 도메인 | x:1060, y:548, "babipanote.com", `#A08B7A`, 14px, 우측 정렬 |

**폰트:**
- 한글 제목: Gowun Batang (없으면 serif 폴백)
- 한글 본문: Pretendard
- 영문: Lora (제목) / Inter (본문)

**입력값:**
- `title`: 메인 타이틀 (감성적, 최대 2줄)
- `type`: 뱃지 텍스트 ("저널", "수익 리포트", "에세이", "빌드로그")
- `date`: 발행일 (YYYY.MM.DD)
- `slug`: 파일 저장용

---

## Figma MCP 실행 패턴

### 1. Figma 파일 생성 (또는 기존 파일 사용)

```javascript
// create_new_file로 새 파일 생성 또는 기존 OG 템플릿 파일 사용
// planKey 없으면 개인 Drafts에 생성
```

### 2. OG 프레임 생성 스크립트 (AIGrit 예시)

```javascript
// use_figma로 실행 — 50k 문자 제한 주의

const page = figma.currentPage;

// 프레임 생성
const frame = figma.createFrame();
frame.name = "OG — {slug}";
frame.resize(1200, 630);

// 배경 그라디언트
frame.fills = [{
  type: "GRADIENT_LINEAR",
  gradientTransform: [[0.7, 0.3, 0], [-0.3, 0.7, 0]],
  gradientStops: [
    { position: 0, color: { r: 15/255, g: 23/255, b: 42/255, a: 1 } },
    { position: 1, color: { r: 30/255, g: 27/255, b: 75/255, a: 1 } }
  ]
}];

// 카테고리 뱃지
const badge = figma.createFrame();
badge.name = "category-badge";
badge.resize(100, 36);
badge.x = 60; badge.y = 40;
badge.cornerRadius = 20;
badge.fills = [{ type: "SOLID", color: { r: 239/255, g: 68/255, b: 68/255 } }];

const badgeText = figma.createText();
await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
badgeText.fontName = { family: "Inter", style: "Semi Bold" };
badgeText.characters = "{category}";
badgeText.fontSize = 14;
badgeText.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
badge.appendChild(badgeText);
// ... 센터 정렬

// 메인 타이틀
const title = figma.createText();
try {
  await figma.loadFontAsync({ family: "Pretendard", style: "Bold" });
  title.fontName = { family: "Pretendard", style: "Bold" };
} catch {
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  title.fontName = { family: "Inter", style: "Bold" };
}
title.characters = "{title}";
title.fontSize = 48;
title.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
title.x = 60; title.y = 180;
title.resize(1000, 120);
title.textAutoResize = "HEIGHT";

// 서브 타이틀 (Cyan)
const subtitle = figma.createText();
subtitle.fontName = { family: "Inter", style: "Bold" };
subtitle.characters = "{subtitle}";
subtitle.fontSize = 40;
subtitle.fills = [{ type: "SOLID", color: { r: 6/255, g: 182/255, b: 212/255 } }];
subtitle.x = 60;
subtitle.y = title.y + title.height + 16;

// ... 로고, 도메인, 구분선, 코너 장식 생략 (패턴 동일)

frame.appendChild(badge);
frame.appendChild(title);
frame.appendChild(subtitle);
page.appendChild(frame);
```

### 3. PNG 내보내기

Figma MCP에서 직접 PNG 내보내기는 제한적. 대안:
1. **`get_screenshot`** 도구로 프레임 캡처 → 로컬 저장
2. 또는 Figma UI에서 수동 Export (Cmd+Shift+E)

### 4. 로컬 저장 경로

```
apps/{app}/public/images/{slug}/og.png
```

---

## 글쓰기 워크플로우 통합

CLAUDE.md의 "글쓰기 워크플로우 Step 4"에서 이 문서를 참조:

1. Claude Code가 slug·title·category(or type) 확인
2. `docs/THUMBNAIL.md` 읽기
3. Figma MCP로 OG 프레임 생성
4. get_screenshot으로 캡처 또는 수동 Export 안내
5. `apps/{app}/public/images/{slug}/og.png` 저장 확인
6. MDX frontmatter `thumbnail: "/images/{slug}/og.png"` 자동 설정

## 카테고리/유형 매핑

### AIGrit 카테고리

| category 값 | 뱃지 텍스트 | 배경색 |
|---|---|---|
| llm | LLM | `#EF4444` |
| coding-tools | 코딩 도구 | `#EF4444` |
| productivity | 생산성 | `#EF4444` |
| saas-review | SaaS 리뷰 | `#EF4444` |
| knowledge | 지식관리 | `#EF4444` |
| notice | 공지 | `#EF4444` |

### babipanote 유형

| type 값 | 뱃지 텍스트 |
|---|---|
| buildlog | 빌드로그 |
| revenue-report | 수익 리포트 |
| lesson | 교훈 |
| essay | 에세이 |
| tool-review | 도구 리뷰 |
| journal (default) | 저널 |

## Figma 주의사항

- 한글 폰트(Pretendard, Gowun Batang)는 워크스페이스 미동기화 빈번 → **항상 try/catch + Inter 폴백**
- Inter "Semi Bold"는 공백 포함 (`"Semi Bold"` O, `"SemiBold"` X)
- 스크립트 50k 문자 초과 시 분할 실행
- `figma.currentPage` 직접 할당 불가 → `figma.setCurrentPageAsync(page)` 사용
