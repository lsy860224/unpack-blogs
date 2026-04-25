# babipanote — 글 작성 가이드

> **babipanote.com** — 1인 빌더 저널. 개인 허브·브랜드 자산. 이 문서는 글의 톤·구조·발행 워크플로우를 정의한다.
> 이미지는 [image/BABIPANOTE.md](../image/BABIPANOTE.md), SEO는 [seo/BABIPANOTE.md](../seo/BABIPANOTE.md) 참조.

---

## 1. 정체성 & 톤

| 항목 | 값 |
|---|---|
| 도메인 | babipanote.com |
| 타겟 | 1인 개발자 · 인디해커 · PKM 덕후 · 독자적 브랜드를 세우려는 빌더 |
| 핵심 컨셉 | **빌더 저널** — 실패·수치·결정을 1인칭으로 기록 |
| 톤 | "저널·종이" 감성. 따뜻한 서체 + Plum/Terracotta 팔레트 |
| 인칭 | **1인칭 "저는 / 나는"** — AIGrit과 정반대 |
| 시제 | 회고형 과거형 기본, 현재 진행형은 "지금 이렇게 하고 있습니다" |

### 표현 규칙

| 사용 | 금지 |
|---|---|
| "나는 이렇게 했다" / "세 번 실패하고 배운 것" | 3인칭 분석가 톤 ("X는 Y를 한다") |
| "월 매출 1,237,400원 공개" | 뭉뚱그린 "월 백만원 이상" |
| "이건 틀렸다. 다시 하겠다" | 자기 정당화 / 합리화 |
| "이 부분은 아직 모릅니다" | 허세 / 가짜 확신 |

---

## 2. 글 유형

| 유형 | 단어수 | FAQ | 내부 링크 | 설명 |
|---|:---:|:---:|:---:|---|
| **buildlog** | 1,500~2,500 | 선택 | 2~3 | "X를 만든 36시간" 류 실전 기록 |
| **lesson** | 1,500~2,500 | 선택 (tool-review만 권장) | 2~3 | "3번 실패 후 배운 것" |
| **essay** | 1,500~2,500 | 없음 | 2~3 | "왜 1인 빌더를 택했나" 류 사유 |
| **revenue-report** | 2,000+ | 없음 | 3~5 | 💰 **실수치 공개** — 월/연 P&L 완전 공개 |
| **pillar** | 3,500+ | 있음 | 10+ | 허브글 (#14 일상 / #17 PKM / #23 재무) |

---

## 3. 본문 구조 (저널식 자유, 단 뼈대는 유지)

1. **훅 문장** (개인적·구체적) — "평일 저녁 9시, 설거지 끝낸 뒤…"
2. **맥락** — 왜 이 글을 쓰는가, 지금 시점 (날짜·단계)
3. **본문** — 시간 순 또는 주제 순
4. **수치/코드 공개** (해당 시) — 정확한 값, 표·차트
5. **배운 점** — 3~5개 bullet 또는 소제목
6. **다음 계획** — "이다음엔 X를 해볼 것"
7. **관련 글** — 이전 저널 링크

---

## 4. Frontmatter 스키마

```yaml
---
title: "글 제목"
date: "2026-04-25 09:00"
updated: "2026-04-25 14:00"
slug: "url-slug"
description: "150자 요약"
tags: ["buildlog", "pkm", "재무"]
thumbnail: "/images/{slug}/og.png"
featured: false
# category 필드 없음 (AIGrit과 차이)
type: buildlog        # buildlog | lesson | essay | revenue-report
series: "Sprint 1차"   # 옵션. 시리즈 연결
---
```

---

## 5. 💰 실수치 공개 정책

`type: revenue-report` 글은 실수치 그대로 공개.

| 허용 공개 | 제외 필수 |
|---|---|
| 월/연 매출·지출·순이익 | 협찬사 개별 금액 (계약 NDA 우려) |
| 채널별 CAC·ROI | 배우자 소득 · 가족 사업 정보 |
| 도구별 월 구독료 | 개인 식별정보 · 계좌 스크린샷 |
| 광고·제휴 수익 구체 수치 | 세무사 견적서 원본 |

**발행 전 체크리스트** (revenue-report):
- [ ] 민감 계약 조항 제외 확인
- [ ] 개인 식별정보 블러 처리
- [ ] 세무 리스크 재검토 (소득 증빙 영향)
- [ ] 경쟁사 노출 허용 범위 판단

---

## 6. 마커 포맷

AIGrit과 동일 (`{IMG:...}`, `{LINK:...}`). 외부 링크는 일반 markdown.
상세는 [CONTENT_RULES.md](../CONTENT_RULES.md).

---

## 7. 절대 금지

- 3인칭 분석가 톤 (AIGrit 영역)
- **광고 켜기** (`adsense: false` 유지, `affiliateLinks: false`)
- **FAQ 남발** — 저널의 본질 훼손 (tool-review만 제한적 허용)
- 상업적 CTA (구독·결제 유도) — 이건 AIGrit에서
- 수치 과장 / 라운딩 숨기기 (실수치는 정확 원본)

---

## 8. 작업 경로

| 목적 | 위치 |
|---|---|
| **MDX 파일** | `apps/babipanote/content/posts/{slug}.mdx` (언어 폴더 없음, ko 전용) |
| **Obsidian Pipeline** | `02. Blog SEO/10. Pipeline/babipanote/{NN}-babipanote-{slug}.md` |
| **Obsidian 지침서** | `02. Blog SEO/03. babipanote 글쓰기 지침서.md` |
| **Craft 초안** | `05. Blog Pipeline / 01. In Progress / babipanote / [babipanote] {제목}` |
| **Craft 아카이브** | `05. Blog Pipeline / 02. Archive / babipanote /` |

---

## 9. 발행 워크플로우

1. **Obsidian Pipeline 카드** — SEO·내부 링크 계획 ([seo/BABIPANOTE.md](../seo/BABIPANOTE.md))
2. **Craft 초안** — 개인 톤 유지하며 작성
3. **이미지 준비** ([image/BABIPANOTE.md](../image/BABIPANOTE.md)) — **OG 제목 포함 필수**
4. **MDX 변환** → slug 유일성 체크
5. **`/review-post`** 통과 (babipanote는 FAQ 선택적)
6. **`/publish-post`** — git commit + push
7. **발행 후 색인** — GSC + IndexNow + 네이버 SearchAdvisor (babipanote.com 등록됨)
8. **Pipeline 갱신** — `status: published`, `publish_url_babipanote`

---

## 10. `/review-post` 통과 기준

- 글자수 1,500~2,500 (revenue-report/pillar는 더 길게)
- FAQ 선택 (있으면 AIGrit 기준)
- 내부 링크 2~3 + broken link 0
- 이미지 1장 이상 + broken image 0 (OG 제목 포함)
- 외부 링크 1~3

상세는 `.claude/rules/post-requirements.md`.

---

## 11. 크로스링크 (AIGrit ↔ babipanote)

`Master Content Plan §크로스 링크 매트릭스` 15쌍 중 해당 글 연결:

| 예시 | 양방향 링크 포인트 |
|---|---|
| AIGrit #13 (AI 부업 로드맵) ↔ babipanote #23 (연간 재무) | "가능성 ↔ 내 실적" |
| AIGrit #14 (Claude 블로그 운영) ↔ babipanote #29 (콘텐츠 ROI) | "생산 ↔ 측정" |

양방향 링크 심을 때 **자연스러운 맥락**만, 광고성 금지.

---

## 12. 관련

- [image/BABIPANOTE.md](../image/BABIPANOTE.md) — 종이·잉크 톤 이미지 규칙
- [seo/BABIPANOTE.md](../seo/BABIPANOTE.md) — E-E-A-T·Author schema
- [CONTENT_RULES.md](../CONTENT_RULES.md) — 공통 마커·금지어
- Obsidian: `02. Blog SEO/03. babipanote 글쓰기 지침서.md`
