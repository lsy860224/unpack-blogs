"use client";

import Link from "next/link";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

export function Header() {
  const brand = useBrand();
  return (
    <header className="sticky top-0 z-40 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] bg-[color-mix(in_oklab,var(--background)_92%,transparent)] backdrop-blur">
      <div className="mx-auto max-w-5xl px-6 py-4 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-1 font-extrabold tracking-tight">
          <span className="text-[var(--color-brand-secondary)]">[</span>
          <span className="text-[var(--color-brand-primary)]">AI</span>
          <span className="text-[var(--color-brand-secondary)]">]</span>
          <span className="text-[var(--color-brand-primary)]">Grit</span>
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
