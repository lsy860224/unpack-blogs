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
} from "@unpack/blog-core";
import { brandConfig } from "../../../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

interface Params {
  slug: string;
}

export function generateStaticParams(): Params[] {
  return getAllPostSlugs(CONTENT_DIR).map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = getPostBySlug(CONTENT_DIR, slug);
  if (!post) return {};
  return buildMetadata({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
    path: `/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    type: "article",
    publishedTime: post.frontmatter.date,
    tags: post.frontmatter.tags,
  });
}

export default async function PostPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  const post = getPostBySlug(CONTENT_DIR, slug);
  if (!post) notFound();

  const allPosts = getAllPostSummaries(CONTENT_DIR);
  const headings = extractHeadings(post.content);

  const articleJsonLd = buildArticleJsonLd({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
    path: `/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    datePublished: post.frontmatter.date,
  });

  const reviewJsonLd = post.frontmatter.review
    ? buildReviewJsonLd({
        productName: post.frontmatter.review.productName,
        productCategory: post.frontmatter.review.productCategory,
        ratingValue: post.frontmatter.review.ratingValue,
        bestRating: post.frontmatter.review.bestRating,
        worstRating: post.frontmatter.review.worstRating,
        authorName: brandConfig.name,
        datePublished: post.frontmatter.date,
        url: `${brandConfig.url}/blog/${post.frontmatter.slug}`,
      })
    : null;

  const adsEnabled = brandConfig.monetization.adsense;
  const adsPubId = brandConfig.monetization.adsensePublisherId;

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

      <PostHeader post={post} />

      <TableOfContents headings={headings} />

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
      />

      <Comments
        repo={brandConfig.comments.giscusRepo}
        repoId={brandConfig.comments.giscusRepoId}
        category={brandConfig.comments.giscusCategory}
        categoryId={brandConfig.comments.giscusCategoryId}
      />
    </article>
  );
}
