# DESIGN_CHECKLIST.md — 디자인 산출 전 자가검증

> `DESIGN.md`의 원칙을 실제로 지켰는지 확인하는 체크리스트.
> 디자인 과업 커밋 직전에 전 항목을 `- [x]`로 채울 수 있어야 한다.
> 한 항목이라도 `- [ ]`면 QC 사전에 해결.

사용법: 신규 브랜드 작업 시 이 파일을 복사해 `docs/_workspace/{brand}-{date}-qc.md`로 두고 체크 → 통과 후 삭제.

---

## Colors

- [ ] 5색 시스템 (Primary / Secondary / Secondary Hover / Accent Green / Accent Red) + Neutral (Dark · Light) 모두 선언
- [ ] **라이트·다크 쌍**이 모든 역할에 존재 (다크에서 Primary는 밝은 톤으로 교체)
- [ ] 각 색상의 **HEX / RGB / HSL** 3포맷 + 용도 한 줄 기재
- [ ] **WCAG 표** 포함 — 본문(Ink on Bg), Primary 링크, Primary 버튼, Secondary CTA, Accent 배지 최소 5행
  - [ ] 본문: **AAA 7:1 이상** 목표
  - [ ] 버튼·링크: **AA 4.5:1 이상** 필수
  - [ ] AA Large(3:1)만 통과한 색은 "배지/아이콘 전용" 명시
- [ ] 자매 사이트와의 **Hue 거리 ≥ 90°** (Primary) — 불가 시 채도 40pp 이상 격차로 보완하고 근거 명시
- [ ] 자매 사이트와의 **차별화 매트릭스** (Hue · Saturation · 폰트 카테고리) 섹션 존재

## Typography

- [ ] **6단계 스케일** (Display / H1 / H2 / Body / Small / XSmall) 크기·line-height·weight 명시
- [ ] 한글 + 영문 폰트 **페어링** 명시, 라이선스(SIL OFL / Apache 등) 포함
- [ ] 무료/오픈소스 폰트 우선 선택. 유료 폰트 사용 시 근거 필수
- [ ] 수치 중심 브랜드는 **Mono 폰트 전용 행** 추가 (예: `Num`)
- [ ] 세리프/산세리프 **카테고리 선택이 자매 사이트와 다른가** — 같다면 다른 신호(weight, spacing)로 구별

## Tokens (Tailwind v4 & CSS)

- [ ] **`@theme` 블록** 예시를 가이드라인 MD `4-1` 섹션에 복붙 가능한 형태로 포함
- [ ] `@import "tailwindcss"` / `@plugin "@tailwindcss/typography"` / `@variant dark (...)` 3줄 시작부 포함
- [ ] `--color-brand-*`, `--font-*`, `--text-*` 네이밍 일관
- [ ] `.dark` 스코프에서 같은 변수명 재지정 (테마 분기 없이)
- [ ] 순수 CSS 변수 버전(`4-2`)도 별도 제공
- [ ] `apps/{brand}/src/app/globals.css` 현재 값과 **대체 여부·Phase 1-3에서 교체** 명시

## Logo

- [ ] 최소 배리언트 **3개**: Primary(라이트) / Dark / Reverse(브랜드 컬러 bg)
- [ ] **Mark-only** 버전 별도 (파비콘·SNS 프로필용)
- [ ] **Mono** 배리언트 (단색 프린트·팩스용)
- [ ] **클리어 스페이스** 규칙 + 시각 예시
- [ ] **최소 크기** 웹(px) · 인쇄(mm) 양쪽 기재
- [ ] **Font family + weight + letter-spacing** 정확 명시 (재현 가능하도록)
- [ ] 금지 사용 예(기울이기·그림자·재배치) 언급

## Digital Assets

- [ ] **OG 이미지**: 1200×630, Default + Article Template (라이트·다크면 4장)
- [ ] **메타 태그 HTML 스니펫** (title, description, og:*, twitter:*, theme-color × 2) 복붙 가능 형태
- [ ] **Social Header**: X 1500×500 (라이트·다크 쌍)
- [ ] **Favicon 사이즈**: 32×32, 16×16, 180×180(apple-touch-icon), `icon.svg` 벡터 방향
- [ ] **Watermark**: 사용 규칙(불투명도·위치·최소 크기) + 라이트/다크 배경 샘플
- [ ] **SNS 핸들 후보** 명시 + 가용성 확인 필요 플래그

## JSX Preview

- [ ] `apps/{brand}/brand-preview.jsx` 단일 파일
- [ ] `"use client"` directive 상단에 있음
- [ ] 라이트/다크 **토글 버튼**
- [ ] 섹션 포함: Hero / Colors 스와치 / Typography 전 스케일 / Logo 배리언트 / UI 컴포넌트 샘플(버튼·배지·카드) / OG 시뮬레이션 / Voice On-Brand vs Off-Brand
- [ ] CDN 폰트 로드 (Pretendard jsDelivr, Google Fonts)
- [ ] `apps/{brand}/src/app/preview/page.tsx` 래퍼 존재, `dev` 서버에서 `/preview` 라우트 200 확인

## Figma

- [ ] 파일명: `{Brand} — Brand` (v2 이상이면 버전 suffix)
- [ ] **8 페이지** 고정: Cover / Style Guide / Logo / Avatar / Social Header / OG Image / Watermark / Favicon
- [ ] Cover에 브랜드명 + 버전 + 날짜
- [ ] Style Guide 페이지에 **라이트·다크 두 프레임** 나란히
- [ ] 각 페이지 첫 프레임에 용도 캡션(예: `X BANNER · LIGHT · 1500×500`)
- [ ] 폰트 미동기화 경고가 뜨면 "Missing Font 해결 필요" 메모를 산출물 응답에 포함

## Differentiation (자매 사이트가 있을 때만)

- [ ] 자매 사이트 가이드라인의 Primary/Secondary/폰트/무드 **읽고** 회피 기준으로 사용
- [ ] 가이드라인 MD 끝에 **구별 매트릭스 표** (Hue · Saturation · 폰트 카테고리 · 배경 온도 · 로고 유형)
- [ ] 두 프리뷰를 나란히 열었을 때 **0.5초 내 구별** 가능한지 본인 눈으로 검증

## Deliverables (한 과업 = 3종 동시 제출)

- [ ] `apps/{brand}/docs/BRAND_GUIDELINES.md` 파일 경로 응답에 명시
- [ ] `apps/{brand}/brand-preview.jsx` + `src/app/preview/page.tsx` 경로 + 로컬 URL (`http://localhost:{port}/preview`)
- [ ] Figma 파일 URL (`https://www.figma.com/design/{fileKey}`)
- [ ] 3종이 **서로 일치** — MD 값 ↔ JSX 프리뷰 값 ↔ Figma 프레임 값이 같은 HEX·폰트·크기

## QC & Commit (메모리 `feedback_phase_qc_workflow.md` 준수)

- [ ] Phase 완료에 해당하는 산출물인가 확인 (브랜드 가이드 = Phase 1 사전 입력)
- [ ] **QC 서브에이전트 독립 검증** (이 체크리스트를 기준으로) — 통과 전 커밋 금지
- [ ] 커밋 메시지: `design({brand}): {산출 요약}` 또는 `feat(design): ...`
- [ ] 변경된 파일에 `.env`·대형 바이너리 섞이지 않았는지 `git status`로 확인

## Voice & Tone (브랜드 가이드라인 작성 시)

- [ ] 퍼스낼리티 5축 스펙트럼 + 각 축 값 + 의미
- [ ] 호칭 / 금지 표현 테이블
- [ ] UVP 1문장
- [ ] 태그라인 3개 (메인·서브·보조)
- [ ] 메시지 기둥 3~5개
- [ ] On-Brand vs Off-Brand 예시 문단 (JSX 프리뷰에도 렌더)

## 3관점 검증 (가이드라인 MD 말미에 필수)

- [ ] 🔴 **비판적**: 상표/색상 충돌, 접근성 미달, 번들/비용 이슈 등 최소 3개
- [ ] 🟢 **긍정적**: 자매 사이트 구별 강도, 타겟 적합성, 확장성 등 최소 3개
- [ ] ⚪ **중립적**: 도메인/핸들 가용성 확인 수준, 로고 제작 전 단계 한계 등 최소 2개
- [ ] **다음 단계**: Phase 1-2/1-3에서 이 산출물을 어떻게 소비할지 구체 명시
