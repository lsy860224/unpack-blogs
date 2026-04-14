"use client";

import Link from "next/link";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

export function Header() {
  const brand = useBrand();
  return (
    <header className="border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
      <div className="mx-auto max-w-3xl px-6 py-5 flex items-center justify-between">
        <Link
          href="/"
          className="text-xl font-bold tracking-tight text-[var(--color-brand-primary)]"
          style={{ fontFamily: "var(--font-serif)" }}
        >
          {brand.name}
          <span className="text-[var(--color-brand-secondary)]">·</span>
        </Link>
        <nav className="flex items-center gap-5 text-sm">
          {brand.nav.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)] transition"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
