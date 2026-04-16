import path from "node:path";
import type { Metadata } from "next";
import {
  PostCard,
  buildMetadata,
  getAllPostSummaries,
  toOgLocale,
} from "@unpack/blog-core";
import { getLocalizedBrand } from "../../../../brand.config";

const BLOG_UI = {
  ko: {
    kicker: "ALL REVIEWS",
    title: "Blog",
    empty: "아직 리뷰가 없습니다.",
    totalSuffix: "편 · 최신순 정렬",
    totalPrefix: "총 ",
  },
  en: {
    kicker: "ALL REVIEWS",
    title: "Blog",
    empty: "No reviews yet.",
    totalSuffix: " posts · sorted by date",
    totalPrefix: "",
  },
} as const;

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const localized = getLocalizedBrand(locale);
  const description =
    locale === "en"
      ? `All reviews from ${localized.name} — ${localized.tagline}`
      : `${localized.name}의 전체 리뷰 — ${localized.tagline}`;
  return buildMetadata({
    title: "Blog",
    description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/blog`,
    locale: toOgLocale(locale),
    hrefLangs: {
      ko: "/ko/blog",
      en: "/en/blog",
      "x-default": "/ko/blog",
    },
  });
}

export default async function BlogIndexPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const ui = BLOG_UI[locale as keyof typeof BLOG_UI] ?? BLOG_UI.ko;
  const CONTENT_DIR = path.join(process.cwd(), "content/posts", locale);
  const posts = getAllPostSummaries(CONTENT_DIR);
  const hrefBase = `/${locale}/blog`;

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
        <div className="flex items-center gap-2 mb-3">
          <span
            aria-hidden
            className="inline-block h-1 w-4 rounded-full"
            style={{ background: "var(--color-brand-secondary)" }}
          />
          <span
            className="text-xs font-semibold uppercase tracking-[0.2em]"
            style={{ color: "var(--color-brand-secondary)", fontFamily: "var(--font-mono)" }}
          >
            {ui.kicker}
          </span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
          {ui.title}
        </h1>
        <p
          className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          {ui.totalPrefix}
          <span className="tabular-nums">{posts.length}</span>
          {ui.totalSuffix}
        </p>
      </header>

      {posts.length === 0 ? (
        <p className="text-sm text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          {ui.empty}
        </p>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2">
          {posts.map((post) => (
            <li key={post.frontmatter.slug}>
              <PostCard post={post} hrefBase={hrefBase} locale={locale} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
