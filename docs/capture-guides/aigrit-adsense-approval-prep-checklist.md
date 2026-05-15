# AdSense 승인 체크리스트 — 스크린샷 캡쳐 가이드

**대상 글:** [aigrit/adsense-approval-prep-checklist](../../apps/aigrit/content/posts/ko/adsense-approval-prep-checklist.mdx)
**발행일:** 2026-05-15
**preflight 기준:** AIGrit Cluster — 본문 3~5장
**primary_keyword:** AdSense 승인
**secondary_keywords:** AdSense 거절 사유, ads.txt, 1인 블로거 수익화, E-E-A-T
**topic_cluster:** AI 수익화·부업
**cluster_role:** cluster (ai-side-income-100man-roadmap Pillar 보조)

## 발행 시점 상태

- 본문 이미지 3장 + OG 1장 모두 matplotlib 자동 생성 완료
- review-post: WARN 1건 (글자 6,983자 — Cluster 권장 상한 4,000자 초과, 깊이 콘텐츠로 수용)
- 그 외 broken 0, FAQ 5, 내부 5, 외부 3, H2 7 전부 PASS

## 이미지 목록

### [자동 생성] — Claude가 렌더 완료
- [x] `og.png` — OG 썸네일 1200×630 (Pretendard·AIGrit Indigo+Cyan, scripts/og/generate-og-all.py)
- [x] `01-rejection-reasons.png` — 거절 사유 Top 7 가로 막대 (matplotlib)
- [x] `02-content-volume.png` — 통과 사이트 평균 글수·글자수·카테고리 분포 (matplotlib)
- [x] `03-prep-checklist.png` — 13항목 4단계 체크리스트 박스 다이어그램 (matplotlib)

### [사용자 캡쳐] — 추후 보강 권장 (선택)

저장 경로 공통: `apps/aigrit/public/images/adsense-approval-prep-checklist/`

- [ ] `04-adsense-console.png` — Google AdSense 콘솔 메인 화면 (실제 거절 메일 또는 승인 메일)
  - 컨텐츠: 사이트 등록 후 "검토 중" 또는 "승인" 상태가 보이는 콘솔 캡쳐
  - 도구: AdSense 콘솔 (https://www.google.com/adsense/) 로그인 후
  - 캡쳐 방법: `Cmd+Shift+4` 영역
  - 민감정보: 게시자 ID(pub-XXXX)·계정 이메일 마스킹 필수

- [ ] `05-ads-txt-example.png` — 실제 ads.txt 파일 내용 (Carbon 코드 스크린샷)
  - 컨텐츠: 본인 게시자 ID 포함한 한 줄 + 주석
  - 도구: Carbon (https://carbon.now.sh) 또는 macOS Terminal + bat
  - 권장 영역: 1,400~1,600px PNG
  - 민감정보: 본인 게시자 ID는 공개 가능 (ads.txt는 어차피 공개 파일)

## 규격 공통

- 자동 생성 차트: matplotlib 12~13인치 × 180dpi + Pretendard 폰트
- 본문 이미지: 가로 1,600~2,000px PNG (80~200KB)
- 색상 토큰: BG `#0F172A` · Indigo `#3730A3` · Cyan `#06B6D4`

## 생성 스크립트

```bash
/Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
  python3 scripts/charts/generate-adsense-checklist-charts.py
```

## 관련

- 같은 cluster Pillar: `ai-side-income-100man-roadmap.mdx`
- `.claude/rules/post-requirements.md` — Cluster 3~5 이미지 요건
- `02. Unpack-Blogs/13. 캡처 백로그 & 이미지 가이드` (Obsidian)
