import type { BrandConfig, BrandLocaleStrings } from "@unpack/blog-core";

export const brandConfig: BrandConfig = {
  name: "AIGrit",
  tagline: "AI의 알맹이만 남긴다",
  description:
    "AI 도구를 직접 며칠간 써보고 속도·비용·정확도를 숫자로 비교하는 한국어 리뷰 — 팔지 않고, 씁니다.",
  url: process.env.NEXT_PUBLIC_SITE_URL || "https://aigrit.dev",
  locale: "ko-KR",
  nav: [
    { label: "Home", href: "/" },
    { label: "Blog", href: "/blog" },
    { label: "About", href: "/about" },
    { label: "Disclaimer", href: "/disclaimer" },
  ],
  supportedLocales: ["ko", "en"],
  locales: {
    ko: {
      tagline: "AI의 알맹이만 남긴다",
      description:
        "AI 도구를 직접 며칠간 써보고 속도·비용·정확도를 숫자로 비교하는 한국어 리뷰 — 팔지 않고, 씁니다.",
      nav: [
        { label: "홈", href: "/" },
        { label: "블로그", href: "/blog" },
        { label: "소개", href: "/about" },
        { label: "제휴 고지", href: "/disclaimer" },
      ],
    },
    en: {
      tagline: "AI essentials, distilled.",
      description:
        "Hands-on AI tool reviews — we test each tool for days and compare speed, cost, and accuracy with numbers. We write, we don't sell.",
      nav: [
        { label: "Home", href: "/" },
        { label: "Blog", href: "/blog" },
        { label: "About", href: "/about" },
        { label: "Disclaimer", href: "/disclaimer" },
      ],
    },
  },
  social: {
    x: "@aigrit_dev",
    instagram: "@aigrit.dev",
    github: "lsy860224/aigrit",
  },
  theme: {
    colors: {
      primary: "#3730A3",
      secondary: "#06B6D4",
      secondaryHover: "#0891B2",
      accentGreen: "#10B981",
      accentRed: "#EF4444",
      background: "#F8FAFC",
      foreground: "#0F172A",
      surface: "#FFFFFF",
    },
    dark: {
      primary: "#818CF8",
      secondary: "#22D3EE",
      accentGreen: "#34D399",
      accentRed: "#F87171",
      background: "#0F172A",
      foreground: "#E2E8F0",
      surface: "#1E293B",
    },
    fonts: {
      sans: "var(--font-pretendard), var(--font-inter), system-ui, sans-serif",
      mono: "var(--font-jetbrains), ui-monospace, monospace",
    },
  },
  monetization: {
    adsense: true,
    affiliateLinks: true,
    adsensePublisherId: process.env.NEXT_PUBLIC_ADSENSE_ID,
  },
  layout: {
    style: "category",
    showSidebar: true,
    postsPerPage: 12,
  },
  analytics: {
    gaId: process.env.NEXT_PUBLIC_GA_ID,
  },
  comments: {
    giscusRepo: process.env.NEXT_PUBLIC_GISCUS_REPO,
    giscusRepoId: process.env.NEXT_PUBLIC_GISCUS_REPO_ID,
    giscusCategory: process.env.NEXT_PUBLIC_GISCUS_CATEGORY,
    giscusCategoryId: process.env.NEXT_PUBLIC_GISCUS_CATEGORY_ID,
  },
};

export interface LocalizedBrand {
  name: string;
  tagline: string;
  description: string;
  url: string;
  nav: BrandLocaleStrings["nav"];
}

export function getLocalizedBrand(locale: string): LocalizedBrand {
  const entry = brandConfig.locales?.[locale];
  return {
    name: brandConfig.name,
    tagline: entry?.tagline ?? brandConfig.tagline,
    description: entry?.description ?? brandConfig.description,
    url: brandConfig.url,
    nav: entry?.nav ?? brandConfig.nav,
  };
}
