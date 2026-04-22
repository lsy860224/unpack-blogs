import type { ReactNode } from "react";

export interface AffiliateLinkProps {
  href: string;
  children: ReactNode;
  /** 제휴 고지 수준: "subtle"(작은 배지) | "full"(문단 주석) */
  disclosure?: "subtle" | "full";
}

export function AffiliateLink({
  href,
  children,
  disclosure = "subtle",
}: AffiliateLinkProps) {
  return (
    <span className="inline-flex flex-wrap items-baseline gap-1.5">
      <a
        href={href}
        rel="nofollow sponsored noopener noreferrer"
        target="_blank"
        className="text-[var(--color-brand-primary)] underline decoration-[var(--color-brand-secondary)] decoration-2 underline-offset-4 hover:decoration-[var(--color-brand-primary)]"
      >
        {children}
      </a>
      {disclosure === "subtle" ? (
        <span
          className="text-[10px] font-bold uppercase tracking-wider rounded-sm px-1.5 py-0.5 font-mono text-brand-secondary bg-[color-mix(in_oklab,var(--color-brand-secondary)_15%,transparent)]"
          title="제휴 링크 — 구매 시 이 사이트에 수수료가 지급될 수 있습니다."
        >
          AD
        </span>
      ) : (
        <span className="text-xs text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          (제휴 링크 · 구매 시 커미션 지급)
        </span>
      )}
    </span>
  );
}
