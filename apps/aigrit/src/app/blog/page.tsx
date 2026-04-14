import path from "node:path";
import type { Metadata } from "next";
import { PostCard, buildMetadata, getAllPostSummaries } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

export const metadata: Metadata = buildMetadata({
  title: "Blog",
  description: `${brandConfig.name}의 전체 리뷰 — ${brandConfig.tagline}`,
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/blog",
});

export default function BlogIndexPage() {
  const posts = getAllPostSummaries(CONTENT_DIR);

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
        <div className="flex items-center gap-2 mb-3">
          <span
            aria-hidden
            className="inline-block h-1 w-4 rounded-full"
            style={{ background: "var(--color-brand-secondary)" }}
          />
          <span
            className="text-xs font-semibold uppercase tracking-[0.2em]"
            style={{ color: "var(--color-brand-secondary)", fontFamily: "var(--font-mono)" }}
          >
            ALL REVIEWS
          </span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
          Blog
        </h1>
        <p
          className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          총 <span className="tabular-nums">{posts.length}</span>편 · 최신순 정렬
        </p>
      </header>

      {posts.length === 0 ? (
        <p className="text-sm text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          아직 리뷰가 없습니다.
        </p>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2">
          {posts.map((post) => (
            <li key={post.frontmatter.slug}>
              <PostCard post={post} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
