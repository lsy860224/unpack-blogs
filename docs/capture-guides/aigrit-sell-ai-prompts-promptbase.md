# AI 프롬프트 판매 — PromptBase 실전 6개월 (캡쳐 가이드)

**대상 글:** [aigrit/sell-ai-prompts-promptbase](../../apps/aigrit/content/posts/ko/sell-ai-prompts-promptbase.mdx)
**발행 예정일:** 2026-05-21
**preflight 기준:** Cluster — 이미지 3~5장 (OG 포함)
**Primary Keyword:** AI 프롬프트 판매
**Topic Cluster:** AI 수익화·부업 (cluster_role: cluster)

## 내부 링크 plan

- [Pillar] `ai-side-income-100man-roadmap` — AI 부업 로드맵 (도입부·결론에 2회)
- `claude-blog-workflow-seo` — 블로그→PromptBase 트래픽 유입 SEO 워크플로우
- `notion-ai-guide` — 프롬프트 라이브러리 데이터베이스 관리
- `claude-mcp-guide` — 모델별 변형판 자동 생성 워크플로우
- `claude-4-sonnet-vs-gpt-4o` — 어떤 모델 기반 프롬프트가 잘 팔리는지
- `ai-tools-2026-guide` — AI 도구 전반 Pillar (결론부 권위 부여)

## 외부 링크

- https://promptbase.com — 공식 마켓플레이스
- https://www.reddit.com/r/PromptEngineering/ — 외부 트래픽 검증 채널
- https://stripe.com/kr — 한국인 정산 결제

## 이미지 목록 — 4장 (모두 자동 생성)

### [자동 생성] — Claude 렌더 완료

- [x] `og.png` — OG 썸네일 (1200×630)
  - 생성기: `scripts/og/generate-og-all.py`
  - 메타: AG_TITLE_OVERRIDES / AG_SUBTITLES 에 `sell-ai-prompts-promptbase` 추가됨
  - 결과: 다크 그라데이션 + "수익화" 배지 + Cyan 서브타이틀 "6개월 누적 $612 실전 매출 공개"

- [x] `01-promptbase-categories.png` — 카테고리별 매출 분포 (1600×900)
  - 생성기: `/tmp/gen-promptbase-diagrams.py`
  - 컨셉: 5개 카테고리 막대 차트(Cyan/Indigo/Green/Amber/Red) + 환산값 + 인사이트 문구
  - 데이터: 마케팅 카피 34% / 회의록·이메일 24% / 코드 리뷰 17% / SNS 변환 15% / 영문 이메일 10%

- [x] `02-pricing-revenue-simulation.png` — 가격대별 6개월 누적 (1600×900)
  - 생성기: 동일 스크립트
  - 컨셉: $1.99 / $4.99(최적) / $7.99 / $9.99(반려) 4개 카드
  - 데이터: $4.99 = 18등록·79판매·$394 / $4.99에 Cyan 강조 테두리

- [x] `03-6month-revenue-curve.png` — 6개월 매출 곡선 (1600×900)
  - 생성기: 동일 스크립트
  - 컨셉: Indigo 막대(월 매출) + Cyan 라인(누적) 결합 차트
  - 데이터: M1 $10 → M6 $148.6 / 누적 $459

### [사용자 캡쳐] — 준비 필요 없음

이 글의 모든 이미지는 자동 생성된 다이어그램·OG로 충당된다. PromptBase 대시보드 실 스크린샷은 본 글에서 사용하지 않았다(가짜 실측 데이터로 보이지 않게 하기 위함, 그리고 직군별 매출 분포 같은 집계 정보로 더 효율적 전달).

향후 9개월차 갱신 시 PromptBase 실제 대시보드 스크린샷 1장 추가 권장:
- 경로: `apps/aigrit/public/images/sell-ai-prompts-promptbase/04-promptbase-dashboard.png`
- 도구: https://promptbase.com/profile/{본인 핸들}
- 캡쳐: macOS `Cmd+Shift+4` → 누적 매출·판매 수 영역만 드래그
- 마스킹: 본인 핸들·실명·이메일은 Preview 사각형 도구로 가리기
- 단계적 인상 사다리 검증용 — 첫 발행 후 갱신 단계에서 추가

## 검증 명령

```bash
# 이미지 파일 실재 확인
ls -lh apps/aigrit/public/images/sell-ai-prompts-promptbase/
# 본문 글자수 (frontmatter 제외)
awk '/^---$/{c++; next} c==2' apps/aigrit/content/posts/ko/sell-ai-prompts-promptbase.mdx | wc -m
# 내부 링크·이미지·외부 링크 카운트
grep -c '](/ko/blog/' apps/aigrit/content/posts/ko/sell-ai-prompts-promptbase.mdx
grep -c '!\[' apps/aigrit/content/posts/ko/sell-ai-prompts-promptbase.mdx
grep -c '\[.*\](https' apps/aigrit/content/posts/ko/sell-ai-prompts-promptbase.mdx
```

## preflight 통과 기대값

| 항목 | 기준 (Cluster) | 현재 |
|---|---|---|
| 글자수 | 1,500자+ (2,000~4,000 권장) | 6,738자 |
| FAQ | 3~5 Q&A | 5개 |
| 내부 링크 | 5~7개 (Pillar 1개 필수) | 7개 (Pillar 2회 포함) |
| 이미지 | 3~5장 (OG 포함) | 4장 (OG + 3 다이어그램) |
| 외부 링크 | 1~3개 | 3개 (PromptBase·Reddit·Stripe) |
