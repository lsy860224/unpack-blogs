# SNS 자동 생성 스펙 — IG · Threads · X

> **트리거**: 블로그 글(AIGrit · babipanote) 발행 직후 — `/publish-post` 마지막 단계 또는 `git push` 후 hook.
> **출력 단위**: 블로그 글 1편으로 각 SNS 플랫폼당 **5번의 피드(=5 separate posts)** 분량. IG 한 피드는 캐러셀 1개(≥5장).
>   - **IG**: 캐러셀 5개 × 카드 ≥5장 = 글 1편당 25장 이상
>   - **Threads**: 단발 포스트 5개 (각 ≤500자, 필요 시 1-2 답글 트리)
>   - **X**: 트윗 5개 (각 280자 + 이미지 1장, 필요 시 1-2 답글 스레드)
> **저장 루트**: `~/dev/sns/{brand}/{NN}-{slug}/`
> **Obsidian 인덱스**: `Personal Hub/02. Unpack-Blogs/20. SNS/{brand}/{platform}/Posts.md`

---

## 1. 입력 (블로그 글에서 가져오는 값)

| 입력 | 출처 | 비고 |
|---|---|---|
| `{brand}` | 글 위치 | `aigrit` 또는 `babipanote` |
| `{NN}` | Pipeline 파일 prefix | 예: `01`, `13` |
| `{slug}` | MDX frontmatter `slug` | kebab-case |
| `{title}` | MDX frontmatter `title` | 카드 표지·트윗 훅 사용 |
| `{description}` | MDX frontmatter `description` | 캡션 본문 보조 |
| `{tags}` | MDX frontmatter `tags` | 해시태그 후보 |
| `{thumbnail}` | MDX frontmatter `thumbnail` | OG 이미지 (X Post 1 fallback) |
| `{topic_cluster}` | MDX frontmatter | 시리즈 묶기 (선택) |
| 본문 발췌 | MDX H2/H3 + 핵심 수치 라인 | 카드·트윗 콘텐츠 추출 소스 |
| 블로그 URL | `{brand}` + `{slug}` | aigrit `https://aigrit.dev/ko/blog/{slug}` · babipanote `https://babipanote.com/blog/{slug}` |

---

## 2. 출력 폴더 구조 (단일 규칙)

```
~/dev/sns/{brand}/{NN}-{slug}/
├── ig/
│   ├── post-1/                # IG 캐러셀 1번 (≥5장)
│   │   ├── 01-cover.png
│   │   ├── 02-card.png
│   │   ├── 03-card.png
│   │   ├── 04-card.png
│   │   └── 05-cta.png
│   ├── post-2/                # IG 캐러셀 2번
│   ├── post-3/                # IG 캐러셀 3번
│   ├── post-4/                # IG 캐러셀 4번
│   └── post-5/                # IG 캐러셀 5번
├── x/
│   ├── post-1.png             # X 트윗 1번 이미지 (1600×900)
│   ├── post-2.png
│   ├── post-3.png
│   ├── post-4.png
│   └── post-5.png
├── ig-captions.md             # 5 캐러셀 × (메인 캡션 + 슬라이드 보조 캡션)
├── threads.md                 # 5 단발 Threads 포스트 (옵션 답글 트리)
├── x.md                       # 5 단발 X 트윗 (옵션 답글 스레드)
└── _meta.json                 # {brand, NN, slug, title, blog_url, ig_posts:5, generated_at}
```

### 글 번호·slug 매칭

- `{NN}` 와 `{slug}` 는 Obsidian Pipeline 파일명에서 추출:
  - 예: `02. Unpack-Blogs/10. Pipeline/AIGrit/01-aigrit-claude-code-vs-cursor.md`
    → `NN=01`, slug 파일명 그대로 사용 가능 (`01-aigrit-claude-code-vs-cursor`)
  - 또는 MDX frontmatter `slug` (`claude-code-vs-cursor`) + Pipeline `NN` 결합
- 폴더명은 Pipeline 파일명과 동일: `01-aigrit-claude-code-vs-cursor`

---

## 3. 이미지 사양

### IG 캐러셀 5개 × 카드 ≥5장 (1080×1080, 정사각형)

각 캐러셀(=피드)은 자체 완결 스토리. 같은 글의 다른 각도를 다룬다 (5번 피드 ≠ 5장 카드).

**캐러셀 내 카드 5장 표준 배치:**

| 슬라이드 | 역할 | AIGrit 톤 | babipanote 톤 |
|---|---|---|---|
| 01-cover | 훅 표지 (해당 캐러셀 주제 + 핵심 수치) | 다크 + Indigo+Cyan + Pretendard Bold | Plum 배경 + Gowun Batang 세리프 + 종이결 |
| 02-card | 문제 제기 / 맥락 | 표·체크리스트 | 손편지 무드 |
| 03-card | 핵심 발견 1 (수치 카드) | 큰 수치 + 1줄 해석 | 큰 인용부호 + 1문장 |
| 04-card | 핵심 발견 2 / 한계 | 비교 카드 | 짧은 단상 |
| 05-cta | CTA + URL | `aigrit.dev/{slug}` 강조 | `babipanote.com/blog/{slug}` |

**캐러셀 5개의 각도 분배 (예시 — 글 구조에 맞춰 변주):**

| 캐러셀 | 각도 | AIGrit 예시 (Claude Code vs Cursor) | babipanote 예시 (36시간 두 블로그) |
|---|---|---|---|
| post-1 | Hook + 한 줄 결론 | 14일 실측 / 워크플로우에 따라 갈림 | 빈 폴더 → 두 도메인 / 36h |
| post-2 | 비교 테이블·전체 그림 | 8축 비교 테이블 | 숫자 회고 (16커밋·60파일·트래픽 0) |
| post-3 | 핵심 디테일 1 | 시나리오 1·2 (Flutter 위젯·버그 수정) | 왜 모노레포 / blog-core·brand.config.ts |
| post-4 | 핵심 디테일 2 | 시나리오 3·5 (리팩토링·반복 작업) | 6 Phase 타임라인 |
| post-5 | 결론·추천·CTA | 비용 + 추천 대상 + CTA | 잘한 것·못한 것 + 다음 주 + CTA |

**규칙:**
- 5개 캐러셀이 **각각 단독으로 읽혀야** 한다 (피드 사이 최소 1일 간격으로 게시)
- 캐러셀끼리 같은 표·이미지를 재사용하지 않는다 (콘텐츠 중복 금지)
- 모든 캐러셀의 5번째(CTA) 카드 URL은 동일

### X 이미지 5장 (1600×900, 16:9)

- 5개 X 트윗 각각의 첨부 이미지 1장씩
- IG `post-N/01-cover.png` 또는 `03-card.png`을 가로 비율로 변환 가능
- 글 OG (`apps/{brand}/public/images/{slug}/og.png`) 는 트윗 1번에 한해 재사용 가능

### 생성 우선순위 (CLAUDE.md `절대 준수 사항` 정합)

1. **Figma Master Component 인스턴스** — 브랜드별 카드뉴스 템플릿 노드 사용
   - AIGrit: `njkSF5MinT8kK7kaoYpp12`
   - babipanote: `D2hOsoihiYzAIuZHy5nnpz`
2. **NapkinAI** — 데이터 시각화 카드 (수치 비교 그래프 등)
3. **sharp + SVG 템플릿** — Figma 미설정 시 fallback (`packages/blog-core/lib/og-template.ts` 패턴 재활용)

> 이미지 직접 생성 시 Figma Master 노드를 절대 수정하지 않는다 (instance 만 사용).

---

## 4. 텍스트 사양

### `ig-captions.md` (5 캐러셀 × 5 캡션)

각 캐러셀의 메인 캡션(슬라이드 1)이 IG 피드 본문이 된다. 슬라이드 2-5의 보조 캡션은 캐러셀 내부 텍스트와 짝지어 작성한다.

```markdown
# {title} · IG Captions (5 캐러셀)

## Carousel post-1 — {각도 라벨} (예: Hook)

### Slide 1 (Main / 피드 본문)
{1-2줄 훅}
{본문 2-4문단}
{CTA — 링크}
.
.
.
{해시태그 20-25개}

### Slide 2-5 (보조)
{슬라이드별 단문 2-3줄 × 4}

## Carousel post-2 — {각도 라벨}
... (동일 구조)

## Carousel post-3 — {각도 라벨}
...

## Carousel post-4 — {각도 라벨}
...

## Carousel post-5 — {각도 라벨} (CTA / 결론)
...
```

### `threads.md` (5 단발 포스트)

각 포스트는 단독으로 게시된다 (1피드 = 1포스트). 답글 트리는 옵션.

```markdown
# {title} · Threads (5 posts)

## Post 1 — Hook
{500자 이내, 첫 문장 훅 + 핵심 수치 + 블로그 URL}

(옵션) Reply 1: {답글 1}

## Post 2 — {각도 2}
...

## Post 3 — {각도 3}
...

## Post 4 — {각도 4}
...

## Post 5 — CTA / 결론
...
```

### `x.md` (5 단발 트윗)

각 트윗은 단독으로 게시된다. 짧은 스레드 확장은 옵션.

```markdown
# {title} · X (5 tweets)

## Tweet 1 — Hook + Link
{280자 이내, 핵심 수치 + 블로그 링크}
[image: x/post-1.png]

(옵션) Reply 1/2: {스레드 확장}

## Tweet 2 — {각도 2}
...
[image: x/post-2.png]

## Tweet 3 — {각도 3}
...
[image: x/post-3.png]

## Tweet 4 — {각도 4}
...
[image: x/post-4.png]

## Tweet 5 — CTA
→ {blog_url}
[image: x/post-5.png]
```

### 톤 분리 (브랜드별)

| 항목 | AIGrit | babipanote |
|---|---|---|
| 인칭 | 존댓말·3인칭 분석가 | 1인칭 일기체 |
| 핵심 수치 | 정면 노출 (`+38%` 큰 글씨) | 자연스럽게 곁들이기 |
| 감탄사·이모지 | 배제 | 1-2회 허용 |
| 해시태그 수 | IG 20-25 / Th·X 1-3 | IG 10-15 / Th·X 1-3 |
| CTA 어조 | "지금 읽기" "측정 조건 공개" | "조용히 보기" "혹시 비슷하세요?" |
| 광고 표기 | 제휴는 본문 글에 명시 (SNS 별도 표기 X) | 광고·제휴 없음 |

---

## 5. 콘텐츠 추출 규칙 (블로그 → SNS)

### IG Slide 1 / Threads Post 1 / Tweet 1 — 훅
- MDX 본문 첫 H2 직후 1-2문장 또는 핵심 수치 라인 추출
- 제목 그대로 쓰지 말고 "왜 읽어야 하는가" 1문장으로 변환

### Slide 3-4 / Posts 3-4 / Tweets 3-4 — 핵심 발견
- 본문에서 큰 수치(`+38%`, `2.1s`, `89.3pts` 등) 또는 강한 인용부호 문장 우선 추출
- AIGrit: 측정 조건 1줄 동반 (`n=200, Next.js monorepo` 등)
- babipanote: 단상·깨달음 1문장으로 압축

### Slide 5 / Post 5 / Tweet 5 — CTA
- AIGrit: `→ aigrit.dev/{slug}` (한국어 i18n 경로 `/ko/blog/{slug}` 자동 적용)
- babipanote: `→ babipanote.com/blog/{slug}`
- 단축 URL 사용 X (브랜드 URL 그대로 노출)

### 풀텍스트 노출 금지

- SNS 포스트는 글 1편의 발췌만 — 본문 70% 이상 복붙 금지
- 항상 블로그 링크 정독을 유도 (광고 수익·SEO 신호)

---

## 6. 자동 생성 트리거

### Option A — `/publish-post` 슬래시 커맨드 마지막 단계 (권장)

`.claude/commands/publish-post.md` 의 발행 후 단계에 다음을 추가:

```
9. SNS 자동 생성 (script: scripts/generate-sns-assets.ts)
   - 인자: --brand={brand} --slug={slug} --pipeline-file={pipeline.md}
   - 출력: ~/dev/sns/{brand}/{NN}-{slug}/
   - Obsidian Posts.md 새 행 자동 추가
```

### Option B — git post-commit hook

`.claude/hooks/post-commit-sns.sh` 가 `feat: post: ...` 커밋 메시지 감지 → 동일 스크립트 실행.

### 출력 후 보고 (사용자 확인용)

```
✅ SNS 자산 생성 완료: ~/dev/sns/{brand}/{NN}-{slug}/
📷 IG 카드뉴스 5장: ig/01~05.png
🐦 X 이미지 5장: x/01~05.png
📝 캡션·포스트·트윗: ig-captions.md / threads.md / x.md
📋 Obsidian 인덱스 업데이트: 02. Unpack-Blogs/20. SNS/{brand}/*/Posts.md
👀 검토 후 수동 게시 (자동 발행 X — 톤·정합성 사용자 확인 단계)
```

---

## 7. Obsidian 인덱스 업데이트

스크립트는 다음 3개 `Posts.md` 에 새 행 추가:

```
Personal Hub/02. Unpack-Blogs/20. SNS/{brand}/Instagram/Posts.md
Personal Hub/02. Unpack-Blogs/20. SNS/{brand}/Threads/Posts.md
Personal Hub/02. Unpack-Blogs/20. SNS/{brand}/X/Posts.md
```

추가 행 예시 (각 파일의 "게시 캘린더" 표 끝):
```
| {N} | {NN}-{slug} | ~/dev/sns/{brand}/{NN}-{slug}/ig/ | ~/dev/sns/{brand}/{NN}-{slug}/ig-captions.md | YYYY-MM-DD HH:mm | ☐ |
```

(상태는 ☐ — 사용자가 게시 후 수동 ☑ 처리 또는 별도 스크립트로 일괄 처리)

---

## 8. 검증 (생성 후 자동 점검)

| 검증 항목 | 합격 기준 |
|---|---|
| 이미지 5장 × 2 (IG + X) | 모두 파일 실재 + 사이즈 일치 |
| 캡션 / 포스트 / 트윗 글자수 | IG 캡션 ≤ 2200자 · Threads ≤ 500자 · X ≤ 280자 |
| 블로그 URL 5회 모두 동일 | `aigrit.dev/{slug}` 또는 `babipanote.com/blog/{slug}` |
| 풀텍스트 복붙 비율 | ≤ 70% (본문 발췌 비율) |
| 브랜드 톤 정합 | 존댓말/일기체 분리 (간단 룰: AIGrit 어미 검사) |
| 해시태그 수 | 브랜드별 § 4 표 기준 충족 |

검증 실패 시 사용자에게 항목 단위 보고 + 수정 요청.

---

## 9. 보안·운영

- 자동 게시 X (생성만, 게시는 수동) — 톤·정합성 검토 후 사용자가 직접 업로드
- API 키·비밀번호 코드 하드코딩 금지 (게시 자동화 도입 시 `.env.local` 경유)
- 같은 글에 대해 재실행 시 기존 폴더 덮어쓰기 전 사용자 확인
- 캠페인(런칭) 자산은 `~/dev/sns/{brand}/` 루트에 보존 — 글 단위 폴더와 분리

---

## 10. 관련 문서

| 문서 | 용도 |
|---|---|
| `docs/POST_AIGRIT.md` · `docs/POST_BABIPANOTE.md` | 글 작성 규칙 (입력 톤 정합성) |
| `docs/IMAGE_GUIDE.md` | 이미지 생성 우선순위 (Figma → NapkinAI → sharp) |
| `docs/THUMBNAIL.md` | OG 썸네일 (X Post 1 fallback 가능) |
| `docs/PUBLISH_CHECKLIST.md` | 발행 플로우 (이 자동화의 트리거 단계) |
| Obsidian `02. Unpack-Blogs/20. SNS/_README.md` | 운영 허브 진입점 |
| Obsidian `02. Unpack-Blogs/11. AIGrit SNS Launch (2026.04) — IG·Threads·X.md` | AIGrit 런칭 캠페인 (선례·톤 레퍼런스) |

---

## 11. 구현 TODO (단계적)

- [ ] `scripts/generate-sns-assets.ts` — Pipeline 파일 → 5장×2 이미지 + 3 텍스트 파일 생성
- [ ] Figma 카드뉴스 Master 템플릿 노드 ID 확정 (브랜드별 5 슬롯)
- [ ] `packages/blog-core/lib/sns-extract.ts` — MDX 본문에서 훅·수치·인용 추출 헬퍼
- [ ] `.claude/commands/publish-post.md` Step 9 추가
- [ ] `Posts.md` 자동 행 추가 (Obsidian REST API 또는 파일 직접 편집)
- [ ] 검증 스크립트 (§ 8)
- [ ] 첫 글로 dry-run (스크립트 출력만, Obsidian/이미지 갱신 X)

---

*최초 작성: 2026-04-29 · `~/dev/unpack-blogs/docs/SNS_AUTOMATION.md`*
