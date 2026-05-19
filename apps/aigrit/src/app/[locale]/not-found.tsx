import Link from "next/link";
import { headers } from "next/headers";
import type { Metadata } from "next";
import { buildMetadata, toOgLocale } from "@unpack/blog-core";
import { brandConfig, getLocalizedBrand } from "../../../brand.config";

/**
 * Locale-scoped 404 page — uses parent layout's Header/Footer.
 * Triggered by `notFound()` in `[locale]/blog/[slug]/page.tsx`,
 * `[locale]/category/[slug]/page.tsx`, and other dynamic routes.
 */

async function resolveLocale(): Promise<string> {
  // Next 16: `headers()` is async and used here to read `x-pathname` if a
  // middleware sets it. We don't have that, so fall back to the default `ko`.
  // The locale prefix in the URL is implicit from the route group anyway.
  await headers();
  return "ko";
}

export async function generateMetadata(): Promise<Metadata> {
  const locale = await resolveLocale();
  const localized = getLocalizedBrand(locale);
  const description =
    locale === "en"
      ? `Page not found on ${localized.name}.`
      : `${localized.name}에서 찾을 수 없는 페이지입니다.`;
  return buildMetadata({
    title: "404 Not Found",
    description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/404`,
    locale: toOgLocale(locale),
  });
}

export default async function NotFound() {
  const locale = await resolveLocale();
  const isEn = locale === "en";
  const t = {
    heading: isEn ? "Page not found" : "찾을 수 없는 페이지",
    body: isEn
      ? "The URL you requested does not exist or has been removed. Please use the links below to navigate."
      : "요청하신 페이지가 존재하지 않거나 삭제되었습니다. 아래 링크로 이동해 주세요.",
    home: isEn ? "Back to home" : "홈으로",
    blog: isEn ? "All posts" : "전체 글 보기",
    about: isEn ? "About" : "운영자 소개",
    privacy: isEn ? "Privacy" : "개인정보 처리방침",
    disclaimer: isEn ? "Disclaimer" : "제휴·광고 고지",
  };
  const prefix = `/${locale}`;

  return (
    <div className="mx-auto max-w-3xl px-6 py-24 text-center">
      <p className="text-7xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
        404
      </p>
      <h1 className="mt-6 text-2xl sm:text-3xl font-bold tracking-tight">
        {t.heading}
      </h1>
      <p className="mt-4 text-[color-mix(in_oklab,var(--foreground)_75%,transparent)]">
        {t.body}
      </p>
      <nav className="mt-10 flex flex-wrap justify-center gap-x-6 gap-y-3 text-sm">
        <Link
          href={prefix}
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          {t.home}
        </Link>
        <Link
          href={`${prefix}/blog`}
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          {t.blog}
        </Link>
        <Link
          href={`${prefix}/about`}
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          {t.about}
        </Link>
        <Link
          href={`${prefix}/privacy`}
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          {t.privacy}
        </Link>
        <Link
          href={`${prefix}/disclaimer`}
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          {t.disclaimer}
        </Link>
      </nav>
      <p className="mt-12 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
        {brandConfig.name} — {brandConfig.tagline}
      </p>
    </div>
  );
}
