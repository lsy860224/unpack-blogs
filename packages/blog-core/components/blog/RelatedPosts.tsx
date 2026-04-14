import Link from "next/link";
import type { PostSummary } from "../../types/post";

export interface RelatedPostsProps {
  /** 후보 풀 — 전체 글 목록 */
  allPosts: PostSummary[];
  /** 현재 글 slug (제외 대상) */
  currentSlug: string;
  /** 현재 글 태그 (매칭 점수 계산용) */
  tags?: string[];
  /** 최대 개수 */
  max?: number;
  hrefBase?: string;
  title?: string;
}

/**
 * 현재 글과 태그 겹침 기준으로 관련 글을 산출.
 * 태그 매칭 점수 동률이면 날짜 역순.
 */
export function RelatedPosts({
  allPosts,
  currentSlug,
  tags = [],
  max = 3,
  hrefBase = "/blog",
  title = "관련 글",
}: RelatedPostsProps) {
  const tagSet = new Set(tags);
  const scored = allPosts
    .filter((p) => p.frontmatter.slug !== currentSlug)
    .map((p) => {
      const matches = (p.frontmatter.tags ?? []).reduce(
        (acc, t) => acc + (tagSet.has(t) ? 1 : 0),
        0,
      );
      return { post: p, score: matches };
    })
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      return b.post.frontmatter.date.localeCompare(a.post.frontmatter.date);
    })
    .slice(0, max);

  if (scored.length === 0) return null;

  return (
    <section className="mt-16 border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pt-8 not-prose">
      <h2 className="text-sm font-bold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
        {title}
      </h2>
      <ul className="mt-4 divide-y divide-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
        {scored.map(({ post }) => (
          <li key={post.frontmatter.slug}>
            <Link
              href={`${hrefBase}/${post.frontmatter.slug}`}
              className="block py-3 group"
            >
              <div className="flex items-baseline justify-between gap-3">
                <h3 className="font-semibold group-hover:text-[var(--color-brand-primary)]">
                  {post.frontmatter.title}
                </h3>
                <time
                  dateTime={post.frontmatter.date}
                  className="shrink-0 text-xs tabular-nums text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
                  style={{ fontFamily: "var(--font-mono)" }}
                >
                  {post.frontmatter.date}
                </time>
              </div>
              <p className="mt-1 text-sm leading-relaxed text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] line-clamp-1">
                {post.frontmatter.description}
              </p>
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}
