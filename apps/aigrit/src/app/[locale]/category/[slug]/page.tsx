import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  PostCard,
  buildMetadata,
  SUPPORTED_LOCALES,
  toOgLocale,
} from "@unpack/blog-core";
import { getLocalizedBrand } from "../../../../../brand.config";
import {
  getAllCategorySlugs,
  getCategoryBySlug,
  getCategoryNav,
  getCategorySlugsWithPosts,
  getPostsInCategory,
} from "../../../../lib/categories";
import { CategorySidebar } from "../../../../components/layout/CategorySidebar";

/** ISR: 예약 발행글이 발행 시각 이후 자동 노출되도록 10분마다 재생성. */
export const revalidate = 600;

const CATEGORY_UI = {
  ko: {
    kicker: "CATEGORY",
    countSuffix: "편 · 최신순 정렬",
    countPrefix: "총 ",
    sidebarHeading: "카테고리",
    allLabel: "전체 보기",
  },
  en: {
    kicker: "CATEGORY",
    countSuffix: " posts · latest first",
    countPrefix: "Total ",
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
  const cat = getCategoryBySlug(slug, locale);
  if (!cat) return {};
  const localized = getLocalizedBrand(locale);

  // 글이 있는 locale 만 hreflang 으로 노출 (빈 카테고리 페이지를 가리키지 않도록)
  const hrefLangs: Record<string, string> = {};
  for (const l of SUPPORTED_LOCALES) {
    if (getCategorySlugsWithPosts(l).has(slug)) {
      hrefLangs[l] = `/${l}/category/${slug}`;
    }
  }
  const xDefault = hrefLangs.ko ?? hrefLangs[locale];
  if (xDefault) hrefLangs["x-default"] = xDefault;

  return buildMetadata({
    title: `${cat.name} — ${localized.name}`,
    description: cat.description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/category/${slug}`,
    locale: toOgLocale(locale),
    hrefLangs,
  });
}

export default async function CategoryPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { locale, slug } = await params;
  const cat = getCategoryBySlug(slug, locale);
  if (!cat) notFound();

  const ui = CATEGORY_UI[locale as keyof typeof CATEGORY_UI] ?? CATEGORY_UI.ko;
  const posts = getPostsInCategory(locale, slug);
  // 글이 없는 카테고리는 200 빈 페이지(soft 404) 대신 404 로 응답한다.
  // AdSense·GSC 모두 빈 목록 페이지를 "가치 낮은 콘텐츠"로 본다.
  if (posts.length === 0) notFound();
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

        <ul className="grid gap-3 sm:grid-cols-2">
          {posts.map((post) => (
            <li key={post.frontmatter.slug}>
              <PostCard post={post} hrefBase={hrefBase} locale={locale} />
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
