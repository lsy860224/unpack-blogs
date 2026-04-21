import Link from "next/link";
import Image from "next/image";
import type { PostSummary } from "../../types/post";
import { formatPostDate, toIsoDatetime } from "../../lib/date";
import { getBlogCoreMessages } from "../../lib/i18n";
import { cn } from "../../lib/cn";

export interface PostCardProps {
  post: PostSummary;
  variant?: "default" | "compact";
  hrefBase?: string;
  className?: string;
  showThumbnail?: boolean;
  locale?: string;
}

export function PostCard({
  post,
  variant = "default",
  hrefBase = "/blog",
  className,
  showThumbnail = true,
  locale,
}: PostCardProps) {
  const msg = getBlogCoreMessages(locale);
  const { frontmatter, readingTimeMinutes } = post;
  const isCompact = variant === "compact";
  const hasThumbnail = showThumbnail && !isCompact && !!frontmatter.thumbnail;

  return (
    <Link
      href={`${hrefBase}/${frontmatter.slug}`}
      className={cn(
        "group block rounded-lg transition overflow-hidden",
        "hover:bg-[color-mix(in_oklab,var(--foreground)_4%,transparent)]",
        isCompact ? "p-3" : "p-4",
        className,
      )}
    >
      {hasThumbnail && (
        <div className="mb-4 overflow-hidden rounded-md bg-[color-mix(in_oklab,var(--foreground)_4%,transparent)]">
          <Image
            src={frontmatter.thumbnail!}
            alt={frontmatter.title}
            width={1200}
            height={630}
            className="w-full h-auto object-cover transition-transform duration-300 group-hover:scale-[1.02]"
          />
        </div>
      )}
      <div className="flex items-baseline justify-between gap-3">
        <time
          dateTime={toIsoDatetime(frontmatter.date)}
          className="text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] tabular-nums"
        >
          {formatPostDate(frontmatter.date)}
        </time>
        <span className="text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
          {readingTimeMinutes}
          {msg.readingTimeUnit}
        </span>
      </div>
      <h3
        className={cn(
          "mt-1 font-semibold leading-snug group-hover:text-[var(--color-brand-primary)]",
          isCompact ? "text-base" : "text-lg",
        )}
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
