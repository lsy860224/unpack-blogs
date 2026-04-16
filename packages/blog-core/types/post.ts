export interface PostReviewMeta {
  productName: string;
  ratingValue: number;
  bestRating?: number;
  worstRating?: number;
  productCategory?: string;
}

export type ClusterRole = "pillar" | "cluster";

export interface PostFrontmatter {
  title: string;
  date: string;
  slug: string;
  description: string;
  tags?: string[];
  thumbnail?: string;
  featured?: boolean;
  category?: string;
  draft?: boolean;
  review?: PostReviewMeta;
  /** 마지막 수정 시각 (KST "YYYY-MM-DD HH:mm"). sitemap lastModified 소스로 사용. */
  updated?: string;
  /** Topic cluster 식별자 — RelatedPosts 및 cluster 네비게이션 대상 */
  topic_cluster?: string;
  /** Pillar(허브) 글 vs Cluster(하위) 글 구분 */
  cluster_role?: ClusterRole;
}

export interface Post {
  frontmatter: PostFrontmatter;
  content: string;
  readingTimeMinutes: number;
}

export interface PostSummary {
  frontmatter: PostFrontmatter;
  readingTimeMinutes: number;
}
