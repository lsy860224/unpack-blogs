/**
 * 구조화 데이터 (JSON-LD) 헬퍼.
 * Next.js의 metadata API가 지원하지 않는 ld+json은 <script> 태그로 주입한다.
 */

export interface ArticleJsonLdInput {
  title: string;
  description: string;
  siteName: string;
  siteUrl: string;
  path: string;
  image?: string;
  author?: string;
  datePublished: string;
  dateModified?: string;
  inLanguage?: string;
}

export function buildArticleJsonLd(input: ArticleJsonLdInput) {
  const url = joinUrl(input.siteUrl, input.path);
  const img = input.image
    ? joinUrl(input.siteUrl, input.image)
    : joinUrl(input.siteUrl, "/og-default.png");
  return {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: input.title,
    description: input.description,
    image: [img],
    url,
    datePublished: input.datePublished,
    dateModified: input.dateModified ?? input.datePublished,
    author: input.author
      ? { "@type": "Person", name: input.author }
      : { "@type": "Organization", name: input.siteName },
    publisher: { "@type": "Organization", name: input.siteName },
    mainEntityOfPage: { "@type": "WebPage", "@id": url },
    ...(input.inLanguage ? { inLanguage: input.inLanguage } : {}),
  };
}

export interface ReviewJsonLdInput {
  productName: string;
  productCategory?: string;
  ratingValue: number;
  bestRating?: number;
  worstRating?: number;
  reviewBody?: string;
  authorName: string;
  datePublished: string;
  url: string;
  inLanguage?: string;
}

export function buildReviewJsonLd(input: ReviewJsonLdInput) {
  return {
    "@context": "https://schema.org",
    "@type": "Review",
    itemReviewed: {
      "@type": input.productCategory ?? "SoftwareApplication",
      name: input.productName,
    },
    reviewRating: {
      "@type": "Rating",
      ratingValue: input.ratingValue.toString(),
      bestRating: (input.bestRating ?? 5).toString(),
      worstRating: (input.worstRating ?? 1).toString(),
    },
    author: { "@type": "Organization", name: input.authorName },
    datePublished: input.datePublished,
    ...(input.reviewBody ? { reviewBody: input.reviewBody } : {}),
    url: input.url,
    ...(input.inLanguage ? { inLanguage: input.inLanguage } : {}),
  };
}

export interface WebSiteJsonLdInput {
  siteName: string;
  siteUrl: string;
  description: string;
  inLanguage?: string;
  /** 검색 폼 경로. default "/blog" — locale prefix 쓸 경우 "/ko/blog" 같이 넘기면 됨. */
  searchPath?: string;
}

export function buildWebSiteJsonLd(input: WebSiteJsonLdInput) {
  const searchPath = input.searchPath ?? "/blog";
  return {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: input.siteName,
    url: input.siteUrl,
    description: input.description,
    inLanguage: input.inLanguage ?? "ko-KR",
    potentialAction: {
      "@type": "SearchAction",
      target: `${input.siteUrl}${searchPath}?q={search_term_string}`,
      "query-input": "required name=search_term_string",
    },
  };
}

function joinUrl(base: string, path: string): string {
  if (/^https?:\/\//i.test(path)) return path;
  const b = base.replace(/\/+$/, "");
  const p = path.startsWith("/") ? path : `/${path}`;
  return `${b}${p}`;
}
