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
  } = input;

  const url = joinUrl(siteUrl, path);
  const ogImage = image ? joinUrl(siteUrl, image) : joinUrl(siteUrl, "/og-default.png");

  return {
    title,
    description,
    alternates: { canonical: url },
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
