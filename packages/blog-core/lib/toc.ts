import GithubSlugger from "github-slugger";
import type { TocHeading } from "../components/blog/TableOfContents";

const HEADING_RE = /^(#{1,6})\s+(.+?)\s*$/gm;

/**
 * Fenced code block(```...```)과 indented code block(4-space) 안의 라인을 제거.
 * extractHeadings가 코드 예제 안의 `## 1. 역할 정의` 같은 텍스트를
 * 실제 heading으로 오인하던 버그 방어.
 */
function stripCodeBlocks(source: string): string {
  // Fenced code blocks — ``` 또는 ~~~ (3개 이상 같은 문자, 같은 길이로 닫힘)
  let out = source.replace(
    /^([`~]{3,})[^\n]*\n[\s\S]*?^\1[ \t]*$/gm,
    "",
  );
  // Inline code (한 줄에 ` ` 한 쌍)도 제거 — heading 판정에는 영향 없지만 일관성 차원
  out = out.replace(/`[^`\n]*`/g, "");
  return out;
}

/**
 * MDX/Markdown 소스에서 heading을 추출해 TocHeading[] 반환.
 * `rehype-slug`과 동일한 `github-slugger`를 사용해 id 일치를 보장한다.
 *
 * 주요 방어:
 * - fenced code block 내부 라인 제외 (코드 예제의 `## ...` 오탐 방지)
 * - github-slugger 직접 사용 (자체 slugify로 인한 ID 어긋남 방지)
 */
export function extractHeadings(source: string): TocHeading[] {
  const headings: TocHeading[] = [];
  const slugger = new GithubSlugger();
  const cleaned = stripCodeBlocks(source);

  for (const match of cleaned.matchAll(HEADING_RE)) {
    const depth = match[1].length;
    const text = match[2].trim();
    const id = slugger.slug(text);
    headings.push({ id, text, depth });
  }

  return headings;
}
