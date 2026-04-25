# AIGrit — SEO 가이드

> **aigrit.dev** — 키워드·스키마·인덱싱·수익화 연계 SEO 전략. 전환율보다 **오소리티 구축**이 먼저.
> 글은 [post/AIGRIT.md](../post/AIGRIT.md), 이미지는 [image/AIGRIT.md](../image/AIGRIT.md) 참조.

---

## 1. 검색 의도 매핑

| 의도 | 키워드 예시 | 글 유형 | Featured Snippet |
|---|---|---|---|
| Commercial | "X vs Y 비교" "X 후기" | Cluster | table |
| Transactional | "X 구독 가격" "X 할인 코드" | Cluster | paragraph |
| How-to | "X 사용법" "X 설정" | Cluster | list (단계) |
| Informational | "X란 무엇인가" | Pillar | paragraph |

AIGrit은 **Commercial + How-to** 중심. Transactional은 제휴 전환 타게팅 시에만.

---

## 2. 키워드 전략

### Primary / Secondary

Pipeline frontmatter에 명시:
```yaml
primary_keyword: "notion ai 사용법"
secondary_keywords:
  - "notion ai 후기"
  - "노션 ai 추천"
  - "notion ai 한국어"
  - "notion ai 가격"
```

### 배치 규칙
- **Title Tag** (50~60자): primary 앞배치
- **Meta description** (150~160자): primary + secondary 1개 자연스럽게
- **H1 = 글 제목**: primary 정확히 포함
- **H2 최소 1개**: primary 변형 포함
- **첫 100단어**: primary 1~2회 자연스럽게
- **FAQ 질문 1개**: "X란 무엇인가요?" 또는 "X 어떻게 쓰나요?"

### 과잉 금지
- 키워드 스터핑 (같은 표현 반복) — 검색 페널티
- 자연스러움 우선, 밀도 1~2% 이내

---

## 3. Topic Cluster (오소리티 구축 핵심)

### 구조
```
Pillar 글 (3,500자+, 종합 가이드)
  ↳ Cluster 글 1 (세부 비교)
  ↳ Cluster 글 2 (세부 사용법)
  ↳ Cluster 글 3 ...
```

### Frontmatter
```yaml
topic_cluster: "AI 도구 비교"   # 동일 cluster 글끼리 RelatedPosts +10 가중치
cluster_role: pillar           # pillar | cluster
```

### 클러스터 정책 (Obsidian `12. Topic Cluster/`)
- 클러스터당 **Pillar 1개 + Cluster 5~10개** = 최적
- 클러스터 목록: `10. Master Content Plan — 60 Posts.md` 참조

---

## 4. 내부 링크 전략

### Cluster 글 (5~7개 필수)
- **같은 cluster의 Pillar 1개 필수**
- 같은 cluster 내 관련 Cluster 2~3개
- 다른 cluster 연관 글 1~2개 (자연스러운 맥락)

### Pillar 글 (10~15개)
- 같은 cluster 모든 Cluster 글 링크
- 다른 Pillar 2~3개 (횡적 연결)

### 앵커 텍스트
- **키워드 자연 삽입** — "여기를 클릭" 금지
- 같은 URL 2회 링크 금지
- `{LINK: target-slug | anchor: 앵커}` 마커 사용

### babipanote 크로스링크
- `Master Content Plan §크로스 링크 매트릭스` 참조
- 양방향 필수, 자연스러운 맥락

---

## 5. 외부 링크

- **최소 1개** 공식 출처 (도구 공식 사이트, 벤치마크 원본)
- 제휴 링크: 본문 하단 "📌 본 글에 제휴 링크가 포함되어 있습니다" 명시
- AdSense 정책 금지: 도박·성인·불법

---

## 6. Structured Data (JSON-LD)

### Article (기본, 자동 주입)
모든 글에 자동 주입됨.

### FAQPage (AIGrit 필수)
```yaml
schema_type: "Article + FAQ"
```
- `/publish-post`가 FAQ 섹션 H3 자동 파싱 → JSON-LD FAQPage 주입
- Google AI Overview 노출 핵심

### Review (리뷰 글 전용)
```yaml
schema_type: "Article + Review"
```
- 도구 리뷰 시 `reviewRating`, `itemReviewed` 자동 주입

### HowTo (Pillar/How-to 전용)
```yaml
schema_type: "Article + HowTo"
```

---

## 7. OG / Twitter Card (메타 태그)

### 자동 생성 (layout.tsx `generateMetadata`)
- `og:title` = post.title
- `og:description` = post.description
- `og:image` = `/images/{slug}/og.png` **(제목 포함 필수)**
- `og:url`, `og:type=article`, `og:locale=ko_KR`
- `twitter:card=summary_large_image`, `twitter:site=@aigrit_dev`

### 수동 확인
- OG 이미지 **제목 시각적 확인** ([image/AIGRIT.md](../image/AIGRIT.md))
- 카카오톡·슬랙 링크 프리뷰 테스트

---

## 8. 인덱싱

### 본사이트 (aigrit.dev)
- **Google Search Console**: 등록 완료, URL 검사 → 색인 요청
- **IndexNow**: `/publish-post`가 자동 핑 (Bing·Yandex 즉시 반영)
- **네이버 Search Advisor**: 사이트 등록 완료 (aigrit.dev), 글별 수동 수집 요청 권장

### 발행 후 체크리스트
1. `aigrit.dev/ko/blog/{slug}` 접속 가능 확인 (2xx)
2. GSC URL 검사 → 색인 요청
3. 네이버 Search Advisor → 요청 → 웹페이지 수집
4. `/publish-post`가 IndexNow 자동 처리

---

## 9. Core Web Vitals (성능)

- **LCP < 2.5s**: `next/image` 필수, OG 이미지 priority
- **CLS < 0.1**: 이미지 width/height 명시 (자동 컴포넌트가 처리)
- **INP < 200ms**: JS 최소, Giscus 지연 로드

점검: `pnpm turbo run build` 후 Lighthouse + PageSpeed Insights.

---

## 10. 수익화 SEO

### AdSense
- `enabled: true` (brand.config.ts)
- 4구좌 배치 (intro 하단, H2×3 사이)
- 광고 위반 키워드 회피

### 제휴 링크
- `affiliateLinks: true` (brand.config.ts)
- 본문 하단 고지 자동 삽입
- 제휴 도구 배열: `monetization.affiliates[]`

---

## 11. Pipeline 추적 필드

```yaml
primary_keyword: ""
secondary_keywords: []
meta_description: ""
search_intent: informational | commercial | transactional | how-to
content_type: guide | comparison | tutorial | review
topic_cluster: ""
cluster_role: pillar | cluster
featured_snippet_target: list | table | paragraph
first_paragraph_summary: ""
schema_type: "Article + FAQ"
internal_links_planned:
  - { slug: "...", anchor_context: "..." }
internal_links_used: []
external_links_planned:
  - { url: "...", anchor_context: "..." }
# 발행 후
publish_url_aigrit: "https://aigrit.dev/ko/blog/{slug}"
monthly_views: 0
organic_clicks_7d: null
avg_position: null
```

---

## 12. 관련

- [post/AIGRIT.md](../post/AIGRIT.md) — 글 작성 규칙
- [image/AIGRIT.md](../image/AIGRIT.md) — OG 이미지 제작 (제목 포함 필수)
- [PUBLISH_CHECKLIST.md](../PUBLISH_CHECKLIST.md) — 발행 직전 점검
- Obsidian: `02. Blog SEO/02. AIGrit 글쓰기 지침서.md`, `10. Master Content Plan — 60 Posts.md`
