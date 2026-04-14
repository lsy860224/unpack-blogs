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
