export interface PostReviewMeta {
  productName: string;
  ratingValue: number;
  bestRating?: number;
  worstRating?: number;
  productCategory?: string;
}

export type ClusterRole = "pillar" | "cluster";

export type NaverEditionStatus = "candidate" | "drafted" | "published";

export interface PostNaverEdition {
  status: NaverEditionStatus;
  /** 네이버 에디션 리프레이밍 앵글 (ex. "퇴근 후 1시간 자동화") */
  angle?: string;
  /** 네이버용으로 추가 확보한 이미지 수 (목표 10장+) */
  extraImages?: number;
  /** 네이버 발행 시각 (KST "YYYY-MM-DD HH:mm") */
  publishedAt?: string;
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
  /**
   * 마지막 수정 시각 (KST "YYYY-MM-DD HH:mm"). sitemap lastModified 소스.
   * frontmatter에 값이 없으면 parseMdxFile이 date로 자동 채움.
   */
  updated?: string;
  /** Topic cluster 식별자 — RelatedPosts 및 cluster 네비게이션 대상 */
  topic_cluster?: string;
  /** Pillar(허브) 글 vs Cluster(하위) 글 구분 */
  cluster_role?: ClusterRole;
  /** 네이버 에디션 파이프라인 상태 */
  naver_edition?: PostNaverEdition;
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
