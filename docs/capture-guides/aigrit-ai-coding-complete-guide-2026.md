# AI 코딩 완벽 가이드 2026 (Pillar) — 스크린샷 캡쳐 가이드

**대상 글:** [aigrit/ai-coding-complete-guide-2026](../../apps/aigrit/content/posts/ko/ai-coding-complete-guide-2026.mdx)
**발행일:** 2026-05-19
**preflight 기준:** AIGrit Pillar — 본문 5장+
**primary_keyword:** AI 코딩
**secondary_keywords:** Claude Code, Cursor, MCP, AI 페어 프로그래밍, 1인 빌더
**topic_cluster:** AI 코딩
**cluster_role:** pillar
**보조 cluster 글:** claude-code-flutter-app-guide · claude-mcp-guide · obsidian-claude-code-mcp · claude-code-vs-cursor

## 발행 시점 상태

- 본문 이미지 5장 모두 matplotlib 자동 생성 완료 + OG 1장
- review-post: 중복 링크 모두 fix 후 PASS 예정

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Pretendard·AIGrit Indigo+Cyan)
- [x] `01-tools-matrix.png` — 4-quadrant 도구 매트릭스 (matplotlib)
- [x] `02-cli-vs-ide.png` — Claude Code vs Cursor 시나리오 시간 비교 (matplotlib)
- [x] `03-mcp-layers.png` — MCP 3단 레이어 박스 다이어그램 (matplotlib)
- [x] `04-workflow-6steps.png` — 6단계 워크플로우 박스 (matplotlib)
- [x] `05-cost-productivity.png` — 비용·생산성 scatter (matplotlib)

### [사용자 캡쳐] — 추후 보강 권장 (선택)

저장 경로: `apps/aigrit/public/images/ai-coding-complete-guide-2026/`

- [ ] `06-claude-code-cli-demo.png` — Claude Code 실행 화면 (다중 파일 동시 생성 demo)
  - 도구: macOS Terminal + `claude` 실행
  - 캡쳐 방법: `Cmd+Shift+4` 영역
  - 민감정보: API key·계정 이메일 마스킹

## 생성 스크립트

```bash
/Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
  python3 scripts/charts/generate-ai-coding-pillar-charts.py
```

## 관련

- 같은 cluster: `claude-code-flutter-app-guide.mdx`·`claude-mcp-guide.mdx`·`obsidian-claude-code-mcp.mdx`
- `.claude/rules/post-requirements.md` — Pillar 5+ 이미지 + 10~15 내부 링크 요건
