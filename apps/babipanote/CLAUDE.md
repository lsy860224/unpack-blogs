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

## 현재 상태 (2026-04-15)
Phase 0-1 / 0-2 모노레포 전환만 완료. babipanote 앱의 실제 UI·콘텐츠는 미착수.

```
apps/babipanote/
├── package.json                # @unpack/babipanote
├── next.config.ts              # transpilePackages: ["@unpack/blog-core"]
├── tsconfig.json
├── eslint.config.mjs · postcss.config.mjs
├── CLAUDE.md · AGENTS.md · README.md
├── content/posts/              # (비어있음 — Phase 2에서 첫 글)
├── public/{fonts,images}/      # fonts는 aigrit와 동일 Pretendard, images는 비어있음
├── .claude/commands/           # 앱 스코프 커맨드 (publish-post 등)
└── src/
    └── app/
        ├── layout.tsx          # ⚠️ 현재 aigrit 사본 — Phase 2에서 babipanote 브랜드로 교체
        ├── page.tsx            # ⚠️ Next 기본 템플릿 — Phase 2에서 타임라인 홈으로 교체
        ├── globals.css
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

## 브랜드 (목표 — Phase 1에서 `brand.config.ts`로 이동 예정)
- **톤:** 솔직한 1인 개발자 일기. "결과보다 과정", "실패도 공유"
- **컬러:** Primary `#8B5CF6` (Violet) · Secondary `#F97316` (Orange) · Accent `#06B6D4` (Cyan)
- **폰트:** Pretendard (한글) + Inter (영문) + JetBrains Mono (코드)
- **네비게이션:** Home · Blog · Projects · About

## docs 폴더
현재 없음. Phase 2에서 babipanote 특화 주제(타임라인 홈 구조, Projects 페이지, 브랜드 자산 전략 등)만 선별 작성. aigrit과 공통되는 주제(MDX 엔진, SEO 골격, blog-core API)는 `apps/aigrit/docs/`의 문서를 참조로 링크.

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
