---
description: Mandatory requirements for every blog post MDX — checked by /review-post before publish
globs: ["apps/*/content/posts/**/*.mdx"]
---

# 글 발행 필수 요건 — /review-post 자동 검증

## 핵심 원칙

**모든 블로그 글은 발행(git commit + push) 전에 `/review-post` 통과와 사용자 명시 승인이 필요하다.** Claude가 직접 작성하는 부분(내부 링크·외부 링크·구조)은 초안 단계에서부터 필수 요건을 반영한다.

## 필수 항목 (모든 글 공통)

| 항목 | 최소 기준 | 검증 방법 |
|---|---|---|
| 글자수 | **1,500자 이상** (본문, frontmatter 제외) | `wc -m` |
| FAQ 섹션 | **AIGrit 필수 / babipanote 권장** | `grep -c "FAQ\|자주 묻는 질문"` |
| 내부 링크 | 아래 타입별 기준 + **broken link 0** | `<Link href=` 카운트 + 실재 slug 검증 |
| 스크린샷·이미지 | 아래 타입별 기준 + **broken image 0** | `![` 카운트 + 파일 실재 검증 |
| 외부 링크 | **최소 1개** (공식 문서·출처) | `[...](https?://...)` 카운트 |

## 글 타입별 세부 기준

### AIGrit — Cluster

| 항목 | 기준 |
|---|---|
| 글자수 | 2,000~4,000자 권장 (1,500자 하한) |
| FAQ | **3~5 Q&A 필수** (JSON-LD FAQPage 노출 목적) |
| 내부 링크 | **5~7개** (같은 topic_cluster의 Pillar 1개 필수) |
| 이미지 | **3~5장** (OG 포함) |
| 외부 링크 | 1~3개 (공식 docs·출처) |

### AIGrit — Pillar

| 항목 | 기준 |
|---|---|
| 글자수 | **3,500자+ 필수** |
| FAQ | **5~8 Q&A 필수** |
| 내부 링크 | **10~15개** (같은 cluster 글 다수 링크) |
| 이미지 | **5장+** |
| 외부 링크 | 2~4개 |
| 기타 | `featured: true` 필수, 분기 1회 갱신 |

### babipanote (buildlog·lesson·essay)

| 항목 | 기준 |
|---|---|
| 글자수 | 1,500~2,500자 |
| FAQ | **선택** (tool-review 유형만 권장) |
| 내부 링크 | **2~3개 필수** |
| 이미지 | **1장 이상** (OG 외 본문 이미지 최소 1장) |
| 외부 링크 | 1~3개 (공식 출처·도구) |

## FAQ 작성 규칙

- H3(`###`)로 질문, 그 아래 답변 문단
- **질문은 물음표로 끝** (`~인가요?`, `~할 수 있나요?` 등)
- **답변 40~80단어**, 첫 문장이 핵심
- 최소 3개, Pillar는 5개 이상
- `/publish-post` 가 JSON-LD FAQPage 자동 주입 (AIGrit 한정)

## 내부 링크 규칙

- **타겟 slug는 반드시 실재 파일이어야 함**:
  - AIGrit: `apps/aigrit/content/posts/ko/{slug}.mdx`
  - babipanote: `apps/babipanote/content/posts/{slug}.mdx`
- URL 포맷:
  - AIGrit → `/ko/blog/{slug}`
  - babipanote → `/blog/{slug}`
  - 교차 참조는 절대 URL (`https://aigrit.dev/ko/blog/{slug}`)
- 앵커 텍스트: **키워드 자연 삽입** (`"여기를 클릭" 금지, 같은 URL 2회 링크 금지`)
- **Pillar 링크 1개 필수** (Cluster 글의 경우)

## 이미지 규칙

- **파일 실재 검증 필수** — MDX 에 참조된 모든 `![alt](/images/...)` 경로가 public 디렉토리에 존재해야 함
- 파일명: `NN-kebab-case.png` (순서 접두어, OG 제외)
- 저장: `apps/{app}/public/images/{slug}/`
- 최소 해상도: OG 1200×630, 본문 이미지 1200px 이상 가로
- **broken image 는 발행 차단** (빈 참조 상태로 push 금지)

## 외부 링크 규칙

- **최소 1개** 공식 출처 또는 도구 링크
- `rel="noopener noreferrer" target="_blank"` 자동 주입됨
- 링크 깨짐 검증은 선택 (시간 경과로 404 자연 발생)
- AdSense 정책: 도박·성인·불법 사이트 링크 금지

## 작성 시점 행동 지침

**Claude가 초안 작성할 때 반드시 포함:**

1. FAQ 섹션 (AIGrit) — 최소 3 Q&A 를 글 하단에 직접 작성
2. 내부 링크 — 작성 시점에 **이미 발행된 글 목록을 Glob으로 조회**한 뒤, 자연스러운 문맥에 배치
3. 외부 링크 — 공식 도구·문서는 처음 언급 시 1회 링크
4. 이미지 마커 — 본문 흐름상 필요한 지점에 배치, 사용자 캡처 필요 여부 명시

**자동 생성 가능 이미지:**
- OG 썸네일 (sharp + SVG 템플릿)
- 다이어그램 (플로우·비교·차트)
- 브랜드 배너

**사용자 캡처 필수:**
- 실제 앱/도구 UI 스크린샷
- 대시보드 실사용 데이터

## 검증 순서

`/publish-post` 는 커밋 전 반드시 `/review-post` 결과를 받아 사용자 승인(`승인`, `approve`, `ok` 등) 을 기다린다. 미승인 상태에서 커밋 금지.

## 관련
- `/review-post` — 이 요건을 자동 검증하는 에이전트 호출 슬래시 커맨드
- `.claude/agents/post-reviewer.md` — 검증 에이전트 정의
- `.claude/commands/publish-post.md` — 발행 플로우 (review-post 호출 포함)
