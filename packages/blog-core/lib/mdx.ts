import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import readingTime from "reading-time";
import type { Post, PostFrontmatter, PostReviewMeta } from "../types/post";

export function parseMdxFile(filePath: string): Post {
  const raw = fs.readFileSync(filePath, "utf8");
  const { data, content } = matter(raw);
  const frontmatter = normalizeFrontmatter(data, filePath);
  return {
    frontmatter,
    content,
    readingTimeMinutes: Math.max(1, Math.round(readingTime(content).minutes)),
  };
}

function normalizeFrontmatter(
  data: Record<string, unknown>,
  filePath: string,
): PostFrontmatter {
  const { title, date, slug, description } = data as Record<string, unknown>;
  if (typeof title !== "string" || typeof date !== "string" || typeof description !== "string") {
    throw new Error(`Invalid frontmatter in ${filePath}: title/date/description required`);
  }
  const resolvedSlug =
    typeof slug === "string" && slug.length > 0
      ? slug
      : path.basename(filePath, path.extname(filePath));
  return {
    title,
    date,
    slug: resolvedSlug,
    description,
    tags: Array.isArray(data.tags) ? (data.tags as string[]) : undefined,
    thumbnail: typeof data.thumbnail === "string" ? data.thumbnail : undefined,
    featured: typeof data.featured === "boolean" ? data.featured : undefined,
    category: typeof data.category === "string" ? data.category : undefined,
    draft: typeof data.draft === "boolean" ? data.draft : undefined,
    review: parseReview(data.review),
  };
}

function parseReview(value: unknown): PostReviewMeta | undefined {
  if (!value || typeof value !== "object") return undefined;
  const v = value as Record<string, unknown>;
  const productName = typeof v.productName === "string" ? v.productName : undefined;
  const ratingValue = typeof v.ratingValue === "number" ? v.ratingValue : undefined;
  if (!productName || ratingValue === undefined) return undefined;
  return {
    productName,
    ratingValue,
    bestRating: typeof v.bestRating === "number" ? v.bestRating : undefined,
    worstRating: typeof v.worstRating === "number" ? v.worstRating : undefined,
    productCategory:
      typeof v.productCategory === "string" ? v.productCategory : undefined,
  };
}
