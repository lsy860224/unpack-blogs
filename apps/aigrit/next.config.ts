import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: ["@unpack/blog-core"],
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "avatars.githubusercontent.com" },
      { protocol: "https", hostname: "cdn.jsdelivr.net" },
    ],
  },
};

export default nextConfig;
