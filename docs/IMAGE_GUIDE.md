# 이미지 보강 가이드 — #1~#7 (2026-04-22 감사 기준)

preflight 기준 달성을 위해 필요한 이미지 목록. **자동 생성(Claude가 처리)** + **사용자 캡쳐 필요** 두 범주로 구분.

## 📁 공통 규격

- **저장 경로**: `apps/{app}/public/images/{slug}/`
- **포맷**: PNG (투명 가능), 손실 없는 압축
- **OG 이미지**: 1200×630 고정
- **본문 이미지**: 가로 1,600~2,000px 권장 (블로그 본문 표시용)
- **모바일 캡쳐**: 1,080~1,290px 리사이즈 (iPhone 15 Pro Max 기준)
- **민감정보 가림**: 이메일·프로필·API 키는 Preview 앱 사각형 도구(검정 채움)로 마스킹

## 📸 캡쳐 기본 단축키 (macOS)

| 단축키 | 용도 |
|---|---|
| `Cmd+Shift+4` | 드래그 영역 캡쳐 (권장) |
| `Cmd+Shift+4` → 스페이스 → 창 클릭 | 창 단위 (그림자 포함) |
| `Cmd+Shift+4` → 스페이스 → `Option` + 창 클릭 | 창 단위 (그림자 제거) |
| `Cmd+Shift+5` | 유틸리티 (타이머·저장위치) |

---

# 🚨 Tier 1 — Broken 이미지 (즉시 필요 2건)

실제 라이브 페이지에 **이미지 깨짐 아이콘 노출 중**. 최우선.

## 1. `notion-ai-guide` — `02-meeting-notes.png`

**경로**: `apps/aigrit/public/images/notion-ai-guide/02-meeting-notes.png`

**컨텐츠**: Notion AI 회의록 자동 요약의 Before/After 2분할

**캡쳐 방법**:
1. Notion 에 테스트 회의록 3~5문단 붙여넣기 (실 회의 말고 샘플)
2. 전체 선택 → AI 메뉴 → Custom prompt
3. 프롬프트: "이 회의록에서 결정사항·액션 아이템·미해결 이슈 추출"
4. 결과가 같은 페이지에 생성된 상태를 **한 화면에 캡쳐**
5. 좌측 사이드바에 개인 vault 이름 노출되지 않게 **사이드바 닫고** 캡쳐

**권장 캡쳐 영역**: 회의록 원본 섹션 + AI 생성 액션 아이템 섹션 2개 모두 보이게

**해상도**: 가로 1,800~2,000px

---

## 2. `craft-naver-workflow` — `01-craft-to-naver-before-after.png`

**경로**: `apps/babipanote/public/images/craft-naver-workflow/01-craft-to-naver-before-after.png`

**컨텐츠**: Craft 원본 vs 네이버 스마트에디터 붙여넣기 결과 좌우 2분할

**캡쳐 방법**:
1. Craft 에 테이블·볼드·리스트 포함 샘플 문서 준비 (10줄 내외면 OK)
2. **좌측**: Craft 에서 해당 문서 열고 전체 영역 캡쳐 (창 단위)
3. **우측**: 네이버 블로그 글쓰기 → Cmd+V 붙여넣기 → 포맷 유지된 상태 캡쳐
4. Preview 앱 또는 Figma 에서 좌우 나란히 배치 → PNG export
5. 중앙에 "→" 화살표 넣어 변환 방향 표시 (선택)

**주의**: 네이버 캡쳐에 글쓰기 UI 상단 메뉴바·프로필 보이지 않게 에디터 본문 영역만

---

# 📸 Tier 2 — 사용자 캡쳐 필요 (실 UI 스크린샷)

Claude 가 만들 수 없는 실제 앱·도구 화면들. 준비되면 이 경로에 PNG 저장.

## 3. `week1-sprint-two-blogs` (babipanote) — Vercel 대시보드

**경로 예시**: `apps/babipanote/public/images/week1-sprint-two-blogs/02-vercel-dashboard.png`

**컨텐츠**: Vercel 프로젝트 2개(aigrit·babipanote) 성공 배포 리스트 + 빌드 로그 일부

**캡쳐 방법**:
1. https://vercel.com/dashboard 접속
2. 두 프로젝트 카드가 나란히 보이는 구간으로 스크롤
3. 최근 배포 "Ready" 상태 확인
4. `Cmd+Shift+4` 로 두 프로젝트 카드 영역 드래그 캡쳐
5. 프로필 아이콘 마스킹

**대안 컨텐츠**: GitHub commit graph (마지막 36시간 commit 밀도 시각화)

---

## 4. `building-app-with-claude-code` (babipanote) — Claude Code 대화

**경로 예시**: `apps/babipanote/public/images/building-app-with-claude-code/02-claude-code-session.png`

**컨텐츠**: Claude Code 터미널에서 실제 Flutter 코드 생성 대화 스냅샷

**캡쳐 방법**:
1. iTerm2 또는 Terminal 에서 Claude Code 실행
2. 프로젝트 루트에서 간단 질문: "이 앱의 구조 요약해줘" 등
3. Claude 응답 받은 시점 스냅샷 (2~3문단 응답 + 프롬프트 포함)
4. 터미널 테마는 다크 (Pro, Homebrew, Solarized Dark 등) 권장

**해상도**: 1,800×1,100 정도 (터미널 창 최대화 후 캡쳐)

---

## 5. `obsidian-seo-dashboard` (babipanote) — Dataview 쿼리 결과 추가

**경로 예시**: `apps/babipanote/public/images/obsidian-seo-dashboard/02-dataview-cluster.png`

**컨텐츠**: 클러스터 건강도 쿼리(`GROUP BY topic_cluster`) 결과 테이블

**캡쳐 방법**:
1. Obsidian `02. Blog SEO/06. Dashboard.md` 열기 (Live Preview)
2. "3. 클러스터 건강도" 섹션으로 스크롤
3. Dataview 쿼리 결과 테이블이 렌더된 상태 캡쳐
4. 좌우 사이드바 숨김 권장

**이미지 3장까지 늘리면 좋은 쿼리들**:
- 상태별 글 수
- 클러스터 건강도
- 네이버 에디션 후보 리스트

---

## 6. `adsense-prep-checklist` (babipanote) — 본문 이미지 (현재 0장)

**경로 예시**: `apps/babipanote/public/images/adsense-prep-checklist/01-required-pages.png`

**Option A — 실 About/Privacy 페이지 캡쳐**:
1. https://aigrit.dev/ko/about 접속
2. About 페이지 상단 부분 캡쳐 (프로필·운영원칙까지)
3. 2x2 그리드로 About/Privacy/Disclaimer/Contact 4장 합성

**Option B — Claude가 자동 생성 가능 (택 1 가능)**:
- 필수 페이지 4개 아이콘 보드 인포그래픽 → **자동 생성해 드릴 예정** (아래 Tier 3 참조)

---

## 7. `apple-shortcuts-ai-automation` (AIGrit) — `04-shortcut-voice-notion.png`

**경로**: `apps/aigrit/public/images/apple-shortcuts-ai-automation/04-shortcut-voice-notion.png`

**컨텐츠**: 음성 → Whisper → Notion 단축어 실행 결과

**캡쳐 방법**: 세션 이전 대화에서 상세 가이드 제공됨. 3분할 몽타주 or 단일 Notion DB 방금 들어온 항목.

**또는 스킵** — 이전에 사용자가 "04번 사진 빼고" 라고 했으므로 해당 섹션 텍스트 유지하고 이미지 마커만 삭제하는 옵션 있음.

---

## 8. `time-management-solo-builder` (babipanote) — 선택

**경로 예시**: `apps/babipanote/public/images/time-management-solo-builder/02-calendar-routine.png`

**컨텐츠**: 주간 캘린더 뷰 (Google Calendar 색상별 블록)

**캡쳐 방법**: Google Calendar Week 뷰에서 평일 23:00~01:00 블록이 명확히 보이는 주 캡쳐. 개인 일정은 "Personal" 로 모자이크.

**우선도: 낮음 (WARN 만 해결)**

---

# 🎨 Tier 3 — Claude 자동 생성 (사용자 작업 없음)

아래 이미지들은 Claude가 SVG→PNG 변환으로 **자동 생성합니다**. 사용자는 아무 작업 없음.

## AIGrit 추가 생성 예정 (현재 turn 즉시 실행)

| 파일 | 글 | 컨텐츠 |
|---|---|---|
| `claude-code-vs-cursor/02-workflow-comparison.png` | AIGrit #1 | CLI vs IDE 워크플로우 2분할 다이어그램 |
| `claude-code-vs-cursor/03-use-case-matrix.png` | AIGrit #1 | 5가지 시나리오별 승자 매트릭스 |
| `claude-4-sonnet-vs-gpt-4o/02-benchmark-chart.png` | AIGrit #2 | 5개 태스크 그룹드 바 차트 |
| `claude-4-sonnet-vs-gpt-4o/03-cost-timeline.png` | AIGrit #2 | 토큰 비용·응답 속도 scatter |
| `perplexity-ai-guide/04-pro-vs-free.png` | AIGrit #4 | 기능별 체크리스트 인포그래픽 |
| `solo-developer-automation-stack/02-stack-cost-breakdown.png` | AIGrit #5 Pillar | 월 비용 도넛 차트 |
| `solo-developer-automation-stack/03-tool-categories.png` | AIGrit #5 Pillar | 4카테고리 아이콘 보드 |
| `solo-developer-automation-stack/04-roi-time-saved.png` | AIGrit #5 Pillar | 도구별 시간 절약 수평 바 |
| `solo-developer-automation-stack/05-adoption-order.png` | AIGrit #5 Pillar | 10단계 도입 순서 플로우 |
| `notion-ai-guide/03-use-cases-infographic.png` | AIGrit #6 | 5가지 용도 아이콘 인포그래픽 |
| `craft-vs-notion/02-role-separation.png` | AIGrit #7 | 역할 분리 3-column (Craft·Obsidian·Notion) |
| `craft-vs-notion/03-price-platform.png` | AIGrit #7 | 가격·플랫폼 비교 표 시각화 |

## babipanote 추가 생성 예정

| 파일 | 글 | 컨텐츠 |
|---|---|---|
| `adsense-prep-checklist/01-required-pages.png` | babipanote #6 | 4개 필수 페이지 아이콘 보드 |
| `adsense-prep-checklist/02-approval-criteria.png` | babipanote #6 | 승인 실측 기준 체크리스트 |

---

# 📋 체크리스트 요약

**사용자가 해야 할 작업 (우선순위 순):**

- [ ] 🚨 `apps/aigrit/public/images/notion-ai-guide/02-meeting-notes.png` — Notion 회의록 Before/After
- [ ] 🚨 `apps/babipanote/public/images/craft-naver-workflow/01-craft-to-naver-before-after.png` — Craft/네이버 비교
- [ ] `apps/babipanote/public/images/week1-sprint-two-blogs/02-vercel-dashboard.png` — Vercel 대시보드
- [ ] `apps/babipanote/public/images/building-app-with-claude-code/02-claude-code-session.png` — Claude Code 터미널
- [ ] `apps/babipanote/public/images/obsidian-seo-dashboard/02-dataview-cluster.png` — 추가 Dataview
- [ ] `apps/aigrit/public/images/apple-shortcuts-ai-automation/04-shortcut-voice-notion.png` — 선택
- [ ] `apps/babipanote/public/images/time-management-solo-builder/02-calendar-routine.png` — 선택 (WARN 해소)

**Claude가 즉시 처리:**

- ✅ Tier 3 자동 생성 14장 (아래 turn에서 렌더)
- ✅ FAQ 섹션 신설 (AIGrit #1, #2)
- ✅ 내부 링크 일괄 보강 (9개 글)
- ✅ 외부 링크 일괄 보강 (7개 글)

## 💡 캡쳐 팁 — 공통 권장

1. **브라우저/앱 줌 100%** (`Cmd+0`) 로 맞춘 뒤 캡쳐
2. **시크릿 창**으로 개인정보 노출 최소화
3. **다크모드 통일** — AIGrit은 다크, babipanote는 라이트 테마가 조화
4. **캡쳐 후 Preview 앱에서 불필요 여백 crop**
5. 파일명은 위 표의 **정확한 이름** 사용 (MDX 참조와 매칭)

---

이미지 준비 중 막히면 특정 경로·파일명 알려주세요. 합성·리사이즈·검증 지원 가능.
