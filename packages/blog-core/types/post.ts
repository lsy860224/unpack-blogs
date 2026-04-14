export interface PostReviewMeta {
  productName: string;
  ratingValue: number;
  bestRating?: number;
  worstRating?: number;
  productCategory?: string;
}

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
