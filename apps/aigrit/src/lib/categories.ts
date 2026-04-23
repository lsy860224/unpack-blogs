import path from "node:path";
import { getAllPostSummaries } from "@unpack/blog-core";

export interface CategoryMeta {
  slug: string;
  description: string;
}

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

export function getCategorySlug(name: string): string {
  return CATEGORY_META[name]?.slug ?? encodeURIComponent(name);
}

export function getCategoryBySlug(
  slug: string,
): { name: string; description: string } | null {
  const hit = Object.entries(CATEGORY_META).find(([, v]) => v.slug === slug);
  if (!hit) return null;
  return { name: hit[0], description: hit[1].description };
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

  const categoryEntries: CategoryNavEntry[] = Object.entries(CATEGORY_META)
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
