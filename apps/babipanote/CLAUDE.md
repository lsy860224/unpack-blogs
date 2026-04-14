@AGENTS.md

# CLAUDE.md — babipanote

> 상위 맥락(모노레포 전체 규칙)은 루트 `CLAUDE.md`를 먼저 읽으세요. 이 문서는 babipanote 앱 특화 규칙만 다룹니다.

## 프로젝트 개요
- **사이트명:** babipanote (바비파노트)
- **도메인:** babipanote.com
- **한 줄 설명:** 1인 개발자 바비파의 빌더 저널 — 만드는 과정을 기록
- **타겟 독자:** 인디해커, 1인 창업자, 사이드 프로젝트 빌더
- **포지션:** 브랜드 자산 축적 (수익 최소)
- **톤:** 개인적, 솔직, 일기체
- **레이아웃:** 타임라인형 (연대기 스크롤, 사이드바 없음)
- **태그라인:** "만드는 과정을 기록합니다"

## 기술 스택
aigrit과 동일 (루트 `CLAUDE.md` 참조). babipanote 특화 차이점:
- **광고 없음** — AdSense 연동 / `AdBanner`·`AdInArticle` 비활성 (`brand.config.ts`의 `monetization.adsense = false`로 제어 예정, Phase 1)
- **제휴링크 비활성** — `AffiliateLink` 컴포넌트 비활성 (Phase 1)
- **Header 미니멀** — 검색 UI 없음
- **홈 레이아웃** — 카테고리 없이 날짜순 타임라인

## 현재 상태 (Phase 1 완료)
Phase 0-1 / 0-2 모노레포 전환 + Phase 1 브랜드 분리 완료. 페이지·레이아웃 컴포넌트·콘텐츠는 Phase 2에서.

```
apps/babipanote/
├── package.json                # @unpack/babipanote
├── next.config.ts              # transpilePackages: ["@unpack/blog-core"]
├── brand.config.ts             # 브랜드 런타임 설정 (Phase 1-2)
├── tsconfig.json
├── eslint.config.mjs · postcss.config.mjs
├── CLAUDE.md · AGENTS.md · README.md
├── content/posts/              # (비어있음 — Phase 2에서 첫 글)
├── public/{fonts,images}/
├── docs/BRAND_GUIDELINES.md    # 브랜드 설계 문서
├── .claude/commands/           # 앱 스코프 커맨드 (publish-post 등)
└── src/
    └── app/
        ├── layout.tsx          # BrandProvider + 폰트(Pretendard/Inter/Gowun Batang/Lora/JetBrains)
        ├── page.tsx            # ⚠️ Next 기본 템플릿 — Phase 2에서 타임라인 홈으로 교체
        ├── globals.css         # Tailwind v4 @theme — babipanote 팔레트 (Phase 1-3)
        └── favicon.ico
```

## 코딩 컨벤션
루트 `CLAUDE.md`의 컨벤션을 그대로 따름. 추가 제약 없음.

## 핵심 규칙
1. 글은 `content/posts/*.mdx`에만 추가한다
2. 새 MDX 컴포넌트는 `@unpack/blog-core/components/mdx/`에 추가한다 (사이트 특화 금지)
3. 광고 컴포넌트는 babipanote에서 **절대 사용하지 않는다** (AdSense 미연동)
4. 환경변수(`.env.local`)는 **절대 커밋하지 않는다**
5. 이미지는 `public/images/{slug}/` 폴더에 포스트별로 구분한다
6. 모든 페이지에 SEO 메타태그를 포함한다 (`@unpack/blog-core`의 `buildMetadata` 사용)
7. 커밋 메시지: `post(babipanote): 글제목` / `feat(babipanote): 기능` / `fix(babipanote): 수정`

## 환경변수
광고 미연동이므로 `NEXT_PUBLIC_ADSENSE_ID` 없음. 나머지 변수는 AIGrit과 동일하되 **별도 값** 사용.

| 변수명 | 용도 |
|---|---|
| `NEXT_PUBLIC_GA_ID` | GA4 측정 ID (babipanote 전용) |
| `NEXT_PUBLIC_GISCUS_REPO` | Giscus 댓글용 GitHub 저장소 (별도) |
| `NEXT_PUBLIC_GISCUS_REPO_ID` | Giscus 저장소 ID |
| `NEXT_PUBLIC_GISCUS_CATEGORY` | Giscus 카테고리명 |
| `NEXT_PUBLIC_GISCUS_CATEGORY_ID` | Giscus 카테고리 ID |
| `NEXT_PUBLIC_SITE_URL` | `https://babipanote.com` |

## 브랜드 (`brand.config.ts` + `docs/BRAND_GUIDELINES.md` 참조)
디자인 컨셉: **잉크와 종이 (Ink & Paper)** — 책·저널·원고지. AIGrit(Indigo+Cyan, 계측기)의 대척점. 전체 팔레트·타이포·로고 규격은 `docs/BRAND_GUIDELINES.md`, 런타임 값은 `brand.config.ts`.

- **톤:** 솔직한 1인 개발자 일기. "결과보다 과정", "실패도 공유" — 인칭 "나" 기본
- **Primary:** `#6B2E4E` (Plum) — 제목, 링크, 브랜드
- **Secondary:** `#C89F7C` (Terracotta) — 배지·구분선 배경 (텍스트 금지)
- **Accent Green:** `#6B8A63` — "완료" · "출시" 배지
- **Accent Red:** `#9C4A3E` — "실패" · "중단" 배지
- **Neutral:** Ink `#2B2420` / Paper `#FAF7F2`
- **폰트:** 헤딩 Gowun Batang (한글) + Lora (영문) **세리프** / 본문 Pretendard + Inter / 코드 JetBrains Mono
- **네비게이션:** Home · Blog · Projects · About

## docs 폴더 참조 규칙

| 상황 | 읽을 파일 |
|---|---|
| 브랜드 팔레트·타이포·로고·OG 규격 | `docs/BRAND_GUIDELINES.md` |
| MDX 파싱/글 목록/frontmatter | `apps/aigrit/docs/MDX_ENGINE.md` (공용 동작) |
| SEO 메타·구조화 데이터 | `apps/aigrit/docs/SEO_MONETIZATION.md` (광고 섹션은 skip) |
| Vercel 배포·CI | `apps/aigrit/docs/DEPLOYMENT.md` (모노레포 공통) |
| 글 발행 워크플로우 | `apps/aigrit/docs/PUBLISH_WORKFLOW.md` (공용) + 앱별 publish-post 커맨드 |
| 타임라인 홈·Projects 페이지 등 babipanote 특화 | Phase 2에서 신규 작성 예정 |

## 배포 워크플로우
```bash
git add .
git commit -m "post(babipanote): 글제목"
git push origin main
# → Vercel babipanote 프로젝트 (Root Directory = apps/babipanote) 자동 빌드
# → packages/blog-core 변경 시에도 Turborepo가 감지해 재배포
```

## 주의
- babipanote 작업 시 aigrit 문서(`apps/aigrit/docs/*`)를 참고할 수 있지만 **AIGrit 고유 전략(애드센스 최적화, 제휴 링크 등)은 적용하지 않는다**.
- `src/app/layout.tsx`와 `page.tsx`는 현재 aigrit 사본이므로 Phase 2 전까지 렌더 결과가 AIGrit으로 보일 수 있음. 브랜드 분리(Phase 1)와 babipanote 레이아웃(Phase 2) 이후 정상화.
