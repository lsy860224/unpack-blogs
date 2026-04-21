import type { ReactNode } from "react";
import { cn } from "../../lib/cn";

export type CalloutType = "info" | "warning" | "success" | "error" | "note";

export interface CalloutProps {
  type?: CalloutType;
  title?: string;
  children: ReactNode;
  className?: string;
}

const STYLES: Record<CalloutType, { bar: string; bg: string; icon: string }> = {
  info: {
    bar: "var(--color-brand-primary)",
    bg: "color-mix(in oklab, var(--color-brand-primary) 8%, transparent)",
    icon: "i",
  },
  note: {
    bar: "color-mix(in oklab, var(--foreground) 50%, transparent)",
    bg: "color-mix(in oklab, var(--foreground) 5%, transparent)",
    icon: "•",
  },
  warning: {
    bar: "var(--color-brand-secondary)",
    bg: "color-mix(in oklab, var(--color-brand-secondary) 12%, transparent)",
    icon: "!",
  },
  success: {
    bar: "var(--color-brand-accent-green)",
    bg: "color-mix(in oklab, var(--color-brand-accent-green) 12%, transparent)",
    icon: "✓",
  },
  error: {
    bar: "var(--color-brand-accent-red)",
    bg: "color-mix(in oklab, var(--color-brand-accent-red) 12%, transparent)",
    icon: "✗",
  },
};

export function Callout({
  type = "info",
  title,
  children,
  className,
}: CalloutProps) {
  const s = STYLES[type];
  return (
    <aside
      className={cn(
        "my-6 flex gap-3 rounded-md border-l-4 px-4 py-3 not-prose",
        className,
      )}
      style={{ borderColor: s.bar, background: s.bg }}
    >
      <span
        aria-hidden
        className="font-bold tabular-nums"
        style={{ color: s.bar, fontFamily: "var(--font-mono)" }}
      >
        {s.icon}
      </span>
      <div className="flex-1">
        {title && <p className="font-semibold mb-1">{title}</p>}
        <div className="text-sm leading-relaxed text-[color-mix(in_oklab,var(--foreground)_85%,transparent)]">
          {children}
        </div>
      </div>
    </aside>
  );
}
