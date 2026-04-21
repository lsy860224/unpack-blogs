import path from "node:path";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  PostHeader,
  PostRenderer,
  buildMetadata,
  buildArticleJsonLd,
  buildReviewJsonLd,
  getAllPostSlugs,
  getAllPostSummaries,
  getPostBySlug,
  defaultMdxComponents,
  AdInArticle,
  Comments,
  RelatedPosts,
  TableOfContents,
  extractHeadings,
  toIsoDatetime,
  SUPPORTED_LOCALES,
  toOgLocale,
  toBcp47,
} from "@unpack/blog-core";
import { brandConfig, getLocalizedBrand } from "../../../../../brand.config";

function contentDirFor(locale: string) {
  return path.join(process.cwd(), "content/posts", locale);
}

interface Params {
  locale: string;
  slug: string;
}

export function generateStaticParams(): Params[] {
  const params: Params[] = [];
  for (const locale of SUPPORTED_LOCALES) {
    for (const slug of getAllPostSlugs(contentDirFor(locale), {
      brand: "aigrit",
    })) {
      params.push({ locale, slug });
    }
  }
  return params;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}): Promise<Metadata> {
  const { locale, slug } = await params;
  const post = getPostBySlug(contentDirFor(locale), slug, { brand: "aigrit" });
  if (!post) return {};
  const localized = getLocalizedBrand(locale);
  return buildMetadata({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    type: "article",
    publishedTime: toIsoDatetime(post.frontmatter.date),
    tags: post.frontmatter.tags,
    locale: toOgLocale(locale),
    hrefLangs: {
      ko: `/ko/blog/${post.frontmatter.slug}`,
      en: `/en/blog/${post.frontmatter.slug}`,
      "x-default": `/ko/blog/${post.frontmatter.slug}`,
    },
  });
}

export default async function PostPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { locale, slug } = await params;
  const dir = contentDirFor(locale);
  const post = getPostBySlug(dir, slug, { brand: "aigrit" });
  if (!post) notFound();

  const allPosts = getAllPostSummaries(dir, { brand: "aigrit" });
  const headings = extractHeadings(post.content);
  const localized = getLocalizedBrand(locale);
  const bcp47 = toBcp47(locale);

  const articleJsonLd = buildArticleJsonLd({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    datePublished: toIsoDatetime(post.frontmatter.date),
    inLanguage: bcp47,
  });

  const reviewJsonLd = post.frontmatter.review
    ? buildReviewJsonLd({
        productName: post.frontmatter.review.productName,
        productCategory: post.frontmatter.review.productCategory,
        ratingValue: post.frontmatter.review.ratingValue,
        bestRating: post.frontmatter.review.bestRating,
        worstRating: post.frontmatter.review.worstRating,
        authorName: localized.name,
        datePublished: toIsoDatetime(post.frontmatter.date),
        url: `${localized.url}/${locale}/blog/${post.frontmatter.slug}`,
        inLanguage: bcp47,
      })
    : null;

  const adsEnabled = brandConfig.monetization.adsense;
  const adsPubId = brandConfig.monetization.adsensePublisherId;
  const hrefBase = `/${locale}/blog`;

  return (
    <article className="mx-auto max-w-3xl px-6 py-12">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
      />
      {reviewJsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(reviewJsonLd) }}
        />
      )}

      <PostHeader post={post} locale={locale} />

      <TableOfContents headings={headings} locale={locale} />

      <div className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)] prose-code:text-[var(--color-brand-primary)]">
        <PostRenderer source={post.content} components={defaultMdxComponents} />
      </div>

      <AdInArticle
        enabled={adsEnabled}
        publisherId={adsPubId}
        slot={process.env.NEXT_PUBLIC_ADSENSE_IN_ARTICLE_SLOT}
      />

      <RelatedPosts
        allPosts={allPosts}
        currentSlug={post.frontmatter.slug}
        tags={post.frontmatter.tags}
        currentCluster={post.frontmatter.topic_cluster}
        hrefBase={hrefBase}
        locale={locale}
      />

      <Comments
        repo={brandConfig.comments.giscusRepo}
        repoId={brandConfig.comments.giscusRepoId}
        category={brandConfig.comments.giscusCategory}
        categoryId={brandConfig.comments.giscusCategoryId}
        lang={locale}
        brand="aigrit"
      />
    </article>
  );
}
