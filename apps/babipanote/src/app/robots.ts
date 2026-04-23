import type { MetadataRoute } from "next";
import { brandConfig } from "../../brand.config";

export default function robots(): MetadataRoute.Robots {
  const configUrl = brandConfig.url;
  const base = (configUrl.includes("localhost") ? "https://babipanote.com" : configUrl).replace(/\/+$/, "");
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/api/"],
      },
    ],
    sitemap: `${base}/sitemap.xml`,
    host: base,
  };
}
