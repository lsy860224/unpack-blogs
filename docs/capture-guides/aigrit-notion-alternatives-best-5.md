# Notion 대체 앱 BEST 5 — 스크린샷 캡쳐 가이드

**대상 글:** [aigrit/notion-alternatives-best-5](../../apps/aigrit/content/posts/ko/notion-alternatives-best-5.mdx)
**발행일:** 2026-05-14
**preflight 기준:** AIGrit Pillar — 본문 5장+
**primary_keyword:** Notion 대체 앱
**secondary_keywords:** 노트앱 비교, Obsidian, Craft, Logseq, Anytype, Capacities
**topic_cluster:** 지식관리
**cluster_role:** pillar

## 발행 시점 상태

- 본문 이미지 5장 모두 matplotlib 차트 자동 생성 완료 (#01·#02·#03·#04·#05)
- review-post: PASS 통과 (Pillar 5+ 본문 만족)
- Craft vs Obsidian 에디터 실제 스크린샷(원래 #02 자리)은 추후 보강 권장 — 텍스트로 1문단 대체됨

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Pretendard·AIGrit Indigo+Cyan)
- [x] `01-five-apps-overview.png` — 5개 앱 5박스 한눈 비교 (matplotlib)
- [x] `02-ai-integration-depth.png` — 6개 노트앱 AI 통합도 점수 (matplotlib)
- [x] `03-comparison-matrix.png` — 로컬↔클라우드 × 글쓰기↔DB scatter (matplotlib)
- [x] `04-user-type-decision.png` — 사용자 유형 6 × 앱 6 매트릭스 (matplotlib)
- [x] `05-cluster-positioning.png` — 데이터 소유권 × 협업 scatter (matplotlib)

### [사용자 캡쳐] — 추후 보강 권장 (1장, 선택)

저장 경로 공통: `apps/aigrit/public/images/notion-alternatives-best-5/`

> 실제 스크린샷이 준비되면 `02-ai-integration-depth.png` 옆 또는 Craft 섹션 내부에 새 번호로 추가 (06번 이후 권장 — 기존 차트 번호 재정렬 회피).

- [ ] `06-craft-vs-obsidian-editor.png` — Craft(좌) vs Obsidian(우) 에디터 분할 화면
  - 컨텐츠: 같은 한 문단을 양쪽 앱에 띄운 상태, Craft의 디자인 미려함 + Obsidian의 백링크 그래프 패널 동시 노출
  - 도구: Craft + Obsidian 두 창 나란히 배치
  - 캡쳐 방법: `Cmd+Shift+4` 영역 드래그 (두 창 모두 보이도록)
  - 권장 영역: 가로 1,800~2,000px
  - 민감정보: 본인 vault 이름·노트 제목 마스킹 (Preview 사각형 도구)

## 규격 공통

- 자동 생성 차트: 가로 12~13인치 × 200dpi matplotlib + Pretendard 폰트
- 본문 이미지: 가로 1,600~2,000px PNG (80~200KB)
- 색상 토큰: BG `#0F172A` · Indigo `#3730A3` · Cyan `#06B6D4`

## 생성 스크립트

```bash
# 차트 4장 재생성 시
/Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
  python3 scripts/charts/generate-notion-alternatives-charts.py
```

## 관련

- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian)
- `.claude/rules/post-requirements.md` — Pillar 5+ 이미지 요건
- 같은 cluster 글: `aigrit-obsidian-mcp-plugins-best-5.md`, `aigrit-obsidian-claude-code-mcp.md`
