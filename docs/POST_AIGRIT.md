> ⚠️ **이 파일은 요약본입니다.** 상세 가이드는 아래 3개 문서를 따르세요:
> - 글: [`docs/post/AIGRIT.md`](post/AIGRIT.md)
> - 이미지: [`docs/image/AIGRIT.md`](image/AIGRIT.md)
> - SEO: [`docs/seo/AIGRIT.md`](seo/AIGRIT.md)

# AIGrit 글쓰기 가이드 (요약)

> aigrit.dev — AI·생산성 도구를 직접 써보고 솔직하게 비교하는 리뷰 블로그

## 정체성

- 태그라인: "AI의 알맹이만 남긴다"
- 톤: 전문적이되 친근, 비판적이되 건설적
- 타겟: AI 입문 직장인 / 생산성 덕후 / 1인 개발자
- 수익: AdSense + SaaS 제휴

## 글 구조 (Cluster 기준, 2,000~2,500단어)

```
H1 제목 (키워드 앞배치, 55~60자)
├── 도입 — 역피라미드 (50~60자 볼드 요약 + 2~3문장 맥락)
├── H2 핵심 섹션 1 (질문형 권장)
├── H2 핵심 섹션 2
├── H2 비교 테이블 (비교글)
├── H2 실사용 후기 (스크린샷 필수)
├── H2 장단점 (단점 2개 이상)
├── H2 누구에게 추천?
├── H2 FAQ (3~5개, JSON-LD 자동 주입)
└── H2 마무리 + CTA
```

## 첫 문단 — 역피라미드 (필수)

```markdown
**결론부터: Claude는 장문 글쓰기에 자연스럽고, ChatGPT는 구조적 글에 강하다.**
3주간 같은 주제 10개 글을 써본 실험 결과다.
```

- 첫 줄 볼드 = Featured Snippet 후보 (50~60자 완결 문장)
- 2~3줄 추가 맥락

## H2 규칙

- 글당 H2 중 **2~3개는 질문형** ("~일까?", "~나은 점은?")
- 질문형 H2 아래 답변 첫 문장 = 55자 이내 완결
- H2 5~7개 (Pillar는 8~12개)

## FAQ (guide/review/comparison 필수)

```markdown
## 자주 묻는 질문 (FAQ)

### Claude 무료로 쓸 수 있나요?

네, claude.ai에서 무료로 사용 가능합니다. 다만 일일 메시지 한도가 있습니다.
```

- H3 = 질문 (물음표로 끝)
- 답변 40~80단어, 첫 문장이 핵심
- `/publish-post`가 JSON-LD FAQPage 자동 주입

## Pillar vs Cluster

| | Cluster | Pillar |
|---|---|---|
| 단어 수 | 1,500~2,500 | 3,000~5,000 |
| H2 | 5~7 | 8~12 |
| FAQ | 3~5 | 5~8 |
| 내부 링크 | 5~7 (Pillar 1개 필수) | 10~15 |
| featured | 선택 | **필수** |
| 업데이트 | 최소 수정 | **분기 1회 전면 갱신** |
| 작성 트리거 | — | 같은 클러스터에 Cluster 3개+ 누적 시 |

## 문체 규칙

- 경어체 기본, 핵심 판단은 단정적
- 실사용 표현 필수: "3일 써봤는데", "실제로 해보니"
- 비교글 단점 2개 이상 필수
- E-E-A-T: 실사용 기간 + 스크린샷 + 수치

### 금지어 (AI 냄새)

획기적인, 혁신적인, 놀라운, ~을 통해, 다양한, 효율적인, 최적의, 원활한, 심층적인, 포괄적인

## 내부 링크 (B-4)

| 글 유형 | 내부 링크 수 | Pillar 필수 | 크로스 클러스터 |
|---|---|---|---|
| Cluster | 5~7 | 1개 | 1~2개 |
| Pillar | 10~15 | — | 제한 없음 |

앵커: 키워드 자연 삽입 ("Claude Code 설치 가이드에서 다뤘듯이")
금지: "여기를 클릭", 같은 URL 2회 링크

## MDX frontmatter

```yaml
title: "글 제목"
date: "YYYY-MM-DD HH:mm"
updated: "YYYY-MM-DD HH:mm"
slug: "url-slug"
description: "150자 SEO 설명"
tags: ["태그1", "태그2"]
thumbnail: "/images/{slug}/og.png"
featured: false
category: "카테고리명"
topic_cluster: "AI 도구 비교"
cluster_role: cluster
```

## 네이버 에디션 연계

네이버 에디션 후보인 글은 Pipeline 카드에 `naver_edition_candidate: true` + `naver_edition_angle` 기재.
리프레이밍 규칙은 `docs/POST_NAVER.md` 참조.

## Obsidian 참고 문서

- `02. Blog SEO/02. AIGrit 글쓰기 지침서.md` — 전체 지침서 (카테고리 표, 수익화 규칙 포함)
- `02. Blog SEO/12. Topic Cluster/_README.md` — Pillar/Cluster 전략
- `02. Blog SEO/10. Pipeline/AIGrit/_README.md` — 마스터 넘버링
