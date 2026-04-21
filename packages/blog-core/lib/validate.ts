import type { Post, PostSummary } from "../types/post";

const LINK_MARKER_RE = /\{LINK:\s*([a-z0-9-]+)\s*\|\s*anchor:\s*([^}]+)\}/g;
const INTERNAL_LINK_ANCHOR_RE =
  /<Link\s+href="(?:\/[a-z]{2})?\/blog\/([a-z0-9-]+)"[^>]*>[\s\S]*?<\/Link>/g;

export interface BrokenLink {
  source: string; // source post slug
  target: string; // missing target slug
  anchor: string;
  line: number;
}

export interface LinkStats {
  perPost: Map<string, number>;
  broken: BrokenLink[];
}

/**
 * 본문의 `{LINK: slug | anchor: ...}` 마커 + 이미 치환된 `<Link href="/blog/slug">` 를
 * 카운트하고, target slug가 allSlugs에 없으면 broken으로 기록.
 */
export function validateInternalLinks(
  posts: Post[],
  allSlugs?: string[],
): LinkStats {
  const valid = new Set(allSlugs ?? posts.map((p) => p.frontmatter.slug));
  const perPost = new Map<string, number>();
  const broken: BrokenLink[] = [];

  for (const post of posts) {
    const { slug } = post.frontmatter;
    let count = 0;

    const lines = post.content.split("\n");
    lines.forEach((line, idx) => {
      for (const match of line.matchAll(LINK_MARKER_RE)) {
        count += 1;
        const target = match[1]?.trim() ?? "";
        const anchor = match[2]?.trim() ?? "";
        if (target && !valid.has(target)) {
          broken.push({ source: slug, target, anchor, line: idx + 1 });
        }
      }
      for (const match of line.matchAll(INTERNAL_LINK_ANCHOR_RE)) {
        count += 1;
        const target = match[1]?.trim() ?? "";
        if (target && !valid.has(target)) {
          broken.push({ source: slug, target, anchor: "", line: idx + 1 });
        }
      }
    });
    perPost.set(slug, count);
  }

  return { perPost, broken };
}

export interface LinkRangeViolation {
  slug: string;
  count: number;
  min: number;
  max: number;
}

/**
 * 앱별 내부 링크 개수 규칙 검증.
 * AIGrit: 5~7개 / babipanote: 2~3개.
 */
export function checkLinkCountRange(
  stats: LinkStats,
  brand: "aigrit" | "babipanote",
): LinkRangeViolation[] {
  const [min, max] = brand === "aigrit" ? [5, 7] : [2, 3];
  const out: LinkRangeViolation[] = [];
  for (const [slug, count] of stats.perPost) {
    if (count < min || count > max) {
      out.push({ slug, count, min, max });
    }
  }
  return out;
}

export interface NaverDraftInput {
  post: Post;
  /** 제목 리프레이밍 앵글. e.g. "퇴근 후 AI" */
  angle?: string;
  /** 네이버 전용 추가 이미지 수(목표 10장+) */
  extraImages?: number;
}

/**
 * 네이버 에디션 초안 생성 — 본사 MDX를 스마트에디터 친화 텍스트로 변환.
 * 실제 리프레이밍은 LLM이 담당하고, 여기서는 구조적 변환만 수행:
 * - 마커 제거 ({IMG:}, {LINK:})
 * - H2 → 볼드 줄바꿈
 * - 2~3줄 문단 쪼개기 힌트
 */
export function buildNaverDraft(input: NaverDraftInput): string {
  const { post } = input;
  let body = post.content;
  body = body.replace(LINK_MARKER_RE, (_m, _slug, anchor) =>
    String(anchor).trim(),
  );
  body = body.replace(/\{IMG:[^}]*\}/g, "");
  body = body.replace(/^##\s+(.*)$/gm, "**$1**");
  body = body.replace(/^###\s+(.*)$/gm, "**$1**");
  return body;
}

export function summarizeLinkStats(
  stats: LinkStats,
  posts: PostSummary[],
): string {
  const lines = ["# Internal link audit", ""];
  if (stats.broken.length > 0) {
    lines.push("## ❌ Broken links");
    for (const b of stats.broken) {
      lines.push(`- ${b.source}:${b.line} → missing "${b.target}"`);
    }
    lines.push("");
  }
  lines.push("## Counts");
  for (const p of posts) {
    const n = stats.perPost.get(p.frontmatter.slug) ?? 0;
    lines.push(`- ${p.frontmatter.slug}: ${n}`);
  }
  return lines.join("\n");
}
