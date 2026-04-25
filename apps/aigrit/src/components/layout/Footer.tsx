"use client";

import Link from "next/link";
import { useBrand } from "@unpack/blog-core/contexts/brand-context";

const SISTER_LINKS = [
  {
    name: "babipanote",
    href: "https://babipanote.com",
    descriptionKo: "빌더 저널",
    descriptionEn: "Builder journal",
  },
];

const FOOTER_UI = {
  ko: {
    site: "사이트",
    social: "소셜",
    copyrightTail: "실사용에 기반한 의견입니다.",
    adsNotice:
      "이 사이트는 Google AdSense 광고와 제휴 마케팅 수익으로 운영됩니다.",
    seeDisclaimer: "자세한 내용은",
    disclaimerLink: "고지사항",
    seeDisclaimerSuffix: "을 참고하세요.",
  },
  en: {
    site: "Pages",
    social: "Social",
    copyrightTail: "All reviews are opinions based on hands-on use.",
    adsNotice:
      "This site is supported by Google AdSense and affiliate marketing.",
    seeDisclaimer: "See our",
    disclaimerLink: "disclaimer",
    seeDisclaimerSuffix: "for details.",
  },
} as const;

export function Footer({ locale }: { locale: string }) {
  const brand = useBrand();
  const year = new Date().getFullYear();
  const ui = FOOTER_UI[locale as keyof typeof FOOTER_UI] ?? FOOTER_UI.ko;

  const withLocale = (href: string) => `/${locale}${href === "/" ? "" : href}`;

  return (
    <footer className="mt-24 border-t border-[color-mix(in_oklab,var(--foreground)_8%,transparent)]">
      <div className="mx-auto max-w-5xl px-6 py-10 grid gap-8 sm:grid-cols-4 text-sm">
        <div className="sm:col-span-2">
          {/* Brand Master `[AI]Grit Wordmark` 사양 — Header.tsx와 동일 */}
          <p className="text-base font-extrabold tracking-tight">
            <span className="text-[var(--color-brand-secondary)]">[</span>
            <span className="text-[var(--color-brand-primary)] dark:text-white">
              AI
            </span>
            <span className="text-[var(--color-brand-secondary)]">]</span>
            <span className="ml-1 text-[var(--foreground)]">Grit</span>
          </p>
          <p className="mt-2 text-[color-mix(in_oklab,var(--foreground)_65%,transparent)] leading-relaxed max-w-sm">
            {brand.description}
          </p>
        </div>

        <div>
          <p className="font-semibold mb-2">{ui.site}</p>
          <ul className="space-y-1">
            {brand.nav.map((l) => (
              <li key={l.href}>
                <Link
                  href={withLocale(l.href)}
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
                    — {locale === "en" ? s.descriptionEn : s.descriptionKo}
                  </span>
                </a>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <p className="font-semibold mb-2">{ui.social}</p>
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
        <span>
          © {year} {brand.name}. {ui.copyrightTail}
        </span>
        {brand.monetization.adsense && (
          <span>
            {ui.adsNotice} {ui.seeDisclaimer}{" "}
            <Link
              href={withLocale("/disclaimer")}
              className="underline hover:text-[var(--color-brand-primary)]"
            >
              {ui.disclaimerLink}
            </Link>
            {ui.seeDisclaimerSuffix}
          </span>
        )}
      </div>
    </footer>
  );
}
