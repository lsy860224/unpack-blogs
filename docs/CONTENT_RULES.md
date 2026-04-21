# 공통 콘텐츠 규칙

> AIGrit + babipanote 공통. 플랫폼별 차이는 POST_AIGRIT.md / POST_BABIPANOTE.md 참조.

## 마커 포맷

초안에서 사용. `/publish-post`가 실제 컴포넌트로 치환.

### 이미지 마커
```
{IMG: 01-claude-home | alt: Claude 홈 화면 | caption: 첫 진입 화면}
```
→ `<Image src="/images/{slug}/01-claude-home.png" alt="Claude 홈 화면" />`

### 내부 링크 마커
```
{LINK: aigrit-claude-code-guide | anchor: Claude Code 설치 가이드}
```
→ `<Link href="/ko/blog/aigrit-claude-code-guide">Claude Code 설치 가이드</Link>`

- 타겟 slug 실재 검증: 없으면 빌드 에러
- AIGrit: 5~7개, babipanote: 2~3개

## 내부 링크 전략 (B-4)

### 우선순위
1. 같은 topic_cluster의 Pillar (Cluster 글은 필수 1개)
2. 같은 topic_cluster의 다른 Cluster
3. 크로스 클러스터 (1~2개)
4. 교차 사이트 (AIGrit ↔ babipanote, 수동·신중)

### 앵커 텍스트
- ✅ "Claude Code 설치 가이드에서 다뤘듯이"
- ❌ "여기를 클릭", "이 글을 참고하세요"
- ❌ 같은 URL 2회 링크 금지

## Featured Snippet 타겟 (AIGrit만)

Pipeline frontmatter `featured_snippet_target` 필드:

| 값 | 글 유형 | 필수 구성 |
|---|---|---|
| `table` | 비교 글 | 1st H2 아래 스펙 비교표 |
| `list` | 튜토리얼 | 번호 리스트 5~10단계 |
| `paragraph` | 정의·개념 | 첫 문단 50~60자 요약 |
| `none` | 해당 없음 | — |

## AI 냄새 금지어 (공통)

획기적인, 혁신적인, 놀라운, ~을 통해, 다양한, 효율적인, 최적의, 원활한, 심층적인, 포괄적인

초안 작성 후 반드시 위 단어 검색 → 자연스러운 표현으로 교체.

## E-E-A-T (AIGrit)

- Experience: 실사용 기간 명시 ("3주 써봤다")
- Expertise: 스크린샷 + 수치 + 워크플로우
- Authority: About 페이지 프로필
- Trust: Disclaimer + 솔직한 단점

## 이미지 규칙

- 파일명: `NN-kebab-case.png` (순서 접두어)
- 저장: `apps/{app}/public/images/{slug}/`
- AIGrit: 3~5장 (네이버 에디션은 10장+)
- babipanote: 스크린샷·코드 스냅샷 중심
- Next.js `<Image>` 컴포넌트 필수 (자동 최적화)

### 원본 이미지 규격 (필수)

| 항목 | 기준 |
|---|---|
| 최대 해상도 | **1600px** (가로·세로 중 큰 쪽) |
| 최대 용량 | **300KB/장** (OG는 200KB) |
| 권장 포맷 | WebP > AVIF > PNG(UI 캡처) > JPG(사진) |
| 캡처 후 | `sips --resampleHeightWidthMax 1600 file.png --out file.png` |

큰 원본(1M+)을 그대로 커밋하면 LCP·빌드 시간을 악화시킨다. 커밋 전 반드시 리샘플.
빌드 타임에 Next.js가 여러 크기로 재생성하지만 원본이 작아야 처리가 빠르다.

## Obsidian 참고 문서

- `02. Blog SEO/09. 실전 워크플로우 매뉴얼.md` — Step별 복붙 프롬프트
- `02. Blog SEO/12. Topic Cluster/_README.md` — 클러스터·내부 링크 알고리즘
- `02. Blog SEO/99. Templates/` — frontmatter 템플릿
