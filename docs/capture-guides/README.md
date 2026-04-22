# 스크린샷 캡쳐 가이드 (capture-guides/)

모든 블로그 글은 **발행 전** 자체 캡쳐 가이드를 갖는다. Claude 가 Obsidian SEO Pipeline 카드 + Craft 초안을 읽고 MDX 변환할 때 **매번 자동으로** 이 디렉토리에 가이드 파일을 생성한다.

## 파일 구조

```
docs/capture-guides/
├── README.md                           ← 이 파일 (워크플로우·템플릿)
├── retro/                              ← 과거 발행 글 회고용 가이드
│   ├── aigrit-1-7.md                  ← AIGrit #1~#7 통합
│   └── babipanote-1-7.md              ← babipanote #1~#7 통합
└── {app}-{slug}.md                     ← 신규 글은 개별 파일
    예: aigrit-claude-mcp-guide.md
```

## 신규 글 발행 워크플로우 (매회 반복)

1. **Obsidian 카드 읽기** — `02. Blog SEO/10. Pipeline/{app}/{slug}.md`
   - `primary_keyword`, `secondary_keywords`, `content_type`, `topic_cluster`
   - `featured_snippet_target`, `internal_links_planned`
2. **Craft 초안 읽기** — `05. Blog Pipeline/01. In Progress/{app}/#N [{app}] {제목}`
   - `{IMG: NN-name | alt: 설명}` 마커 추출
   - `{LINK: target-slug}` 마커 추출
3. **MDX 변환** — 자동 생성 가능 이미지(OG·다이어그램) 렌더
4. **캡쳐 가이드 생성** (신규 추가 단계) — `docs/capture-guides/{app}-{slug}.md` 에 아래 정보 기록:
   - 각 이미지별 경로·파일명·규격
   - 자동 생성 vs 사용자 캡쳐 구분
   - 사용자 캡쳐 필요 시 구체적 도구·앱·화면 지시
   - 권장 쿼리·버튼 위치·창 크기 등 재현 가능한 단계
   - 민감정보 마스킹 주의사항
5. **/review-post** 자동 호출 → preflight 통과 확인
6. **사용자 승인** → commit + push
7. **Obsidian·Craft 정리** (이미 자동화됨)

## 개별 가이드 파일 템플릿

각 신규 글에 대해 아래 템플릿으로 생성:

```markdown
# {제목} — 스크린샷 캡쳐 가이드

**대상 글:** [{app}/{slug}](../../apps/{app}/content/posts/**/{slug}.mdx)
**발행 예정일:** YYYY-MM-DD
**preflight 기준:** Cluster 3~5장 / Pillar 5장+ / babipanote 1장+

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 (1200×630)
- [x] `NN-xxx.png` — 다이어그램/차트 (컨셉: …)

### [사용자 캡쳐] — 준비 필요
- [ ] `NN-xxx.png` — 경로 `apps/{app}/public/images/{slug}/`
  - 컨텐츠: (구체적으로)
  - 도구: (앱·웹사이트 URL)
  - 캡쳐 방법: (Cmd+Shift+4 등)
  - 권장 영역: (보여야 할 UI 요소 명시)
  - 민감정보 마스킹: (이메일·이름 등)

## 규격 공통

- 본문 이미지: 가로 1,600~2,000px PNG
- 모바일 캡쳐: 1,080~1,290px 리사이즈
- macOS `Cmd+Shift+4` 드래그 / `Cmd+Shift+4` → 스페이스 → 창 클릭
- Preview 앱 사각형 도구로 민감정보 마스킹
```

## 관련 규정

- `.claude/rules/post-requirements.md` — 글 타입별 이미지 최소 요건
- `.claude/commands/publish-post.md` — 발행 플로우 (Step 2.5 에 캡쳐 가이드 생성)
- `.claude/agents/post-reviewer.md` — 발행 전 broken image 검증
- `docs/IMAGE_GUIDE.md` — 공통 규격·macOS 캡쳐 단축키 (레거시, 이 파일이 대체)
