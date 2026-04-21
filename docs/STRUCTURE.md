# 프로젝트 구조 — UnpackBlogs

## 현재 구조

```
unpack-blogs/
├── CLAUDE.md                       # Claude Code 프로젝트 컨텍스트
├── DESIGN.md                       # 디자인 에이전트 운영 매뉴얼
├── turbo.json · pnpm-workspace.yaml · package.json
├── .env.example · .gitignore
├── docs/
│   ├── STRUCTURE.md                # 이 파일
│   ├── ENV.md                      # 환경변수 가이드
│   ├── HOOKS_RULES.md              # Hooks·Rules 상세
│   ├── DESIGN_CHECKLIST.md         # 디자인 커밋 전 체크리스트
│   └── MONOREPO_MIGRATION.md       # 모노레포 전환 아카이브
├── .github/workflows/ci.yml
├── .claude/
│   ├── commands/                   # 슬래시 커맨드 10개
│   ├── hooks/                      # Hook 스크립트 7개
│   ├── rules/                      # 파일별 규칙 8개
│   ├── settings.json               # Hooks 등록 (git 커밋)
│   └── settings.local.json         # 권한 설정 (gitignore)
│
├── packages/
│   └── blog-core/                  # 공유 엔진 (@unpack/blog-core)
│       ├── index.ts                # barrel export
│       ├── lib/
│       │   ├── mdx.ts              # parseMdxFile (gray-matter + reading-time)
│       │   ├── posts.ts            # getAllPosts / getPostBySlug
│       │   ├── seo.ts              # buildMetadata (OG/Twitter)
│       │   ├── jsonld.ts           # Article / FAQ / WebSite JSON-LD
│       │   └── toc.ts              # extractHeadings
│       ├── contexts/
│       │   └── brand-context.tsx   # BrandProvider / useBrand
│       ├── components/
│       │   ├── blog/               # PostCard, PostHeader, PostRenderer,
│       │   │                       # Comments, RelatedPosts, TableOfContents
│       │   ├── mdx/                # Callout, CompareTable, ProCon,
│       │   │                       # AffiliateLink, defaultMdxComponents
│       │   ├── ads/                # AdBanner, AdInArticle
│       │   └── analytics/          # GoogleAnalytics, AdSenseScript
│       └── types/
│           ├── post.ts             # PostFrontmatter, Post, PostSummary
│           └── brand.ts            # BrandConfig 스키마
│
└── apps/
    ├── aigrit/                     # @unpack/aigrit
    │   ├── brand.config.ts
    │   ├── CLAUDE.md · AGENTS.md
    │   ├── content/posts/*.mdx
    │   ├── public/{fonts,images}/
    │   ├── docs/BRAND_GUIDELINES.md
    │   ├── .claude/commands/       # 앱 스코프 커맨드
    │   └── src/app/
    │       ├── layout.tsx          # BrandProvider + GA4/AdSense
    │       ├── page.tsx            # Latest + By Category 홈
    │       ├── blog/[slug]/page.tsx
    │       ├── about · privacy · disclaimer
    │       ├── sitemap.ts · robots.ts
    │       └── globals.css         # @theme — Indigo 팔레트
    │
    └── babipanote/                 # @unpack/babipanote
        ├── brand.config.ts
        ├── CLAUDE.md · AGENTS.md
        ├── content/posts/*.mdx
        ├── docs/BRAND_GUIDELINES.md
        ├── .claude/commands/
        └── src/app/
            ├── layout.tsx          # BrandProvider + 폰트 5종
            ├── page.tsx            # 연도별 타임라인 홈
            ├── blog/[slug]/page.tsx
            ├── projects · about
            └── globals.css         # @theme — Plum 팔레트
```

## Phase 계획

상세는 `MONOREPO_MIGRATION.md` 참조. 현재 Phase 2.5 완료.

| Phase | 산출물 | 상태 |
|---|---|---|
| 0 | Next.js + Turborepo 초기화 | ✅ |
| 1 | BrandConfig 타입 + brand.config.ts + BrandProvider | ✅ |
| 2 | 블로그 엔진 (MDX, PostCard, 라우팅) | ✅ |
| 2.5 | SEO, 광고, 댓글, JSON-LD, 정적 페이지 | ✅ |
| 3 | 다크모드, RelatedPosts 고도화, EN 콘텐츠 | 예정 |
