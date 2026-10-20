import Link from "next/link";
import path from "node:path";
import {
  getAllPostSummaries,
  PostCard,
  buildWebSiteJsonLd,
  toBcp47,
} from "@unpack/blog-core";
import { getLocalizedBrand } from "../../../brand.config";
import { resolveCategory } from "../../lib/categories";

/** ISR: 예약 발행글이 발행 시각 이후 자동 노출되도록 10분마다 재생성. */
export const revalidate = 600;

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
  const byCategory = groupByCategory(posts, locale, ui.other);
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
            className="inline-block h-1.5 w-6 rounded-full bg-brand-secondary"
          />
          <span className="text-xs font-semibold uppercase tracking-[0.2em] text-brand-secondary font-mono">
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
            className="rounded-md bg-brand-primary px-5 py-2.5 text-sm font-semibold text-[var(--background)] transition"
          >
            {ui.ctaLatest}
          </Link>
          <Link
            href={`/${locale}/about`}
            className="rounded-md border border-[color-mix(in_oklab,var(--foreground)_20%,transparent)] px-5 py-2.5 text-sm font-semibold text-[var(--foreground)]"
          >
            {ui.ctaAbout}
          </Link>
        </div>
      </section>

      {/* Latest */}
      {latest.length > 0 && (
        <section className="mb-14">
          <div className="flex items-baseline justify-between mb-4">
            <h2 className="text-xs font-bold uppercase tracking-[0.2em] font-mono text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
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
          <h2 className="text-xs font-bold uppercase tracking-[0.2em] font-mono text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] mb-6">
            {ui.byCategory}
          </h2>
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {byCategory.map(({ slug: catSlug, name: cat, posts: catPosts }) => {
              const catHref = catSlug ? `/${locale}/category/${catSlug}` : null;
              return (
                <div key={catSlug ?? cat}>
                  <h3 className="mb-3 text-lg font-bold">
                    {catHref ? (
                      <Link
                        href={catHref}
                        className="text-[var(--color-brand-primary)] transition hover:text-[var(--color-brand-secondary)]"
                      >
                        {cat}
                      </Link>
                    ) : (
                      <span className="text-[var(--color-brand-primary)]">
                        {cat}
                      </span>
                    )}
                    <span className="ml-2 text-xs tabular-nums font-mono text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
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
                  {catHref && catPosts.length > 4 && (
                    <Link
                      href={catHref}
                      className="mt-2 inline-block text-xs font-mono text-[color-mix(in_oklab,var(--foreground)_55%,transparent)] hover:text-[var(--color-brand-primary)]"
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

interface CategoryGroup {
  /** null = 카테고리 미지정 글 묶음 (카테고리 페이지 없음) */
  slug: string | null;
  name: string;
  posts: Summary[];
}

/** 별칭("AI 도구"·"LLM" 등)까지 같은 slug 로 묶어 대표명으로 표시한다. */
function groupByCategory(
  posts: Summary[],
  locale: string,
  otherLabel: string,
): CategoryGroup[] {
  const map = new Map<string, CategoryGroup>();
  for (const p of posts) {
    const raw = p.frontmatter.category;
    const resolved = raw ? resolveCategory(raw, locale) : null;
    const key = resolved?.slug ?? "__uncategorized__";
    const group = map.get(key) ?? {
      slug: resolved?.slug ?? null,
      name: resolved?.name ?? otherLabel,
      posts: [],
    };
    group.posts.push(p);
    map.set(key, group);
  }
  return Array.from(map.values()).sort(
    (a, b) => b.posts.length - a.posts.length,
  );
}
