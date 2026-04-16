"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

const LOCALES = ["ko", "en"] as const;

export function Header({ locale }: { locale: string }) {
  const brand = useBrand();
  const pathname = usePathname();

  const swapLocale = (target: string) => {
    if (!pathname) return `/${target}`;
    const segments = pathname.split("/");
    if (
      segments.length >= 2 &&
      (LOCALES as readonly string[]).includes(segments[1])
    ) {
      segments[1] = target;
      return segments.join("/") || `/${target}`;
    }
    return `/${target}${pathname === "/" ? "" : pathname}`;
  };

  const withLocale = (href: string) =>
    `/${locale}${href === "/" ? "" : href}`;

  return (
    <header className="sticky top-0 z-40 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] bg-[color-mix(in_oklab,var(--background)_92%,transparent)] backdrop-blur">
      <div className="mx-auto max-w-5xl px-6 py-4 flex items-center justify-between">
        <Link
          href={`/${locale}`}
          className="flex items-center gap-1 font-extrabold tracking-tight"
        >
          <span className="text-[var(--color-brand-secondary)]">[</span>
          <span className="text-[var(--color-brand-primary)]">AI</span>
          <span className="text-[var(--color-brand-secondary)]">]</span>
          <span className="text-[var(--color-brand-primary)]">Grit</span>
        </Link>
        <nav className="flex items-center gap-5 text-sm">
          {brand.nav.map((item) => (
            <Link
              key={item.href}
              href={withLocale(item.href)}
              className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)] transition"
            >
              {item.label}
            </Link>
          ))}
          <span
            className="mx-1 h-4 w-px bg-[color-mix(in_oklab,var(--foreground)_15%,transparent)]"
            aria-hidden
          />
          <div
            className="flex items-center gap-1 text-xs"
            style={{ fontFamily: "var(--font-mono)" }}
          >
            {LOCALES.map((l, i) => (
              <span key={l} className="flex items-center gap-1">
                {i > 0 && (
                  <span className="text-[color-mix(in_oklab,var(--foreground)_35%,transparent)]">
                    /
                  </span>
                )}
                <Link
                  href={swapLocale(l)}
                  className={
                    l === locale
                      ? "font-bold text-[var(--color-brand-primary)]"
                      : "text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] hover:text-[var(--color-brand-primary)]"
                  }
                  aria-current={l === locale ? "page" : undefined}
                >
                  {l.toUpperCase()}
                </Link>
              </span>
            ))}
          </div>
        </nav>
      </div>
    </header>
  );
}
