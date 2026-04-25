# babipanote — SEO 가이드

> **babipanote.com** — 키워드 타깃팅보다 **토픽 오소리티·E-E-A-T·Author schema** 중심.
> 글은 [post/BABIPANOTE.md](../post/BABIPANOTE.md), 이미지는 [image/BABIPANOTE.md](../image/BABIPANOTE.md) 참조.

---

## 1. SEO 철학 (AIGrit과 정반대)

| 축 | babipanote | (참고: AIGrit) |
|---|---|---|
| 우선 지표 | **Author authority · 브랜드 검색량** | 키워드 순위 · 페이지뷰 |
| 검색 의도 | Informational · Experiential · Opinion | Commercial · Transactional · How-to |
| 경쟁 전략 | **차별화된 개인 경험·수치 공개** | 동일 키워드 점수 경쟁 |
| 전환 | 브랜드 팬 · 구독자 확보 | 제휴 클릭 · AdSense |

---

## 2. E-E-A-T 강화 포인트

**E**xperience — **내가 직접 한 경험만** 기록 (간접 경험·인용 리뷰 금지)
**E**xpertise — 특정 도메인 반복 (PKM·1인 빌드·재무·AI 코딩)
**A**uthoritativeness — 실수치·실패 공개로 **검증 가능성** 확보
**T**rustworthiness — 외부 검증 링크 (도구 공식·소스코드·GitHub)

### 실천 방법
- **Author schema** 모든 글 주입 (`babipa` 프로필)
- GitHub 저장소 링크 본문 삽입
- 수치 인용 시 원본 데이터 JSON·CSV GitHub 공개
- "나는 X를 모른다" 솔직 인정

---

## 3. 키워드 전략 (보조 역할)

### 강조점
- Primary는 보조 지표, **Author + Topic 조합 장기 검색어** 위주
- 예: `"바비파 PKM 스택"` / `"1인 개발자 연간 재무"` / `"Craft vs Notion 3개월 후기"`

### Pipeline Frontmatter
```yaml
primary_keyword: "1인 개발자 연간 재무"
secondary_keywords:
  - "인디해커 수익 공개"
  - "솔로 빌더 매출"
brand_query_target: "바비파 재무 보고서"   # 브랜드 검색어 의도
```

---

## 4. Topic Authority 구축

### 3대 Pillar (babipanote 자산 허브)

| Pillar # | 주제 | 역할 |
|---|---|---|
| #14 | 1인 빌더의 하루 (일상 허브) | 루틴·타임블록 공개 |
| #17 | PKM 스택 전체 (지식관리 허브) | Obsidian·Craft·Claude 1년 지표 |
| #23 | 💰 인디해커 연간 재무 (수치 허브) | 월별 P&L 공개 |

각 Pillar = 관련 Cluster 7~10개 → 토픽 독점.

### 분기별 업데이트 규칙 (Pillar)
- `featured: true` + 분기 1회 갱신
- `updated: YYYY-MM-DD` 필드로 Google에 신선도 신호
- 댓글·피드백 반영해서 "살아있는 문서"

---

## 5. 내부 링크 (2~3개 필수)

- 이전 저널 글 1~2개 (시간 순 서사 연결)
- 같은 Pillar 1개
- 크로스링크 (AIGrit) 자연스러운 맥락일 때만

### 시리즈 연결 (옵션)
```yaml
series: "Sprint 1차"
series_index: 3
```
- 같은 시리즈는 RelatedPosts에서 자동 연결
- "이전 / 다음 회차" 네비게이션 자동 생성

---

## 6. Structured Data

### Author schema (필수 — AIGrit 대비 차별 포인트)
자동 주입 (layout.tsx):
```json
{
  "@type": "Person",
  "name": "babipa",
  "url": "https://babipanote.com/about",
  "sameAs": [
    "https://github.com/lsy860224",
    "https://x.com/babipanote",
    "https://aigrit.dev"
  ]
}
```

### Article schema
모든 글 기본.

### Review / HowTo
- Review는 `tool-review` 타입에만
- HowTo는 본문이 명확한 단계형일 때만

### FAQPage 지양
- babipanote 본질(저널)과 충돌 → tool-review에만 제한적

---

## 7. OG / Twitter Card

### 자동 생성
- `og:title` = post.title
- `og:image` = `/images/{slug}/og.png` **(제목 포함 필수)**
- `og:type=article`, `og:locale=ko_KR`
- `twitter:card=summary_large_image`, `twitter:site=@babipanote`

### 수동 확인
- OG 이미지 **종이 톤 + 세리프 헤딩 + 제목 시각적 확인**
- 카카오톡·X 링크 프리뷰 테스트

---

## 8. 인덱싱

### 본사이트 (babipanote.com)
- **GSC 등록 완료** → URL 검사로 색인 요청
- **IndexNow** `/publish-post` 자동 핑
- **네이버 Search Advisor 등록 완료** → 글별 수동 수집 요청 (**babipa의 AIGrit 네이버 블로그와 별개!**)

---

## 9. Core Web Vitals
AIGrit과 동일 기준 (LCP<2.5s, CLS<0.1, INP<200ms). 종이 톤은 이미지 용량 주의 — 크림 배경이 JPG로 뭉개지기 쉬움. **PNG 유지 + pngquant 압축**.

---

## 10. 수익화 정책 (광고 OFF 원칙)

- **`adsense: false` 유지** — brand.config.ts 절대 변경 금지
- **`affiliateLinks: false` 유지**
- 수익은 **구독·커뮤니티·브랜드 자산화**로 (장기)
- 단기 수익 압박 있으면 AIGrit 쪽 강화하고 babipanote는 그대로

---

## 11. Pipeline 추적 필드

```yaml
primary_keyword: ""
brand_query_target: ""
secondary_keywords: []
meta_description: ""
search_intent: informational | experiential | opinion
content_type: buildlog | lesson | essay | revenue-report
topic_cluster: ""
cluster_role: pillar | cluster
schema_type: "Article + Author"   # 기본
internal_links_planned: []
internal_links_used: []
external_links_planned: []
# 발행 후
publish_url_babipanote: "https://babipanote.com/blog/{slug}"
monthly_views: 0
avg_position: null
brand_query_impressions: null   # 브랜드 검색량
```

---

## 12. 관련

- [post/BABIPANOTE.md](../post/BABIPANOTE.md) — 1인칭 저널 톤
- [image/BABIPANOTE.md](../image/BABIPANOTE.md) — 종이·잉크 이미지
- [PUBLISH_CHECKLIST.md](../PUBLISH_CHECKLIST.md) — 발행 직전 점검
- Obsidian: `02. Blog SEO/03. babipanote 글쓰기 지침서.md`, `10. Master Content Plan — 60 Posts.md`
