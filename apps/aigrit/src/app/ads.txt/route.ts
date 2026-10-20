import { buildAdsTxt } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

/**
 * /ads.txt — NEXT_PUBLIC_ADSENSE_ID 하나로 광고 스크립트·소유권 메타·ads.txt 를 함께 맞춘다.
 * 정적 public/ads.txt 를 손으로 고치던 방식을 대체 (ID 를 바꾸면 재배포만 하면 됨).
 */
export const dynamic = "force-static";

export function GET(): Response {
  const clientId = brandConfig.monetization.adsense
    ? brandConfig.monetization.adsensePublisherId
    : undefined;
  return new Response(buildAdsTxt(clientId), {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
