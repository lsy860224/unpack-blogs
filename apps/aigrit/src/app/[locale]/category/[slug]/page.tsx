import Link from "next/link";
import path from "node:path";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  PostCard,
  buildMetadata,
  getAllPostSummaries,
  SUPPORTED_LOCALES,
  toOgLocale,
} from "@unpack/blog-core";
import { getLocalizedBrand } from "../../../../../brand.config";
import {
  getAllCategorySlugs,
  getCategoryBySlug,
  getCategoryNav,
} from "../../../../lib/categories";
import { CategorySidebar } from "../../../../components/layout/CategorySidebar";

const CATEGORY_UI = {
  ko: {
    kicker: "CATEGORY",
    countSuffix: "편 · 최신순 정렬",
    countPrefix: "총 ",
    empty: "아직 이 카테고리의 리뷰가 없습니다.",
    sidebarHeading: "카테고리",
    allLabel: "전체 보기",
  },
  en: {
    kicker: "CATEGORY",
    countSuffix: " posts · latest first",
    countPrefix: "Total ",
    empty: "No reviews in this category yet.",
    sidebarHeading: "CATEGORY",
    allLabel: "All",
  },
} as const;

interface Params {
  locale: string;
  slug: string;
}

export function generateStaticParams(): { slug: string }[] {
  return getAllCategorySlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}): Promise<Metadata> {
  const { locale, slug } = await params;
  const cat = getCategoryBySlug(slug);
  if (!cat) return {};
  const localized = getLocalizedBrand(locale);
  return buildMetadata({
    title: `${cat.name} — ${localized.name}`,
    description: cat.description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/category/${slug}`,
    locale: toOgLocale(locale),
    hrefLangs: {
      ...Object.fromEntries(
        SUPPORTED_LOCALES.map((l) => [l, `/${l}/category/${slug}`]),
      ),
      "x-default": `/ko/category/${slug}`,
    },
  });
}

export default async function CategoryPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { locale, slug } = await params;
  const cat = getCategoryBySlug(slug);
  if (!cat) notFound();

  const ui = CATEGORY_UI[locale as keyof typeof CATEGORY_UI] ?? CATEGORY_UI.ko;
  const CONTENT_DIR = path.join(process.cwd(), "content/posts", locale);
  const posts = getAllPostSummaries(CONTENT_DIR, { brand: "aigrit" }).filter(
    (p) => p.frontmatter.category === cat.name,
  );
  const hrefBase = `/${locale}/blog`;
  const navEntries = getCategoryNav(locale, ui.allLabel);

  return (
    <div className="mx-auto max-w-6xl px-6 py-12 lg:flex lg:gap-10">
      <aside className="mb-8 lg:mb-0 lg:w-56 lg:shrink-0">
        <CategorySidebar
          entries={navEntries}
          activeSlug={slug}
          heading={ui.sidebarHeading}
        />
      </aside>
      <div className="min-w-0 flex-1">
        <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
          <div className="flex items-center gap-2 mb-3">
            <span
              aria-hidden
              className="inline-block h-1 w-4 rounded-full bg-brand-secondary"
            />
            <Link
              href={`/${locale}/blog`}
              className="text-xs font-semibold uppercase tracking-[0.2em] text-brand-secondary font-mono hover:opacity-80"
            >
              {ui.kicker}
            </Link>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
            {cat.name}
          </h1>
          <p className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_70%,transparent)]">
            {cat.description}
          </p>
          <p className="mt-3 text-xs font-mono text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
            {ui.countPrefix}
            <span className="tabular-nums">{posts.length}</span>
            {ui.countSuffix}
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
    </div>
  );
}
