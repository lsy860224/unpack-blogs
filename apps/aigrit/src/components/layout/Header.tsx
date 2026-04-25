"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

const LOCALES = ["ko", "en"] as const;

export function Header({ locale }: { locale: string }) {
  const brand = useBrand();
  const pathname = usePathname();
  const [open, setOpen] = useState(false);

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

  const withLocale = (href: string) => `/${locale}${href === "/" ? "" : href}`;

  const localeSwitcher = (
    <div className="flex items-center gap-1 text-xs font-mono">
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
            onClick={() => setOpen(false)}
          >
            {l.toUpperCase()}
          </Link>
        </span>
      ))}
    </div>
  );

  return (
    <header className="sticky top-0 z-40 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] bg-[color-mix(in_oklab,var(--background)_92%,transparent)] backdrop-blur">
      <div className="mx-auto max-w-5xl px-6 py-4 flex items-center justify-between">
        {/* Logo — Brand Master `[AI]Grit Wordmark` 사양:
            bracket=secondary, AI=primary(light)/snow(dark), Grit=foreground */}
        <Link
          href={`/${locale}`}
          className="flex items-baseline font-display font-extrabold tracking-logo shrink-0"
        >
          <span className="text-[var(--color-brand-secondary)]">[</span>
          <span className="text-[var(--color-brand-primary)] dark:text-white">
            AI
          </span>
          <span className="text-[var(--color-brand-secondary)]">]</span>
          <span className="ml-1 text-[var(--foreground)]">Grit</span>
        </Link>

        {/* Desktop nav (md+) */}
        <nav className="hidden md:flex items-center gap-5 text-sm">
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
          {localeSwitcher}
        </nav>

        {/* Mobile: locale switcher + hamburger */}
        <div className="flex md:hidden items-center gap-3">
          {localeSwitcher}
          <button
            type="button"
            onClick={() => setOpen(!open)}
            className="relative w-6 h-6 flex flex-col items-center justify-center gap-1.5"
            aria-label={open ? "Close menu" : "Open menu"}
            aria-expanded={open}
          >
            <span
              className={`block h-0.5 w-5 rounded-full bg-[var(--foreground)] transition-all duration-200 ${
                open ? "translate-y-[7px] rotate-45" : ""
              }`}
            />
            <span
              className={`block h-0.5 w-5 rounded-full bg-[var(--foreground)] transition-opacity duration-200 ${
                open ? "opacity-0" : ""
              }`}
            />
            <span
              className={`block h-0.5 w-5 rounded-full bg-[var(--foreground)] transition-all duration-200 ${
                open ? "-translate-y-[7px] -rotate-45" : ""
              }`}
            />
          </button>
        </div>
      </div>

      {/* Mobile dropdown */}
      {open && (
        <nav className="md:hidden border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] bg-[var(--background)]">
          <ul className="mx-auto max-w-5xl px-6 py-3 flex flex-col gap-1">
            {brand.nav.map((item) => (
              <li key={item.href}>
                <Link
                  href={withLocale(item.href)}
                  onClick={() => setOpen(false)}
                  className="block py-2.5 text-sm text-[color-mix(in_oklab,var(--foreground)_80%,transparent)] hover:text-[var(--color-brand-primary)] transition"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      )}
    </header>
  );
}
