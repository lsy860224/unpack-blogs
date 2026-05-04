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
    return [
      // 모노레포 전환 이전 레거시 URL — 현재 모두 404. GSC W18에 12 clicks 잡혀
      // 트래픽 흘리는 중. 임시 방어로 /blog 메인 301 (옵션 B).
      // 추후 신규 콘텐츠 작성 후 해당 글로 destination 업그레이드 권장.
      { source: "/rent-increase-negotiation-checklist", destination: "/blog", permanent: true },
      { source: "/rent-increase-negotiation-checklist/:path*", destination: "/blog", permanent: true },
      { source: "/mx-keys-review-why-external-keyboard", destination: "/blog", permanent: true },
      { source: "/mx-keys-review-why-external-keyboard/:path*", destination: "/blog", permanent: true },
      { source: "/category/aution-risk", destination: "/blog", permanent: true },
      { source: "/category/aution-risk/:path*", destination: "/blog", permanent: true },
    ];
  },
};

export default nextConfig;
