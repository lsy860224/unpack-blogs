# SEO_MONETIZATION.md — SEO + 수익화 상세 설계

> 검색 최적화, 애드센스, 제휴 마케팅, 분석 관련 모든 구현 사항.

## SEO 메타태그 (src/lib/seo.ts)

### 헬퍼 함수

```typescript
// 사이트 전체 기본 메타데이터
export function generateSiteMetadata(): Metadata

// 글별 메타데이터 (frontmatter → Metadata 변환)
export function generatePostMetadata(meta: PostMeta): Metadata

// OG 이미지 URL 생성
export function getOGImageUrl(slug?: string): string
```

### 기본 메타데이터

```typescript
const SITE_CONFIG = {
  title: 'AIGrit',
  titleTemplate: '%s — AIGrit',
  description: 'AI 도구를 직접 써보고 솔직하게 비교합니다.',
  url: 'https://aigrit.dev',
  locale: 'ko_KR',
  author: 'AIGrit',
  twitterHandle: '@aigrit_dev',
}
```

### 글별 메타데이터 구조

```html
<title>{title} — AIGrit</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://aigrit.dev/images/{slug}/og.png">
<meta property="og:url" content="https://aigrit.dev/blog/{slug}">
<meta property="og:type" content="article">
<meta property="article:published_time" content="{date}">
<meta property="article:tag" content="{tags}">
<link rel="canonical" href="https://aigrit.dev/blog/{slug}">
```

## 사이트맵 (src/app/sitemap.ts)

```typescript
export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getAllPosts()
  const postEntries = posts.map((post) => ({
    url: `https://aigrit.dev/blog/${post.slug}`,
    lastModified: new Date(post.date),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  }))

  return [
    { url: 'https://aigrit.dev', priority: 1.0, changeFrequency: 'daily' },
    { url: 'https://aigrit.dev/blog', priority: 0.9, changeFrequency: 'daily' },
    { url: 'https://aigrit.dev/about', priority: 0.5, changeFrequency: 'yearly' },
    ...postEntries,
  ]
}
```

## robots.txt (src/app/robots.ts)

```typescript
export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: '*', allow: '/', disallow: '/api/' },
    sitemap: 'https://aigrit.dev/sitemap.xml',
  }
}
```

## 구조화 데이터 (JSON-LD)

### Article 스키마 (글별)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{description}",
  "image": "https://aigrit.dev/images/{slug}/thumbnail.png",
  "datePublished": "{date}",
  "author": { "@type": "Person", "name": "AIGrit" },
  "publisher": {
    "@type": "Organization",
    "name": "AIGrit",
    "url": "https://aigrit.dev"
  }
}
```

### FAQ 스키마 (FAQ 섹션이 있는 글)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "질문",
      "acceptedAnswer": { "@type": "Answer", "text": "답변" }
    }
  ]
}
```

## Google AdSense

### 설치

`src/app/layout.tsx`의 `<head>`에:

```html
<script
  async
  src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXX"
  crossOrigin="anonymous"
/>
```

### 광고 배치 전략

| 위치 | 컴포넌트 | 형식 | 비고 |
|------|---------|------|------|
| 글 상단 (본문 시작 전) | AdBanner | horizontal | 데스크탑만 |
| 글 중간 (H2 2개 후) | AdInArticle | fluid | 자동 삽입 |
| 글 하단 (댓글 전) | AdBanner | rectangle | 항상 표시 |
| 사이드바 | AdBanner | rectangle | 데스크탑만, sticky |

### 애드센스 승인 요건

- [ ] 최소 15~20개 글 발행
- [ ] About 페이지 (E-E-A-T)
- [ ] Privacy Policy 페이지
- [ ] Disclaimer 페이지 (제휴 마케팅 고지)
- [ ] 네비게이션 + 사이트맵
- [ ] HTTPS (Vercel 자동)
- [ ] 오리지널 콘텐츠 (AI 생성 → 사람 편집 필수)

## 제휴 마케팅

### AffiliateLink 컴포넌트 규칙

1. 항상 `rel="nofollow sponsored"` 적용
2. 항상 "제휴 링크" 라벨 표시 (투명성)
3. 클릭 시 GA4 이벤트: `affiliate_click` + `{service, slug}`
4. Disclaimer 페이지에 제휴 마케팅 고지 포함

### 초기 제휴 프로그램

| 서비스 | 커미션 | 가입 URL |
|--------|--------|----------|
| Hostinger | 40% 건당 | hostinger.com/affiliates |
| Grammarly | $20/건 | grammarly.com/affiliates |
| Scalenut | 30% 반복 | scalenut.com/affiliates |

## Google Analytics 4

### 설치

```typescript
// src/components/layout/Analytics.tsx
import Script from 'next/script'

export function Analytics() {
  const gaId = process.env.NEXT_PUBLIC_GA_ID
  if (!gaId) return null

  return (
    <>
      <Script src={`https://www.googletagmanager.com/gtag/js?id=${gaId}`} strategy="afterInteractive" />
      <Script id="ga4" strategy="afterInteractive">
        {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${gaId}');`}
      </Script>
    </>
  )
}
```

### 커스텀 이벤트

| 이벤트 | 파라미터 | 트리거 |
|--------|---------|--------|
| page_view | page_title, page_path | 자동 (GA4 기본) |
| affiliate_click | service, slug, position | AffiliateLink 클릭 |
| toc_click | heading_id, slug | 목차 클릭 |
| share_click | method (twitter/copy), slug | 공유 버튼 클릭 |
| scroll_depth | depth (25/50/75/100), slug | 스크롤 깊이 |

## 검색 등록

### Google Search Console
1. aigrit.dev 속성 추가
2. DNS TXT 레코드로 소유권 인증
3. sitemap.xml 제출

### 네이버 서치어드바이저
1. searchadvisor.naver.com에서 사이트 등록
2. `<meta name="naver-site-verification">` 태그 추가
3. 사이트맵 제출

## 필수 페이지

### About (app/about/page.tsx)
- E-E-A-T의 핵심. 저자 소개, 전문성, 블로그 목적 설명
- 프로필 사진 (선택)
- "직접 써보고 리뷰한다"는 방법론 설명

### Privacy Policy (app/privacy/page.tsx)
- GA4, AdSense, Giscus 데이터 수집 고지
- 쿠키 정책
- 연락처

### Disclaimer (app/disclaimer/page.tsx)
- 제휴 마케팅 고지: "이 블로그는 제휴 링크를 포함할 수 있습니다"
- 리뷰 독립성 선언
- 정확성 면책
