import Link from "next/link";
import type { CategoryNavEntry } from "../../lib/categories";

export interface CategorySidebarProps {
  entries: CategoryNavEntry[];
  activeSlug: string | null;
  heading: string;
}

export function CategorySidebar({
  entries,
  activeSlug,
  heading,
}: CategorySidebarProps) {
  return (
    <nav aria-label={heading}>
      {/* Desktop: vertical sticky sidebar */}
      <div className="hidden lg:block lg:sticky lg:top-20">
        <h2
          className="mb-3 text-xs font-bold uppercase tracking-[0.2em] text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          {heading}
        </h2>
        <ul className="space-y-1">
          {entries.map((entry) => {
            const active = entry.slug === activeSlug;
            return (
              <li key={entry.slug ?? "__all__"}>
                <Link
                  href={entry.href}
                  aria-current={active ? "page" : undefined}
                  className={`flex items-center justify-between rounded-md border-l-[3px] px-3 py-1.5 text-sm transition ${
                    active
                      ? "border-[var(--color-brand-primary)] bg-[color-mix(in_oklab,var(--color-brand-primary)_8%,transparent)] font-semibold text-[var(--color-brand-primary)]"
                      : "border-transparent text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] hover:border-[var(--color-brand-secondary)] hover:text-[var(--color-brand-primary)]"
                  }`}
                >
                  <span className="truncate">{entry.name}</span>
                  <span
                    className="ml-2 text-xs tabular-nums text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]"
                    style={{ fontFamily: "var(--font-mono)" }}
                  >
                    {entry.count}
                  </span>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>

      {/* Mobile: horizontal scrollable pills */}
      <div className="lg:hidden -mx-6 px-6 overflow-x-auto">
        <ul className="flex gap-2 whitespace-nowrap pb-1">
          {entries.map((entry) => {
            const active = entry.slug === activeSlug;
            return (
              <li key={entry.slug ?? "__all__"}>
                <Link
                  href={entry.href}
                  aria-current={active ? "page" : undefined}
                  className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs transition ${
                    active
                      ? "border-[var(--color-brand-primary)] bg-[color-mix(in_oklab,var(--color-brand-primary)_10%,transparent)] font-semibold text-[var(--color-brand-primary)]"
                      : "border-[color-mix(in_oklab,var(--foreground)_15%,transparent)] text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] hover:border-[var(--color-brand-secondary)] hover:text-[var(--color-brand-primary)]"
                  }`}
                >
                  <span>{entry.name}</span>
                  <span
                    className="tabular-nums text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]"
                    style={{ fontFamily: "var(--font-mono)" }}
                  >
                    {entry.count}
                  </span>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    </nav>
  );
}
