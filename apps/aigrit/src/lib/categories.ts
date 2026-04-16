export interface CategoryMeta {
  slug: string;
  description: string;
}

export const CATEGORY_META: Record<string, CategoryMeta> = {
  "공지": {
    slug: "notice",
    description: "AIGrit 운영 공지 및 업데이트",
  },
  "코딩 도구": {
    slug: "coding-tools",
    description: "Cursor, Claude Code 등 개발 보조 AI 도구 리뷰",
  },
  "LLM": {
    slug: "llm",
    description: "GPT, Claude, Gemini 등 대형 언어 모델 비교",
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
