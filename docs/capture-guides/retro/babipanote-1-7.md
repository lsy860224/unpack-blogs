# babipanote #1~#7 스크린샷 회고 가이드 (2026-04-22)

현재 7편 모두 preflight **PASS** 상태. 자동 생성 다이어그램으로 최소 기준은 만족하지만 빌드로그 특성상 **실사용 스크린샷**이 진정성을 가장 크게 올린다.

## 공통 규격

- 가로 1,600~2,000px PNG
- macOS 캡쳐 단축키 동일
- 저장 경로: `apps/babipanote/public/images/{slug}/`
- **다크/라이트 테마**: babipanote 는 크림 BG 라 라이트 모드가 조화

---

## #1 week1-sprint-two-blogs

**경로:** `apps/babipanote/public/images/week1-sprint-two-blogs/`
**현재 이미지 1장 (PASS 최소):** og

### 추천 추가 캡쳐

- [ ] `02-vercel-dashboard.png` — Vercel 프로젝트 2개 성공 배포
  - **도구:** [vercel.com/dashboard](https://vercel.com/dashboard)
  - **캡쳐 방법:**
    1. Dashboard 접속 → 두 프로젝트(aigrit·babipanote) 카드 보이게 스크롤
    2. "Ready" 상태 확인
    3. 두 카드 영역 + 최근 배포 목록 부분 드래그 캡쳐
  - **민감정보:** 우상단 프로필 아이콘 마스킹

- [ ] `03-commit-graph.png` — GitHub 36시간 commit 집중도
  - **도구:** GitHub 리포 Insights > Commits
  - **캡쳐 방법:** 4월 14~15일 구간의 commit density 차트

---

## #2 building-app-with-claude-code

**경로:** `apps/babipanote/public/images/building-app-with-claude-code/`
**현재 이미지 1장 (PASS 최소):** og

### 추천 추가 캡쳐

- [ ] `02-claude-code-terminal.png` — Claude Code 실제 대화
  - **도구:** Terminal.app / iTerm2 + [Claude Code](https://claude.ai/claude-code)
  - **캡쳐 방법:** Flutter 프로젝트 열고 간단 질문 (예: "이 앱의 아키텍처 요약해줘")
  - **보여야 할 것:** 질문 + 응답 2~3문단 + 참조된 파일 목록
  - **테마:** 다크 권장

- [ ] `03-gentledo-simulator.png` — 완성된 Flutter 앱 스크린샷
  - **도구:** Xcode Simulator 또는 실 기기
  - **컨텐츠:** GentleDo 홈 화면 또는 주요 기능 화면 1~2장

---

## #3 sprint-week1-review

**경로:** `apps/babipanote/public/images/sprint-week1-review/`
**현재 이미지 2장 (PASS):** og, 01-week1-ga4

### 선택 추가 캡쳐 (이미 PASS이므로 선택)

- [ ] `02-work-hours-chart.png` — 주간 작업 시간 수동 기록
  - **도구:** Numbers / Google Sheets
  - **컨텐츠:** 월~금 작업 시간 막대 그래프 (실측 9.5시간 시각화)
  - **또는 자동 생성도 가능** (sharp + 차트 SVG) — 요청 시 Claude 가 렌더

---

## #4 obsidian-seo-dashboard

**경로:** `apps/babipanote/public/images/obsidian-seo-dashboard/`
**현재 이미지 1장 (PASS):** og + 01-dataview-dashboard (이전 세션 캡쳐)

### 추천 추가 캡쳐

- [ ] `02-dataview-cluster.png` — 클러스터 건강도 쿼리 결과
  - **도구:** Obsidian + Dataview 플러그인
  - **캡쳐 방법:**
    1. Dashboard.md 열기 (Live Preview)
    2. "3. 클러스터 건강도" 섹션 스크롤
    3. Dataview 렌더된 테이블 캡쳐
  - **사이드바 숨김**: `Cmd+Option+L/R` 로 양쪽 닫기
  - **테마:** 라이트 권장 (크림 톤과 조화)

- [ ] `03-pipeline-card-example.png` — 실제 Pipeline 카드 frontmatter
  - 예: `10. Pipeline/AIGrit/01-aigrit-claude-code-vs-cursor.md`
  - **속성 패널이 보이는 상태** (frontmatter 확장) 캡쳐

---

## #5 craft-naver-workflow

**경로:** `apps/babipanote/public/images/craft-naver-workflow/`
**현재 이미지 1장 (PASS):** og, 01-craft-to-naver-diagram(auto)

### 추천 추가 캡쳐 (자동 다이어그램 대신 실 Before/After)

- [ ] `02-craft-original.png` — Craft 원본 문서 창 캡쳐
  - **도구:** Craft 앱
  - **컨텐츠:** 테이블·볼드·리스트 포함 샘플 문서
  - **창 단위 캡쳐** (`Cmd+Shift+4` → 스페이스)

- [ ] `03-naver-paste-result.png` — 네이버 스마트에디터 붙여넣기 결과
  - **도구:** [blog.naver.com](https://blog.naver.com) 글쓰기
  - **컨텐츠:** 02 의 Craft 내용을 그대로 붙여넣은 상태 (포맷 유지 확인)
  - **네이버 UI 상단 프로필 영역 마스킹**

> 현재 자동 생성 다이어그램(`01-craft-to-naver-diagram.png`)은 유지. 위 2장은 **추가 배치** 권장 — 실 스크린샷이 글의 신뢰도를 크게 올림.

---

## #6 adsense-prep-checklist

**경로:** `apps/babipanote/public/images/adsense-prep-checklist/`
**현재 이미지 2장 (PASS):** og, 01-required-pages(auto), 02-approval-criteria(auto)

### 추천 추가 캡쳐

- [ ] `03-about-page-real.png` — 실제 About 페이지
  - **도구:** 브라우저 + https://aigrit.dev/ko/about
  - **캡쳐 방법:** 페이지 상단 (프로필 + 운영 원칙)부터 하단까지 2~3 스크롤샷
  - **또는 Full Page Capture** (브라우저 확장)

- [ ] `04-adsense-application.png` — AdSense 신청 첫 화면
  - **도구:** [adsense.google.com](https://adsense.google.com)
  - **신청 직전 상태** (사이트 입력 + "시작하기" 버튼)
  - **민감정보:** 계정 이메일 마스킹

---

## #7 time-management-solo-builder

**경로:** `apps/babipanote/public/images/time-management-solo-builder/`
**현재 이미지 1장 (PASS):** og, 01-time-split-week(auto)

### 선택 추가 캡쳐

- [ ] `02-calendar-week-view.png` — Google Calendar 주간 뷰
  - **도구:** [calendar.google.com](https://calendar.google.com)
  - **캡쳐 방법:** Week 뷰 + 23:00~01:00 작업 블록이 명확한 주
  - **민감정보:** 개인 일정 이름·참석자 마스킹
  - **컬러 코딩** 권장 (본업 회색 · 가족 주황 · 사이드 자주색)

- [ ] `03-burndown-mockup.png` — 하루 에너지 곡선
  - 선택적 인포그래픽 (자동 생성 가능)

---

## 📊 우선순위 요약

| 우선 | 글 | 가장 필요한 캡쳐 | 이유 |
|:---:|---|---|---|
| 🔥 1 | #5 craft-naver | 02-craft-original + 03-naver-result | 글의 핵심 주장(복붙 포맷 유지)의 직접 증거 |
| 🔥 2 | #6 adsense-prep | 04-adsense-application | 승인 신청 과정의 리얼함 |
| ⚡ 3 | #2 building-app-with-claude-code | 02-claude-code-terminal | 바이브 코딩의 증거 |
| ⚡ 4 | #1 week1-sprint-two-blogs | 02-vercel-dashboard | 36시간 스프린트의 증거 |
| 📌 5 | #4 obsidian-seo | 02-dataview-cluster | Dataview 플러그인 실력 증명 |
| 선택 | #3, #7 | 추가 차트/캘린더 | 이미 PASS, 시각 풍부화 |

**준비 완료 시** 기존 경로에 드롭하고 해당 글 MDX에 `<figcaption>` 포함 `![alt](/images/...)` 블록 추가. Claude 가 다음 커밋 때 자동 반영 가능.
