import path from "node:path";
import type { MetadataRoute } from "next";
import { getAllPostSummaries } from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

const STATIC_PATHS: { path: string; priority: number }[] = [
  { path: "/", priority: 1.0 },
  { path: "/blog", priority: 0.9 },
  { path: "/about", priority: 0.6 },
  { path: "/privacy", priority: 0.3 },
  { path: "/disclaimer", priority: 0.3 },
];

export default function sitemap(): MetadataRoute.Sitemap {
  const configUrl = brandConfig.url;
  const base = (configUrl.includes("localhost") ? "https://aigrit.dev" : configUrl).replace(/\/+$/, "");
  const now = new Date();

  const staticEntries: MetadataRoute.Sitemap = STATIC_PATHS.map((s) => ({
    url: `${base}${s.path}`,
    lastModified: now,
    changeFrequency: s.path === "/" || s.path === "/blog" ? "weekly" : "monthly",
    priority: s.priority,
  }));

  const posts = getAllPostSummaries(CONTENT_DIR);
  const postEntries: MetadataRoute.Sitemap = posts.map((p) => ({
    url: `${base}/blog/${p.frontmatter.slug}`,
    lastModified: new Date(p.frontmatter.date),
    changeFrequency: "monthly",
    priority: 0.8,
  }));

  return [...staticEntries, ...postEntries];
}
