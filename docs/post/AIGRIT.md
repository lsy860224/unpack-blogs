# AIGrit — 글 작성 가이드

> **aigrit.dev** — AI 도구 실측 리뷰 블로그. 이 문서는 글의 톤·구조·발행 워크플로우를 정의한다.
> 이미지는 [image/AIGRIT.md](../image/AIGRIT.md), SEO는 [seo/AIGRIT.md](../seo/AIGRIT.md) 참조.

---

## 1. 정체성 & 톤

| 항목 | 값 |
|---|---|
| 도메인 | aigrit.dev |
| 타겟 | 직장인 AI 입문자 · 생산성 덕후 · 개발자 |
| 핵심 UVP | "AI 도구를 직접 써보고 속도·비용·정확도를 숫자로 비교 — 팔지 않고 씁니다" |
| 태그라인 | "AI의 알맹이만 남긴다" |
| 인칭 | "에이아이그릿" / "저희가 직접 써본 결과" (복수 중립) |
| 시제 | 현재형 기본, 체험기는 과거형 |

### 브랜드 보이스 5축 (0-10)
- Formal **5** · Serious **7** · Expert(권위+겸손) **4** · Matter-of-fact **7** · Modern **8**

### 표현 규칙

| 사용 | 금지 |
|---|---|
| "테스트한 결과" / "24시간 써본 뒤" | "개쩐다" "미쳤다" "레전드" |
| "3,200원/월 기준" | "꽤 비싼" "상당히 빠른" |
| "정확도 89% (n=200)" | "매우 정확함" "완벽한" |
| "제휴 링크 포함" (명시) | "스폰서 여부 미공개" |

---

## 2. 글 유형별 기준

| 유형 | 단어수 | FAQ | 내부 링크 | 이미지 | featured |
|---|:---:|:---:|:---:|:---:|:---:|
| **Pillar** | 3,500자+ | 5~8 | 10~15 | 5장+ | true 필수 |
| **Cluster** | 2,000~4,000 | 3~5 | 5~7 (Pillar 1 필수) | 3~5 | false |

---

## 3. 본문 구조 (역피라미드 필수)

1. **도입 (50~60자 핵심 결론 선제시)** — 검색 유입 즉시 답
2. **TL;DR 박스** (선택, 3줄 요약)
3. **H2 본문** — 질문형 H2 권장 ("~인가요?" "~할 수 있나요?")
4. **표·점수표·체크리스트** — 수치 시각화 우선
5. **FAQ 섹션** — H3 질문 + 40~80단어 답변 (3~5개, Pillar는 5~8)
6. **결론 & 다음 액션**
7. **관련 글 링크** — Pillar 1개 + Cluster 내 자연스러운 인용

---

## 4. Frontmatter 스키마

```yaml
---
title: "글 제목"                         # 필수
date: "2026-04-25 09:00"                 # KST. 최초 발행일. 절대 수정 금지
updated: "2026-04-25 14:00"              # /publish-post 자동 갱신
slug: "url-slug"                         # kebab-case, 영문 소문자. 변경 금지
description: "150자 SEO 설명"             # 필수
tags: ["태그1", "태그2"]                  # 필수
thumbnail: "/images/{slug}/og.png"       # 필수
featured: false                          # Pillar는 true
category: "AI 도구 비교"                  # AIGrit 필수 (babipanote는 없음)
topic_cluster: "AI 도구 비교"            # RelatedPosts 가중치 핵심
cluster_role: cluster                    # pillar | cluster
---
```

---

## 5. 마커 포맷 (초안 작성 시)

초안 단계에 마커 사용 → `/publish-post`가 컴포넌트로 치환.

- 이미지: `{IMG: NN-name | alt: 키워드 포함 설명 | caption: 옵션 캡션}`
- 내부 링크: `{LINK: target-slug | anchor: 앵커 텍스트}`
- 외부 링크: 일반 markdown `[텍스트](url)` (공식 출처·도구)

**내부 링크 타겟 slug가 존재하지 않으면 빌드 에러**.

---

## 6. 절대 금지

- 과장어 / 감탄사 / 모호어 (§1.3 표)
- `date` 필드 수정 (수정 시 `updated` 사용)
- `slug` 변경 (301 리다이렉트 없이)
- 하드코딩 색상 (CSS 변수 또는 Tailwind 토큰)
- 도박·성인·불법 외부 링크 (AdSense 정책)
- `database.g.dart` 수동 편집 (해당 없음, but 유사: 자동 생성물 건드리지 말 것)

---

## 7. 작업 경로

| 목적 | 위치 |
|---|---|
| **MDX 파일** | `apps/aigrit/content/posts/ko/{slug}.mdx` |
| **Obsidian Pipeline 카드** | `02. Blog SEO/10. Pipeline/AIGrit/{NN}-aigrit-{slug}.md` |
| **Obsidian 지침서** | `02. Blog SEO/02. AIGrit 글쓰기 지침서.md` |
| **Craft 초안** | `05. Blog Pipeline / 01. In Progress / AIGrit / [AIGrit] {제목}` |
| **Craft 아카이브 (발행 후)** | `05. Blog Pipeline / 02. Archive / AIGrit /` |

---

## 8. 발행 워크플로우

1. **Obsidian Pipeline 카드** 생성 또는 확인 → SEO 설계 + 내부 링크 계획 ([seo/AIGRIT.md](../seo/AIGRIT.md))
2. **Craft 초안** 작성 (마커 포함, 본문+FAQ)
3. **이미지 준비** ([image/AIGRIT.md](../image/AIGRIT.md) 참조) — **OG는 반드시 제목 포함**
4. **MDX 변환** (Craft → frontmatter + 마커 치환)
5. **slug 유일성** 체크 (`apps/aigrit/content/posts/ko/`에 동일 slug 없는지)
6. **`/review-post`** 통과 ← **필수 게이트**
7. **`/publish-post`** 실행 → git commit + push
8. **발행 후 색인 요청** — GSC + IndexNow + 네이버 SearchAdvisor (aigrit.dev는 등록 가능)
9. **Pipeline 갱신** — `status: published`, `publish_url_aigrit`, `last_updated`

---

## 9. `/review-post` 통과 기준

- 글자수 ≥ 1,500 (Pillar ≥ 3,500)
- FAQ 섹션 존재 (AIGrit 필수)
- 내부 링크 5~7 + broken link 0
- 이미지 3~5장 + broken image 0 (OG 제목 포함 확인)
- 외부 링크 ≥ 1

상세 기준은 `.claude/rules/post-requirements.md`.

---

## 10. 관련 문서

- [image/AIGRIT.md](../image/AIGRIT.md) — 이미지 규칙 (OG 제목 포함 필수, Figma/NapkinAI 우선)
- [seo/AIGRIT.md](../seo/AIGRIT.md) — SEO·키워드·스키마
- [CONTENT_RULES.md](../CONTENT_RULES.md) — 공통 마커·금지어
- [PUBLISH_CHECKLIST.md](../PUBLISH_CHECKLIST.md) — 발행 직전 체크
- [WORKFLOW.md](../WORKFLOW.md) — 파이프라인 전체 흐름
- Obsidian: `02. Blog SEO/02. AIGrit 글쓰기 지침서.md`
