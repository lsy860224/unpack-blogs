import Link from "next/link";
import type { PostSummary } from "../../types/post";
import { getBlogCoreMessages } from "../../lib/i18n";

export interface RelatedPostsProps {
  allPosts: PostSummary[];
  currentSlug: string;
  tags?: string[];
  /** 현재 글의 topic_cluster — 같은 클러스터 글에 +10점 */
  currentCluster?: string;
  max?: number;
  hrefBase?: string;
  title?: string;
  locale?: string;
}

/**
 * 스코어링: 태그 일치 1점 × N + 같은 클러스터 10점 + pillar 5점.
 * 동점 시 날짜 역순.
 */
export function RelatedPosts({
  allPosts,
  currentSlug,
  tags = [],
  currentCluster,
  max = 3,
  hrefBase = "/blog",
  title,
  locale,
}: RelatedPostsProps) {
  const resolvedTitle = title ?? getBlogCoreMessages(locale).relatedPosts;
  const tagSet = new Set(tags);
  const scored = allPosts
    .filter((p) => p.frontmatter.slug !== currentSlug)
    .map((p) => {
      const tagMatches = (p.frontmatter.tags ?? []).reduce(
        (acc, t) => acc + (tagSet.has(t) ? 1 : 0),
        0,
      );
      const clusterBonus =
        currentCluster &&
        p.frontmatter.topic_cluster &&
        p.frontmatter.topic_cluster === currentCluster
          ? 10
          : 0;
      const pillarBonus = p.frontmatter.cluster_role === "pillar" ? 5 : 0;
      return { post: p, score: tagMatches + clusterBonus + pillarBonus };
    })
    .filter(({ score }) => score > 0)
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      return b.post.frontmatter.date.localeCompare(a.post.frontmatter.date);
    })
    .slice(0, max);

  if (scored.length === 0) return null;

  return (
    <section className="mt-16 border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pt-8 not-prose">
      <h2 className="text-sm font-bold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
        {resolvedTitle}
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
