"use client";

import Link from "next/link";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

const LEGAL_LINKS = [
  { label: "About", href: "/about" },
  { label: "Privacy", href: "/privacy" },
  { label: "Disclaimer", href: "/disclaimer" },
];

const SISTER_LINKS = [
  { name: "babipanote", href: "https://babipanote.com", description: "빌더 저널" },
];

export function Footer() {
  const brand = useBrand();
  const year = new Date().getFullYear();

  return (
    <footer className="mt-24 border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
      <div className="mx-auto max-w-5xl px-6 py-10 grid gap-8 sm:grid-cols-4 text-sm">
        <div className="sm:col-span-2">
          <p className="text-base font-extrabold tracking-tight">
            <span className="text-[var(--color-brand-secondary)]">[</span>
            <span className="text-[var(--color-brand-primary)]">AI</span>
            <span className="text-[var(--color-brand-secondary)]">]</span>
            <span className="text-[var(--color-brand-primary)]">Grit</span>
          </p>
          <p className="mt-2 text-[color-mix(in_oklab,var(--foreground)_65%,transparent)] leading-relaxed max-w-sm">
            {brand.description}
          </p>
        </div>

        <div>
          <p className="font-semibold mb-2">사이트</p>
          <ul className="space-y-1">
            {LEGAL_LINKS.map((l) => (
              <li key={l.href}>
                <Link
                  href={l.href}
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  {l.label}
                </Link>
              </li>
            ))}
            {SISTER_LINKS.map((s) => (
              <li key={s.href}>
                <a
                  href={s.href}
                  rel="noopener noreferrer"
                  target="_blank"
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  {s.name}
                  <span className="ml-1 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
                    — {s.description}
                  </span>
                </a>
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
                  rel="noopener noreferrer"
                  target="_blank"
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  X (Twitter)
                </a>
              </li>
            )}
            {brand.social.instagram && (
              <li>
                <a
                  href={`https://instagram.com/${brand.social.instagram.replace(/^@/, "")}`}
                  rel="noopener noreferrer"
                  target="_blank"
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  Instagram
                </a>
              </li>
            )}
            {brand.social.github && (
              <li>
                <a
                  href={`https://github.com/${brand.social.github}`}
                  rel="noopener noreferrer"
                  target="_blank"
                  className="text-[color-mix(in_oklab,var(--foreground)_70%,transparent)] hover:text-[var(--color-brand-primary)]"
                >
                  GitHub
                </a>
              </li>
            )}
          </ul>
        </div>
      </div>
      <div className="mx-auto max-w-5xl px-6 pb-8 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)] flex flex-col gap-1">
        <span>© {year} {brand.name}. All reviews are opinions based on hands-on use.</span>
        {brand.monetization.adsense && (
          <span>이 사이트는 Google AdSense 광고와 제휴 마케팅 수익으로 운영됩니다. 자세한 내용은 <Link href="/disclaimer" className="underline hover:text-[var(--color-brand-primary)]">고지사항</Link>을 참고하세요.</span>
        )}
      </div>
    </footer>
  );
}
