import { getBlogCoreMessages } from "../../lib/i18n";

export interface TocHeading {
  id: string;
  text: string;
  depth: number;
}

export interface TableOfContentsProps {
  /** Markdown 본문에서 추출된 heading들 */
  headings: TocHeading[];
  minDepth?: number;
  maxDepth?: number;
  title?: string;
  locale?: string;
}

/**
 * 서버에서 미리 추출한 heading 배열을 받아 렌더.
 * heading 추출은 extractHeadings(markdown) 유틸 사용 (lib/toc.ts).
 */
export function TableOfContents({
  headings,
  minDepth = 2,
  maxDepth = 3,
  title,
  locale,
}: TableOfContentsProps) {
  const resolvedTitle = title ?? getBlogCoreMessages(locale).tableOfContents;
  const filtered = headings.filter(
    (h) => h.depth >= minDepth && h.depth <= maxDepth,
  );
  if (filtered.length === 0) return null;

  return (
    <nav className="my-6 rounded-md border border-[color-mix(in_oklab,var(--foreground)_10%,transparent)] bg-[color-mix(in_oklab,var(--foreground)_3%,transparent)] px-4 py-3 text-sm not-prose">
      <p className="mb-2 text-xs font-bold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
        {resolvedTitle}
      </p>
      <ul className="space-y-1">
        {filtered.map((h) => (
          <li key={h.id} style={{ paddingLeft: `${(h.depth - minDepth) * 12}px` }}>
            <a
              href={`#${h.id}`}
              className="text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] hover:text-[var(--color-brand-primary)]"
            >
              {h.text}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
