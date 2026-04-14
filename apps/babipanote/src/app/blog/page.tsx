import path from "node:path";
import type { Metadata } from "next";
import { PostCard, buildMetadata, getAllPostSummaries } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

export const metadata: Metadata = buildMetadata({
  title: "Blog",
  description: `${brandConfig.name}의 전체 글 목록 — ${brandConfig.tagline}`,
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/blog",
});

export default function BlogIndexPage() {
  const posts = getAllPostSummaries(CONTENT_DIR);

  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <h1
        className="text-3xl font-bold tracking-tight"
        style={{ fontFamily: "var(--font-serif)" }}
      >
        Blog
      </h1>
      <p className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
        총 {posts.length}편. 오래된 순이 아니라 새 글부터.
      </p>

      {posts.length === 0 ? (
        <p className="mt-8 text-sm text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          아직 글이 없습니다.
        </p>
      ) : (
        <ul className="mt-8 divide-y divide-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
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
