import path from "node:path";
import { getAllPostSlugs, SUPPORTED_LOCALES } from "@unpack/blog-core";
import { getCategorySlugsWithPosts } from "./categories";

/** locale 별로 실제 존재하는 글·카테고리 slug — 헤더 언어 토글이 404 로 보내지 않게 한다. */
export interface LocaleContentIndex {
  posts: string[];
  categories: string[];
}

export type LocaleIndexMap = Record<string, LocaleContentIndex>;

/**
 * 레이아웃이 요청마다 렌더되므로 MDX 전체 파싱을 매번 하지 않도록 짧게 캐시한다.
 * 예약 발행 글이 열리는 시점과 최대 TTL 만큼 어긋날 수 있지만, 그동안은
 * 토글이 대상 언어 블로그 목록으로 안전하게 대체될 뿐이다. (페이지 revalidate 600s 와 맞춤)
 */
const TTL_MS = 10 * 60 * 1000;
let cache: { at: number; value: LocaleIndexMap } | null = null;

export function buildLocaleIndex(): LocaleIndexMap {
  const now = Date.now();
  if (cache && now - cache.at < TTL_MS) return cache.value;

  const index: LocaleIndexMap = {};
  for (const locale of SUPPORTED_LOCALES) {
    index[locale] = {
      posts: getAllPostSlugs(path.join(process.cwd(), "content/posts", locale), {
        brand: "aigrit",
      }),
      categories: Array.from(getCategorySlugsWithPosts(locale)),
    };
  }
  cache = { at: now, value: index };
  return index;
}
