import path from "node:path";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  Comments,
  PostHeader,
  PostRenderer,
  RelatedPosts,
  buildArticleJsonLd,
  buildMetadata,
  defaultMdxComponents,
  getAllPostSlugs,
  getAllPostSummaries,
  getPostBySlug,
  toIsoDatetime,
} from "@unpack/blog-core";
import { brandConfig } from "../../../../brand.config";

const CONTENT_DIR = path.join(process.cwd(), "content/posts");

interface Params {
  slug: string;
}

export function generateStaticParams(): Params[] {
  return getAllPostSlugs(CONTENT_DIR, { brand: "babipanote" }).map((slug) => ({
    slug,
  }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = getPostBySlug(CONTENT_DIR, slug, { brand: "babipanote" });
  if (!post) return {};
  return buildMetadata({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
    path: `/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    type: "article",
    publishedTime: toIsoDatetime(post.frontmatter.date),
    tags: post.frontmatter.tags,
  });
}

export default async function PostPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  const post = getPostBySlug(CONTENT_DIR, slug, { brand: "babipanote" });
  if (!post) notFound();

  const allPosts = getAllPostSummaries(CONTENT_DIR, { brand: "babipanote" });

  const articleJsonLd = buildArticleJsonLd({
    title: post.frontmatter.title,
    description: post.frontmatter.description,
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
    path: `/blog/${post.frontmatter.slug}`,
    image: post.frontmatter.thumbnail,
    datePublished: toIsoDatetime(post.frontmatter.date),
    dateModified: post.frontmatter.updated
      ? toIsoDatetime(post.frontmatter.updated)
      : undefined,
    inLanguage: brandConfig.locale,
  });

  return (
    <article className="mx-auto max-w-3xl px-6 py-12">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
      />
      <PostHeader post={post} />
      <div className="prose prose-neutral max-w-none dark:prose-invert">
        <PostRenderer source={post.content} components={defaultMdxComponents} />
      </div>

      <RelatedPosts
        allPosts={allPosts}
        currentSlug={post.frontmatter.slug}
        tags={post.frontmatter.tags}
        currentCluster={post.frontmatter.topic_cluster}
      />

      <Comments
        repo={brandConfig.comments.giscusRepo}
        repoId={brandConfig.comments.giscusRepoId}
        category={brandConfig.comments.giscusCategory}
        categoryId={brandConfig.comments.giscusCategoryId}
        lang="ko"
        brand="babipanote"
      />
    </article>
  );
}
