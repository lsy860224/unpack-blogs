# Obsidian × Claude Code MCP 연결 — 스크린샷 캡쳐 가이드

**대상 글:** [aigrit/obsidian-claude-code-mcp](../../apps/aigrit/content/posts/ko/obsidian-claude-code-mcp.mdx)
**발행일:** 2026-05-13
**preflight 기준:** AIGrit Cluster — 본문 3~5장
**primary_keyword:** Obsidian Claude Code MCP
**secondary_keywords:** Claude Code Obsidian 연결, MCP 자동화, 노트와 코드 양방향 동기화
**topic_cluster:** AI 코딩

## 발행 시점 상태

- 본문 이미지 마커 **4개 모두 제거** 후 발행 (#14·#15와 동일 패턴, 흐름 1~2문장 텍스트 보강)
- review-post: WARN (이미지 0장 — 사용자 결정 사항)
- 추후 캡쳐 완료 시 본문에 다시 삽입하고 보강 commit 예정

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Pretendard·AIGrit Indigo+Cyan, `scripts/og/generate-og-all.py`)

### [사용자 캡쳐] — 추후 보강 필요 (4장)

저장 경로 공통: `apps/aigrit/public/images/obsidian-claude-code-mcp/`

- [ ] `01-architecture.png` — Obsidian↔MCP↔Claude Code 양방향 흐름 다이어그램
  - 컨텐츠: 노트(Obsidian vault) — MCP server (양방향) — Claude Code 흐름, 화살표 양방향
  - 도구: **NapkinAI** (https://app.napkin.ai/) `visual_query=flowchart` 또는 Figma Master Indigo+Cyan 박스
  - 권장 영역: 1,600~2,000px 가로
  - 민감정보: 없음

- [ ] `02-config-example.png` — `.mcp.json` 설정 화면
  - 컨텐츠: `claude_desktop_config.json` (또는 `.mcp.json`) 안에 Obsidian MCP server + Claude Code MCP server 두 항목 정의
  - 도구: macOS Terminal + bat/cat 표시 또는 **Carbon** (https://carbon.now.sh) 코드 스크린샷
  - 캡쳐 방법: 코드 한 화면 + 다크 테마
  - 민감정보: API key·token 마스킹 필수

- [ ] `03-vault-edit-demo.png` — spec.md → page.tsx 자동 생성 데모
  - 컨텐츠: 좌(Obsidian 기획 노트 `spec.md`) → 우(자동 생성된 `page.tsx`) 분할 뷰
  - 도구: Obsidian + VS Code(또는 Claude Code CLI) 나란히
  - 캡쳐 방법: `Cmd+Shift+4` 영역 드래그 (두 창 모두 보이도록)
  - 민감정보: 대화 내용·파일 경로 일부 마스킹

- [ ] `04-multi-agent-workflow.png` — 멀티 에이전트 vault·코드·로그 동시 갱신 흐름
  - 컨텐츠: 한 명령 → 1) vault 노트 업데이트 2) 코드 트리 수정 3) 로그/회고 파일 추가 — 동시 진행 다이어그램
  - 도구: NapkinAI 또는 Figma
  - 권장 영역: 1,600~2,000px 가로
  - 민감정보: 없음

## 규격 공통

- 본문 이미지: 가로 1,600~2,000px PNG (80~200KB)
- macOS 캡쳐: `Cmd+Shift+4` 드래그 / `Cmd+Shift+4` → 스페이스 → 창 클릭
- 마스킹: Preview 앱 사각형 도구

## 관련

- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian) — 도구 비교
- `docs/capture-guides/aigrit-obsidian-mcp-plugins-best-5.md` — 같은 cluster 글 (지식관리 ↔ AI 코딩)
