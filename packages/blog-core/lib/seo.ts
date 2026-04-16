import type { Metadata } from "next";

export interface SeoInput {
  title: string;
  description: string;
  siteName: string;
  siteUrl: string;
  path?: string;
  image?: string;
  locale?: string;
  type?: "website" | "article";
  publishedTime?: string;
  tags?: string[];
  /** hreflang alternates: { ko: "/ko/...", en: "/en/...", "x-default": "/ko/..." } — 값이 절대 URL 이 아니면 siteUrl 기준으로 절대화됨 */
  hrefLangs?: Record<string, string>;
}

export function buildMetadata(input: SeoInput): Metadata {
  const {
    title,
    description,
    siteName,
    siteUrl,
    path = "/",
    image,
    locale = "ko_KR",
    type = "website",
    publishedTime,
    tags,
    hrefLangs,
  } = input;

  const url = joinUrl(siteUrl, path);
  const ogImage = image ? joinUrl(siteUrl, image) : joinUrl(siteUrl, "/og-default.png");

  const languages = hrefLangs
    ? Object.fromEntries(
        Object.entries(hrefLangs).map(([k, v]) => [k, joinUrl(siteUrl, v)]),
      )
    : undefined;

  return {
    title,
    description,
    alternates: {
      canonical: url,
      ...(languages ? { languages } : {}),
    },
    openGraph: {
      title,
      description,
      url,
      siteName,
      locale,
      type,
      images: [{ url: ogImage }],
      ...(publishedTime ? { publishedTime } : {}),
      ...(tags ? { tags } : {}),
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: [ogImage],
    },
  };
}

function joinUrl(base: string, path: string): string {
  if (/^https?:\/\//i.test(path)) return path;
  const b = base.replace(/\/+$/, "");
  const p = path.startsWith("/") ? path : `/${path}`;
  return `${b}${p}`;
}
