# AIGrit #1~#7 스크린샷 회고 가이드 (2026-04-22)

현재 7편 모두 preflight **PASS** 상태지만, 실제 앱 UI 스크린샷을 추가하면 **E-E-A-T·진정성이 크게 올라간다**. 자동 생성 다이어그램으로 채운 슬롯을 실 스크린샷으로 교체하거나 추가 배치 권장.

## 공통 규격

- 가로 1,600~2,000px PNG
- macOS `Cmd+Shift+4` 드래그 / 창 캡쳐는 `Cmd+Shift+4` → 스페이스 → 창 클릭
- 시크릿 창 권장 (북마크바·프로필 노출 방지)
- Preview 앱 사각형 도구로 이메일·프로필 마스킹
- 저장 경로: `apps/aigrit/public/images/{slug}/`

---

## #1 claude-code-vs-cursor

**경로:** `apps/aigrit/public/images/claude-code-vs-cursor/`
**현재 이미지 3장 (PASS):** og, 02-workflow-comparison(auto), 03-use-case-matrix(auto), scenarios-comparison(legacy)

### 추천 추가 캡쳐

- [ ] `04-claude-code-session.png` — Claude Code 터미널 실제 대화
  - **도구:** iTerm2 또는 Terminal.app + [Claude Code](https://claude.ai/claude-code)
  - **캡쳐 방법:** 빈 프로젝트 폴더에서 간단 질문 (예: "이 레포의 구조 요약해줘")
  - **보여야 할 것:** 프롬프트 + 응답 2~3문단 + 파일 목록
  - **테마:** 다크 (Homebrew/Pro 계열)
  - **해상도:** 1,800×1,100 (터미널 최대화 후 캡쳐)

- [ ] `05-cursor-composer.png` — Cursor Composer 창
  - **도구:** [Cursor](https://cursor.com)
  - **캡쳐 방법:** `Cmd+I` Composer 열기 → 샘플 파일 생성 요청
  - **보여야 할 것:** Composer 패널 + 대기 중인 diff
  - **민감정보:** 왼쪽 파일 트리에 개인 프로젝트명 노출되면 마스킹

---

## #2 claude-4-sonnet-vs-gpt-4o

**경로:** `apps/aigrit/public/images/claude-4-sonnet-vs-gpt-4o/`
**현재 이미지 3장:** og, 02-benchmark-chart(auto), 03-cost-timeline(auto), score-comparison(legacy)

### 추천 추가 캡쳐

- [ ] `04-claude-kr-output.png` — Claude.ai 한국어 결과
  - **도구:** [claude.ai](https://claude.ai)
  - **캡쳐 방법:** 기사의 태스크 1(한국어 글쓰기) 프롬프트 복붙 → 결과 캡쳐
  - **영역:** 프롬프트 + 응답 첫 문단까지
  - **민감정보:** 좌측 사이드바 과거 대화 히스토리 마스킹

- [ ] `05-gpt4o-kr-output.png` — ChatGPT 동일 프롬프트 결과
  - **도구:** [chat.openai.com](https://chat.openai.com)
  - **동일 프롬프트** 입력 → 결과 캡쳐 (비교 짝)
  - **두 이미지를 Preview 또는 Figma 로 2분할 합성**해도 좋음

---

## #3 apple-shortcuts-ai-automation

**경로:** `apps/aigrit/public/images/apple-shortcuts-ai-automation/`
**현재 이미지 5장 (PASS 최고):** og, 01-api-flow, 02-summarize, 03-screenshot-ai, 05-translate, 06-calendar

### 선택 추가 캡쳐

- [ ] `04-shortcut-voice-notion.png` — 음성→Whisper→Notion 단축어 (이전에 사용자 보류)
  - **컨텐츠:** 3-분할 몽타주 (녹음 중 / 완료 알림 / Notion DB 신규 항목)
  - **또는 단일:** Notion DB 에 방금 들어온 항목 상세 뷰
  - **이전 세션 안내 참조**: 음성 녹음 → Whisper 변환 → Notion Pages API 체인

---

## #4 perplexity-ai-guide

**경로:** `apps/aigrit/public/images/perplexity-ai-guide/`
**현재 이미지 4장 (PASS):** og, 01-google-vs-perplexity, 02-perplexity-free-search, 03-usage-log-chart, 04-pro-vs-free(auto)

### 추천 추가 캡쳐

- [ ] `05-perplexity-spaces.png` — Pro 전용 Spaces 기능
  - **도구:** [perplexity.ai](https://www.perplexity.ai) Pro 계정 (무료 체험 가능)
  - **캡쳐 방법:** Spaces 탭 → 새 Space 생성 화면
  - **보여야 할 것:** Space 이름·설명·파일 업로드 영역

- [ ] `06-source-citations.png` — 출처 번호 상세 패널
  - 답변에서 `¹` 번호 클릭 시 나오는 출처 미리보기 팝업
  - 이 기능이 차별점이므로 강조 가치 높음

---

## #5 solo-developer-automation-stack (Pillar)

**경로:** `apps/aigrit/public/images/solo-developer-automation-stack/`
**현재 이미지 5장 (PASS 최고):** og, 02~05 auto charts, 07-daily-automation-flow

### 선택 추가 캡쳐

- [ ] `06-claude-max-billing.png` — Claude Max 플랜 결제 화면
  - **도구:** [console.anthropic.com](https://console.anthropic.com)
  - 월 $20 플랜 명세 캡쳐 + 사용량 그래프 (비용 투명성 보강)
  - **민감정보:** 결제 정보·계정 ID 마스킹

- [ ] `08-tool-stack-overview.png` — 실제 Mac 에 설치된 10개 도구 앱 아이콘 전체
  - **도구:** Dock 또는 Launchpad 캡쳐
  - **컨텐츠:** Apple Shortcuts, Claude Code, Cursor, Obsidian, Craft, VSCode 등 아이콘이 한 화면에

---

## #6 notion-ai-guide

**경로:** `apps/aigrit/public/images/notion-ai-guide/`
**현재 이미지 3장 (PASS):** og, 01-notion-ai-vs-chatgpt(auto), 03-use-cases-infographic(auto), 04-pricing-scenarios(auto)

### 추천 추가 캡쳐 (broken 참조는 이미 제거됨)

- [ ] `02-meeting-notes.png` — 실제 Notion AI 회의록 요약 Before/After
  - **도구:** [notion.so](https://www.notion.so) + AI 기능
  - **캡쳐 방법:**
    1. Notion에 샘플 회의록 3~5문단 붙여넣기
    2. 전체 선택 → `Space` 키 → AI 메뉴 → Custom prompt
    3. 프롬프트: "결정사항·액션 아이템·미해결 이슈 추출"
    4. 결과가 생성된 상태 캡쳐
  - **사이드바 닫고** 본문 영역만 캡쳐
  - **민감정보:** vault 경로·프로필 마스킹

- [ ] `05-db-query-demo.png` — DB 자연어 쿼리 실행 결과
  - Notion Task DB 에서 "이번 주 마감" 쿼리 AI 자동 필터 적용 화면

---

## #7 craft-vs-notion

**경로:** `apps/aigrit/public/images/craft-vs-notion/`
**현재 이미지 3장 (PASS):** og, 01-ui(legacy/mockup), 02-role-separation(auto), 03-price-platform(auto)

### 추천 추가 캡쳐

- [ ] `04-craft-editor-real.png` — 실제 Craft 에디터 글쓰기 화면
  - **도구:** Craft 앱 (macOS)
  - **컨텐츠:** 빈 페이지 + 커서 + 블록 메뉴 오픈 상태 (기능성 강조)
  - **창 크기:** 가로 1,600~1,800

- [ ] `05-notion-db-real.png` — 실제 Notion 관계형 DB 뷰
  - **도구:** notion.so
  - **컨텐츠:** 다중 속성 DB 테이블 뷰 (예: 블로그 글 DB)
  - **민감정보:** 개인 워크스페이스 이름 · 이메일 마스킹

> 01-ui 는 목업 다이어그램이라 실 스크린샷으로 교체하면 진정성 한 단계 상승. 기존 파일은 유지하거나 `01-craft-vs-notion-ui-mockup.png` 으로 리네임 가능.

---

## 📊 우선순위 요약

| 우선 | 글 | 가장 필요한 캡쳐 | 이유 |
|:---:|---|---|---|
| 🔥 1 | #6 notion-ai | 02-meeting-notes | 원래 참조됐던 이미지, 실 스크린샷이 글의 핵심 예시 |
| 🔥 2 | #1 claude-code-vs-cursor | 04-claude-code-session | CLI 도구의 실사용 증거 (E-E-A-T) |
| ⚡ 3 | #2 claude-4-sonnet-vs-gpt-4o | 04/05 두 모델 결과 Before/After | 비교 주장의 증거 |
| ⚡ 4 | #7 craft-vs-notion | 04·05 실 앱 UI | 현재 목업이라 진정성 보강 |
| 📌 5 | #4 perplexity | 05-spaces, 06-citations | Pro 기능 강조 |
| 📌 6 | #5 Pillar | 08-tool-stack-overview | 스택 전체 가시화 |
| 선택 | #3 apple-shortcuts | 04-voice-notion | 이전에 보류했던 유일한 이미지 |

**완료된 자동 생성은 유지**. 위 캡쳐들은 **추가**·**선택적 교체** 용도. 준비되면 기존 경로에 드롭하고 커밋만 하면 다음 배포에 반영.
