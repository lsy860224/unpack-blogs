import type { MetadataRoute } from "next";
import { brandConfig } from "../../brand.config";

export default function robots(): MetadataRoute.Robots {
  const configUrl = brandConfig.url;
  const base = (configUrl.includes("localhost") ? "https://aigrit.dev" : configUrl).replace(/\/+$/, "");
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
