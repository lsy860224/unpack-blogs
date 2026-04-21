---
description: Rules for MDX content files — frontmatter schema, markers, SEO
globs: ["apps/*/content/posts/**/*.mdx", "content/**/*.mdx"]
---

# MDX 콘텐츠 규칙

## Frontmatter 스키마

```yaml
---
title: "글 제목"                          # 필수
date: "2026-04-14 21:30"                 # 필수. YYYY-MM-DD HH:mm (KST). 수정 금지
updated: "2026-04-17 03:00"              # 수정 시 자동 갱신. sitemap lastModified 소스
slug: "url-slug"                         # 필수. kebab-case 영문 소문자. 변경 금지
description: "150자 SEO 설명"             # 필수
tags: ["태그1", "태그2"]                  # 필수
thumbnail: "/images/{slug}/og.png"       # 필수
featured: false                          # 홈 상단 고정 여부
category: "카테고리명"                    # AIGrit만 (babipanote는 없음)
topic_cluster: "AI 도구 비교"            # RelatedPosts 알고리즘 핵심
cluster_role: cluster                    # pillar | cluster
---
```

## 필드별 규칙
- `date`: 최초 발행일. 한 번 설정 후 절대 수정 금지
- `updated`: 내용 수정 시 `/publish-post`가 자동 갱신 (KST)
- `slug`: 변경 시 301 리다이렉트 필수 — 원칙적으로 변경 금지
- `topic_cluster`: 같은 클러스터 글끼리 RelatedPosts에서 +10점
- `cluster_role`: pillar 글은 featured=true 필수, 분기 1회 갱신

## 마커 포맷
초안에서 사용. `/publish-post` 커맨드가 실제 컴포넌트로 치환.

- 이미지: `{IMG: NN-name | alt: 설명 | caption: 캡션}`
- 내부 링크: `{LINK: target-slug | anchor: 앵커 텍스트}`
  - 타겟 slug가 존재하지 않으면 빌드 에러
  - AIGrit: 5~7개 / babipanote: 2~3개

## 금지 사항
- slug 변경 금지
- date 필드 수정 금지 (updated를 대신 사용)
- 하드코딩 색상 금지 (CSS 변수 또는 Tailwind 토큰)
- 본문에 `any` 타입 코드 블록 지양
