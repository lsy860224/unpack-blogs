import type { Post } from "../../types/post";
import { formatPostDate, toIsoDatetime } from "../../lib/date";

export interface PostHeaderProps {
  post: Post;
  className?: string;
}

export function PostHeader({ post, className }: PostHeaderProps) {
  const { frontmatter, readingTimeMinutes } = post;
  return (
    <header className={["mb-8", className ?? ""].join(" ")}>
      {frontmatter.tags && frontmatter.tags.length > 0 && (
        <div className="mb-3 flex flex-wrap gap-1.5">
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
      <h1 className="text-3xl sm:text-4xl font-bold leading-tight tracking-tight">
        {frontmatter.title}
      </h1>
      <p className="mt-3 text-base leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)]">
        {frontmatter.description}
      </p>
      <div className="mt-4 flex items-center gap-3 text-sm text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
        <time dateTime={toIsoDatetime(frontmatter.date)} className="tabular-nums">
          {formatPostDate(frontmatter.date)}
        </time>
        <span aria-hidden>·</span>
        <span>읽는 시간 {readingTimeMinutes}분</span>
      </div>
    </header>
  );
}
