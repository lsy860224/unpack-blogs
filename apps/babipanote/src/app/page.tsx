import Link from "next/link";
import path from "node:path";
import {
  formatPostDateShort,
  getAllPostSummaries,
  toIsoDatetime,
} from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

export default function HomePage() {
  const posts = getAllPostSummaries(CONTENT_DIR);
  const grouped = groupByYear(posts);

  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <section className="mb-16">
        <h1
          className="text-4xl sm:text-5xl font-bold leading-tight tracking-tight"
          style={{ fontFamily: "var(--font-serif)" }}
        >
          {brandConfig.tagline}
        </h1>
        <p className="mt-4 text-base leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] max-w-xl">
          {brandConfig.description}
        </p>
      </section>

      {posts.length === 0 ? (
        <p className="text-sm text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          아직 작성된 글이 없습니다. 곧 첫 글을 올릴게요.
        </p>
      ) : (
        <section className="space-y-12">
          {grouped.map(([year, yearPosts]) => (
            <div key={year}>
              <h2
                className="text-xs font-semibold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_45%,transparent)] mb-4"
                style={{ fontFamily: "var(--font-mono)" }}
              >
                {year}
              </h2>
              <ul className="space-y-1 border-l border-[color-mix(in_oklab,var(--foreground)_10%,transparent)]">
                {yearPosts.map((post) => (
                  <li key={post.frontmatter.slug} className="relative pl-5">
                    <span className="absolute left-[-4px] top-3 w-2 h-2 rounded-full bg-[var(--color-brand-secondary)]" />
                    <Link
                      href={`/blog/${post.frontmatter.slug}`}
                      className="block py-2 group"
                    >
                      <div className="flex items-baseline justify-between gap-3">
                        <time
                          dateTime={toIsoDatetime(post.frontmatter.date)}
                          className="text-xs tabular-nums text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
                          style={{ fontFamily: "var(--font-mono)" }}
                        >
                          {formatPostDateShort(post.frontmatter.date)}
                        </time>
                        <span className="text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
                          {post.readingTimeMinutes}분
                        </span>
                      </div>
                      <h3 className="mt-0.5 text-base font-semibold group-hover:text-[var(--color-brand-primary)] transition">
                        {post.frontmatter.title}
                      </h3>
                      <p className="mt-1 text-sm leading-relaxed text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] line-clamp-2">
                        {post.frontmatter.description}
                      </p>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </section>
      )}
    </div>
  );
}

function groupByYear<T extends { frontmatter: { date: string } }>(
  items: T[],
): [string, T[]][] {
  const map = new Map<string, T[]>();
  for (const item of items) {
    const year = item.frontmatter.date.slice(0, 4);
    const bucket = map.get(year) ?? [];
    bucket.push(item);
    map.set(year, bucket);
  }
  return Array.from(map.entries()).sort(([a], [b]) => b.localeCompare(a));
}
