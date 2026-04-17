---
description: Rules for MDX content files
globs: ["apps/*/content/posts/**/*.mdx", "content/**/*.mdx"]
---

# MDX 콘텐츠 규칙

## Frontmatter 필수 필드
모든 MDX 파일은 아래 frontmatter를 포함해야 한다:
- title, date, slug, description, tags, thumbnail, featured, category (AIGrit만)
- updated: 수정 시 자동 갱신 (KST)
- topic_cluster: RelatedPosts 알고리즘 핵심
- cluster_role: "pillar" | "cluster"

## 금지 사항
- slug 변경 절대 금지 (301 리다이렉트 필요한 예외만)
- date 필드 수정 금지 (updated 필드를 대신 사용)
- `any` 타입 사용 금지
- 하드코딩된 색상 금지 (CSS 변수 또는 Tailwind 토큰 사용)

## 마커 포맷
- 이미지: `{IMG: NN-name | alt: 설명 | caption: 캡션}`
- 내부 링크: `{LINK: target-slug | anchor: 앵커 텍스트}`
- /publish-post 커맨드가 마커를 실제 컴포넌트로 치환
