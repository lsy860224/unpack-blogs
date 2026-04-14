@AGENTS.md

# CLAUDE.md — AIGrit

> 상위 맥락(모노레포 전체 규칙)은 루트 `CLAUDE.md`를 먼저 읽으세요. 이 문서는 AIGrit 앱 특화 규칙만 다룹니다.

## 프로젝트 개요
- **제품명:** AIGrit (에이아이그릿)
- **도메인:** aigrit.dev
- **한 줄 설명:** AI 도구를 직접 써보고 솔직하게 비교하는 수익형 블로그
- **타겟 독자:** 직장인 AI 입문자 / 생산성 덕후 / 개발자
- **수익 구조:** Google AdSense + SaaS 제휴 마케팅 + 네이버 블로그 협찬
- **태그라인:** "AI의 알맹이만 남긴다"

## 기술 스택
- **프레임워크:** Next.js 16 (App Router, TypeScript) — 참고: `AGENTS.md`
- **콘텐츠:** MDX (Markdown + 커스텀 컴포넌트) via next-mdx-remote
- **스타일링:** Tailwind CSS + @tailwindcss/typography
- **공유 엔진:** `@unpack/blog-core` (`packages/blog-core/`)
- **배포:** GitHub → Vercel (AIGrit 프로젝트, Root Directory = `apps/aigrit`)
- **분석:** GA4 + Vercel Analytics
- **댓글:** Giscus (GitHub Discussions 기반, 무료)
- **도메인:** Vercel Domains (aigrit.dev)

## 코딩 컨벤션
- **언어:** TypeScript strict mode
- **린터:** ESLint + Prettier
- **컴포넌트:** 함수형 컴포넌트 + React Hooks
- **네이밍:**
  - 파일: kebab-case (예: post-card.tsx)
  - 컴포넌트: PascalCase (예: PostCard)
  - 함수/변수: camelCase (예: getAllPosts)
  - 상수: UPPER_SNAKE_CASE (예: SITE_CONFIG)
  - 타입: PascalCase (예: PostMeta, not IPostMeta)
- **import 순서:** react → next → 외부 라이브러리 → `@unpack/*` 공유 → `@/` 내부 → 상대 경로
- **export:** named export 기본. 페이지 컴포넌트만 default export

## 파일 구조 (목표 — 일부는 Phase별로 점진 도입)
현재 실제 상태는 루트 `CLAUDE.md`의 "현재 구조" 섹션과 `ls apps/aigrit/src`로 확인. 아래는 앱 완성 시 구조.

```
aigrit/
├── content/posts/              ← MDX 글 파일 (이 폴더만 터치하면 글 추가)
├── public/images/              ← 포스트별 이미지 (slug 폴더로 구분)
├── brand.config.ts             ← (Phase 1-2) 사이트 메타·컬러·네비·광고 on/off
├── tailwind.config.ts          ← (Phase 1-3) brand 토큰 기반 확장
├── src/
│   ├── app/                    ← Next.js App Router 페이지
│   │   ├── layout.tsx          ← 루트 레이아웃 (BrandProvider, GA4, AdSense, 폰트)
│   │   ├── page.tsx            ← (Phase 2) 홈 (최신 글 목록)
│   │   ├── blog/
│   │   │   ├── page.tsx        ← (Phase 2) 전체 글 목록
│   │   │   └── [slug]/page.tsx ← (Phase 2) 개별 글 페이지 (SSG)
│   │   ├── about/page.tsx      ← (Phase 2) E-E-A-T 핵심 페이지
│   │   ├── privacy/page.tsx    ← (Phase 2) 애드센스 필수
│   │   ├── disclaimer/page.tsx ← (Phase 2) 제휴 마케팅 고지
│   │   ├── sitemap.ts          ← (Phase 2) 자동 사이트맵
│   │   └── robots.ts           ← (Phase 2) robots.txt
│   └── components/
│       └── layout/             ← (Phase 2) Header, Footer, Sidebar, ThemeToggle
├── .env.local                  ← 환경변수 (절대 커밋 금지)
├── .env.example                ← 환경변수 템플릿
├── docs/                       ← 상세 설계 문서 (아래 참조)
├── scripts/setup.sh            ← 초기화 스크립트 (이미 수행됨)
└── CLAUDE.md                   ← 이 파일
```

> **공유 코드는 `@unpack/blog-core`로 이동:** `src/lib/{mdx,posts,seo}.ts`, `src/types/post.ts`, `src/components/{blog,mdx,ads}/*`는 더이상 앱 로컬이 아니라 `packages/blog-core/`에 있음. 앱에는 레이아웃 컴포넌트(`src/components/layout/`)와 페이지만 남음.

## 핵심 규칙
1. 글은 `content/posts/*.mdx`에만 추가한다
2. 새 MDX 컴포넌트는 `packages/blog-core/components/mdx/`에 추가한다 (사이트 특화 금지)
3. 광고 컴포넌트는 `packages/blog-core/components/ads/`에서만 관리한다. AIGrit에서 `brand.config.ts`의 `monetization.adsense = true`로 활성화
4. 환경변수(`.env.local`)는 **절대 커밋하지 않는다**
5. 이미지는 `public/images/{slug}/` 폴더에 포스트별로 구분한다
6. 모든 페이지에 SEO 메타태그를 포함한다 (`@unpack/blog-core`의 `buildMetadata` 사용)
7. 커밋 메시지: `post(aigrit): 글제목` / `feat(aigrit): 기능` / `fix(aigrit): 수정` / `style(aigrit): 스타일`

## 환경변수
| 변수명 | 용도 | 발급처 |
|--------|------|--------|
| NEXT_PUBLIC_GA_ID | GA4 트래픽 분석 | analytics.google.com |
| NEXT_PUBLIC_ADSENSE_ID | 애드센스 광고 | adsense.google.com |
| NEXT_PUBLIC_GISCUS_REPO | Giscus 저장소 | giscus.app |
| NEXT_PUBLIC_GISCUS_REPO_ID | Giscus 저장소 ID | giscus.app |
| NEXT_PUBLIC_GISCUS_CATEGORY | Giscus 카테고리명 | giscus.app |
| NEXT_PUBLIC_GISCUS_CATEGORY_ID | Giscus 카테고리 ID | giscus.app |
| NEXT_PUBLIC_SITE_URL | 사이트 URL | 직접 설정 (`https://aigrit.dev`) |

## 브랜드 (목표 — Phase 1-2에서 `brand.config.ts`로 이동 예정)
- **SNS:** X @aigrit_dev · Instagram @aigrit.dev · GitHub lsy860224/aigrit
- **Primary:** #1E293B (Slate-800) — 로고, 헤더, 주요 텍스트
- **Secondary:** #F59E0B (Amber-500) — CTA, 강조, 배지
- **Accent Red:** #EF4444 — "별로" 태그
- **Accent Green:** #10B981 — "추천" 태그
- **폰트:** Pretendard (한글) + Inter (영문) + JetBrains Mono (코드)
- **톤:** 전문적이지만 친근한. "같이 실험해보는 동료" 느낌
- **로고:** [AI]Grit 워드마크 — AI는 Amber, Grit은 Slate

## docs 폴더 참조 규칙
아래 상황에서 해당 docs 파일을 **반드시 읽고** 작업한다:

| 상황 | 읽을 파일 |
|------|----------|
| 프로젝트 최초 세팅, 패키지 설치 | `docs/SETUP.md` |
| MDX 파싱, 글 목록, frontmatter 작업 | `docs/MDX_ENGINE.md` |
| 컴포넌트 생성/수정 (layout, blog, mdx, ads) | `docs/COMPONENTS.md` |
| SEO 메타태그, 애드센스, 제휴링크 작업 | `docs/SEO_MONETIZATION.md` |
| Vercel 배포, 도메인, CI/CD 작업 | `docs/DEPLOYMENT.md` |
| 글 발행 (/publish-post 커맨드) | `docs/PUBLISH_WORKFLOW.md` |
| 앱 스케폴딩 단계 순서 확인 | `docs/APP_SCAFFOLDING_GUIDE.md` |
| 모노레포 전환 경위 확인 | 루트 `docs/MONOREPO_MIGRATION.md` |

## MDX frontmatter 포맷
```yaml
---
title: "글 제목"
date: "YYYY-MM-DD"
slug: "url-slug"
description: "150자 이내 설명"
tags: ["태그1", "태그2"]
thumbnail: "/images/{slug}/thumbnail.png"
featured: false
category: "카테고리명"
---
```

## 배포 워크플로우
```bash
git add apps/aigrit/content/posts/{slug}.mdx apps/aigrit/public/images/{slug}/
git commit -m "post(aigrit): 글제목"
git push origin main
# → Vercel AIGrit 프로젝트 (Root Directory = apps/aigrit) 자동 빌드
# → packages/blog-core 변경 시에도 Turborepo가 감지해 재배포 (1~2분)
# → aigrit.dev에 반영
```

## 로컬 개발
모노레포 루트(`unpack-blogs/`)에서:
```bash
pnpm install                               # 한 번만
pnpm dev --filter=@unpack/aigrit           # AIGrit 개발 서버
pnpm turbo run build --filter=@unpack/aigrit  # 빌드 테스트
pnpm turbo run build                       # 양쪽 앱 전체 빌드 (blog-core 변경 시 권장)
```
