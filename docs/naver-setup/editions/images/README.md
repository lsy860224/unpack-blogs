# 네이버 에디션 이미지 패키지

Batch 1 네이버 발행용 이미지를 **편별로 번호 순서대로** 정리한 폴더. 각 폴더 내용을 네이버 스마트에디터에 01부터 순서대로 업로드하면 됩니다.

## 📦 패키지 구조

```
images/
├── 01-apple-shortcuts/     ← 네이버 #1 · 9장
├── 02-notion-ai/           ← 네이버 #2 · 8장
└── 03-perplexity/          ← 네이버 #3 · 9장
```

## 🎨 이미지 출처 분류

| 표기 | 출처 | 설명 |
|---|---|---|
| 📋 **재활용** | AIGrit 본사이트 | `apps/aigrit/public/images/*/` 에서 복사 |
| 🎨 **Figma** | 브랜드 템플릿 | 파일 `1Md9ud8CQ43AQn2dKUo7YV` Dividers 페이지 디자인 → PIL로 PNG 렌더 |
| 📊 **Napkin AI** | 자동 인포그래픽 | horizontal bar chart 생성 |
| 🖌 **PIL (babipa 브랜드)** | 신규 생성 | Gowun Batang + Pretendard + Plum/Terracotta 팔레트 카드 그리드 · 타임라인 |

## 📁 에디션별 상세

### #1 Apple 단축어 편 (9장)

| 번호 | 파일 | 출처 | 용도 |
|:---:|---|---|---|
| 01 | cover.png | 📋 og.png | 대표 썸네일 |
| 02 | structure.png | 📋 01-shortcut-api-flow.png | 구조 개념도 |
| 03 | summarize.png | 📋 02-shortcut-summarize.png | 요약 단축어 |
| 04 | screenshot-ai.png | 📋 03-shortcut-screenshot-ai.png | 스크린샷 AI |
| 05 | translate.png | 📋 05-shortcut-translate.png | 번역 단축어 |
| 06 | calendar.png | 📋 06-shortcut-calendar.png | 캘린더 입력 |
| 07 | divider.png | 🎨 Figma/PIL | 구분선 (Terracotta 3-dot) |
| 08 | cost-infographic.png | 📊 Napkin AI | 월 5만원 절약 비교 차트 |
| 09 | closing.png | 📋 og.png 재활용 | 마무리 이미지 |

### #2 Notion AI 편 (8장)

| 번호 | 파일 | 출처 | 용도 |
|:---:|---|---|---|
| 01 | cover.png | 📋 og.png | 대표 썸네일 |
| 02 | vs-chatgpt.png | 📋 01-notion-ai-vs-chatgpt.png | Notion vs ChatGPT 비교 |
| 03 | use-cases.png | 📋 03-use-cases-infographic.png | 활용 사례 인포그래픽 |
| 04 | pricing.png | 📋 04-pricing-scenarios.png | 가격 비교 |
| 05 | divider.png | 🎨 Figma/PIL | 구분선 |
| 06 | use-cases.png | 🖌 PIL 신규 | Notion AI 5가지 활용법 카드 그리드 |
| 07 | routine.png | 🖌 PIL 신규 | 평일 저녁 30분 부업 루틴 타임라인 |
| 08 | closing.png | 📋 og.png 재활용 | 마무리 이미지 |

### #3 Perplexity 편 (9장)

| 번호 | 파일 | 출처 | 용도 |
|:---:|---|---|---|
| 01 | cover.png | 📋 og.png | 대표 썸네일 |
| 02 | main-screen.png | 📋 02-perplexity-free-search.png | Perplexity 메인 화면 |
| 03 | research-vs.png | 📋 01-google-vs-perplexity.png | 네이버·구글 vs Perplexity 리서치 비교 |
| 04 | usage-chart.png | 📋 03-usage-log-chart.png | 사용 로그 차트 |
| 05 | pro-vs-free.png | 📋 04-pro-vs-free.png | Pro vs 무료 비교 |
| 06 | divider.png | 🎨 Figma/PIL | 구분선 |
| 07 | weaknesses.png | 🖌 PIL 신규 | Perplexity 단점 3가지 카드 그리드 |
| 08 | use-cases.png | 🖌 PIL 신규 | 부업 활용 꿀팁 5가지 카드 그리드 |
| 09 | closing.png | 📋 og.png 재활용 | 마무리 이미지 |

## 🔁 사용 방법

### 방법 A — Craft → 네이버 복붙 (권장)

1. Craft에서 해당 네이버 에디션 문서 열기 (`05. Blog Pipeline / 01. In Progress / Naver/`)
2. Craft 문서 내 노란 하이라이트 `📷 ...` 블록 위치에 이 폴더의 이미지를 **드래그**로 삽입
3. Craft 전체 선택 (Cmd+A) → 복사 (Cmd+C)
4. 네이버 스마트에디터에 붙여넣기 (Cmd+V)
5. Craft의 이미지는 따라오지 않으므로 **네이버에서 재업로드** (이 폴더의 파일을 그대로 씀)

### 방법 B — 네이버에 직접 작성

1. 네이버 스마트에디터에서 새 글 시작
2. 제목·본문은 `docs/naver-setup/editions/0X-*.md` 파일에서 복사
3. 본문 `[이미지 삽입]` 자리표시자에 해당 폴더의 이미지를 번호 순서대로 업로드

## 📊 총 이미지 수

- **복사 재활용:** 19장 (AIGrit 본사이트 이미지)
- **신규 생성:** 7장
  - Figma/PIL 구분선: 3장 (공통 디자인, 3 폴더 배포)
  - Napkin AI 인포그래픽: 1장 (#1 slot 08 — 바 차트)
  - PIL 브랜드 인포그래픽: 3장 (#2 slot 06-07, #3 slot 07-08)
- **총:** 26장

## 🆘 문제 발생 시

### Napkin AI 차트 재생성
`docs/naver-setup/editions/0X-*.md` 파일의 해당 slot 콘텐츠를 참고해 Napkin AI에서 재생성 가능. 현재 `#1 slot 08 (cost-infographic)` 는 Napkin이 5개 항목 중 3개만 시각화했기에, 네이버 본문에서 5개 항목 전체 표도 함께 사용 중.

### PIL 인포그래픽 재렌더
`/tmp/generate-infographics.py` 실행으로 재생성. 데이터 수정 시 스크립트 내 `items` 리스트만 교체.

### 구분선 재렌더
`/tmp/generate-dividers.py` 실행. 3가지 변형(warm/cool/neutral) 중 선택.
