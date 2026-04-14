# CLAUDE.md — UnpackBlogs Monorepo

## 프로젝트 개요
- 프로젝트명: unpack-blogs (모노레포)
- 목적: AIGrit + babipanote 두 블로그를 하나의 코드베이스로 운영
- 구조: Turborepo 모노레포 (공유 엔진 + 사이트별 앱)

### 사이트별 정체성

| | AIGrit (aigrit.dev) | babipanote (babipanote.com) |
|---|---|---|
| 포지션 | AI 도구 리뷰 블로그 | 바비파의 빌더 저널 |
| 톤 | 전문적, 비판적, 리뷰체 | 개인적, 솔직, 일기체 |
| 타겟 | AI 입문자, 생산성 덕후 | 인디해커, 1인 창업자 |
| 수익 | 애드센스 + SaaS 제휴 | 최소 (브랜드 자산 축적) |
| 레이아웃 | 카테고리 중심, 검색 강조 | 타임라인형, 연대기 |

## 기술 스택
- 모노레포: Turborepo + pnpm workspaces
- 프레임워크: Next.js 16 (App Router, TypeScript) — 참고: `apps/*/AGENTS.md`
- 콘텐츠: MDX (next-mdx-remote + gray-matter)
- 스타일: Tailwind CSS + @tailwindcss/typography
- 배포: GitHub → Vercel (사이트별 프로젝트)
- 분석: GA4 + Vercel Analytics
- 댓글: Giscus (GitHub Discussions 기반)
- 도메인: Vercel Domains (aigrit.dev, babipanote.com)

## 프로젝트 구조

### 현재 구조 (Phase 0-1 / 0-2 / 1 완료 기준)

지금 실제로 존재하는 파일만 기술. 빈 디렉토리는 표기 생략. 단계별 계획은 `docs/MONOREPO_MIGRATION.md` 참조.

```
unpack-blogs/
├── turbo.json
├── pnpm-workspace.yaml
├── package.json                    # 루트 (워크스페이스 + turbo 스크립트)
├── pnpm-lock.yaml
├── .env.example
├── .gitignore
├── CLAUDE.md                       # 이 파일
├── docs/
│   └── MONOREPO_MIGRATION.md       # 모노레포 전환 아카이브
├── .github/
│   └── workflows/ci.yml            # pnpm + turbo (lint + build)
│
├── packages/
│   └── blog-core/                  # 공유 엔진 (@unpack/blog-core)
│       ├── package.json
│       ├── tsconfig.json
│       ├── index.ts                # barrel export
│       ├── lib/
│       │   ├── mdx.ts              # parseMdxFile (gray-matter + reading-time)
│       │   ├── posts.ts            # getAllPosts / getPostBySlug (contentDir 주입)
│       │   └── seo.ts              # buildMetadata (Next Metadata + OG/Twitter)
│       ├── contexts/
│       │   └── brand-context.tsx   # BrandProvider / useBrand (Phase 1-3)
│       └── types/
│           ├── post.ts             # PostFrontmatter, Post, PostSummary
│           └── brand.ts            # BrandConfig 스키마 (Phase 1-1)
│
└── apps/
    ├── aigrit/                     # @unpack/aigrit
    │   ├── package.json · next.config.ts · tsconfig.json
    │   ├── eslint.config.mjs · postcss.config.mjs
    │   ├── brand.config.ts         # 브랜드 런타임 (Phase 1-2)
    │   ├── CLAUDE.md · AGENTS.md · README.md
    │   ├── content/posts/          # (비어있음)
    │   ├── public/{fonts,images}/
    │   ├── docs/                   # BRAND_GUIDELINES + 앱 가이드 6개
    │   ├── scripts/
    │   ├── .claude/commands/       # 앱 스코프 커맨드 10개
    │   └── src/
    │       └── app/
    │           ├── layout.tsx      # BrandProvider + 폰트 (Pretendard/Inter/JetBrains)
    │           ├── page.tsx        # Next 기본 템플릿 (Phase 2에서 교체)
    │           ├── globals.css     # Tailwind v4 @theme — AIGrit 팔레트
    │           └── favicon.ico
    │
    └── babipanote/                 # @unpack/babipanote
        ├── package.json · next.config.ts
        ├── brand.config.ts         # 브랜드 런타임 (Phase 1-2)
        ├── CLAUDE.md · AGENTS.md · README.md
        ├── content/posts/          # (비어있음)
        ├── public/
        ├── docs/BRAND_GUIDELINES.md
        ├── .claude/commands/       # 앱 스코프 커맨드 10개
        └── src/
            └── app/
                ├── layout.tsx      # BrandProvider + 폰트 (Pretendard/Inter/Gowun Batang/Lora/JetBrains)
                ├── page.tsx        # ⚠️ aigrit 사본 — Phase 2에서 타임라인 홈으로 교체
                ├── globals.css     # Tailwind v4 @theme — babipanote 팔레트
                └── favicon.ico
```

### 목표 구조 (Phase 3 완료 후)

Phase 1~3이 끝나면 아래 구조로 수렴. 각 미구현 항목에는 도입 Phase를 명시.

```
unpack-blogs/
├── turbo.json · pnpm-workspace.yaml · package.json
├── .env.example · .gitignore · CLAUDE.md
├── docs/MONOREPO_MIGRATION.md
├── .github/workflows/ci.yml
│
├── packages/
│   └── blog-core/
│       ├── index.ts · package.json · tsconfig.json
│       ├── lib/{mdx,posts,seo}.ts
│       ├── types/
│       │   ├── post.ts
│       │   └── brand.ts                           # (Phase 1-1)
│       ├── contexts/
│       │   └── brand-context.tsx                  # BrandProvider (Phase 1-3)
│       ├── components/
│       │   ├── blog/                              # (Phase 2+) PostCard, PostHeader,
│       │   │                                      #   TableOfContents, RelatedPosts, Comments
│       │   ├── mdx/                               # (Phase 2+) Callout, CompareTable,
│       │   │                                      #   ProCon, AffiliateLink
│       │   └── ads/                               # (Phase 2+) AdBanner, AdInArticle
│       └── hooks/                                 # (Phase 2+) use-dark-mode,
│                                                  #   use-reading-progress
│
└── apps/
    ├── aigrit/
    │   ├── brand.config.ts                        # (Phase 1-2)
    │   ├── tailwind.config.ts                     # (Phase 1-3)
    │   ├── content/posts/*.mdx
    │   ├── public/{favicon.ico, og-default.png, images/}
    │   └── src/
    │       ├── app/
    │       │   ├── layout.tsx                     # BrandProvider 래핑 (Phase 1-3)
    │       │   ├── page.tsx                       # (Phase 2) 홈 — 최신 글 + 카테고리
    │       │   ├── blog/{page.tsx, [slug]/page.tsx}  # (Phase 2)
    │       │   ├── about/privacy/disclaimer/page.tsx  # (Phase 2)
    │       │   ├── sitemap.ts · robots.ts         # (Phase 2)
    │       │   └── globals.css
    │       └── components/
    │           └── layout/                        # (Phase 2) Header, Footer, Sidebar
    │
    └── babipanote/
        ├── brand.config.ts                        # (Phase 1-2)
        ├── tailwind.config.ts                     # (Phase 1-3)
        ├── content/posts/*.mdx
        ├── public/{favicon.ico, og-default.png, images/}
        └── src/
            ├── app/
            │   ├── layout.tsx                     # BrandProvider (Phase 1-3)
            │   ├── page.tsx                       # (Phase 2) 타임라인형 홈
            │   ├── blog/{page.tsx, [slug]/page.tsx}
            │   ├── projects/page.tsx              # (Phase 2-1) AIGrit + GentleLab 소개
            │   ├── about/page.tsx
            │   └── sitemap.ts · robots.ts
            └── components/
                └── layout/                        # (Phase 2-1) Header, Footer (사이드바 없음)
```

## 코딩 컨벤션
- 언어: TypeScript strict mode
- 린터: ESLint + Prettier
- 패키지 매니저: pnpm (워크스페이스)
- 컴포넌트: 함수형 컴포넌트 + React Hooks
- 네이밍:
  - 파일: kebab-case (예: post-card.tsx)
  - 컴포넌트: PascalCase (예: PostCard)
  - 함수/변수: camelCase (예: getAllPosts)
  - 상수: UPPER_SNAKE_CASE (예: DEFAULT_OG_IMAGE)
  - 타입: PascalCase (예: PostFrontmatter)

## 핵심 규칙

### 공유 코드 (packages/blog-core/)
- 사이트 특화 로직 금지 — brand.config.ts에서 주입
- 모든 컴포넌트는 className prop 수용 (Tailwind 오버라이드 가능)
- 광고 컴포넌트는 enabled prop으로 on/off 제어
- 색상은 CSS 변수 또는 Tailwind 테마 토큰 사용 (하드코딩 금지)

### 사이트별 앱 (apps/aigrit/, apps/babipanote/)
- 글은 각 앱의 content/posts/*.mdx에 추가
- 브랜드 설정은 brand.config.ts에서만 관리
- 레이아웃 컴포넌트만 사이트별로 커스텀
- blog-core 컴포넌트를 import하여 조합

### 환경변수
- .env.local은 절대 커밋 금지
- 사이트별 환경변수는 Vercel 프로젝트에서 각각 설정
- NEXT_PUBLIC_ 접두사가 없는 변수는 서버 전용

## 환경변수

루트 `.env.example`이 단일 소스. 로컬 개발 시 작업 대상 앱의 변수만 `.env.local`에 채우면 됨. Vercel에서는 각 프로젝트에 별도 설정.

### AIGrit (aigrit.dev)
- `NEXT_PUBLIC_GA_ID` — GA4 측정 ID (analytics.google.com)
- `NEXT_PUBLIC_ADSENSE_ID` — 애드센스 Publisher ID (adsense.google.com)
- `NEXT_PUBLIC_GISCUS_REPO` — 댓글용 GitHub 저장소 (giscus.app)
- `NEXT_PUBLIC_GISCUS_REPO_ID` — Giscus 저장소 ID
- `NEXT_PUBLIC_GISCUS_CATEGORY` — Giscus 카테고리명
- `NEXT_PUBLIC_GISCUS_CATEGORY_ID` — Giscus 카테고리 ID
- `NEXT_PUBLIC_SITE_URL` — `https://aigrit.dev`

### babipanote (babipanote.com)
광고 비활성 — AdSense 변수 없음.
- `NEXT_PUBLIC_GA_ID` — GA4 측정 ID (AIGrit과 별도)
- `NEXT_PUBLIC_GISCUS_REPO` / `..._REPO_ID` / `..._CATEGORY` / `..._CATEGORY_ID` — 별도 저장소
- `NEXT_PUBLIC_SITE_URL` — `https://babipanote.com`

## Vercel 배포 설정
- GitHub 모노레포 1개 → Vercel 프로젝트 2개
- AIGrit 프로젝트: Root Directory = `apps/aigrit`
- babipanote 프로젝트: Root Directory = `apps/babipanote`
- 둘 다 `packages/blog-core` 변경 시 자동 재배포 (Turborepo 감지)

## 브랜드 설정 (brand.config.ts)
- 각 앱의 brand.config.ts에서 사이트명, 설명, 컬러, 네비게이션, 소셜 링크 등 정의
- blog-core 컴포넌트는 이 설정을 props 또는 context로 주입받아 사용
- 자세한 스키마는 packages/blog-core/types/brand.ts 참조

## MDX 글 포맷 (frontmatter)

```yaml
---
title: "글 제목"
date: "2026-04-14"
slug: "url-slug"
description: "150자 설명"
tags: ["태그1", "태그2"]
thumbnail: "/images/thumbnail.png"
featured: false
category: "카테고리명"
---
```

## 주의사항
- blog-core 수정 시 양쪽 사이트 모두 영향 — 반드시 양쪽 빌드 확인
- `turbo run build`로 전체 빌드 테스트 후 push
- 이미지는 각 앱의 public/images/에 관리 (공유 이미지 없음)
- MDX 커스텀 컴포넌트 추가 시 blog-core/components/mdx/에 작성
