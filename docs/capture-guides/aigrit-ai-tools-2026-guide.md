# 2026 AI 도구 완벽 가이드 — 스크린샷 캡쳐 가이드

**대상 글:** [apps/aigrit/content/posts/ko/ai-tools-2026-guide.mdx](../../apps/aigrit/content/posts/ko/ai-tools-2026-guide.mdx)
**발행 예정일:** 2026-04-22 22:00
**타입:** AIGrit **Pillar** (AI 도구 비교)
**preflight 기준:** 본문 이미지 5+장, FAQ 5~8, 내부 링크 10~15, 3,500자+

## 이미지 목록 (총 5장)

### [자동 생성 필요] — Claude 렌더 / Figma

#### `og.png` — OG 썸네일 1200×630
- **경로:** `apps/aigrit/public/images/ai-tools-2026-guide/og.png`
- **디자인:** AIGrit Indigo(#3730A3) + Cyan(#06B6D4) 그라디언트
- **카피:** "2026 AI 도구 완벽 가이드 — 20개 써보고 살아남은 10개"
- **생성 방법:** Figma MCP 또는 `docs/THUMBNAIL.md` 템플릿

#### `01-chatbot-comparison.png` — 챗봇 3대장 실사용 비교 (1600×900)
- **경로:** `apps/aigrit/public/images/ai-tools-2026-guide/01-chatbot-comparison.png`
- **구성:** Claude · ChatGPT · Gemini 로고 + "한국어 자연스러움 점수" 바 차트
- **생성 방법:** Figma 또는 Napkin AI 다이어그램 (`mcp__napkin-ai__generate_and_save`)

#### `02-coding-tools-workflow.png` — Claude Code + Cursor 듀얼 스크린 (1600×900)
- **경로:** `apps/aigrit/public/images/ai-tools-2026-guide/02-coding-tools-workflow.png`
- **구성:** 왼쪽 터미널(Claude Code) + 오른쪽 IDE(Cursor) 병렬 스크린샷 합성
- **생성 방법:** Figma 2-pane 합성

#### `03-automation-stack.png` — 자동화 스택 다이어그램 (1600×900)
- **경로:** `apps/aigrit/public/images/ai-tools-2026-guide/03-automation-stack.png`
- **구성:** Notion AI / Apple 단축어 / Claude MCP 3 레이어 일러스트
- **생성 방법:** Napkin AI 시스템 다이어그램

#### `04-failed-tools.png` — 버린 AI 도구 5개 일러스트 (1600×900)
- **경로:** `apps/aigrit/public/images/ai-tools-2026-guide/04-failed-tools.png`
- **구성:** Jasper / Copy.ai / Grammarly Premium / Quillbot / Rytr 로고 회색 스케일
- **생성 방법:** Figma 로고 그리드 (스트라이크스루 처리)

### [사용자 캡쳐 필요]
해당 없음 — Pillar 글은 범용 그래픽 중심이라 실제 앱 스크린샷은 각 Cluster 글에서 처리.

## 규격 공통

- PNG/WebP, 가로 1,600px 권장 (최대 1,600px로 리샘플)
- 파일당 300KB 이하 (OG는 200KB 이하)
- `sips --resampleHeightWidthMax 1600 file.png --out file.png`

## Pillar 특수 체크

- [ ] `featured: true` 설정 확인 (frontmatter에 이미 반영됨)
- [ ] FAQ 7개 (5~8 범위) — ✅ 본문에 포함
- [ ] 내부 링크 10개 (최소 10) — ✅ 포함 (claude-4-sonnet-vs-gpt-4o, perplexity-ai-guide, claude-code-vs-cursor, babipanote building-app-with-claude-code, notion-ai-guide, apple-shortcuts-ai-automation, claude-mcp-guide, solo-developer-automation-stack, craft-vs-notion, babipanote aigrit-month1-revenue)
- [ ] 외부 링크 3개 — ✅ anthropic.com, openai.com, deepmind.google
- [ ] 분기 1회 갱신 일정 Obsidian Pipeline 카드에 반영

## 준비 상태

- [ ] 자동 생성 5장 (og + 01~04) — Figma/Napkin MCP로 생성 필요
- [ ] 생성 후 `apps/aigrit/public/images/ai-tools-2026-guide/` 폴더에 드롭

**캡쳐/생성 완료 후**: 해당 경로에 PNG 드롭 → 다음 커밋 시 자동 반영. MDX는 이미 참조 경로를 포함하고 있어 수정 불필요.
