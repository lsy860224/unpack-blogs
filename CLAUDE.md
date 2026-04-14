# CLAUDE.md — AIGrit

## 프로젝트 개요
- **제품명:** AIGrit (에이아이그릿)
- **도메인:** aigrit.dev
- **한 줄 설명:** AI 도구를 직접 써보고 솔직하게 비교하는 수익형 블로그
- **타겟 독자:** 직장인 AI 입문자 / 생산성 덕후 / 개발자
- **수익 구조:** Google AdSense + SaaS 제휴 마케팅 + 네이버 블로그 협찬
- **태그라인:** "AI의 알맹이만 남긴다"

## 기술 스택
- **프레임워크:** Next.js 15 (App Router, TypeScript)
- **콘텐츠:** MDX (Markdown + 커스텀 컴포넌트) via next-mdx-remote
- **스타일링:** Tailwind CSS + @tailwindcss/typography
- **배포:** GitHub → Vercel 자동 배포 (git push → 1~2분 라이브)
- **분석:** GA4 + Vercel Analytics
- **댓글:** Giscus (GitHub Discussions 기반, 무료)
- **도메인:** Namecheap (aigrit.dev)

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
- **import 순서:** react → next → 외부 라이브러리 → @/ 내부 → 상대 경로
- **export:** named export 기본. 페이지 컴포넌트만 default export

## 파일 구조
```
aigrit/
├── content/posts/              ← MDX 글 파일 (이 폴더만 터치하면 글 추가)
├── public/images/              ← 포스트별 이미지 (slug 폴더로 구분)
├── src/
│   ├── app/                    ← Next.js App Router 페이지
│   │   ├── layout.tsx          ← 루트 레이아웃 (GA4, AdSense, 폰트)
│   │   ├── page.tsx            ← 홈 (최신 글 목록)
│   │   ├── blog/
│   │   │   ├── page.tsx        ← 전체 글 목록
│   │   │   └── [slug]/page.tsx ← 개별 글 페이지 (SSG)
│   │   ├── about/page.tsx      ← E-E-A-T 핵심 페이지
│   │   ├── privacy/page.tsx    ← 애드센스 필수
│   │   ├── disclaimer/page.tsx ← 제휴 마케팅 고지
│   │   ├── sitemap.ts          ← 자동 사이트맵
│   │   └── robots.ts           ← robots.txt
│   ├── components/
│   │   ├── layout/             ← Header, Footer, ThemeToggle
│   │   ├── blog/               ← PostCard, PostHeader, TOC, RelatedPosts, Comments
│   │   ├── mdx/                ← AffiliateLink, CompareTable, Callout, ProCon
│   │   └── ads/                ← AdBanner, AdInArticle
│   ├── lib/
│   │   ├── mdx.ts              ← MDX 파싱 + frontmatter 추출
│   │   ├── posts.ts            ← 글 목록 조회 유틸
│   │   └── seo.ts              ← OG/메타태그 생성 헬퍼
│   └── types/
│       └── post.ts             ← PostMeta, PostData 타입
├── .env.local                  ← 환경변수 (절대 커밋 금지)
├── .env.example                ← 환경변수 템플릿
├── docs/                       ← 상세 설계 문서 (아래 참조)
├── scripts/setup.sh            ← 초기화 스크립트
└── CLAUDE.md                   ← 이 파일
```

## 핵심 규칙
1. 글은 `content/posts/*.mdx`에만 추가한다
2. 새 MDX 컴포넌트는 `src/components/mdx/`에 추가한다
3. 광고 컴포넌트는 `src/components/ads/`에서만 관리한다
4. 환경변수(.env.local)는 **절대 커밋하지 않는다**
5. 이미지는 `public/images/{slug}/` 폴더에 포스트별로 구분한다
6. 모든 페이지에 SEO 메타태그를 포함한다 (lib/seo.ts 사용)
7. 커밋 메시지: `post: 글제목` / `feat: 기능` / `fix: 수정` / `style: 스타일`

## 환경변수
| 변수명 | 용도 | 발급처 |
|--------|------|--------|
| NEXT_PUBLIC_GA_ID | GA4 트래픽 분석 | analytics.google.com |
| NEXT_PUBLIC_ADSENSE_ID | 애드센스 광고 | adsense.google.com |
| NEXT_PUBLIC_GISCUS_REPO | 댓글 시스템 | giscus.app |
| NEXT_PUBLIC_GISCUS_REPO_ID | Giscus 저장소 ID | giscus.app |
| NEXT_PUBLIC_GISCUS_CATEGORY_ID | Giscus 카테고리 ID | giscus.app |
| NEXT_PUBLIC_SITE_URL | 사이트 URL | 직접 설정 |

## 브랜드
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
| 단계별 구현 순서 확인 | `docs/IMPLEMENTATION_GUIDE.md` |

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
---
```

## 배포 워크플로우
```bash
git add .
git commit -m "post: 글제목"
git push origin main
# → Vercel 자동 빌드 + 배포 (1~2분)
# → aigrit.dev에 즉시 반영
```
