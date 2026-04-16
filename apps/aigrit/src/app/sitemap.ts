import path from "node:path";
import type { MetadataRoute } from "next";
import { getAllPostSummaries, SUPPORTED_LOCALES } from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";
import { CATEGORY_META } from "../lib/categories";

type ChangeFreq = NonNullable<MetadataRoute.Sitemap[number]["changeFrequency"]>;

const STATIC_PATHS: { path: string; priority: number; changeFrequency: ChangeFreq }[] = [
  { path: "/", priority: 1.0, changeFrequency: "weekly" },
  { path: "/blog", priority: 0.9, changeFrequency: "weekly" },
  { path: "/about", priority: 0.6, changeFrequency: "monthly" },
  { path: "/privacy", priority: 0.3, changeFrequency: "monthly" },
  { path: "/disclaimer", priority: 0.3, changeFrequency: "monthly" },
];

function buildLanguageMap(base: string, pathSuffix: string): Record<string, string> {
  return Object.fromEntries(
    SUPPORTED_LOCALES.map((l) => [l, `${base}/${l}${pathSuffix === "/" ? "" : pathSuffix}`]),
  );
}

export default function sitemap(): MetadataRoute.Sitemap {
  const configUrl = brandConfig.url;
  const base = (configUrl.includes("localhost") ? "https://aigrit.dev" : configUrl).replace(
    /\/+$/,
    "",
  );
  const now = new Date();
  const entries: MetadataRoute.Sitemap = [];

  for (const locale of SUPPORTED_LOCALES) {
    for (const s of STATIC_PATHS) {
      entries.push({
        url: `${base}/${locale}${s.path === "/" ? "" : s.path}`,
        lastModified: now,
        changeFrequency: s.changeFrequency,
        priority: s.priority,
        alternates: { languages: buildLanguageMap(base, s.path) },
      });
    }
  }

  for (const locale of SUPPORTED_LOCALES) {
    const CONTENT_DIR = path.join(process.cwd(), "content/posts", locale);
    const posts = getAllPostSummaries(CONTENT_DIR);
    for (const p of posts) {
      entries.push({
        url: `${base}/${locale}/blog/${p.frontmatter.slug}`,
        lastModified: new Date(p.frontmatter.date),
        changeFrequency: "monthly",
        priority: 0.8,
        alternates: {
          languages: buildLanguageMap(base, `/blog/${p.frontmatter.slug}`),
        },
      });
    }
  }

  for (const locale of SUPPORTED_LOCALES) {
    for (const cat of Object.values(CATEGORY_META)) {
      entries.push({
        url: `${base}/${locale}/category/${cat.slug}`,
        lastModified: now,
        changeFrequency: "weekly",
        priority: 0.7,
        alternates: {
          languages: buildLanguageMap(base, `/category/${cat.slug}`),
        },
      });
    }
  }

  return entries;
}
