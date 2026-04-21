import Link from "next/link";
import path from "node:path";
import {
  getAllPostSummaries,
  PostCard,
  buildWebSiteJsonLd,
  toBcp47,
} from "@unpack/blog-core";
import { getLocalizedBrand } from "../../../brand.config";
import { getCategorySlug } from "../../lib/categories";

const HOME_UI = {
  ko: {
    kicker: "AI TOOL REVIEW",
    ctaLatest: "최신 리뷰 →",
    ctaAbout: "어떻게 리뷰하나요",
    latest: "LATEST REVIEWS",
    seeAll: "전체 보기 →",
    byCategory: "BY CATEGORY",
    seeCategoryAll: "카테고리 전체 보기 →",
    empty: "아직 작성된 리뷰가 없습니다. 곧 첫 글을 올릴게요.",
    other: "기타",
  },
  en: {
    kicker: "AI TOOL REVIEW",
    ctaLatest: "Latest reviews →",
    ctaAbout: "How we review",
    latest: "LATEST REVIEWS",
    seeAll: "View all →",
    byCategory: "BY CATEGORY",
    seeCategoryAll: "See all in category →",
    empty: "No reviews yet. The first post is coming soon.",
    other: "Other",
  },
} as const;

export default async function HomePage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const ui = HOME_UI[locale as keyof typeof HOME_UI] ?? HOME_UI.ko;
  const localized = getLocalizedBrand(locale);
  const CONTENT_DIR = path.join(process.cwd(), "content/posts", locale);
  const posts = getAllPostSummaries(CONTENT_DIR, { brand: "aigrit" });
  const latest = posts.slice(0, 6);
  const byCategory = groupByCategory(posts, ui.other);
  const jsonLd = buildWebSiteJsonLd({
    siteName: localized.name,
    siteUrl: localized.url,
    description: localized.description,
    inLanguage: toBcp47(locale),
    searchPath: `/${locale}/blog`,
  });
  const hrefBase = `/${locale}/blog`;

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* Hero */}
      <section className="mb-14">
        <div className="flex items-center gap-2 mb-4">
          <span
            aria-hidden
            className="inline-block h-1.5 w-6 rounded-full"
            style={{ background: "var(--color-brand-secondary)" }}
          />
          <span
            className="text-xs font-semibold uppercase tracking-[0.2em]"
            style={{
              color: "var(--color-brand-secondary)",
              fontFamily: "var(--font-mono)",
            }}
          >
            {ui.kicker}
          </span>
        </div>
        <h1 className="text-4xl sm:text-5xl font-extrabold leading-[1.15] tracking-tight text-[var(--color-brand-primary)]">
          {localized.tagline}
        </h1>
        <p className="mt-4 text-base sm:text-lg leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)] max-w-2xl">
          {localized.description}
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Link
            href={`/${locale}/blog`}
            className="rounded-md px-5 py-2.5 text-sm font-semibold transition"
            style={{
              background: "var(--color-brand-primary)",
              color: "var(--background)",
            }}
          >
            {ui.ctaLatest}
          </Link>
          <Link
            href={`/${locale}/about`}
            className="rounded-md border px-5 py-2.5 text-sm font-semibold"
            style={{
              borderColor:
                "color-mix(in oklab, var(--foreground) 20%, transparent)",
              color: "var(--foreground)",
            }}
          >
            {ui.ctaAbout}
          </Link>
        </div>
      </section>

      {/* Latest */}
      {latest.length > 0 && (
        <section className="mb-14">
          <div className="flex items-baseline justify-between mb-4">
            <h2
              className="text-xs font-bold uppercase tracking-[0.2em] text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
              style={{ fontFamily: "var(--font-mono)" }}
            >
              {ui.latest}
            </h2>
            <Link
              href={`/${locale}/blog`}
              className="text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] hover:text-[var(--color-brand-primary)]"
            >
              {ui.seeAll}
            </Link>
          </div>
          <ul className="grid gap-2 sm:grid-cols-2">
            {latest.map((post) => (
              <li key={post.frontmatter.slug}>
                <PostCard post={post} hrefBase={hrefBase} locale={locale} />
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Categories */}
      {byCategory.length > 0 && (
        <section>
          <h2
            className="text-xs font-bold uppercase tracking-[0.2em] text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] mb-6"
            style={{ fontFamily: "var(--font-mono)" }}
          >
            {ui.byCategory}
          </h2>
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {byCategory.map(([cat, catPosts]) => {
              const catHref = `/${locale}/category/${getCategorySlug(cat)}`;
              return (
                <div key={cat}>
                  <h3 className="mb-3 text-lg font-bold">
                    <Link
                      href={catHref}
                      className="text-[var(--color-brand-primary)] transition hover:text-[var(--color-brand-secondary)]"
                    >
                      {cat}
                    </Link>
                    <span
                      className="ml-2 text-xs tabular-nums text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]"
                      style={{ fontFamily: "var(--font-mono)" }}
                    >
                      {catPosts.length}
                    </span>
                  </h3>
                  <ul className="space-y-1">
                    {catPosts.slice(0, 4).map((p) => (
                      <li key={p.frontmatter.slug}>
                        <Link
                          href={`/${locale}/blog/${p.frontmatter.slug}`}
                          className="block py-1 text-sm text-[color-mix(in_oklab,var(--foreground)_80%,transparent)] hover:text-[var(--color-brand-primary)]"
                        >
                          {p.frontmatter.title}
                        </Link>
                      </li>
                    ))}
                  </ul>
                  {catPosts.length > 4 && (
                    <Link
                      href={catHref}
                      className="mt-2 inline-block text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] hover:text-[var(--color-brand-primary)]"
                      style={{ fontFamily: "var(--font-mono)" }}
                    >
                      {ui.seeCategoryAll}
                    </Link>
                  )}
                </div>
              );
            })}
          </div>
        </section>
      )}

      {posts.length === 0 && (
        <section className="mt-8 rounded-md border border-[color-mix(in_oklab,var(--foreground)_10%,transparent)] p-8 text-center">
          <p className="text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
            {ui.empty}
          </p>
        </section>
      )}
    </div>
  );
}

type Summary = ReturnType<typeof getAllPostSummaries>[number];

function groupByCategory(
  posts: Summary[],
  otherLabel: string,
): [string, Summary[]][] {
  const map = new Map<string, Summary[]>();
  for (const p of posts) {
    const cat = p.frontmatter.category ?? otherLabel;
    const bucket = map.get(cat) ?? [];
    bucket.push(p);
    map.set(cat, bucket);
  }
  return Array.from(map.entries()).sort((a, b) => b[1].length - a[1].length);
}
