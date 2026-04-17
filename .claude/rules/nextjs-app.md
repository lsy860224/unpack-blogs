---
description: Rules for Next.js App Router pages
globs: ["apps/*/src/app/**/*.tsx", "apps/*/src/app/**/*.ts"]
---

# Next.js App Router 규칙

## 라우팅
- App Router 사용 (Pages Router 금지)
- 정적 생성(SSG) 기본: generateStaticParams 활용
- 동적 렌더링은 명시적으로만 (export const dynamic = 'force-dynamic')

## SEO
- 모든 page.tsx에 generateMetadata 또는 metadata export 필수
- OG 이미지: opengraph-image.tsx 또는 thumbnail frontmatter
- sitemap.ts의 lastModified: post.updated || post.date 사용

## 레이아웃
- layout.tsx에서 BrandProvider 래핑
- 폰트 로딩은 layout.tsx에서만 (next/font)
- GA4, AdSense 스크립트는 layout.tsx에서 조건부 렌더링

## 금지
- 'use client' 최소화 — 서버 컴포넌트 기본
- inline style 금지 — Tailwind 클래스 사용
- .env 값 직접 참조 금지 — brand.config 또는 환경변수 헬퍼 경유
