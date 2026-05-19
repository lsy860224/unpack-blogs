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

export interface FaqJsonLdInput {
  /** 본문 MDX 원본. FAQ 섹션과 ### 질문 패턴을 자동 추출한다. */
  content: string;
  inLanguage?: string;
}

// JavaScript regex 주의: `\b`는 한국어 글자 뒤에서 매칭 실패 (`\w` 경계 룰),
// `\Z`는 JS에 없는 anchor (Python/Ruby 전용). 그래서 단순 lookahead 사용.
const FAQ_SECTION_PATTERN =
  /(?:^|\n)##\s+(?:자주\s*묻는\s*질문|FAQ|Frequently\s+Asked\s+Questions|FAQs)[^\n]*\n([\s\S]*?)(?=\n## |$)/;

interface FaqPair {
  question: string;
  answer: string;
}

function extractFaqPairs(content: string): FaqPair[] {
  const match = FAQ_SECTION_PATTERN.exec(content);
  if (!match) return [];
  const block = match[1];
  const pairs: FaqPair[] = [];
  const h3Re = /^###\s+(.+?)\s*$/gm;
  const matches = [...block.matchAll(h3Re)];
  for (let i = 0; i < matches.length; i++) {
    const m = matches[i];
    const question = m[1].trim();
    const start = (m.index ?? 0) + m[0].length;
    const end = i + 1 < matches.length ? (matches[i + 1].index ?? block.length) : block.length;
    const raw = block.slice(start, end).trim();
    const answer = raw
      .split(/\n{2,}/)
      .map((p) => p.replace(/\s+/g, " ").trim())
      .filter(Boolean)
      .join(" ")
      .replace(/<[^>]+>/g, "")
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
      .trim();
    if (question && answer) pairs.push({ question, answer });
  }
  return pairs;
}

export function buildFaqJsonLd(input: FaqJsonLdInput) {
  const pairs = extractFaqPairs(input.content);
  if (pairs.length === 0) return null;
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: pairs.map((p) => ({
      "@type": "Question",
      name: p.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: p.answer,
      },
    })),
    ...(input.inLanguage ? { inLanguage: input.inLanguage } : {}),
  };
}

export interface BreadcrumbItem {
  name: string;
  url: string;
}

export function buildBreadcrumbJsonLd(items: BreadcrumbItem[]) {
  if (items.length === 0) return null;
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: item.name,
      item: item.url,
    })),
  };
}

function joinUrl(base: string, path: string): string {
  if (/^https?:\/\//i.test(path)) return path;
  const b = base.replace(/\/+$/, "");
  const p = path.startsWith("/") ? path : `/${path}`;
  return `${b}${p}`;
}
