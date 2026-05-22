# /sns-build

발행된 블로그 글의 SNS 자산(IG 캐러셀 5 × ≥5장 + X 5장 + Threads/X/IG 캡션) 일괄 생성.

## 인자

`/sns-build <brand> <slug>` 또는 `/sns-build <brand> <NN-pipeline-prefix>`

- `<brand>`: `aigrit` 또는 `babipanote`
- `<slug>` 또는 `<NN-pipeline-prefix>`:
  - slug만 전달하면 Obsidian Pipeline 디렉토리에서 매칭 파일 prefix 자동 추출
  - 예: `/sns-build aigrit sell-ai-prompts-promptbase` → 자동으로 `15-aigrit-sell-ai-prompts-promptbase` 매칭

## 사전 조건

- 글이 이미 `apps/{brand}/content/posts/(ko/)?{slug}.mdx`에 존재해야 한다 (frontmatter title·description·tags 추출 소스)
- Obsidian Pipeline 카드(`02. Unpack-Blogs/10. Pipeline/{Brand}/{NN}-{brand}-{slug}.md`)가 존재해야 한다 (primary_keyword·featured_snippet_target·internal_links_used 추출 소스)
- 폰트 캐시(`/tmp/og-fonts/`) 준비됨 — 없으면 `bash scripts/og/download-fonts.sh`
- 단일 진실 공급원: `docs/SNS_AUTOMATION.md`

## 처리 순서

### Step 1 — Pipeline prefix 결정
slug만 전달된 경우:
```bash
ls "$OBSIDIAN_VAULT/02. Unpack-Blogs/10. Pipeline/{Brand}/" | grep -E "^[0-9]+-{brand}-{slug}\.md$"
```
매칭 0건/2건+ 이면 사용자에게 prefix 직접 지정 요청.

### Step 2 — 자산 폴더 준비
```bash
mkdir -p ~/dev/sns/{brand}/{NN-prefix}/{ig,x}
```
기존 폴더가 있고 `_spec.json` 도 있으면 **재생성 확인** 후 진행.

### Step 3 — `_spec.json` 작성 (핵심)
MDX 본문을 읽고 5개 캐러셀의 각도를 설계. 표준 분배 (글 구조에 맞춰 변주):

| 캐러셀 | 각도 | 콘텐츠 소스 |
|---|---|---|
| post-1 | Hook + 한 줄 결론 | 도입부 + frontmatter `description` |
| post-2 | 전체 그림 (표·플로우) | H2 1~2번 + 핵심 표 |
| post-3 | 핵심 발견 1 | featured_snippet_target 섹션 |
| post-4 | 핵심 발견 2 / 사례 | 본문 사례·수치 카드 |
| post-5 | 결론·추천·CTA | 마무리 H2 + blog URL |

각 캐러셀의 카드 5장 표준:
| 슬라이드 | role | 콘텐츠 |
|---|---|---|
| 01 | cover | 캐러셀 훅 + 핵심 수치 |
| 02 | context | 맥락·문제 제기 |
| 03 | finding/list | 핵심 발견 1 (수치·표) |
| 04 | finding/list | 핵심 발견 2 (사례·비교) |
| 05 | cta | CTA + blog URL |

작성한 spec을 `~/dev/sns/{brand}/{NN-prefix}/_spec.json` 으로 저장.
스키마 참조: 기존 `~/dev/sns/aigrit/01-aigrit-claude-code-vs-cursor/_spec.json`

**필수 최상위 필드:**
- `brand`, `pipeline_file`, `slug`, `title`, `blog_url`, `date_published`, `tags`
- `carousels`: 5개 항목 (각 항목에 `label`, `cards[5]`)

### Step 4 — 이미지 30장 자동 렌더
```bash
python3 scripts/sns/generate-sns-cards.py --brand {brand} --slug-prefix {NN-prefix}
```
- 출력: `ig/post-{1..5}/{01..05}-{role}.png` (1080×1080) + `x/post-{1..5}.png` (1600×900)
- `_meta.json` 자동 생성 (spec에서 추출)
- 실패 시 spec 검증 에러 메시지 출력 후 중단

### Step 5 — 텍스트 3종 작성 (`ig-captions.md`, `threads.md`, `x.md`)
MDX 본문 + Pipeline 카드를 읽고 직접 작성:

**`ig-captions.md`** — 5 캐러셀 각각의 메인 캡션 (각 700~1500자, 슬라이드별 보조 캡션 포함)
- 첫 문단: 캐러셀 후크 + 한 줄 결론
- 본문: 카드 5장 내용을 자연스러운 문장으로 풀어쓰기
- 마지막: blog URL + 해시태그 8~12개 (브랜드 + 토픽 + 트렌딩)

**`threads.md`** — Threads 단발 포스트 5개 (각 ≤500자)
- 톤: 짧고 직설적, Hook 문장 + 핵심 + 후속 답글 트리(옵션 1~2)
- 각 포스트는 독립 발행 가능해야 함

**`x.md`** — X 트윗 5개 (각 ≤280자) + 이미지 1장(`x/post-N.png`)
- 톤: 단정적, 수치·결론 중심
- 옵션 1~2 답글 스레드

### Step 6 — Obsidian Posts.md 로그 갱신
`02. Unpack-Blogs/20. SNS/{brand}/{Instagram|Threads|X}/Posts.md` 의 해당 글 행 추가:

| 항목 | 값 |
|---|---|
| 발행일 | 본 글 frontmatter `date` |
| 자산 경로 | `~/dev/sns/{brand}/{NN-prefix}/` |
| 상태 | `drafted-not-posted` |
| 게시 예정일 | 미정 (사용자 수동 게시) |

각 플랫폼당 5행 (총 15행)을 한 번에 추가.

### Step 7 — 결과 출력
```
✅ SNS 자산 생성 완료 — {brand}/{NN-prefix}
📂 폴더: ~/dev/sns/{brand}/{NN-prefix}/
🖼️ 이미지: 25 IG + 5 X = 30장
📝 텍스트: ig-captions.md ({총자수}) · threads.md (5포스트) · x.md (5트윗)
📊 _meta.json: status=drafted-not-posted

다음 단계:
1. 폴더에서 자산 시각 검토
2. 캡션·트윗 텍스트 톤 점검 (브랜드 가이드라인 일치 여부)
3. IG 캐러셀 5개를 1일 간격으로 게시 (콘텐츠 중복 금지 — 같은 글의 다른 각도)
4. 게시 완료 후 _meta.json status: posted 로 업데이트
```

## 주의사항

- 자동 게시는 절대 하지 않음 — 생성된 자산을 사용자가 수동 업로드
- 같은 글의 5개 캐러셀이 콘텐츠 중복되지 않도록 spec 작성 시 각도 분배 신중
- 모든 캐러셀의 5번째(CTA) 카드 URL은 동일 — `https://{DOMAIN}/{LOCALE_PREFIX}/blog/{slug}`
- 브랜드별 톤:
  - **aigrit**: 다크 + Indigo+Cyan + Pretendard Bold + 데이터 중심 분석가 톤
  - **babipanote**: Paper + Plum + Gowun Batang 세리프 + 1인칭 일기체 톤
- 민감정보(이메일·실명·내부 URL) spec에 포함 금지
- 텍스트에 AI 냄새 금지어 사용 금지 (글로벌 룰 `feedback_*` 참조)

## 관련

- 스펙: `docs/SNS_AUTOMATION.md`
- 이미지 렌더 스크립트: `scripts/sns/generate-sns-cards.py`
- 폰트 캐시: `scripts/og/download-fonts.sh`
- 자산 저장소: `~/dev/sns/{brand}/{NN-prefix}/`
- Obsidian 인덱스: `02. Unpack-Blogs/20. SNS/_README.md`
