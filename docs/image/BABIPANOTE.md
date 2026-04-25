# babipanote — 이미지 가이드

> **babipanote.com** — 종이·잉크 톤의 저널 이미지. Plum + Terracotta 팔레트.
> 글은 [post/BABIPANOTE.md](../post/BABIPANOTE.md), SEO는 [seo/BABIPANOTE.md](../seo/BABIPANOTE.md) 참조.

---

## 🛡️ 절대 준수 사항

1. **OG 이미지는 반드시 제목을 포함한다** — 1200×630 캔버스 내 제목 시각적 배치
2. **이미지 생성 시 Figma를 우선 고려**한다 — babipanote Brand Master Component
3. **인포그래픽은 NapkinAI를 우선 고려**한다 — 단, babipanote 팔레트로 톤 조정

---

## 1. 브랜드 톤 (AIGrit과 완전 분리)

| 항목 | babipanote | (참고: AIGrit) |
|---|---|---|
| 컨셉 | **"잉크와 종이"** — 저널 감성 | "정밀 계측기" |
| 헤딩 폰트 | **Gowun Batang Bold** (세리프) | Inter ExtraBold |
| 본문 폰트 | Pretendard | Pretendard |
| Primary | **Plum `#6B2E4E`** | Indigo `#3730A3` |
| Accent | **Terracotta `#C26F4E`** | Cyan `#06B6D4` |
| BG (Paper) | `#FAF7F2` (크림) | `#F8FAFC` (슬레이트) |
| Ink (FG) | `#2A1A22` (짙은 와인) | `#0F172A` (네이비) |

**헤딩은 반드시 Gowun Batang (세리프)** — AIGrit의 산세리프와 시각적으로 구별. 이게 브랜드 정체성 핵심.

---

## 2. 이미지 타입

| 타입 | 규격 | 파일명 | 도구 |
|---|---|---|---|
| **OG 썸네일** | 1200×630 | `og.png` | **Figma 우선** (Brand Master) |
| **본문 인포그래픽** | 1200px+ 가로 | `NN-name.png` | **NapkinAI 우선** (Plum 톤 적용) |
| **스크린샷** | 1200px+ 가로 | `NN-name.png` | 사용자 캡처 (라이트 모드 권장 — 종이 톤) |
| **손글씨/스케치** | 가변 | `NN-sketch.png` | iPad + Procreate 또는 Figma 손글씨 컴포넌트 |

---

## 3. OG 썸네일 (최우선)

### 규격
- **1200×630**, PNG, < 300KB
- **제목 포함 필수** — Gowun Batang Bold, 40~72pt, 좌측 또는 중앙
- 좌하단 `babipanote·` 워드마크 (Plum) + Terracotta dot
- 배경: Paper `#FAF7F2` (크림) / Ink 반전 옵션

### Figma Master Component

| 파일 | fileKey | Component |
|---|---|---|
| OG Templates | `1Md9ud8CQ43AQn2dKUo7YV` | babipanote: `1:20` |
| babipanote Brand | `D2hOsoihiYzAIuZHy5nnpz` | Wordmark / Mark variants |

**워드마크 Spec** (Brand Master):
- `-1% tracking` · 모두 소문자 · "babipanote·" (인용 점은 Terracotta secondary)
- 사용 시 반드시 Master 인스턴스. 직접 수정 금지.

### Figma MCP 자동 생성
`docs/THUMBNAIL.md` 플로우 동일. `apps/babipanote/public/images/{slug}/og.png` 저장.

---

## 4. 본문 인포그래픽 (NapkinAI 우선, 톤 조정 필수)

### NapkinAI 사용 시 주의
- AIGrit의 Cyan·Indigo 대신 **Plum `#6B2E4E` + Terracotta `#C26F4E`** 로 지정
- 프롬프트 예: `"timeline chart, cream background (#FAF7F2), Plum accent, serif headings"`

### 특히 유용한 유형
- **재무 차트** (revenue-report): 월별 매출·지출 bar chart
- **타임라인** (buildlog): "Day 1 → Day 36 빌드 과정"
- **크로스 비교** (lesson): "V1 실패 vs V2 성공" 표

### NapkinAI 불가 시
- 복잡한 손글씨: iPad Procreate → 스캔
- 간단한 인용구·데이터: Markdown table + MDX `<Quote>` 컴포넌트

---

## 5. 스크린샷

### 캡처 기준
- 해상도: Retina 2x
- **UI 테마: 라이트 모드 우선** (종이 톤과 조화)
- 민감 정보 가림 — 특히 revenue-report는 계좌·거래처 정보 철저히

### 편집
- 손글씨 주석 허용 (iPad Procreate로 "메모" 추가) — 저널 감성 강화
- 압축: 각 이미지 < 200KB

---

## 6. 파일 네이밍 & 경로

```
apps/babipanote/public/images/{slug}/
├── og.png                    ← 제목 포함 필수
├── 01-timeline-chart.png
├── 02-revenue-table.png
└── ...
```

- `og.png` 고정
- 본문: `NN-kebab-case.png`

---

## 7. Alt 텍스트

- 키워드 포함 + 개인 맥락
- 예: ✅ `"Sprint 1차 5주간 매출 월별 추이 — 최저 0원 ~ 최고 237만원"`

---

## 8. 본문 마커

AIGrit과 동일:
```
{IMG: 01-timeline-chart | alt: Sprint 1차 빌드 타임라인 36시간 | caption: Week 1 회고}
```

---

## 9. 검증

- OG 파일 존재 + 제목 포함 (수동 확인)
- 본문 1장 이상 (필수) — revenue-report는 2장+ 권장 (차트·표)
- broken image = 발행 차단

---

## 10. 자주 쓰는 자동 생성 명령

```bash
# Figma MCP로 OG 생성 (babipanote Master 사용)
# NapkinAI 인포그래픽 — Plum 톤 프롬프트

# 이미지 최적화
pngquant --quality=70-90 --ext .png --force apps/babipanote/public/images/{slug}/*.png
```

---

## 11. 관련

- [THUMBNAIL.md](../THUMBNAIL.md) — OG Figma 자동 생성 상세
- [post/BABIPANOTE.md](../post/BABIPANOTE.md) — 글 톤
- [seo/BABIPANOTE.md](../seo/BABIPANOTE.md) — E-E-A-T·Author 이미지
- Memory: `reference_figma_og_templates` / `reference_brand_master_figma` (babipanote: `D2hOsoihiYzAIuZHy5nnpz`)
