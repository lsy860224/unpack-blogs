import type { BrandConfig } from "@unpack/blog-core";

function resolveSiteUrl(fallback: string): string {
  const envUrl = process.env.NEXT_PUBLIC_SITE_URL;
  const isLocalhost = !!envUrl && /localhost|127\.0\.0\.1/.test(envUrl);
  const isProduction = process.env.NODE_ENV === "production";
  if (isProduction && isLocalhost) return fallback;
  return envUrl || fallback;
}

export const brandConfig: BrandConfig = {
  name: "babipanote",
  tagline: "오늘도 만들고, 내일 더 나은 것을 만든다",
  description:
    "1인 빌더의 실패와 배움을 가감 없이 기록하는 개인 저널 — 매출·숫자·감정까지 날것으로.",
  url: resolveSiteUrl("https://babipanote.com"),
  locale: "ko-KR",
  nav: [
    { label: "Home", href: "/" },
    { label: "Blog", href: "/blog" },
    { label: "Projects", href: "/projects" },
    { label: "About", href: "/about" },
  ],
  social: {
    x: "@babipanote",
    instagram: "@babipanote",
    threads: "@babipanote",
  },
  theme: {
    colors: {
      primary: "#6B2E4E",
      secondary: "#C89F7C",
      secondaryHover: "#A87F5C",
      accentGreen: "#6B8A63",
      accentRed: "#9C4A3E",
      background: "#FAF7F2",
      foreground: "#2B2420",
    },
    dark: {
      primary: "#C89BAE",
      secondary: "#E0BEA0",
      accentGreen: "#A8BFA0",
      accentRed: "#C88072",
      background: "#1A1614",
      foreground: "#E8E0D6",
    },
    fonts: {
      sans: "var(--font-pretendard), var(--font-inter), system-ui, sans-serif",
      serif: "var(--font-gowun-batang), var(--font-lora), Georgia, serif",
      mono: "var(--font-jetbrains), ui-monospace, monospace",
    },
  },
  monetization: {
    adsense: false,
    affiliateLinks: false,
  },
  layout: {
    style: "timeline",
    showSidebar: false,
    postsPerPage: 20,
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
