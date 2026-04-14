"use client";

import { useEffect } from "react";

declare global {
  interface Window {
    adsbygoogle?: unknown[];
  }
}

export interface AdInArticleProps {
  enabled?: boolean;
  publisherId?: string;
  slot?: string;
  className?: string;
}

/**
 * 글 본문 사이에 삽입하는 in-article 광고.
 * AdSense "글 내 광고" 슬롯을 사용한다.
 */
export function AdInArticle({
  enabled = true,
  publisherId,
  slot,
  className,
}: AdInArticleProps) {
  useEffect(() => {
    if (!enabled || !publisherId || !slot) return;
    try {
      (window.adsbygoogle = window.adsbygoogle ?? []).push({});
    } catch {
      /* noop */
    }
  }, [enabled, publisherId, slot]);

  if (!enabled || !publisherId || !slot) return null;

  return (
    <div
      className={[
        "my-8 text-center text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)] not-prose",
        className ?? "",
      ].join(" ")}
    >
      <p className="mb-1 uppercase tracking-widest" style={{ fontFamily: "var(--font-mono)" }}>
        Sponsored
      </p>
      <ins
        className="adsbygoogle"
        style={{ display: "block", textAlign: "center" }}
        data-ad-layout="in-article"
        data-ad-format="fluid"
        data-ad-client={publisherId}
        data-ad-slot={slot}
      />
    </div>
  );
}
