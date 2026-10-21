import path from "node:path";
import { getAllPostSummaries, SUPPORTED_LOCALES } from "@unpack/blog-core";

export interface CategoryLabel {
  /** 화면에 표시하는 대표 이름 */
  name: string;
  description: string;
  /**
   * frontmatter `category` 에서 같은 카테고리로 취급할 다른 이름.
   * 카테고리 통합 이력(예: "LLM" → AI 도구 비교)을 여기에 남겨
   * 기존 글 frontmatter 를 고치지 않고도 같은 slug 로 모인다.
   */
  aliases?: string[];
}

export interface CategoryDef {
  slug: string;
  ko: CategoryLabel;
  /** 없으면 영어 페이지에서도 ko 라벨을 쓴다 */
  en?: CategoryLabel;
}

/**
 * 카테고리 단일 소스. slug 하나에 locale 별 라벨 + 별칭을 묶는다.
 *
 * - 같은 slug 를 KO/EN 이 공유해야 헤더 언어 토글이 /ko/category/x ↔ /en/category/x 로
 *   정확히 이동한다.
 * - 여기에 없는 이름을 글에서 쓰면 자동 slug 가 만들어지고 빌드 로그에 경고가 뜬다.
 *   (자동 slug 는 한글이 많으면 충돌하기 쉬우니 반드시 여기에 등록할 것)
 * - 통합 이력: 2026-05-19 LLM·AI 검색·코딩 도구·생산성 → AI 도구 비교·AI 코딩·자동화,
 *   2026-10-20 "AI 도구" → AI 도구 비교. 옛 URL 은 next.config.ts redirect 로 보존.
 */
export const CATEGORY_DEFS: CategoryDef[] = [
  {
    slug: "notice",
    ko: { name: "공지", description: "AIGrit 운영 공지 및 업데이트" },
    en: {
      name: "Announcement",
      description: "AIGrit announcements and updates",
    },
  },
  {
    slug: "ai-tools",
    ko: {
      name: "AI 도구 비교",
      description:
        "Claude·GPT·Gemini·Perplexity 등 AI 도구를 직접 써보고 숫자로 비교",
      aliases: ["AI 도구", "LLM", "AI 검색"],
    },
    en: {
      name: "AI Tools",
      description:
        "Hands-on comparisons of Claude, GPT, Gemini, Perplexity and other AI tools",
      aliases: ["LLM", "AI Search"],
    },
  },
  {
    slug: "ai-coding",
    ko: {
      name: "AI 코딩",
      description:
        "Claude Code·Cursor·MCP — AI 페어 프로그래밍과 1인 빌더 워크플로우",
      aliases: ["코딩 도구"],
    },
    en: {
      name: "AI Coding",
      description:
        "Claude Code, Cursor, MCP — AI pair programming and solo-builder workflows",
      aliases: ["Coding Tools"],
    },
  },
  {
    slug: "automation",
    ko: {
      name: "자동화",
      description: "Apple 단축어·Make·Notion AI로 만드는 반복 업무 자동화",
      aliases: ["생산성"],
    },
    en: {
      name: "Automation",
      description: "Automating repetitive work with Shortcuts, Make, and Notion AI",
      aliases: ["Productivity"],
    },
  },
  {
    slug: "knowledge",
    ko: { name: "지식관리", description: "Obsidian·Craft·Notion 등 PKM 도구 비교" },
    en: {
      name: "Knowledge Management",
      description: "Comparing PKM tools — Obsidian, Craft, Notion",
    },
  },
  {
    slug: "monetization",
    ko: {
      name: "수익화",
      description: "AI 부업·블로그 수익화·AdSense 등 수익 경로",
    },
    en: {
      name: "Monetization",
      description: "AI side income, blog monetization, and AdSense",
    },
  },
  // 예약 발행 글(2026-12~)이 쓰는 카테고리. 미등록 시 자동 slug 가 전부 "ai" 로
  // 충돌해 카테고리 페이지가 하나만 열리던 문제를 막기 위해 미리 등록한다.
  {
    slug: "ai-video",
    ko: { name: "AI 영상", description: "AI 영상 생성·편집·자막 도구 비교" },
  },
  {
    slug: "ai-design",
    ko: { name: "AI 디자인", description: "AI 이미지·디자인·썸네일 도구 비교" },
  },
  {
    slug: "nocode",
    ko: { name: "노코드", description: "노코드·바이브 코딩으로 서비스 만들기" },
  },
  {
    slug: "ai-agents",
    ko: { name: "AI 에이전트", description: "AI 에이전트 설계·자동화 워크플로우" },
  },
  {
    slug: "ai-marketing",
    ko: { name: "AI 마케팅", description: "AI로 하는 콘텐츠·마케팅 자동화" },
  },
  {
    slug: "ai-music",
    ko: { name: "AI 음악", description: "AI 음악 생성 도구 비교" },
  },
  {
    slug: "ai-voice",
    ko: { name: "AI 음성", description: "AI 음성 합성·보이스 클로닝 도구" },
  },
];

type CategoryLocale = "ko" | "en";

function asCategoryLocale(locale: string): CategoryLocale {
  return locale === "en" ? "en" : "ko";
}

function labelFor(def: CategoryDef, locale: string): CategoryLabel {
  return (asCategoryLocale(locale) === "en" ? def.en : undefined) ?? def.ko;
}

/** Derive a URL-safe kebab slug for categories not registered in CATEGORY_DEFS. */
function fallbackSlug(name: string): string {
  const ascii = name
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, " ")
    .trim()
    .replace(/\s+/g, "-");
  return ascii.length >= 2 ? ascii : encodeURIComponent(name);
}

interface CategoryIndex {
  defs: Map<string, CategoryDef>;
  /** frontmatter 이름(대표명·별칭, KO·EN 공통) → slug */
  nameToSlug: Map<string, string>;
}

let _indexCache: CategoryIndex | null = null;
const warnedCategories = new Set<string>();

function readAllCategoryNames(): Array<{ locale: string; name: string }> {
  const out: Array<{ locale: string; name: string }> = [];
  for (const locale of SUPPORTED_LOCALES) {
    try {
      for (const p of getAllPostSummaries(
        path.join(process.cwd(), "content/posts", locale),
        { brand: "aigrit", includeFuture: true },
      )) {
        if (p.frontmatter.category) {
          out.push({ locale, name: p.frontmatter.category });
        }
      }
    } catch {
      // locale dir may not exist yet — skip silently
    }
  }
  return out;
}

function getIndex(): CategoryIndex {
  if (_indexCache) return _indexCache;

  const defs = new Map<string, CategoryDef>();
  const nameToSlug = new Map<string, string>();
  for (const def of CATEGORY_DEFS) {
    defs.set(def.slug, def);
    for (const label of [def.ko, def.en]) {
      if (!label) continue;
      for (const n of [label.name, ...(label.aliases ?? [])]) {
        if (!nameToSlug.has(n)) nameToSlug.set(n, def.slug);
      }
    }
  }

  // 미등록 카테고리: 자동 slug 생성 (충돌 시 이름 전체를 인코딩해 분리)
  const unregistered: string[] = [];
  for (const { locale, name } of readAllCategoryNames()) {
    if (nameToSlug.has(name)) continue;
    let slug = fallbackSlug(name);
    if (defs.has(slug)) slug = encodeURIComponent(name.toLowerCase());
    const label: CategoryLabel = {
      name,
      description:
        locale === "en"
          ? `Posts in the ${name} category`
          : `${name} 카테고리의 글 모음`,
    };
    defs.set(slug, { slug, ko: label, en: locale === "en" ? label : undefined });
    nameToSlug.set(name, slug);
    unregistered.push(name);
  }

  const fresh = unregistered.filter((n) => !warnedCategories.has(n));
  if (fresh.length > 0) {
    for (const n of fresh) warnedCategories.add(n);
    console.warn(
      `[aigrit/categories] Unregistered categor${fresh.length === 1 ? "y" : "ies"} auto-derived: ${fresh
        .map((n) => `"${n}"`)
        .join(", ")}. Add to CATEGORY_DEFS with a curated slug + description.`,
    );
  }

  _indexCache = { defs, nameToSlug };
  return _indexCache;
}

export interface ResolvedCategory {
  slug: string;
  name: string;
  description: string;
}

/** frontmatter 의 category 값(대표명 또는 별칭)을 locale 에 맞는 slug·표시명으로 해석. */
export function resolveCategory(
  rawName: string,
  locale: string,
): ResolvedCategory {
  const { defs, nameToSlug } = getIndex();
  const slug = nameToSlug.get(rawName) ?? fallbackSlug(rawName);
  const def = defs.get(slug);
  if (!def) return { slug, name: rawName, description: "" };
  const label = labelFor(def, locale);
  return { slug, name: label.name, description: label.description };
}

export function getCategorySlug(name: string): string {
  return resolveCategory(name, "ko").slug;
}

export function getCategoryBySlug(
  slug: string,
  locale: string = "ko",
): { name: string; description: string } | null {
  const def = getIndex().defs.get(slug);
  if (!def) return null;
  const label = labelFor(def, locale);
  return { name: label.name, description: label.description };
}

/** All registered + auto-derived slugs — used by generateStaticParams. */
export function getAllCategorySlugs(): string[] {
  return Array.from(getIndex().defs.keys());
}

type Summary = ReturnType<typeof getAllPostSummaries>[number];

function publishedPosts(locale: string): Summary[] {
  return getAllPostSummaries(
    path.join(process.cwd(), "content/posts", locale),
    { brand: "aigrit" },
  );
}

/** 해당 locale 에서 이 slug 카테고리에 속한 (발행된) 글 */
export function getPostsInCategory(locale: string, slug: string): Summary[] {
  return publishedPosts(locale).filter(
    (p) =>
      p.frontmatter.category !== undefined &&
      resolveCategory(p.frontmatter.category, locale).slug === slug,
  );
}

/** 발행된 글이 1편 이상 있는 카테고리 slug 집합 — sitemap·언어 토글·hreflang 용 */
export function getCategorySlugsWithPosts(locale: string): Set<string> {
  const set = new Set<string>();
  for (const p of publishedPosts(locale)) {
    if (p.frontmatter.category) {
      set.add(resolveCategory(p.frontmatter.category, locale).slug);
    }
  }
  return set;
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
  const posts = publishedPosts(locale);

  const counts = new Map<string, number>();
  for (const p of posts) {
    const cat = p.frontmatter.category;
    if (!cat) continue;
    const { slug } = resolveCategory(cat, locale);
    counts.set(slug, (counts.get(slug) ?? 0) + 1);
  }

  const all: CategoryNavEntry = {
    slug: null,
    name: allLabel,
    count: posts.length,
    href: `/${locale}/blog`,
  };

  const categoryEntries: CategoryNavEntry[] = Array.from(counts.entries())
    .map(([slug, count]) => ({
      slug,
      name: getCategoryBySlug(slug, locale)?.name ?? slug,
      count,
      href: `/${locale}/category/${slug}`,
    }))
    .sort((a, b) => b.count - a.count);

  return [all, ...categoryEntries];
}
