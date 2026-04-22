"use client";

import Link from "next/link";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

const PROJECT_LINKS = [
  {
    name: "AIGrit",
    href: "https://aigrit.dev",
    description: "AI 도구 리뷰",
  },
  {
    name: "GentleLab",
    href: "/projects",
    description: "가족을 위한 앱 시리즈",
  },
];

export function Footer() {
  const brand = useBrand();
  const year = new Date().getFullYear();

  return (
    <footer className="mt-20 border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
      <div className="mx-auto max-w-3xl px-6 py-10 grid gap-8 sm:grid-cols-3 text-sm">
        <div>
          <p className="text-base font-bold font-serif text-[var(--color-brand-primary)]">
            {brand.name}
            <span className="text-[var(--color-brand-secondary)]">·</span>
          </p>
          <p className="mt-2 text-[color-mix(in_oklab,var(--foreground)_65%,transparent)] leading-relaxed">
            {brand.tagline}
          </p>
        </div>

        <div>
          <p className="font-semibold mb-2">프로젝트</p>
          <ul className="space-y-1">
            {PROJECT_LINKS.map((p) => (
              <li key={p.name}>
                <Link
                  href={p.href}
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  {p.name}
                  <span className="ml-1 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
                    — {p.description}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <p className="font-semibold mb-2">소셜</p>
          <ul className="space-y-1">
            {brand.social.x && (
              <li>
                <a
                  href={`https://x.com/${brand.social.x.replace(/^@/, "")}`}
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                  rel="noopener noreferrer"
                  target="_blank"
                >
                  X (Twitter)
                </a>
              </li>
            )}
            {brand.social.instagram && (
              <li>
                <a
                  href={`https://instagram.com/${brand.social.instagram.replace(/^@/, "")}`}
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                  rel="noopener noreferrer"
                  target="_blank"
                >
                  Instagram
                </a>
              </li>
            )}
            {brand.social.threads && (
              <li>
                <a
                  href={`https://threads.net/${brand.social.threads.replace(/^@/, "")}`}
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                  rel="noopener noreferrer"
                  target="_blank"
                >
                  Threads
                </a>
              </li>
            )}
          </ul>
        </div>
      </div>
      <div className="mx-auto max-w-3xl px-6 pb-8 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
        © {year} {brand.name}. 개인 저널.
      </div>
    </footer>
  );
}
