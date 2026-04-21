# 발행 전 점검 체크리스트

> Claude Code가 "글쓰기 시작" 요청 시 자동으로 실행하는 점검 프로세스.

## Phase 1: 초안 확인

### 확인 순서
1. slug로 MDX 파일 존재 여부 확인
   - `apps/{app}/content/posts/ko/{slug}.mdx` (AIGrit)
   - `apps/{app}/content/posts/{slug}.mdx` (babipanote)
2. 결과에 따라 분기:

| MDX 존재? | 의미 | 다음 행동 |
|---|---|---|
| ✅ 있음 | 이미 발행됨 | "수정 발행인가요?" 확인 → updated 갱신 |
| ❌ 없음 | 미발행 → Craft 초안 확인 필요 | Phase 2로 |

### Craft 초안 위치
- AIGrit: `05. Blog Pipeline/01. In Progress/AIGrit/` → `#N [AIGrit] 제목`
- babipanote: `05. Blog Pipeline/01. In Progress/babipanote/` → `#N [babipanote] 제목`

### 초안이 없을 때 — Claude Desktop 프롬프트 제안

AIGrit 예시:
```
AIGrit 블로그 글 써줘.

주제: {title}
핵심 키워드: {primary_keyword}
유형: {content_type}
단어수: {target_word_count}
토픽 클러스터: {topic_cluster} (역할: {cluster_role})
Featured Snippet 타겟: {featured_snippet_target}

요구사항:
- 첫 문단에 50~60자 요약문 1줄 볼드 (역피라미드)
- H2 중 2~3개를 질문형 제목으로
- FAQ 3~5개
- AI 냄새 금지어 배제

내부 링크 후보:
{internal_links_planned 각각 → {LINK: slug | anchor: text} 형태}

Craft에 저장해줘 (05. Blog Pipeline / 01. In Progress / AIGrit / #{number} [AIGrit] {title})
```

babipanote 예시:
```
babipanote 빌더 저널 글 써줘.

주제: {title}
유형: {content_type} (buildlog/revenue-report/lesson/essay)
단어수: ~1,500

요구사항:
- 스토리 훅으로 시작 (역피라미드 금지!)
- 1인칭, 솔직한 톤, 구체 수치 필수
- AI 냄새 금지어 배제

Craft에 저장해줘 (05. Blog Pipeline / 01. In Progress / babipanote / #{number} [babipanote] {title})
```

## Phase 2: 에셋 점검

### 필수 에셋 목록

| 에셋 | 경로 | 필수? |
|---|---|---|
| OG 이미지 | `apps/{app}/public/images/{slug}/og.png` | ✅ 필수 |
| 본문 이미지 | `apps/{app}/public/images/{slug}/NN-name.png` | 초안의 {IMG:} 마커 수만큼 |
| 썸네일 | OG 이미지 재사용 (별도 불필요) | — |

### 점검 방법

1. 이미지 디렉토리 존재 확인: `apps/{app}/public/images/{slug}/`
2. 없으면 생성: `mkdir -p apps/{app}/public/images/{slug}/`
3. 초안에서 `{IMG:` 마커 카운트
4. 디렉토리 내 실제 이미지 파일 수와 비교
5. 부족분 리스트 생성

### 부족 에셋 리포트 포맷

```
📋 에셋 체크리스트 — {title}

✅ 완료:
  - og.png (1200×630)

❌ 필요:
  경로: apps/aigrit/public/images/{slug}/
  - [ ] 01-claude-home.png — alt: "Claude 홈 화면" (스크린샷)
  - [ ] 02-chatgpt-home.png — alt: "ChatGPT 홈 화면" (스크린샷)
  - [ ] 03-comparison-table.png — alt: "비교 테이블" (캡처 또는 제작)

💡 OG 이미지 생성:
  - 사이즈: 1200×630
  - 제목 텍스트 포함
  - 브랜드 컬러 배경
  - 경로: apps/aigrit/public/images/{slug}/og.png
```

## Phase 3: MDX 변환 준비

### frontmatter 자동 생성

```yaml
---
title: "{title}"
date: "{now YYYY-MM-DD HH:mm}"      # KST
updated: "{now YYYY-MM-DD HH:mm}"
slug: "{slug}"
description: "{description}"
tags: [{tags}]
thumbnail: "/images/{slug}/og.png"
featured: {featured}
category: "{category}"                # AIGrit만
topic_cluster: "{topic_cluster}"
cluster_role: {cluster_role}
---
```

### 마커 치환

- `{IMG: NN-name | alt: ... | caption: ...}` → `<Image>` 컴포넌트
- `{LINK: slug | anchor: text}` → `<Link>` 컴포넌트 (slug 실재 검증)

### 발행 명령

```bash
# Claude Code에서
/publish-post {app} {slug}
```

## Phase 4: 발행 후 확인

- [ ] Vercel 배포 성공 확인
- [ ] IndexNow 자동 호출 확인
- [ ] GSC URL 검사 → 색인 요청 (수동 30초)
- [ ] 네이버 서치어드바이저 수집 요청 (수동 30초)
- [ ] Obsidian Pipeline 카드 status → published
- [ ] Craft 초안 → Archive 폴더 이동
