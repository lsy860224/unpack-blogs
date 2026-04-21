import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import readingTime from "reading-time";
import type {
  ClusterRole,
  NaverEditionStatus,
  Post,
  PostFrontmatter,
  PostNaverEdition,
  PostReviewMeta,
} from "../types/post";

export type Brand = "aigrit" | "babipanote";

export interface ParseMdxOptions {
  /** 앱별 스키마 검증을 강제. 미지정 시 공통 스키마만 검사. */
  brand?: Brand;
}

const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export function parseMdxFile(
  filePath: string,
  opts: ParseMdxOptions = {},
): Post {
  const raw = fs.readFileSync(filePath, "utf8");
  const { data, content } = matter(raw);
  if (!isPlainObject(data)) {
    throw new Error(`Invalid frontmatter (not object) in ${filePath}`);
  }
  const frontmatter = normalizeFrontmatter(data, filePath, opts);
  return {
    frontmatter,
    content,
    readingTimeMinutes: Math.max(1, Math.round(readingTime(content).minutes)),
  };
}

function normalizeFrontmatter(
  data: Record<string, unknown>,
  filePath: string,
  opts: ParseMdxOptions,
): PostFrontmatter {
  const title = asString(data.title);
  const date = asString(data.date);
  const description = asString(data.description);
  if (!title) throw new Error(`frontmatter.title missing in ${filePath}`);
  if (!date) throw new Error(`frontmatter.date missing in ${filePath}`);
  if (!description)
    throw new Error(`frontmatter.description missing in ${filePath}`);

  const slugFromData = asString(data.slug);
  const resolvedSlug =
    slugFromData && slugFromData.length > 0
      ? slugFromData
      : path.basename(filePath, path.extname(filePath));
  if (!SLUG_RE.test(resolvedSlug)) {
    throw new Error(
      `frontmatter.slug "${resolvedSlug}" must be kebab-case ([a-z0-9-]) in ${filePath}`,
    );
  }

  const category = asString(data.category);
  if (opts.brand === "babipanote" && category) {
    throw new Error(
      `babipanote frontmatter.category is forbidden ("${category}") in ${filePath}`,
    );
  }

  const tags = asStringArray(data.tags);
  if (tags && tags.length === 0) {
    throw new Error(`frontmatter.tags must not be empty in ${filePath}`);
  }

  const updatedRaw = asString(data.updated);

  return {
    title,
    date,
    slug: resolvedSlug,
    description,
    tags: tags ?? undefined,
    thumbnail: asString(data.thumbnail) ?? undefined,
    featured: typeof data.featured === "boolean" ? data.featured : undefined,
    category: category ?? undefined,
    draft: typeof data.draft === "boolean" ? data.draft : undefined,
    review: parseReview(data.review),
    updated: updatedRaw ?? date,
    topic_cluster: asString(data.topic_cluster) ?? undefined,
    cluster_role: parseClusterRole(data.cluster_role),
    naver_edition: parseNaverEdition(data.naver_edition),
  };
}

function parseClusterRole(value: unknown): ClusterRole | undefined {
  return value === "pillar" || value === "cluster" ? value : undefined;
}

function parseReview(value: unknown): PostReviewMeta | undefined {
  if (!isPlainObject(value)) return undefined;
  const productName = asString(value.productName);
  const ratingValue =
    typeof value.ratingValue === "number" ? value.ratingValue : undefined;
  if (!productName || ratingValue === undefined) return undefined;
  return {
    productName,
    ratingValue,
    bestRating:
      typeof value.bestRating === "number" ? value.bestRating : undefined,
    worstRating:
      typeof value.worstRating === "number" ? value.worstRating : undefined,
    productCategory: asString(value.productCategory) ?? undefined,
  };
}

function parseNaverEdition(value: unknown): PostNaverEdition | undefined {
  if (!isPlainObject(value)) return undefined;
  const status = asNaverStatus(value.status);
  if (!status) return undefined;
  const extra =
    typeof value.extraImages === "number" ? value.extraImages : undefined;
  return {
    status,
    angle: asString(value.angle) ?? undefined,
    extraImages: extra,
    publishedAt: asString(value.publishedAt) ?? undefined,
  };
}

function asNaverStatus(value: unknown): NaverEditionStatus | undefined {
  return value === "candidate" || value === "drafted" || value === "published"
    ? value
    : undefined;
}

function asString(value: unknown): string | undefined {
  return typeof value === "string" && value.length > 0 ? value : undefined;
}

function asStringArray(value: unknown): string[] | undefined {
  if (!Array.isArray(value)) return undefined;
  return value.filter((v): v is string => typeof v === "string");
}

function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
