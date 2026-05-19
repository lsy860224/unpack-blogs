import type { MetadataRoute } from "next";
import { brandConfig } from "../../brand.config";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: brandConfig.name,
    short_name: brandConfig.name,
    description: brandConfig.description,
    start_url: "/",
    display: "standalone",
    background_color: "#0F172A",
    theme_color: "#3730A3",
    icons: [
      {
        src: "/icon.svg",
        sizes: "any",
        type: "image/svg+xml",
      },
      {
        src: "/apple-icon.png",
        sizes: "180x180",
        type: "image/png",
      },
    ],
  };
}
