# AIGrit — 이미지 가이드

> **aigrit.dev** — 이미지 제작·배치·검증 규칙. 발행 전 브로큰 이미지가 있으면 `/review-post` 차단.
> 글 규칙은 [post/AIGRIT.md](../post/AIGRIT.md), SEO는 [seo/AIGRIT.md](../seo/AIGRIT.md) 참조.

---

## 🛡️ 절대 준수 사항 (전 블로그 공통)

1. **OG 이미지는 반드시 제목을 포함한다** — 1200×630 캔버스 내 제목 텍스트 시각적 배치 필수
2. **이미지 생성 시 Figma를 우선 고려**한다 — Master Component 재사용
3. **인포그래픽은 NapkinAI를 우선 고려**한다 — 데이터 시각화 자동 생성

---

## 1. 이미지 타입

| 타입 | 규격 | 파일명 | 제작 도구 |
|---|---|---|---|
| **OG 썸네일** | 1200×630 (필수) | `og.png` | **Figma 우선** (Master Component) |
| **본문 인포그래픽** | 1200px 이상 가로 | `NN-name.png` | **NapkinAI 우선** (차트·비교표·타임라인) |
| **스크린샷** | 1200px 이상 가로 | `NN-name.png` | 사용자 직접 캡처 (Retina 2x) |
| **다이어그램** | 1200px 이상 가로 | `NN-name.png` | Figma → PNG 익스포트 |

---

## 2. OG 썸네일 (최우선)

### 규격
- **크기**: 1200×630 (가로형)
- **포맷**: PNG, < 300KB
- **제목 포함**: **필수** — 좌측 또는 중앙에 글 제목 (32~64pt)
- **브랜드 요소**: 좌하단 `[AI]Grit` 워드마크 + 우하단 `aigrit.dev`
- **카테고리 배지** (선택): 상단 좌측 Cyan pill

### Figma Master Component

| 파일 | fileKey | Component ID |
|---|---|---|
| OG Templates | `1Md9ud8CQ43AQn2dKUo7YV` | AIGrit: `6:13` |
| AIGrit Brand Master | `njkSF5MinT8kK7kaoYpp12` | Wordmark/Mark variants |

**사용법**:
1. OG Templates Figma 파일 열기
2. AIGrit OG Component 인스턴스 복제
3. 제목 텍스트만 교체 (폰트: Inter ExtraBold + Pretendard Bold)
4. Export as PNG 2x → 1200×630 확인

### Figma MCP 자동 생성

`docs/THUMBNAIL.md`의 MCP 플로우:
1. `use_figma` 또는 `get_screenshot` 호출
2. 제목·카테고리 텍스트 주입
3. `apps/aigrit/public/images/{slug}/og.png` 저장

### 색상 팔레트 (참고)

| 역할 | 라이트 | 다크 |
|---|---|---|
| Primary | `#3730A3` | `#818CF8` |
| Secondary (액센트) | `#06B6D4` | `#22D3EE` |
| BG | `#F8FAFC` | `#0F172A` |
| FG | `#0F172A` | `#E2E8F0` |

---

## 3. 본문 인포그래픽 (NapkinAI 우선)

### 언제 NapkinAI를 쓰는가
- 속도·비용·정확도 **3축 비교 차트**
- **벤치마크 점수표** (pts, seconds, $/mo)
- **타임라인** (일별·주별 사용 로그)
- **파이차트·막대차트**

### NapkinAI 워크플로우
1. `mcp__napkin-ai__generate_and_wait` 호출 (또는 `generate_and_save`)
2. 프롬프트에 데이터 텍스트 + 스타일 지정 ("horizontal bar chart, dark theme, Cyan accent")
3. 생성 대기 → `docs/inspection-log/` 또는 이미지 폴더 저장
4. 파일명: `NN-keyword-chart.png` (예: `03-claude-vs-gpt4-accuracy.png`)

### NapkinAI 불가 시 대체
- 복잡한 커스텀 레이아웃: Figma 수동 제작
- 간단한 표: Markdown table로 직접 (이미지 대신)
- 코드 블록: MDX 코드 블록 (syntax highlighting)

---

## 4. 스크린샷

### 캡처 기준
- 해상도: **Retina 2x** (1200px 이상 가로)
- 민감 정보 가림 (API 키, 이메일, 개인 파일명)
- UI 테마: 다크 모드 우선 (AIGrit 톤 일치)

### 편집
- 하이라이트·주석: Figma 또는 Skitch
- 파일 크기 압축: `pngquant` 또는 ImageOptim
- 목표: 각 이미지 < 200KB

---

## 5. 파일 네이밍 & 경로

### 저장 경로
```
apps/aigrit/public/images/{slug}/
├── og.png                    ← 필수, 제목 포함
├── 01-first-asset.png        ← 본문 순서대로 번호 접두어
├── 02-second-asset.png
└── ...
```

### 네이밍 규칙
- `og.png` — 고정
- 본문: `NN-kebab-case.png` (NN = 01, 02, 03…)
- 예: `01-cursor-latency-chart.png`, `02-claude-code-screenshot.png`

---

## 6. Alt 텍스트 (SEO·접근성)

- **키워드 포함**: primary keyword + 맥락 설명
- **길이**: 50~125자
- **예**:
  - ✅ `"Claude 3 Sonnet과 GPT-4 Turbo의 인용 정확도 비교 막대 차트 — 89.3 vs 87.1"`
  - ❌ `"image"` / `"chart"`

---

## 7. 본문 이미지 마커

MDX 초안에서:
```
{IMG: 01-cursor-latency-chart | alt: Cursor 0.45 vs 1.2.3 응답 시간 -38% 감소 차트 | caption: 200회 반복 Tab 자동완성 평균}
```

`/publish-post`가 `<Image>` 컴포넌트로 치환. 자동 `rel`, lazy loading, `width/height` 주입.

---

## 8. 검증 (`/review-post`)

- 모든 `![alt](/images/...)` 실재 파일 확인 → broken image 차단
- OG 이미지 필수 존재 (`thumbnail:` 필드)
- OG 제목 포함 여부는 **수동 확인** (자동 OCR 미도입)
- 이미지 3~5장 (Cluster) / 5장+ (Pillar)

---

## 9. 자주 쓰는 자동 생성 명령

```bash
# Figma MCP로 OG 생성
# (Claude가 use_figma + get_screenshot 조합으로 처리)

# NapkinAI 인포그래픽
# mcp__napkin-ai__generate_and_save 로 자동 저장

# 이미지 최적화 (발행 전)
pngquant --quality=70-90 --ext .png --force apps/aigrit/public/images/{slug}/*.png
```

---

## 10. 관련

- [THUMBNAIL.md](../THUMBNAIL.md) — OG Figma 자동 생성 상세 플로우
- [post/AIGRIT.md](../post/AIGRIT.md) — 글 작성 규칙
- [seo/AIGRIT.md](../seo/AIGRIT.md) — 이미지 SEO (alt·OG 메타)
- Memory: `reference_figma_og_templates` / `reference_brand_master_figma`
