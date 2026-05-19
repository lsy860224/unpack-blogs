import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: ["@unpack/blog-core"],
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "avatars.githubusercontent.com" },
      { protocol: "https", hostname: "cdn.jsdelivr.net" },
    ],
  },
  async redirects() {
    // 카테고리 통합 (2026-05-19) — 글 1편짜리 4개 카테고리 → 3개로 흡수.
    // 기존 URL 신뢰성 유지 위해 영구 redirect 처리.
    return [
      { source: "/:locale/category/llm", destination: "/:locale/category/ai-tools", permanent: true },
      { source: "/:locale/category/ai-search", destination: "/:locale/category/ai-tools", permanent: true },
      { source: "/:locale/category/coding-tools", destination: "/:locale/category/ai-coding", permanent: true },
      { source: "/:locale/category/productivity", destination: "/:locale/category/automation", permanent: true },
    ];
  },
};

export default nextConfig;
