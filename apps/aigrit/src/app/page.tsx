import Link from "next/link";
import path from "node:path";
import { getAllPostSummaries, PostCard, buildWebSiteJsonLd } from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

export default function HomePage() {
  const posts = getAllPostSummaries(CONTENT_DIR);
  const latest = posts.slice(0, 6);
  const byCategory = groupByCategory(posts);
  const jsonLd = buildWebSiteJsonLd({
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
    description: brandConfig.description,
  });

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* Hero */}
      <section className="mb-14">
        <div className="flex items-center gap-2 mb-4">
          <span
            aria-hidden
            className="inline-block h-1.5 w-6 rounded-full"
            style={{ background: "var(--color-brand-secondary)" }}
          />
          <span
            className="text-xs font-semibold uppercase tracking-[0.2em]"
            style={{ color: "var(--color-brand-secondary)", fontFamily: "var(--font-mono)" }}
          >
            AI TOOL REVIEW
          </span>
        </div>
        <h1 className="text-4xl sm:text-5xl font-extrabold leading-[1.15] tracking-tight text-[var(--color-brand-primary)]">
          {brandConfig.tagline}
        </h1>
        <p className="mt-4 text-base sm:text-lg leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] max-w-2xl">
          {brandConfig.description}
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Link
            href="/blog"
            className="rounded-md px-5 py-2.5 text-sm font-semibold transition"
            style={{ background: "var(--color-brand-primary)", color: "var(--background)" }}
          >
            최신 리뷰 →
          </Link>
          <Link
            href="/about"
            className="rounded-md border px-5 py-2.5 text-sm font-semibold"
            style={{
              borderColor: "color-mix(in oklab, var(--foreground) 20%, transparent)",
              color: "var(--foreground)",
            }}
          >
            어떻게 리뷰하나요
          </Link>
        </div>
      </section>

      {/* Latest */}
      {latest.length > 0 && (
        <section className="mb-14">
          <div className="flex items-baseline justify-between mb-4">
            <h2
              className="text-xs font-bold uppercase tracking-[0.2em] text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
              style={{ fontFamily: "var(--font-mono)" }}
            >
              LATEST REVIEWS
            </h2>
            <Link
              href="/blog"
              className="text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] hover:text-[var(--color-brand-primary)]"
            >
              전체 보기 →
            </Link>
          </div>
          <ul className="grid gap-2 sm:grid-cols-2">
            {latest.map((post) => (
              <li key={post.frontmatter.slug}>
                <PostCard post={post} />
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Categories */}
      {byCategory.length > 0 && (
        <section>
          <h2
            className="text-xs font-bold uppercase tracking-[0.2em] text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] mb-6"
            style={{ fontFamily: "var(--font-mono)" }}
          >
            BY CATEGORY
          </h2>
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {byCategory.map(([cat, catPosts]) => (
              <div key={cat}>
                <h3 className="mb-3 text-lg font-bold text-[var(--color-brand-primary)]">
                  {cat}
                  <span
                    className="ml-2 text-xs tabular-nums text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]"
                    style={{ fontFamily: "var(--font-mono)" }}
                  >
                    {catPosts.length}
                  </span>
                </h3>
                <ul className="space-y-1">
                  {catPosts.slice(0, 4).map((p) => (
                    <li key={p.frontmatter.slug}>
                      <Link
                        href={`/blog/${p.frontmatter.slug}`}
                        className="block py-1 text-sm text-[color-mix(in_oklab,var(--foreground)_80%,transparent)] hover:text-[var(--color-brand-primary)]"
                      >
                        {p.frontmatter.title}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>
      )}

      {posts.length === 0 && (
        <section className="mt-8 rounded-md border border-[color-mix(in_oklab,var(--foreground)_10%,transparent)] p-8 text-center">
          <p className="text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
            아직 작성된 리뷰가 없습니다. 곧 첫 글을 올릴게요.
          </p>
        </section>
      )}
    </div>
  );
}

type Summary = ReturnType<typeof getAllPostSummaries>[number];

function groupByCategory(posts: Summary[]): [string, Summary[]][] {
  const map = new Map<string, Summary[]>();
  for (const p of posts) {
    const cat = p.frontmatter.category ?? "기타";
    const bucket = map.get(cat) ?? [];
    bucket.push(p);
    map.set(cat, bucket);
  }
  return Array.from(map.entries()).sort((a, b) => b[1].length - a[1].length);
}
