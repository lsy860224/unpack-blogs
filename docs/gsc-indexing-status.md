# GSC 색인·인지 추적표 (AIGrit · babipanote)

> Google Search Console URL Inspection 제출 + Internal Links 보고서 인지 상태 추적용. 마지막 갱신: 2026-04-29 23:50 KST.
>
> **상태 정의:**
> - **제출 (`gsc_submitted`)**: GSC URL Inspection 색인 생성 요청 완료
> - **인지 (`gsc_indexed`)**: GSC `링크 → 상위 링크된 페이지 - 내부` 보고서 또는 `색인 → 페이지` 보고서에 노출
> - **인지 ≠ 색인**: 인지는 GSC가 페이지를 크롤링·발견했다는 신호. 실제 색인(검색 노출)까지는 추가 시간 필요.

## 현 상태 요약 (2026-04-29 23:50 GSC Internal Links 보고서 기준)

| 도메인 | 발행 | 제출 | 🟢 인지 | 🔴 미인지 | 인지율 |
|---|:---:|:---:|:---:|:---:|:---:|
| AIGrit ko | 14 | 14 | 8 | 6 | 57% |
| AIGrit en | 3 | 3 | 0 | 3 | 0% |
| **AIGrit 합계** | **17** | **17** | **8** | **9** | **47%** |
| **babipanote** | **14** | **14** | **2** | **12** | **14%** |
| **전체** | **31** | **31** | **10** | **21** | **32%** |

**핵심 인사이트:**
- 04-22 발행 babipanote 글이 6일 경과해도 다수 미인지 → 도메인 권위·내부 링크 그래프 보강 필요
- 04-27 이후 발행 글은 미인지가 정상 (시간 부족)
- AIGrit이 babipanote보다 인지 속도 3배 이상 빠름 → 교차 백링크로 babipanote 권위 끌어올리기 권장

---

## AIGrit (`aigrit.dev`)

### Korean (`/ko/blog/`) — 14개

| # | slug | 발행일 | 우선 | 제출 | GSC 인지 |
|:---:|---|---|:---:|:---:|:---:|
| 1 | `hello-world` | 2026-04-15 | ⭐ | [x] | 🟢 |
| 2 | `claude-code-vs-cursor` | 2026-04-16 | ⭐⭐⭐ | [x] | 🟢 |
| 3 | `claude-4-sonnet-vs-gpt-4o` | 2026-04-17 | ⭐⭐⭐ | [x] | 🟢 |
| 4 | `perplexity-ai-guide` | 2026-04-21 | ⭐⭐⭐ | [x] | 🟢 |
| 5 | `apple-shortcuts-ai-automation` | 2026-04-21 | ⭐⭐⭐ | [x] | 🟢 |
| 6 | `solo-developer-automation-stack` (Pillar) | 2026-04-22 | ⭐⭐⭐ | [x] | 🔴 |
| 7 | `notion-ai-guide` | 2026-04-22 | ⭐⭐ | [x] | 🟢 |
| 8 | `craft-vs-notion` | 2026-04-22 | ⭐⭐ | [x] | 🟢 |
| 9 | `claude-mcp-guide` | 2026-04-22 | ⭐⭐ | [x] | 🟢 |
| 10 | `ai-tools-2026-guide` (Pillar) | 2026-04-22 | ⭐⭐⭐ | [x] | 🔴 |
| 11 | `claude-code-flutter-app-guide` | 2026-04-27 | ⭐⭐⭐ | [x] | 🔴 |
| 12 | `ai-side-income-100man-roadmap` (Pillar) | 2026-04-28 | ⭐⭐⭐ | [x] | 🔴 |
| 13 | `make-automation-guide` | 2026-04-28 | ⭐⭐ | [x] | 🔴 |
| 14 | `obsidian-getting-started` | 2026-04-29 | ⭐⭐ | [x] | 🔴 |

### English (`/en/blog/`) — 3개

| # | slug | 발행일 | 제출 | GSC 인지 |
|:---:|---|---|:---:|:---:|
| 1 | `hello-world` | 2026-04-15 | [x] | 🔴 |
| 2 | `claude-code-vs-cursor` | 2026-04-16 | [x] | 🔴 |
| 3 | `claude-4-sonnet-vs-gpt-4o` | 2026-04-17 | [x] | 🔴 |

### AIGrit 미인지 9개 — 보강 우선순위

1. **Pillar 3개 우선** (가장 큰 SEO 손실)
   - `solo-developer-automation-stack` — Cluster 내 백링크 ↑ 확보 필요
   - `ai-tools-2026-guide` — 동일
   - `ai-side-income-100man-roadmap` — 발행 1일 차, 시간 부여
2. **04-22 1주 경과 글 0건** — 04-22 발행 1개 글(solo-developer-automation-stack)만 미인지. 다른 04-22 글들은 모두 인지됨. 결국 Pillar 두 글이 cluster 글에 비해 인지가 늦은 것이 패턴.
3. **04-27~04-29 신규 4개**는 정상 (시간 부족). 1주 후 재확인.
4. **en 3개**는 후순위 (KO 안정 후)

---

## babipanote (`babipanote.com`) — 14개

| # | slug | 발행일 | 우선 | 제출 | GSC 인지 |
|:---:|---|---|:---:|:---:|:---:|
| 1 | `hello-world` | 2026-04-15 | ⭐ | [x] | 🔴 |
| 2 | `week1-sprint-two-blogs` | 2026-04-15 | ⭐⭐ | [x] | 🟢 |
| 3 | `building-app-with-claude-code` | 2026-04-15 | ⭐⭐⭐ | [x] | 🔴 |
| 4 | `obsidian-seo-dashboard` | 2026-04-21 | ⭐⭐⭐ | [x] | 🔴 |
| 5 | `sprint-week1-review` | 2026-04-21 | ⭐⭐ | [x] | 🟢 |
| 6 | `craft-naver-workflow` | 2026-04-22 | ⭐⭐ | [x] | 🔴 |
| 7 | `adsense-prep-checklist` | 2026-04-22 | ⭐⭐ | [x] | 🔴 |
| 8 | `time-management-solo-builder` | 2026-04-22 | ⭐⭐ | [x] | 🔴 |
| 9 | `aigrit-month1-revenue` | 2026-04-22 | ⭐⭐ | [x] | 🔴 |
| 10 | `naver-dual-platform-strategy` | 2026-04-22 | ⭐⭐ | [x] | 🔴 |
| 11 | `gentledo-naming-from-keelry` | 2026-04-23 | ⭐⭐⭐ | [x] | 🔴 |
| 12 | `building-gentledo-with-claude-code` | 2026-04-23 | ⭐⭐⭐ | [x] | 🔴 |
| 13 | `app-store-review-gentledo-launch` | 2026-04-23 | ⭐⭐⭐ | [x] | 🔴 |
| 14 | `turborepo-brand-config` | 2026-04-28 | ⭐⭐ | [x] | 🔴 |

### babipanote 미인지 12개 — 도메인 권위 보강 액션

**원인 추정:**
- 도메인이 신규 (1주 경과)
- 외부 백링크 0개에 가까움
- AIGrit ↔ babipanote 교차 인용이 단방향(AIGrit → babipanote 일부)

**즉시 보강 액션 (이번 PR에 포함):**
- AIGrit `solo-developer-automation-stack` Pillar 본문에 babipanote 백링크 2개 신규 추가
  - `obsidian-seo-dashboard` (지식관리 → 자동화 연결)
  - `building-gentledo-with-claude-code` (개발 자동화 실사례)
- → babipanote 미인지 글 2개에 첫 외부(타 도메인) 인링크 발생 → 크롤 신호 강화

**중기 보강:**
- AIGrit `ai-tools-2026-guide` Pillar에 babipanote 추가 1개 더 (이미 3개 있음)
- babipanote 발행 글 끼리 상호 백링크 강화 (현재 2~3개로 약함)

---

## 자동화 (Pipeline frontmatter 필드)

`/publish-post` Step 11 발행 후 자동 동작에 다음 추가 (이번 PR 적용):

```yaml
# Pipeline 카드 frontmatter 신규 필드
gsc_submitted: true              # URL Inspection 제출 완료 여부
gsc_submitted_date: "2026-04-29" # 제출 일자 (KST)
gsc_indexed: false               # Internal Links 보고서 노출 여부 (수동 갱신)
gsc_indexed_check_date: "2026-04-29" # 마지막 확인 일자
```

**현 31개 카드 일괄 적용:**
- 모두 `gsc_submitted: true`, `gsc_submitted_date: "2026-04-29"` (사용자 확인 — 전부 제출됨)
- 위 표 기준으로 `gsc_indexed: true|false` 분기

**주간 검증 루틴:** 일요일 22시 주간 리뷰에 GSC `링크 → 상위 링크된 페이지 - 내부` 보고서 확인 → 미인지에서 인지로 전환된 글 `gsc_indexed: true` + `gsc_indexed_check_date` 갱신.

---

## 관련

- [docs/PUBLISH_CHECKLIST.md](PUBLISH_CHECKLIST.md) — 발행 후 GSC 단계
- [.claude/commands/publish-post.md](../.claude/commands/publish-post.md) — Step 11 자동 추가 대상
- Naver는 별개: `blog.naver.com` 호스트는 SearchAdvisor 등록 불가 (memory `reference_naver_blog_indexing`)
