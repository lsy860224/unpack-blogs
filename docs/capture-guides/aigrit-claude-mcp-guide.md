# Claude MCP 활용법 — 스크린샷 캡쳐 가이드

**대상 글:** [apps/aigrit/content/posts/ko/claude-mcp-guide.mdx](../../apps/aigrit/content/posts/ko/claude-mcp-guide.mdx)
**발행 예정일:** 2026-04-22 16:30
**타입:** AIGrit Cluster (AI 코딩)
**preflight 기준:** 본문 이미지 3~5장, FAQ 3+, 내부 링크 5~7

## 이미지 목록

### [자동 생성 완료] — Claude 렌더
- [x] `og.png` — OG 썸네일 1200×630 (Indigo/Cyan)
- [x] `01-mcp-architecture.png` — Claude Client ↔ MCP Server ↔ 외부 도구 아키텍처 다이어그램 (1600×900)

### [사용자 캡쳐 필요]

#### `02-obsidian-mcp-demo.png` — Claude Desktop + Obsidian MCP 대화

- **경로**: `apps/aigrit/public/images/claude-mcp-guide/02-obsidian-mcp-demo.png`
- **도구**: [Claude Desktop](https://claude.ai/download) + Obsidian MCP 서버 연결
- **캡쳐 방법**:
  1. Claude Desktop 설정에서 Obsidian MCP 등록 (이 프로젝트에 이미 구성됨)
  2. 새 대화 시작 → "Obsidian 에서 `02. Blog SEO/10. Pipeline/AIGrit` 폴더 목록 보여줘" 입력
  3. Claude 가 MCP 로 실제 파일 읽어 응답하는 순간 캡쳐
  4. 프롬프트 + 응답 + 도구 호출 상태까지 한 화면에
- **권장 영역**: 대화창 전체 (가로 1,600~1,800)
- **민감정보**: 좌측 사이드바 과거 대화 히스토리 마스킹, 프로필 아이콘 가리기
- **테마**: 다크 권장 (AIGrit 브랜드 조화)

#### `03-craft-mcp-demo.png` — Claude → Craft 문서 자동 생성

- **경로**: `apps/aigrit/public/images/claude-mcp-guide/03-craft-mcp-demo.png`
- **도구**: Claude Desktop + Craft MCP (이 프로젝트 구성됨) + Craft 앱
- **캡쳐 방법**:
  1. Claude Desktop 에서 "Craft 에 '테스트 초안' 제목 문서 만들어줘" 실행
  2. Craft 앱에서 해당 문서가 실제로 생성된 화면 확인
  3. **2-분할 합성** (Preview 앱 또는 Figma):
     - 좌: Claude Desktop 대화 (도구 호출 결과)
     - 우: Craft 앱 새 문서 화면
- **권장 영역**: 합성 후 가로 1,800~2,000
- **민감정보**: Craft Space 이름 · 계정 이메일 마스킹

## 규격 공통

- PNG, 가로 1,600~2,000px
- `Cmd+Shift+4` → 스페이스 → 창 클릭 (그림자 포함 창 캡쳐)
- `Option + 창 클릭` 으로 그림자 제거 옵션
- Preview.app 사각형 도구로 민감정보 마스킹

## Obsidian Pipeline 메타

- **primary_keyword:** `claude mcp 사용법`
- **secondary_keywords:** mcp 서버, claude desktop mcp, model context protocol
- **featured_snippet_target:** list (스택 비교 테이블 + 우선순위 리스트)
- **internal_links_planned:** `solo-developer-automation-stack` (Pillar), `claude-code-vs-cursor`, `obsidian-seo-dashboard` (cross-site), `craft-vs-notion`, `notion-ai-guide`, `apple-shortcuts-ai-automation`

## 준비 상태

- [x] 자동 생성 2장
- [ ] 사용자 캡쳐 2장 (02, 03) — 준비되면 경로에 드롭

**캡쳐 완료 후**: 해당 경로에 PNG 드롭 → 다음 커밋 시 자동 반영. MDX는 이미 참조 경로를 포함하고 있어서 추가 수정 불필요.
