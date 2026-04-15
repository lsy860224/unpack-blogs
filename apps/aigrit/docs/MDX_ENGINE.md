# MDX_ENGINE.md — MDX 콘텐츠 엔진 상세 설계

> MDX 파싱, frontmatter, 글 목록 조회, 검색, 태그 필터링 관련 모든 로직.
> **모노레포 배치:** 파싱·목록 조회·타입은 **공유 엔진** `@unpack/blog-core`로 추출됨. 앱은 import만. 렌더링(서버 컴포넌트 compileMDX)과 컴포넌트 매핑은 **앱 특화**라 `apps/aigrit/src/lib/`에 남음(Phase 2에서 구현).

## 핵심 파일

```
packages/blog-core/lib/mdx.ts      ← parseMdxFile (frontmatter + reading-time)
packages/blog-core/lib/posts.ts    ← getAllPosts / getPostBySlug (contentDir 주입)
packages/blog-core/types/post.ts   ← PostFrontmatter, Post, PostSummary 타입
apps/aigrit/src/lib/mdx.ts         ← (Phase 2) compileMDX + rehype 체인 + 컴포넌트 매핑
apps/aigrit/content/posts/*.mdx    ← 글 파일들
```

## 타입 정의 (packages/blog-core/types/post.ts)

```typescript
export interface PostFrontmatter {
  title: string
  date: string           // YYYY-MM-DD 또는 YYYY-MM-DD HH:mm (KST)
  slug: string           // URL slug
  description: string
  tags?: string[]
  thumbnail?: string
  featured?: boolean
  category?: string
  draft?: boolean
}

export interface Post {
  frontmatter: PostFrontmatter
  content: string              // MDX raw content
  readingTimeMinutes: number   // 자동 계산
}

export interface PostSummary {
  frontmatter: PostFrontmatter
  readingTimeMinutes: number
}
```

## MDX 파싱

### 공유 엔진 (`@unpack/blog-core`)

```typescript
// packages/blog-core/lib/mdx.ts
export function parseMdxFile(filePath: string): Post
// 내부: fs.readFileSync → gray-matter 파싱 → reading-time 계산

// packages/blog-core/lib/posts.ts
export function getAllPosts(contentDir: string, opts?): Post[]
export function getAllPostSummaries(contentDir: string, opts?): PostSummary[]
export function getPostBySlug(contentDir: string, slug: string): Post | null
export function getAllPostSlugs(contentDir: string): string[]
```

앱에서 사용:
```typescript
import path from "node:path"
import { getAllPosts, getPostBySlug } from "@unpack/blog-core"

const CONTENT_DIR = path.join(process.cwd(), "content/posts")
const posts = getAllPosts(CONTENT_DIR)
const post = getPostBySlug(CONTENT_DIR, params.slug)
```

### 앱 특화 — MDX → React 변환 (Phase 2)

`apps/aigrit/src/lib/mdx.ts`에서 next-mdx-remote의 `compileMDX`(또는 `MDXRemote`) 사용. 컴포넌트 매핑은 앱 브랜드(광고 on/off 등)에 따라 다르므로 앱에 둠.

```typescript
// 예시 — Phase 2에서 구현
import { compileMDX } from "next-mdx-remote/rsc"
export async function renderPost(source: string): Promise<React.ReactElement>
```

### rehype 플러그인 체인

```
MDX source
  → rehype-slug (헤딩에 id 부여)
  → rehype-autolink-headings (앵커 링크)
  → rehype-pretty-code (코드 하이라이팅, theme: 'github-dark')
  → React 컴포넌트
```

### MDX 커스텀 컴포넌트 매핑 (Phase 2 이후)

`compileMDX` 호출 시 components 옵션으로 전달. 실제 구현체는 **공유 엔진**에서 import:

```typescript
import {
  AffiliateLink,   // @unpack/blog-core/components/mdx/AffiliateLink (Phase 2)
  CompareTable,    // @unpack/blog-core/components/mdx/CompareTable (Phase 2)
  Callout,         // @unpack/blog-core/components/mdx/Callout (Phase 2)
  ProCon,          // @unpack/blog-core/components/mdx/ProCon (Phase 2)
} from "@unpack/blog-core"

const components = { AffiliateLink, CompareTable, Callout, ProCon }
```

`AffiliateLink`는 `brand.config.ts`의 `monetization.affiliateLinks` 플래그에 따라 자동 비활성(BrandProvider 컨텍스트 참조).

## 글 목록 조회 확장 함수 (Phase 2에서 앱 또는 blog-core에 추가)

`@unpack/blog-core`는 현재 기본 함수(`getAllPosts` 등)만 제공. 아래 파생 유틸은 Phase 2에서 필요 시 `blog-core`에 추가하거나 앱 로컬 `src/lib/posts.ts`에서 래핑:

```typescript
export function getPostsByTag(tag: string): Post[]
export function getFeaturedPosts(): Post[]
export function getRelatedPosts(currentSlug: string, tags: string[], limit?: number): PostSummary[]
export function getAllTags(): { tag: string; count: number }[]
```

### 구현 로직 (현재 `@unpack/blog-core/lib/posts.ts`)

1. `fs.readdirSync(contentDir)` → `.mdx?/` 파일 목록
2. 각 파일에서 `parseMdxFile()` → frontmatter + content + `readingTimeMinutes`
3. `draft: true`는 `opts.includeDrafts` 지정 시에만 포함
4. `frontmatter.date` 기준 내림차순 정렬 (문자열 `localeCompare`)
5. 서버 컴포넌트에서 호출되므로 빌드 타임에 한 번만 실행

## MDX frontmatter 포맷

```yaml
---
title: "Claude vs ChatGPT — 블로그 글쓰기 직접 실험 비교"
date: "2026-04-20"
slug: "claude-vs-chatgpt-blog-writing"
description: "Claude와 ChatGPT로 블로그 글을 3주간 직접 써봤습니다."
tags: ["AI도구", "Claude", "ChatGPT", "비교"]
thumbnail: "/images/claude-vs-chatgpt-blog-writing/thumbnail.png"
featured: true
---
```

### frontmatter 필수/선택 필드 (blog-core 타입 기준)

| 필드 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| title | string | ✅ | 글 제목 (SEO title에도 사용) |
| date | string | ✅ | 발행일 (YYYY-MM-DD 또는 YYYY-MM-DD HH:mm, KST 기준) |
| slug | string | ✅ | URL 경로 (/blog/{slug}) — 생략 시 파일명 사용 |
| description | string | ✅ | SEO meta description (150자) |
| tags | string[] | ❌ | 태그 목록 |
| thumbnail | string | ❌ | 썸네일 이미지 경로 |
| featured | boolean | ❌ | 홈 featured 여부 (기본 false) |
| category | string | ❌ | 카테고리 (AIGrit에서만 사용) |
| draft | boolean | ❌ | true면 기본 조회에서 제외 |

## 글 추가 프로세스

```
1. apps/aigrit/content/posts/{slug}.mdx 파일 생성
2. frontmatter 작성
3. MDX 본문 작성 (커스텀 컴포넌트 사용 가능 — Phase 2 이후)
4. apps/aigrit/public/images/{slug}/ 에 이미지 배치
5. git push → Vercel 자동 배포 (AIGrit 프로젝트)
```

## SSG (Static Site Generation)

개별 글 페이지 (`src/app/blog/[slug]/page.tsx`, Phase 2):

```typescript
import path from "node:path"
import { getAllPostSlugs, getPostBySlug, buildMetadata } from "@unpack/blog-core"

const CONTENT_DIR = path.join(process.cwd(), "content/posts")

export async function generateStaticParams() {
  return getAllPostSlugs(CONTENT_DIR).map((slug) => ({ slug }))
}

export async function generateMetadata({ params }): Promise<Metadata> {
  const post = getPostBySlug(CONTENT_DIR, params.slug)
  if (!post) return {}
  return buildMetadata({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: "AIGrit",
    siteUrl: "https://aigrit.dev",
    path: `/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    type: "article",
    publishedTime: post.frontmatter.date,
    tags: post.frontmatter.tags,
  })
}
```

## 이미지 마커 → 실제 이미지 변환

Craft → MDX 변환 시 (`/publish-post` 커맨드):

```
📸 [스크린샷: Claude 대화 화면]
→ ![Claude 대화 화면](/images/{slug}/screenshot-01.png)

🔗 [AffiliateLink: claude.ai | Claude Pro]
→ <AffiliateLink href="https://claude.ai" label="Claude Pro" />

📎 [RelatedPost: /blog/cursor-review]
→ [관련 글 보기](/blog/cursor-review)
```
