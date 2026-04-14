"use client";

import { useEffect } from "react";

declare global {
  interface Window {
    adsbygoogle?: unknown[];
  }
}

export interface AdBannerProps {
  /** 광고 활성화 여부. brandConfig.monetization.adsense를 그대로 전달 */
  enabled?: boolean;
  /** AdSense Publisher ID (ca-pub-XXXXXXXX) */
  publisherId?: string;
  /** AdSense Slot ID */
  slot?: string;
  /** layout: auto 등 */
  format?: string;
  responsive?: boolean;
  className?: string;
}

export function AdBanner({
  enabled = true,
  publisherId,
  slot,
  format = "auto",
  responsive = true,
  className,
}: AdBannerProps) {
  useEffect(() => {
    if (!enabled || !publisherId || !slot) return;
    try {
      (window.adsbygoogle = window.adsbygoogle ?? []).push({});
    } catch {
      /* noop — AdSense script not yet loaded */
    }
  }, [enabled, publisherId, slot]);

  if (!enabled || !publisherId || !slot) return null;

  return (
    <div className={["my-6 w-full text-center", className ?? ""].join(" ")}>
      <ins
        className="adsbygoogle"
        style={{ display: "block" }}
        data-ad-client={publisherId}
        data-ad-slot={slot}
        data-ad-format={format}
        data-full-width-responsive={responsive ? "true" : "false"}
      />
    </div>
  );
}
