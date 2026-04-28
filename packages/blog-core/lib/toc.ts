import GithubSlugger from "github-slugger";
import type { TocHeading } from "../components/blog/TableOfContents";

const HEADING_RE = /^(#{1,6})\s+(.+?)\s*$/gm;

/**
 * MDX/Markdown 소스에서 heading을 추출해 TocHeading[] 반환.
 * `rehype-slug`과 동일한 `github-slugger`를 사용해 id 일치를 보장한다.
 * (이전엔 자체 slugify로 인해 `&`/`→` 등 다중 특수문자가 들어간 heading의
 * id가 어긋나 TOC 앵커가 동작하지 않는 버그가 있었음.)
 */
export function extractHeadings(source: string): TocHeading[] {
  const headings: TocHeading[] = [];
  const slugger = new GithubSlugger();

  for (const match of source.matchAll(HEADING_RE)) {
    const depth = match[1].length;
    const text = match[2].replace(/`([^`]+)`/g, "$1").trim();
    const id = slugger.slug(text);
    headings.push({ id, text, depth });
  }

  return headings;
}
