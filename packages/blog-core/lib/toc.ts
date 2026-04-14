import type { TocHeading } from "../components/blog/TableOfContents";

const HEADING_RE = /^(#{1,6})\s+(.+?)\s*$/gm;

function slugify(text: string): string {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

/**
 * MDX/Markdown 소스에서 heading을 추출해 TocHeading[] 반환.
 * rehype-slug 와 동일한 규칙으로 id를 생성한다 (github-slugger 대체).
 */
export function extractHeadings(source: string): TocHeading[] {
  const headings: TocHeading[] = [];
  const seen = new Map<string, number>();

  for (const match of source.matchAll(HEADING_RE)) {
    const depth = match[1].length;
    const text = match[2].replace(/`([^`]+)`/g, "$1").trim();
    let id = slugify(text);
    const count = seen.get(id) ?? 0;
    if (count > 0) id = `${id}-${count}`;
    seen.set(id, count + 1);
    headings.push({ id, text, depth });
  }

  return headings;
}
