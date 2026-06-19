import path from "node:path";
import type { MetadataRoute } from "next";
import { getAllPostSummaries } from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";

/** ISR: 예약 발행글이 발행 시각 이후 sitemap에 자동 반영되도록 10분마다 재생성. */
export const revalidate = 600;

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

const STATIC_PATHS: { path: string; priority: number }[] = [
  { path: "/", priority: 1.0 },
  { path: "/blog", priority: 0.9 },
  { path: "/projects", priority: 0.6 },
  { path: "/about", priority: 0.5 },
];

export default function sitemap(): MetadataRoute.Sitemap {
  const configUrl = brandConfig.url;
  const base = (
    configUrl.includes("localhost") ? "https://babipanote.com" : configUrl
  ).replace(/\/+$/, "");
  const now = new Date();

  const staticEntries: MetadataRoute.Sitemap = STATIC_PATHS.map((s) => ({
    url: `${base}${s.path}`,
    lastModified: now,
    changeFrequency:
      s.path === "/" || s.path === "/blog" ? "weekly" : "monthly",
    priority: s.priority,
  }));

  const posts = getAllPostSummaries(CONTENT_DIR, { brand: "babipanote" });
  const postEntries: MetadataRoute.Sitemap = posts.map((p) => ({
    url: `${base}/blog/${p.frontmatter.slug}`,
    lastModified: new Date(p.frontmatter.updated ?? p.frontmatter.date),
    changeFrequency: "monthly",
    priority: 0.8,
  }));

  return [...staticEntries, ...postEntries];
}
