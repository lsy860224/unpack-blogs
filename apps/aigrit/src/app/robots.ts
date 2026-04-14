import type { MetadataRoute } from "next";
import { brandConfig } from "../../brand.config";

export default function robots(): MetadataRoute.Robots {
  const base = brandConfig.url.replace(/\/+$/, "");
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/api/", "/_next/"],
      },
    ],
    sitemap: `${base}/sitemap.xml`,
    host: base,
  };
}
