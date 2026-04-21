# 콘텐츠 파이프라인 워크플로우

## 6단계 흐름

```
Step 0: Claude.ai 기획 (트렌드·아이디어·경쟁 분석)
  ↓
Step 1: Obsidian Pipeline 카드 생성 (SEO 메타)
  ↓
Step 2: Claude.ai → Craft 초안 작성 (MCP 자동 저장)
  ↓
Step 3: Craft 편집 (이미지 교체, 문체 수정, 내부 링크 확정)
  ↓
Step 4a: /publish-post (MDX 변환 → git push → Vercel 배포 → 색인 요청)
Step 4b: 네이버 에디션 (Craft 복붙 → 스마트에디터) — 해당 글만
  ↓
Step 5: Obsidian status → published, URL·성과 기록
  ↓
Step 0으로 루프
```

## 세션 분리 규칙

글 한 편당 2세션. 컨텍스트 오염 방지.

| 세션 | 범위 |
|---|---|
| Session 1 | Step 0 기획 + Step 2 초안 (맥락 연속 필요) |
| Session 2 | Step 4b 네이버 리프레이밍 (톤·포맷이 다름, 별도 세션) |

## Step 0 기획 — 2단 구조

| 주기 | 작업 | 스킬 |
|---|---|---|
| 월 1회 | 다음 달 글감 20개 일괄 기획 | trend-scanner-kr → idea-generator → content-strategist |
| 글당 | 해당 글 경쟁 분석 + 아웃라인 | competitor-intel 만 |

## 실행 환경

| Step | 환경 |
|---|---|
| 0~2 (기획·초안) | Claude.ai 웹/모바일 |
| 3 (편집) | Craft 앱 단독 |
| 4a (발행) | **Claude Code 터미널 필수** — `/publish-post` |
| 4b (네이버) | Claude.ai + 네이버 스마트에디터 |
| 5 (기록) | Obsidian 수동 |

## 이미지 워크플로우

```
apps/{app}/public/images/{slug}/
├── og.png                 ← OG 이미지
├── 01-name.png            ← 본문 이미지 (순서 접두어)
└── naver/                 ← 네이버 추가 이미지 (해당 시)
```

- Step 2 초안: `{IMG: NN-name | alt: 설명 | caption: 캡션}` 마커만
- Step 3 편집: 실제 스크린샷 캡처·배치
- Step 4a: `/publish-post`가 마커 → `<Image>` 치환

## 수정·롤백

| 상황 | 대응 |
|---|---|
| 오탈자 수정 | Craft 수정 → `/publish-post` 재실행 → updated 자동 갱신 |
| 제목 변경 | Craft + MDX + Obsidian 3곳 동기화 |
| slug 변경 | **원칙 금지.** 불가피하면 next.config.ts에 301 추가 |
| 글 철회 | MDX 삭제 + git push + Obsidian status → archived |

## Obsidian 참고 문서

- `02. Blog SEO/01. Workflow Guide.md` — 전체 운영 원칙
- `02. Blog SEO/09. 실전 워크플로우 매뉴얼.md` — Step별 프롬프트 복붙본
- `02. Blog SEO/07. Sprint 실행 계획.md` — 발행 일정
