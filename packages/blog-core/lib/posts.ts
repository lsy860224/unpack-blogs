import fs from "node:fs";
import path from "node:path";
import { parseMdxFile, type Brand } from "./mdx";
import { isPublished } from "./date";
import type { Post, PostSummary } from "../types/post";

const MDX_EXT = /\.mdx?$/i;

export interface PostQueryOptions {
  includeDrafts?: boolean;
  /**
   * 미래 발행일(date > now) 글을 포함할지. 기본 false → 예약 발행 게이팅.
   * Draft Mode 미리보기에서만 true 로 전달한다.
   */
  includeFuture?: boolean;
  /** 앱별 스키마 검증 강제 (babipanote는 category 금지 등) */
  brand?: Brand;
}

export function getAllPosts(
  contentDir: string,
  opts: PostQueryOptions = {},
): Post[] {
  if (!fs.existsSync(contentDir)) return [];
  const files = fs
    .readdirSync(contentDir)
    .filter((f) => MDX_EXT.test(f))
    .map((f) => path.join(contentDir, f));

  const posts = files
    .map((filePath) => parseMdxFile(filePath, { brand: opts.brand }))
    .filter((post) => opts.includeDrafts || !post.frontmatter.draft)
    .filter(
      (post) => opts.includeFuture || isPublished(post.frontmatter.date),
    );

  return posts.sort((a, b) =>
    b.frontmatter.date.localeCompare(a.frontmatter.date),
  );
}

export function getAllPostSummaries(
  contentDir: string,
  opts?: PostQueryOptions,
): PostSummary[] {
  return getAllPosts(contentDir, opts).map(
    ({ frontmatter, readingTimeMinutes }) => ({
      frontmatter,
      readingTimeMinutes,
    }),
  );
}

export function getPostBySlug(
  contentDir: string,
  slug: string,
  opts: PostQueryOptions = {},
): Post | null {
  if (!fs.existsSync(contentDir)) return null;
  const candidates = [
    path.join(contentDir, `${slug}.mdx`),
    path.join(contentDir, `${slug}.md`),
  ];
  const hit = candidates.find((p) => fs.existsSync(p));
  if (!hit) return null;
  const post = parseMdxFile(hit, { brand: opts.brand });
  // 예약 발행 게이팅: 미래글은 직접 URL 접근 시에도 숨긴다 (Draft Mode 제외).
  if (!opts.includeFuture && !isPublished(post.frontmatter.date)) return null;
  return post;
}

export function getAllPostSlugs(
  contentDir: string,
  opts: PostQueryOptions = {},
): string[] {
  return getAllPostSummaries(contentDir, {
    includeDrafts: false,
    brand: opts.brand,
  }).map((p) => p.frontmatter.slug);
}
