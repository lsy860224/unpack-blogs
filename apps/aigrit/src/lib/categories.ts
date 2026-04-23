import path from "node:path";
import { getAllPostSummaries, SUPPORTED_LOCALES } from "@unpack/blog-core";

export interface CategoryMeta {
  slug: string;
  description: string;
}

/**
 * Curated metadata for known categories.
 *
 * 여기에 없는 카테고리를 글에서 사용하면 `getEffectiveCategories()` 가
 * 자동으로 kebab-case slug + 제네릭 description 을 생성한다. 단,
 * 빌드 로그에 경고가 뜨므로 SEO·노출을 위해 여기에 명시 등록 권장.
 */
export const CATEGORY_META: Record<string, CategoryMeta> = {
  공지: {
    slug: "notice",
    description: "AIGrit 운영 공지 및 업데이트",
  },
  "AI 도구 비교": {
    slug: "ai-tools",
    description: "여러 AI 도구를 직접 써보고 숫자로 비교",
  },
  LLM: {
    slug: "llm",
    description: "GPT, Claude, Gemini 등 대형 언어 모델 비교",
  },
  "코딩 도구": {
    slug: "coding-tools",
    description: "Cursor, Claude Code 등 개발 보조 AI 도구 리뷰",
  },
  "AI 코딩": {
    slug: "ai-coding",
    description: "AI 페어 프로그래밍·MCP·에이전트 코딩 실전",
  },
  "AI 검색": {
    slug: "ai-search",
    description: "Perplexity 등 AI 기반 검색·리서치 도구",
  },
  자동화: {
    slug: "automation",
    description: "Apple 단축어·Make·Zapier로 만드는 반복 업무 자동화",
  },
  생산성: {
    slug: "productivity",
    description: "Notion AI·생산성 앱으로 업무 효율 올리기",
  },
  지식관리: {
    slug: "knowledge",
    description: "Obsidian·Craft·Notion 등 PKM 도구 비교",
  },
};

/** Derive a URL-safe kebab slug for categories not registered in CATEGORY_META. */
function fallbackSlug(name: string): string {
  const ascii = name
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, " ")
    .trim()
    .replace(/\s+/g, "-");
  return ascii.length >= 2 ? ascii : encodeURIComponent(name);
}

function fallbackMeta(name: string): CategoryMeta {
  return {
    slug: fallbackSlug(name),
    description: `${name} 카테고리의 글 모음`,
  };
}

const warnedCategories = new Set<string>();

function warnUnregistered(names: Iterable<string>): void {
  const fresh = [...names].filter((n) => !warnedCategories.has(n));
  if (fresh.length === 0) return;
  for (const n of fresh) warnedCategories.add(n);
  // Warn on both dev and build — actionable before deploy.
  console.warn(
    `[aigrit/categories] Unregistered categor${fresh.length === 1 ? "y" : "ies"} auto-derived: ${fresh
      .map((n) => `"${n}"`)
      .join(", ")}. Add to CATEGORY_META with curated slug + description for better SEO.`,
  );
}

/** Cached union of CATEGORY_META + any categories actually used across all locales. */
let _effectiveCache: Map<string, CategoryMeta> | null = null;

function readAllPosts(): Array<{ frontmatter: { category?: string } }> {
  const all: Array<{ frontmatter: { category?: string } }> = [];
  for (const locale of SUPPORTED_LOCALES) {
    try {
      all.push(
        ...getAllPostSummaries(
          path.join(process.cwd(), "content/posts", locale),
          { brand: "aigrit" },
        ),
      );
    } catch {
      // locale dir may not exist yet — skip silently
    }
  }
  return all;
}

export function getEffectiveCategories(): Map<string, CategoryMeta> {
  if (_effectiveCache) return _effectiveCache;
  const posts = readAllPosts();
  const result = new Map<string, CategoryMeta>();
  for (const [name, meta] of Object.entries(CATEGORY_META)) {
    result.set(name, meta);
  }
  const unregistered: string[] = [];
  for (const p of posts) {
    const cat = p.frontmatter.category;
    if (!cat || result.has(cat)) continue;
    unregistered.push(cat);
    result.set(cat, fallbackMeta(cat));
  }
  warnUnregistered(unregistered);
  _effectiveCache = result;
  return result;
}

export function getCategorySlug(name: string): string {
  const meta = getEffectiveCategories().get(name);
  return meta ? meta.slug : fallbackSlug(name);
}

export function getCategoryBySlug(
  slug: string,
): { name: string; description: string } | null {
  for (const [name, meta] of getEffectiveCategories()) {
    if (meta.slug === slug) return { name, description: meta.description };
  }
  return null;
}

/** All registered + auto-derived slugs — used by generateStaticParams. */
export function getAllCategorySlugs(): string[] {
  return Array.from(getEffectiveCategories().values()).map((m) => m.slug);
}

export interface CategoryNavEntry {
  slug: string | null;
  name: string;
  count: number;
  href: string;
}

export function getCategoryNav(
  locale: string,
  allLabel: string,
): CategoryNavEntry[] {
  const CONTENT_DIR = path.join(process.cwd(), "content/posts", locale);
  const posts = getAllPostSummaries(CONTENT_DIR, { brand: "aigrit" });

  const counts = new Map<string, number>();
  for (const p of posts) {
    const cat = p.frontmatter.category;
    if (!cat) continue;
    counts.set(cat, (counts.get(cat) ?? 0) + 1);
  }

  const all: CategoryNavEntry = {
    slug: null,
    name: allLabel,
    count: posts.length,
    href: `/${locale}/blog`,
  };

  const categoryEntries: CategoryNavEntry[] = Array.from(
    getEffectiveCategories().entries(),
  )
    .map(([name, meta]) => ({
      slug: meta.slug,
      name,
      count: counts.get(name) ?? 0,
      href: `/${locale}/category/${meta.slug}`,
    }))
    .filter((entry) => entry.count > 0)
    .sort((a, b) => b.count - a.count);

  return [all, ...categoryEntries];
}
