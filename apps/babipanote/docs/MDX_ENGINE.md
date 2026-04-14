# MDX_ENGINE.md — MDX 콘텐츠 엔진 상세 설계

> MDX 파싱, frontmatter, 글 목록 조회, 검색, 태그 필터링 관련 모든 로직.

## 핵심 파일

```
src/lib/mdx.ts      ← MDX 파싱 + 렌더링
src/lib/posts.ts     ← 글 목록 조회 유틸
src/types/post.ts    ← 타입 정의
content/posts/*.mdx  ← 글 파일들
```

## 타입 정의 (src/types/post.ts)

```typescript
export interface PostMeta {
  title: string
  date: string           // YYYY-MM-DD
  slug: string           // URL slug
  description: string    // 150자 이내
  tags: string[]
  thumbnail: string      // /images/{slug}/thumbnail.png
  featured: boolean
  readingTime?: string   // 자동 계산
}

export interface PostData {
  meta: PostMeta
  content: string        // MDX raw content
}
```

## MDX 파싱 (src/lib/mdx.ts)

### 핵심 함수

```typescript
// 1. 단일 글 파싱 (slug → PostData)
export async function getPostBySlug(slug: string): Promise<PostData>

// 2. MDX → React 컴포넌트 변환 (서버 컴포넌트용)
export async function compileMDX(source: string): Promise<MDXRemoteSerializeResult>
```

### rehype 플러그인 체인

```
MDX source
  → rehype-slug (헤딩에 id 부여)
  → rehype-autolink-headings (앵커 링크)
  → rehype-pretty-code (코드 하이라이팅, theme: 'github-dark')
  → React 컴포넌트
```

### MDX 커스텀 컴포넌트 매핑

`compileMDX` 호출 시 components 옵션으로 전달:

```typescript
const components = {
  AffiliateLink,    // src/components/mdx/AffiliateLink.tsx
  CompareTable,     // src/components/mdx/CompareTable.tsx
  Callout,          // src/components/mdx/Callout.tsx
  ProCon,           // src/components/mdx/ProCon.tsx
}
```

## 글 목록 조회 (src/lib/posts.ts)

### 핵심 함수

```typescript
// 전체 글 목록 (날짜 내림차순)
export async function getAllPosts(): Promise<PostMeta[]>

// 태그별 필터링
export async function getPostsByTag(tag: string): Promise<PostMeta[]>

// featured 글만
export async function getFeaturedPosts(): Promise<PostMeta[]>

// 관련 글 (같은 태그 기반, 현재 글 제외)
export async function getRelatedPosts(currentSlug: string, tags: string[], limit?: number): Promise<PostMeta[]>

// 전체 태그 목록 (글 수 포함)
export async function getAllTags(): Promise<{ tag: string; count: number }[]>

// 전체 slug 목록 (SSG용)
export async function getAllSlugs(): Promise<string[]>
```

### 구현 로직

1. `fs.readdirSync('content/posts')` → .mdx 파일 목록
2. 각 파일에서 `gray-matter`로 frontmatter 추출
3. `reading-time`으로 읽기 시간 자동 계산
4. date 기준 내림차순 정렬
5. 결과 캐싱 (빌드 타임에 한 번만 실행)

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

### frontmatter 필수 필드

| 필드 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| title | string | ✅ | 글 제목 (SEO title에도 사용) |
| date | string | ✅ | 발행일 (YYYY-MM-DD) |
| slug | string | ✅ | URL 경로 (/blog/{slug}) |
| description | string | ✅ | SEO meta description (150자) |
| tags | string[] | ✅ | 태그 목록 |
| thumbnail | string | ✅ | 썸네일 이미지 경로 |
| featured | boolean | ❌ | 홈 페이지 featured 여부 (기본 false) |

## 글 추가 프로세스

```
1. content/posts/{slug}.mdx 파일 생성
2. frontmatter 작성
3. MDX 본문 작성 (커스텀 컴포넌트 사용 가능)
4. public/images/{slug}/ 에 이미지 배치
5. git push → Vercel 자동 배포
```

## SSG (Static Site Generation)

개별 글 페이지 (`app/blog/[slug]/page.tsx`)에서:

```typescript
// 빌드 타임에 모든 slug를 미리 생성
export async function generateStaticParams() {
  const slugs = await getAllSlugs()
  return slugs.map((slug) => ({ slug }))
}

// 글별 메타데이터 동적 생성
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const post = await getPostBySlug(params.slug)
  return generatePostMetadata(post.meta) // lib/seo.ts 사용
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
