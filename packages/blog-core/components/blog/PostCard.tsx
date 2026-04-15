import Link from "next/link";
import type { PostSummary } from "../../types/post";
import { formatPostDate, toIsoDatetime } from "../../lib/date";

export interface PostCardProps {
  post: PostSummary;
  variant?: "default" | "compact";
  hrefBase?: string;
  className?: string;
}

export function PostCard({
  post,
  variant = "default",
  hrefBase = "/blog",
  className,
}: PostCardProps) {
  const { frontmatter, readingTimeMinutes } = post;
  const isCompact = variant === "compact";

  return (
    <Link
      href={`${hrefBase}/${frontmatter.slug}`}
      className={[
        "group block rounded-lg transition",
        "hover:bg-[color-mix(in_oklab,var(--foreground)_4%,transparent)]",
        isCompact ? "p-3" : "p-4",
        className ?? "",
      ].join(" ")}
    >
      <div className="flex items-baseline justify-between gap-3">
        <time
          dateTime={toIsoDatetime(frontmatter.date)}
          className="text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] tabular-nums"
        >
          {formatPostDate(frontmatter.date)}
        </time>
        <span className="text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
          {readingTimeMinutes}분
        </span>
      </div>
      <h3
        className={[
          "mt-1 font-semibold leading-snug group-hover:text-[var(--color-brand-primary)]",
          isCompact ? "text-base" : "text-lg",
        ].join(" ")}
      >
        {frontmatter.title}
      </h3>
      {!isCompact && (
        <p className="mt-2 text-sm leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] line-clamp-2">
          {frontmatter.description}
        </p>
      )}
      {frontmatter.tags && frontmatter.tags.length > 0 && !isCompact && (
        <div className="mt-3 flex flex-wrap gap-1.5">
          {frontmatter.tags.map((tag) => (
            <span
              key={tag}
              className="text-xs px-2 py-0.5 rounded bg-[color-mix(in_oklab,var(--color-brand-primary)_10%,transparent)] text-[var(--color-brand-primary)]"
            >
              #{tag}
            </span>
          ))}
        </div>
      )}
    </Link>
  );
}
