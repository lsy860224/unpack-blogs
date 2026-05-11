# Obsidian MCP 플러그인 추천 BEST 5 — 스크린샷 캡쳐 가이드

**대상 글:** [aigrit/obsidian-mcp-plugins-best-5](../../apps/aigrit/content/posts/ko/obsidian-mcp-plugins-best-5.mdx)
**발행일:** 2026-05-11
**preflight 기준:** AIGrit Cluster — 본문 3~5장
**primary_keyword:** Obsidian MCP 플러그인 추천
**secondary_keywords:** Obsidian MCP, Model Context Protocol, Obsidian 자동화, Claude Desktop Obsidian
**topic_cluster:** 지식관리

## 발행 시점 상태

- 본문 이미지 마커 **4개 모두 제거** 후 발행 (이미지 흐름은 1~2문장 텍스트 보강으로 대체)
- review-post: WARN (이미지 0장 — 사용자 결정 사항으로 인지)
- 추후 캡쳐 완료 시 본문에 다시 삽입하고 보강 commit 예정

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Pretendard·AIGrit Indigo+Cyan, `scripts/og/generate-og-all.py`)

### [사용자 캡쳐] — 추후 보강 필요 (4장, 현재 본문에서 마커 제거됨)

저장 경로 공통: `apps/aigrit/public/images/obsidian-mcp-plugins-best-5/`

- [ ] `01-mcp-overview.png` — MCP 아키텍처 한눈
  - 컨텐츠: Obsidian vault ↔ MCP server ↔ Claude Desktop 3단 흐름 다이어그램
  - 도구: **NapkinAI** (https://app.napkin.ai/) `visual_query=mindmap` 또는 **Figma Master** Indigo+Cyan 박스
  - 권장 영역: 좌(Obsidian) — 중(MCP server protocol) — 우(Claude Desktop). 화살표 양방향
  - 민감정보: 없음

- [ ] `02-plugin-list.png` — Obsidian Community Plugins 검색 결과
  - 컨텐츠: Obsidian Settings → Community plugins → "mcp" 검색 결과 상위 5개
  - 도구: Obsidian Desktop (https://obsidian.md/download)
  - 캡쳐 방법: `Cmd+Shift+4` 드래그 (검색창 + 상위 5개 결과 카드 영역만)
  - 권장 영역: 1,600~2,000px 가로
  - 민감정보: vault 이름 노출 가능 — Preview 사각형 도구로 마스킹

- [ ] `03-claude-mcp-config.png` — Claude Desktop MCP 설정 화면
  - 컨텐츠: Claude Desktop Settings → Developer → MCP Configuration 패널 (연결된 servers 목록 + 상태 표시)
  - 도구: Claude Desktop (https://claude.ai/download)
  - 캡쳐 방법: 설정 창 활성화 후 `Cmd+Shift+4` → 스페이스 → 창 클릭 (창 전체)
  - 권장 영역: 창 전체 (1,200~1,400px)
  - 민감정보: API key·계정 이름 마스킹 필수 (Preview 사각형 도구)

- [ ] `04-vault-sync-demo.png` — Claude에서 vault 검색 → 자동 노트 생성 데모
  - 컨텐츠: Claude Desktop 대화창 (vault 노트 검색 결과 + 자동 생성된 새 노트 미리보기 분할)
  - 도구: Claude Desktop + Obsidian 함께
  - 캡쳐 방법: 두 창 나란히 배치 → `Cmd+Shift+4` 영역 드래그
  - 권장 영역: 1,800~2,000px 가로 (두 창 모두 보이도록)
  - 민감정보: 대화 내용·노트 제목 일부 마스킹

## 규격 공통

- 본문 이미지: 가로 1,600~2,000px PNG (80~200KB)
- macOS 캡쳐: `Cmd+Shift+4` 드래그 / `Cmd+Shift+4` → 스페이스 → 창 클릭
- 마스킹: Preview 앱 도구 → 사각형 채우기 (배경색 일치)
- 저장 후 `obsidian-mcp-plugins-best-5.mdx`에 다시 마커 삽입 → `/review-post` → commit

## 후속 commit 패턴

```bash
# 캡쳐 4장 저장 후
git add apps/aigrit/public/images/obsidian-mcp-plugins-best-5/
# 본문 MDX에 다시 마커 추가 (4개)
git add apps/aigrit/content/posts/ko/obsidian-mcp-plugins-best-5.mdx
git commit -m "post(aigrit): obsidian-mcp-plugins-best-5 본문 이미지 4장 보강"
./scripts/publish-via-pr.sh "post(aigrit): obsidian-mcp-plugins-best-5 이미지 보강"
```

## 관련

- `.claude/rules/post-requirements.md` — 글 타입별 이미지 최소 요건
- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian) — 캡쳐 도구 비교·NapkinAI 대체 옵션
