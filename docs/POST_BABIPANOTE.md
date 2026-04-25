> ⚠️ **이 파일은 요약본입니다.** 상세 가이드는 아래 3개 문서를 따르세요:
> - 글: [`docs/post/BABIPANOTE.md`](post/BABIPANOTE.md)
> - 이미지: [`docs/image/BABIPANOTE.md`](image/BABIPANOTE.md)
> - SEO: [`docs/seo/BABIPANOTE.md`](seo/BABIPANOTE.md)

# babipanote 글쓰기 가이드 (요약)

> babipanote.com — 1인 빌더의 실험·실패·성공을 가감 없이 기록하는 개인 저널

## 정체성

- 태그라인: "만드는 사람의 저널"
- 톤: 1인칭, 솔직, 일기체. 감정 표현 OK
- 타겟: 같은 길을 가는 빌더·크리에이터·1인 개발자
- 수익: **없음** — 개인 브랜드 자산 축적

## 글 유형

| 유형 | 특징 | FAQ |
|---|---|:---:|
| `buildlog` | 개발 과정·실험 기록, 현재진행형 | ❌ |
| `revenue-report` | 수익·지표 투명 공개, 숫자 중심 | ❌ |
| `lesson` | 실패·교훈, 반성적 | ❌ |
| `essay` | 생각 정리·관점, 주관적 | ❌ |
| `tool-review` | 도구 리뷰 (예외적으로 FAQ 포함) | ✅ |

## 글 구조 (buildlog 기준, ~1,500단어)

```
H1 제목 (감성 + 구체 수치)
├── 도입 — 스토리 훅 (역피라미드 금지!)
├── H2 배경 — 왜 이걸 하려 했나
├── H2 과정 — 실제로 한 일 (숫자·스크린샷)
├── H2 결과 — 구체 수치
├── H2 배운 것 / 실패한 것
└── H2 다음 계획
```

## 첫 문단 — 스토리 훅 (역피라미드 금지)

```markdown
금요일 밤 11시. 아내는 자고 있었고 나는 Cursor를 켰다.
"이번 주말에 블로그 두 개를 런칭하자"고 마음먹었다.
불가능해 보이는 목표였지만 결국 해냈다. 거의.
```

**규칙:**
- 첫 문장: 구체적 시간·장소·감각
- 두 번째 문장: 결정 또는 긴장
- 세 번째 문장: 결과 암시 (결론 아님, 호기심 유발)

독자는 "결론"이 아니라 **"과정"**을 보러 온다. 역피라미드는 babipanote에서 사용하지 않는다.

## 문체 규칙

- 1인칭 "나" 사용
- 감정 표현 허용: "두려웠다", "당황스러웠다", "뿌듯했다"
- 구체 수치 필수: "47줄 코드", "3시간 디버깅", "$0.34 비용"
- 일기체 허용: "오늘은 ~", "지난주에 ~"

### 금지어 (AI 냄새) — AIGrit과 동일

획기적인, 혁신적인, 놀라운, ~을 통해, 다양한, 효율적인, 최적의

## AIGrit과의 경계 (중요)

### ❌ babipanote에서 하면 안 되는 것
- AdSense 광고, 제휴링크 프로모션
- "이 도구 추천합니다" 유형의 영업 글
- SEO 키워드 억지 삽입
- AIGrit 글 전체 재탕

### ✅ babipanote에서 AIGrit 언급 OK
- 맥락상 자연스러울 때: "자세한 가이드는 AIGrit에서 다뤘다"
- 수익 리포트: "AIGrit에서 이번 달 ₩45,000 벌었다" (투명 공개)
- 광고가 아니라 "같은 사람의 다른 프로젝트"로 서술

## SEO (최소한)

- Title: 감성 + 구체 수치 ("Week 1 회고 — 36시간 스프린트")
- Meta Description: 1~2문장 ("블로그 2개를 36시간에 런칭했다. 뭘 배웠나")
- Slug: 영문 kebab-case, 5~7단어
- 본문 ~1,500단어
- 내부 링크 2~3개, 외부 1~2개
- 네이버 에디션 **없음**

## MDX frontmatter

```yaml
title: "글 제목"
date: "YYYY-MM-DD HH:mm"
updated: "YYYY-MM-DD HH:mm"
slug: "url-slug"
description: "1~2문장"
tags: ["buildlog", "unpack-blogs"]
thumbnail: "/images/{slug}/og.png"
featured: false
topic_cluster: "unpack-blogs 구축기"
```

category 필드 없음 (babipanote는 카테고리 미사용).

## 빌드로그 관리 원칙

- 과거형 서술 일관성 (1년 뒤 "타임캡슐")
- 수정은 오탈자·사실 오류만 (감정·상황 유지)
- 수익 리포트만 "Update YYYY-MM-DD:" 섹션 추가 허용

## Obsidian 참고 문서

- `02. Blog SEO/03. babipanote 글쓰기 지침서.md` — 전체 지침서
- `02. Blog SEO/10. Pipeline/babipanote/_README.md` — 마스터 넘버링
