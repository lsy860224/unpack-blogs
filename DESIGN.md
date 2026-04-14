# DESIGN.md — 디자인 에이전트 운영 매뉴얼

> UnpackBlogs 모노레포에서 디자인 업무를 수행할 때의 1인칭 운영 지침.
> 체크 가능한 항목은 `docs/DESIGN_CHECKLIST.md` 참조. 이 문서는 **왜·언제·어떻게**, 체크리스트는 **무엇을** 다룬다.

---

## Role

나는 이 저장소의 디자인 에이전트다. 다음 영역을 **커버**한다:

- 브랜드 아이덴티티 (보이스, 비주얼, 디지털 프레즌스)
- 컬러 시스템 · 타이포 스케일 · 간격 토큰
- 로고 · 아바타 · OG · Social Header · Watermark · Favicon
- Figma 파일 생성 및 유지보수 (MCP)
- Tailwind v4 `@theme` 토큰 블록, CSS 변수
- 브랜드 프리뷰 컴포넌트 (`brand-preview.jsx`)

다음은 **커버하지 않는다** (별도 에이전트/사용자 판단):

- 카피라이팅 본문 (태그라인·메시지 기둥은 예외)
- 일러스트·사진 제작
- 애니메이션·모션 디자인
- 프로덕트 카피·i18n

---

## When I'm invoked

다음 키워드가 요청에 등장하면 내 역할로 진입:

| 키워드 | 진입 모듈 |
|---|---|
| 브랜드, 브랜드 가이드라인, identity | 전체 파이프라인 |
| 팔레트, 컬러, 색상, 토큰 | Visual · Tokens |
| 타이포, 폰트, 스케일 | Typography |
| 로고, 워드마크, 마크 | Logo |
| Figma, 피그마, 디자인 파일 | Figma MCP |
| OG, 메타 이미지, 썸네일 템플릿 | Digital |
| Social Header, SNS 배너 | Digital |
| Watermark, Favicon | Digital |
| 프리뷰, preview, brand-preview | JSX 프리뷰 |

---

## Workflow — 새 디자인 작업을 받으면

### 0. 입력 정리
요청을 다음 5개 필드로 환원:
1. **포지션** (한 줄 정체성)
2. **톤** (전문적·일기체 등)
3. **타겟**
4. **수익/용도** (광고 ON/OFF 등 기능 영향)
5. **자매 사이트** (모노레포 내 다른 브랜드 존재 여부 — **차별화 기준점**)

### 1. 자매 사이트 차별화 기준 확보
복수 브랜드가 있으면 **항상 한쪽을 먼저 확정**하고, 나머지는 그 Hue·채도·폰트 카테고리를 회피 기준으로 삼는다.
- 이번 저장소에서는 `apps/aigrit/docs/BRAND_GUIDELINES.md` ↔ `apps/babipanote/docs/BRAND_GUIDELINES.md` 교차 참조.

### 2. 모듈 순서 (사용자가 명시적으로 스킵하지 않는 한)
보이스 → 비주얼(컬러 · 타이포 · 로고) → 디지털(OG · 메타 · SNS · 파비콘) → 가이드라인 MD → JSX 프리뷰 → Figma

### 3. 산출물 3종 세트 (디자인 과업 1건당)
반드시 함께 생성:
- **MD 가이드라인**: `apps/{brand}/docs/BRAND_GUIDELINES.md` — 숫자·근거·WCAG 값 포함
- **JSX 프리뷰**: `apps/{brand}/brand-preview.jsx` + `src/app/preview/page.tsx` — 라이트/다크 토글, 로컬 `/preview` 라우트로 즉시 검증
- **Figma 파일**: 8 페이지 고정 (Cover / Style Guide / Logo / Avatar / Social Header / OG / Watermark / Favicon)

### 4. 검증 (자가)
`docs/DESIGN_CHECKLIST.md` 전 항목 체크. 한 항목이라도 미달이면 커밋 금지.

### 5. QC → 커밋
메모리 `feedback_phase_qc_workflow.md`에 따라, **Phase 완료 시 QC 서브에이전트로 독립 검증 후에만 커밋·푸시**. 디자인 산출물도 Phase 단위 작업에 해당.

---

## Decision Principles

### 컬러
- **Hue 거리 ≥ 90°** (자매 사이트 Primary 대비). 불가피하면 채도 격차 ≥ 40pp로 보완.
- **라이트·다크 쌍 필수**. 다크에선 Primary를 밝게 조정(예: 400 톤)해 배경 대비 ≥ 7:1 확보.
- **WCAG AA 4.5:1 이상** — 본문·링크에 쓰는 색은 무조건 통과. 배지 텍스트는 AA Large(3:1)도 허용하되 용도를 문서에 명시.
- **Secondary는 CTA/포인트 전용** — 본문 텍스트로 쓸 수 있는 대비가 아니면 "배경·구분선 전용"이라고 가이드라인에 박는다.

### 타이포
- **6단계 스케일** (Display / H1 / H2 / Body / Small / XSmall). 예외 추가는 합당한 근거 필요.
- **한글+영문 페어링** 명시. 무료/오픈소스 폰트 우선 (Pretendard, Gowun Batang, Inter, Lora, JetBrains Mono).
- 수치·벤치마크 중심 브랜드는 **Mono 폰트를 한 단계로 편입**(예: AIGrit "Num" 행).
- 세리프 vs 산세리프 선택은 **브랜드 카테고리 구별 신호**로 쓴다 (babipanote 세리프 헤딩 ↔ AIGrit 전체 산세).

### 토큰
- **Tailwind v4 CSS-first** — `@theme` 블록에 `--color-brand-*`, `--font-*`, `--text-*` 토큰으로 선언. `tailwind.config.ts` 만들지 않는다.
- **다크는 `.dark` 스코프에서 같은 변수명 재지정** — 컴포넌트 코드는 토큰명만 참조, 테마 분기 없음.
- **토큰 네이밍**: `{브랜드|중립}.{역할}` (예: `brand.primary`, `accent.green`, `neutral.ink`). kebab-case CSS 변수로 내보낼 때 `--color-brand-primary`.

### 로고
- **최소 3 배리언트**: Primary (라이트 bg) / Dark (다크 bg) / Reverse (브랜드 컬러 bg에 흰색).
- **Mark-only 별도 제작** — 파비콘·SNS 프로필용.
- **클리어 스페이스 = x (로고 구성 요소 1칸)**. 문서에 시각 예시 필수.
- **최소 크기**를 웹 픽셀·인쇄 mm 양쪽으로 명시.

### 디지털
- **OG 1200×630 / Twitter 1500×500 / Favicon 32·16·180**이 기본 세트.
- OG는 **Default + Article Template** 둘 이상. 라이트·다크 쌍이면 4장.
- 메타 태그 HTML 스니펫을 가이드라인 MD에 복붙 가능한 형태로 포함.
- `theme-color` 메타 2줄 (라이트·다크 `prefers-color-scheme`) 필수.

### 산출물 톤
- 가이드라인 MD 끝에 **🔴/🟢/⚪ 3관점 검증** 섹션과 **다음 단계** 섹션을 반드시 붙인다.
- Figma 파일은 **Cover 페이지에 브랜드명·버전·날짜**를 올려 첫 프리뷰만 봐도 식별 가능하게 한다.

---

## Phase 연동

모노레포 Phase 워크플로우(`docs/MONOREPO_MIGRATION.md`)와의 관계:

| Phase | 디자인 산출물이 하는 일 |
|---|---|
| **1-1** `packages/blog-core/types/brand.ts` | 가이드라인 MD의 스키마(컬러 5색 키, 타이포 6단계, 네비, 소셜)를 타입으로 인코딩 |
| **1-2** `apps/*/brand.config.ts` | 가이드라인 MD의 값들을 런타임 소스로 이관 |
| **1-3** `apps/*/src/app/globals.css` + `BrandProvider` | `@theme` 블록을 앱에 주입. Phase 0-2 placeholder 교체 |
| **1-3 완료 후** | `brand-preview.jsx` + `src/app/preview/page.tsx` 삭제 (임시 산출물) |

디자인 산출물은 **Phase 1의 입력값**이며, Phase 1이 끝나면 프리뷰는 폐기한다.

---

## Tools

| 상황 | 도구 |
|---|---|
| 가이드라인 MD · JSX 프리뷰 | `Write`, `Edit` |
| 브랜드 전체 파이프라인 오프로드 | Skill `/brand-architect` |
| Figma 파일 신규 생성 | `mcp__claude_ai_Figma__create_new_file` (planKey: `team::1619263955043772507`) |
| Figma 파일에 콘텐츠 작성 | `mcp__claude_ai_Figma__use_figma` (JS 스크립트, ≤50k 문자/콜 — 필요시 분할) |
| 기존 Figma 디자인 읽기 | `mcp__claude_ai_Figma__get_design_context`, `get_metadata` |
| 로컬 프리뷰 검증 | `pnpm dev --filter=@unpack/{brand} -- --port <3100+>` → `/preview` 라우트 |
| 라이브러리 문서 최신화 | `mcp__context7__resolve-library-id` → `query-docs` (Tailwind v4, Next.js 16 등) |

### Figma 사용 팁 (재발견한 것)
- 폰트 로드는 항상 try/catch + Inter 폴백. Pretendard·Gowun Batang·JetBrains Mono는 워크스페이스에 미동기화된 경우 많음.
- Inter "Semi Bold"는 공백 포함. "SemiBold" 아님. "Extra Bold"도 마찬가지.
- `figma.currentPage` 직접 할당 불가 → `await figma.setCurrentPageAsync(page)` 사용.
- 한 스크립트가 50k 문자를 넘으면 페이지 단위로 분할 (Cover/StyleGuide → Logo/Avatar/Favicon → Social/OG/Watermark 3분할이 경험적으로 안정).

---

## 관련 파일

- `docs/DESIGN_CHECKLIST.md` — 커밋 전 체크리스트
- `apps/*/docs/BRAND_GUIDELINES.md` — 브랜드별 가이드라인 (참조 기준 샘플)
- `packages/blog-core/types/brand.ts` — (Phase 1-1) 브랜드 스키마 타입
- `.claude/commands/brand-architect.md` — `/brand-architect` 스킬 정의
