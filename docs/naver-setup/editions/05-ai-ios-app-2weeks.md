# 🧾 네이버 에디션 #5 — 퇴근 후 2주, Claude Code로 iOS 앱 만든 후기

> **네이버 복붙용 초안.** "── 제목 ──" 이하만 네이버 스마트에디터에 복사하세요.
> GentleDo 시리즈 **2/3** — #4 네이밍 → **#5 개발기(이 글)** → #6 심사 통과기.

---

## 📋 발행 메타

| 항목 | 값 |
|---|---|
| **원본 1 (감성 일기)** | https://babipanote.com/blog/building-gentledo-with-claude-code |
| **원본 2 (기술 가이드)** | https://aigrit.dev/ko/blog/claude-code-flutter-app-guide |
| **카테고리** | AI 도구 리뷰 (또는 부업 탐구) |
| **제목** | 퇴근 후 2주, Claude Code로 iOS 앱 만든 후기 (25자) |
| **시리즈** | GentleDo 시리즈 2/3 |
| **대표 이미지** | `docs/naver-setup/editions/images/05-gentledo-dev/00-thumb-square.png` (1080×1080) |
| **태그 (8개)** | `GentleDo, ClaudeCode, 바이브코딩, 비개발자앱개발, Flutter, 1인개발, AI앱개발, 직장인부업` |
| **발행 일자** | **2026-04-29 (발행 완료)** |
| **발행 URL** | https://blog.naver.com/aigrit/224269781667 |
| **logNo** | 224269781667 |
| **Craft 본문 ID** | `9cd567fe-8210-59a8-86a7-2d7f61b4acfa` |

---

## 🎨 이미지 9장 + 정사각 썸네일 배치 플랜

| 순서 | 파일 | 용도 |
|:---:|---|---|
| (대표) | `00-thumb-square.png` | 1080×1080 — 톱니바퀴 → 대표 이미지 등록 |
| 1 | `01-cover.png` | 본문 도입 커버 |
| 2 | `02-stack-decision.png` | 기술 스택 + 3가지 제약 |
| 3 | `03-vibe-coding-balance.png` | 사람 vs AI 역할 분담 |
| 4 | `04-2week-timeline.png` | build 2 → 8 타임라인 |
| 5 | `05-divider.png` | 구분선 |
| 6 | `06-cost-breakdown.png` | 월 비용 정산 ($28.25) |
| 7 | `07-ai-cannot.png` | AI가 못한 3가지 |
| 8 | `08-recommend-matrix.png` | 추천 매트릭스 5종 |
| 9 | `09-closing.png` | 마무리 + CTA |

**Finder로 열기:**
```
open /Users/seung-yeoblee/dev/unpack-blogs/docs/naver-setup/editions/images/05-gentledo-dev/
```

---

────────── 제목 ──────────

# 퇴근 후 2주, Claude Code로 iOS 앱 만든 후기

────────── 본문 복붙 시작 ──────────

**"Flutter 한 줄 안 짜본 직장인이, 퇴근 후 2주 만에 Claude Code로 iOS 앱을 출시했습니다."**

평일 저녁 9시. 회사에서 돌아와 노트북을 폅니다. **Claude Code**라는 AI 코딩 도구를 켜고 오늘은 **3일째 연속 build #6** 입니다. 한 줄도 직접 못 짜는 제가 **App Store에 본인 명의 앱**을 올렸어요.

[01-cover.png 삽입 — 본문 도입 커버]

---

비결은 결국 **Claude Code 한 도구**였어요. 이 글은 부업으로 앱 만들어 보고 싶은 분들께 **"AI 코딩으로 진짜 어디까지 되고, 뭐가 안 되는지"** 솔직하게 공유하는 후기입니다.

---

## **2주 동안 뭘 만들었나요?**

이름은 **GentleDo**. 에너지에 맞춰 할 일을 제안하는 iOS 앱이에요.

- 아침에 컨디션 체크 한 번 → 오늘 에너지에 맞는 할 일만 필터링
- iOS 전용, **광고·계정 없이 로컬 저장**
- 한국어·영어 지원

복잡한 서버나 결제 없이 **로컬 전용 MVP**부터 시작한 게 신의 한 수였어요. 첫 앱은 작게, 확실하게.

🔗 App Store에서 **GentleDo** 검색하시거나 [여기로 바로 이동](https://apps.apple.com/us/app/gentledo/id6761796867)하실 수 있어요.

---

## **기술 스택 — 비개발자에게 가장 현실적인 조합**

[02-stack-decision.png 삽입 — 기술 스택 + 3가지 제약]

선택한 조합은 다음과 같아요.

- **언어 / 프레임워크** — Flutter + Dart
- **상태관리** — Riverpod
- **로컬 DB** — Drift (SQLite 래퍼)
- **AI 페어** — Claude Code Max 구독

Flutter를 고른 이유는 단순합니다. **iOS·Android·macOS를 한 코드베이스로 만들 수 있고**, Dart는 정적 타입이라 AI랑 페어 프로그래밍할 때 실수가 적었어요.

---

## **얼마 들었어요? 진짜로?**

[06-cost-breakdown.png 삽입 — 월 비용 정산]

2주간 실제 결제 내역입니다.

- **Claude Code Max** — 월 $20 (≈ ₩28,000)
- **Apple Developer Program** — 연 $99 (월 환산 ≈ $8.25)
- **합계 — 월 $28.25 ≈ ₩40,000**

Flutter 외주 견적 받으면 **최소 300만원부터** 시작합니다. 75배 차이예요. 부업으로 시작하기에 이만한 가성비가 없습니다.

---

## **2주를 어디에 썼어요? — 사람 vs AI 역할 분담**

[03-vibe-coding-balance.png 삽입 — 사람 vs AI 역할 분담]

정직하게 공개합니다. **AI가 다 해 준 게 아니에요.**

### **제가 한 일 (사람의 영역)**

- 프로젝트 컨텍스트 문서화 (`CLAUDE.md` 규칙집)
- 실기기 테스트 + 디자인 결정 + 카피라이팅
- "지금은 하지 마세요" 리스트 유지
- 가설 정의·검증 지표 설정

### **Claude Code가 한 일 (AI의 영역)**

- Dart 코드 실제 작성
- Drift DB 스키마·마이그레이션
- Riverpod 상태관리 설계
- 반복 태스크 스케줄링
- 테스트 케이스·리팩토링 제안

핵심은 **`CLAUDE.md` 규칙 문서**였어요. "Red 컬러 금지", "다국어 파일 경유 필수" 같은 4줄 규칙이 **수백 번의 '그거 말고' 소통을 절약**해 줬습니다.

---

## **2주 타임라인 — build 2 → build 8**

[04-2week-timeline.png 삽입 — build 2 → 8 타임라인]

- **Day 1~3** — 가설 정의 + Flutter 셋업 + Riverpod 골격 (build 2)
- **Day 4~7** — 핵심 기능 (할 일 필터링·에너지 체크) (build 4)
- **Day 8~10** — 다국어 + 디자인 토큰 정리 (build 6)
- **Day 11~12** — 실기기 디버깅 (크래시 잡는 데 시간 많이 씀)
- **Day 13~14** — Xcode 설정·스크린샷·메타데이터 (build 8)

총 투입 시간은 **약 45시간**. 평일 야간 2시간 × 10일 + 주말 5시간 × 2일 + 기타 디버깅·스토어 작업이에요.

---

[05-divider.png 삽입 — 구분선]

---

## **솔직히, AI로 안 됐던 것 3가지**

[07-ai-cannot.png 삽입 — AI가 못한 3가지]

과장 없이 알려드릴게요. 바이브 코딩 한계도 알고 시작해야 해요.

### **1️⃣ 실기기 디버깅**

시뮬레이터는 멀쩡한데 실기기에서만 크래시 나는 버그가 있었어요. **Claude에게 크래시 로그를 줘도 원인 못 찾았습니다.** 결국 GitHub 이슈 트래커 직접 검색해서 해결.

### **2️⃣ Xcode 설정의 체크박스 한 칸**

TestFlight 암호화 선언, iPad 타깃 제거, provisioning profile 설정. **여기서 하루를 날렸어요.** Xcode UI는 AI가 못 봅니다.

### **3️⃣ 디자인 감각**

"이 카드가 무거워 보인다" 같은 피드백은 텍스트로 옮기기 어려워요. Figma에서 직접 조정한 뒤 색·간격 값만 AI에게 옮기는 식이 가장 빨랐어요.

---

## **부업으로 정말 가능한가요? — 추천 매트릭스**

[08-recommend-matrix.png 삽입 — 추천 매트릭스 5종]

**가능합니다. 단 조건이 있어요.**

### ✅ 권장 — 이런 분께

- 월 4만원 구독비 감당 가능
- 주 10~15시간 투입 가능
- 기술 용어 20개 정도는 읽을 수 있음 (Widget, State, Provider 등)
- 로컬 전용 단순 MVP 범위에서 시작

### ❌ 비권장 — 이런 분께는 다른 길

- 서버·인증·결제가 핵심인 앱 (난이도 급상승)
- 기술 문서 자체가 어려운 경우
- 명확한 아이디어 없이 "그냥 만들어 보고 싶다" 수준

---

## **AI 코딩 도구, 뭐부터 시작할까요?**

처음 쓰시는 분께 추천 순서입니다.

- **무료 ChatGPT** — 개념 질문·디버깅 시작점
- **Claude Code Max $20** — 본격 개발 시작 (가성비 최강)
- **Cursor Pro $20** — IDE 안에서 작업하고 싶으면

처음엔 무료로 감 잡고, **프로젝트 시작할 때 Claude Code 전환**이 현실적이에요.

---

## **마무리 — "혼자서는 못 만들었을 앱"이 만들어졌어요**

[09-closing.png 삽입 — 마무리 + CTA]

**"1인 개발 시대"** 같은 말, 뜬 구름 같죠. 그런데 제가 **45시간 + 월 $28**로 출시까지 갔습니다. 완벽한 앱은 못 만들어요. 하지만 **"혼자서는 못 만들었을 앱"** 을 **"혼자서도 만들 수 있게"** 해 주는 도구는 분명히 존재합니다.

부업으로 앱 하나 만들어 보고 싶으셨다면, 지금이 시작하기 좋은 타이밍이에요.

---

🔗 GentleDo 받아 보기 → [App Store에서 GentleDo](https://apps.apple.com/us/app/gentledo/id6761796867)

📌 **이웃 추가**하시면 GentleDo 시리즈 **3화 — 심사 2일 통과기**(금요일) 놓치지 않으세요
❤️ **공감·댓글** 한 번이 다음 글에 큰 힘이 됩니다
💬 어떤 앱 만들어 보고 싶으세요? 댓글로 남겨 주시면 직접 써 본 관점에서 답변드릴게요

기술 깊이는 **aigrit.dev**, 1인 빌더 일기는 **babipanote.com**에서 더 깊게 공유합니다.

────────── 본문 복붙 끝 ──────────

---

## 📝 발행 체크리스트

- [ ] 스마트에디터 ONE 열기 (PC 권장)
- [ ] 카테고리: **AI 도구 리뷰** (또는 부업 탐구)
- [ ] 공개설정: 전체공개 / 댓글·공감 허용 / 검색 허용 ON
- [ ] 제목 붙여넣기
- [ ] 본문 복붙 → 이미지 9장 순서대로 업로드
- [ ] 톱니바퀴 → **대표 이미지로 `00-thumb-square.png` 등록** (프롤로그용)
- [ ] 소제목 굵게(`Cmd+B`) 강조 — 스마트에디터 "본문2" 스타일도 OK
- [ ] 태그 8개 입력
- [ ] 발행 → URL 복사
- [ ] (Naver Blog 호스트는 SearchAdvisor 등록 불가 — C-Rank 자동 인덱싱 대기)
- [ ] Obsidian Pipeline 카드 갱신 (`naver_edition_status: published`, `publish_url_naver`, `logNo`, `publish_date`)
- [ ] AIGrit + babipanote 원본 글에 역참조 (`naver_edition_url`) 추가
- [ ] Craft 문서 → `02. Archive/Naver/` 이동

---

## 📊 KPI 목표 (발행 후 7일)

| 지표 | 목표 |
|---|---|
| 조회수 | 500+ (3편 중 검색 수요 가장 큼) |
| 이웃 신규 | 5+ |
| 공감 | 15+ |
| 댓글 | 5+ |
| GentleDo App Store 방문 (UTM) | 30+ |

---

## 🎯 SEO 노트

- 첫 100단어 안에 **AI**, **앱**, **2주**, **App Store**, **Claude Code**, **비개발자**, **Flutter**, **부업** 키워드 1회씩 배치 완료
- 본사이트 인용 1회만(`aigrit.dev`, `babipanote.com`) — 외부 링크 최소화 (네이버 C-Rank 선호 반영)
- **3편 시리즈 중 검색 수요가 가장 강한 글** — "AI로 앱 만들기", "Claude Code 후기", "비개발자 앱 개발" 키워드 모두 네이버·구글 검색량 보유

---

## 🔗 관련

- [04-app-naming-failure.md](04-app-naming-failure.md) — GentleDo 시리즈 1화 (월요일 발행)
- [06-appstore-review-2days.md](06-appstore-review-2days.md) — GentleDo 시리즈 3화 (금요일 발행)
- 원본 1: https://babipanote.com/blog/building-gentledo-with-claude-code
- 원본 2: https://aigrit.dev/ko/blog/claude-code-flutter-app-guide
