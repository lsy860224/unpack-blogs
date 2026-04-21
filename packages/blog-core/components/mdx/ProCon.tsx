import type { ReactNode } from "react";
import { cn } from "../../lib/cn";

export interface ProConProps {
  /** children API (MDX 권장): <Pros>...</Pros><Cons>...</Cons>를 자식으로 */
  children?: ReactNode;
  /** Array API (.tsx 코드에서 사용) */
  pros?: string[];
  cons?: string[];
  proTitle?: string;
  conTitle?: string;
  className?: string;
}

/**
 * 장점 · 단점 대비 블록.
 *
 * MDX 사용 예 (권장 — array prop은 next-mdx-remote/rsc에서 전달되지 않음):
 *   <ProCon>
 *     <Pros>
 *       - 1:1 비교로 결정 시간 절약
 *       - 가성비 판단이 명확
 *     </Pros>
 *     <Cons>
 *       - 테스트 시간 N배
 *       - 공정한 동일 환경 필요
 *     </Cons>
 *   </ProCon>
 *
 * .tsx 사용 예:
 *   <ProCon pros={["a","b"]} cons={["c","d"]} />
 */
export function ProCon({
  children,
  pros,
  cons,
  proTitle = "장점",
  conTitle = "단점",
  className,
}: ProConProps) {
  const rootClass = cn("my-6 grid gap-3 sm:grid-cols-2 not-prose", className);
  if (children) {
    return <div className={rootClass}>{children}</div>;
  }
  const safePros = pros ?? [];
  const safeCons = cons ?? [];

  return (
    <div className={rootClass}>
      <Pros title={proTitle}>
        <ul className="space-y-1 text-sm leading-relaxed">
          {safePros.map((item, i) => (
            <li key={i} className="flex gap-2">
              <span
                aria-hidden
                style={{ color: "var(--color-brand-accent-green)" }}
              >
                ·
              </span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </Pros>
      <Cons title={conTitle}>
        <ul className="space-y-1 text-sm leading-relaxed">
          {safeCons.map((item, i) => (
            <li key={i} className="flex gap-2">
              <span
                aria-hidden
                style={{ color: "var(--color-brand-accent-red)" }}
              >
                ·
              </span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </Cons>
    </div>
  );
}

export interface ProsConsWrapperProps {
  title?: string;
  children?: ReactNode;
}

export function Pros({ title = "장점", children }: ProsConsWrapperProps) {
  return (
    <div
      className="rounded-md border-l-4 px-4 py-3"
      style={{
        borderColor: "var(--color-brand-accent-green)",
        background:
          "color-mix(in oklab, var(--color-brand-accent-green) 8%, transparent)",
      }}
    >
      <p
        className="mb-2 text-xs font-bold uppercase tracking-wider"
        style={{
          color: "var(--color-brand-accent-green)",
          fontFamily: "var(--font-mono)",
        }}
      >
        ✓ {title}
      </p>
      <div className="text-sm leading-relaxed [&_ul]:space-y-1 [&_ul]:pl-4 [&_li]:list-disc">
        {children}
      </div>
    </div>
  );
}

export function Cons({ title = "단점", children }: ProsConsWrapperProps) {
  return (
    <div
      className="rounded-md border-l-4 px-4 py-3"
      style={{
        borderColor: "var(--color-brand-accent-red)",
        background:
          "color-mix(in oklab, var(--color-brand-accent-red) 8%, transparent)",
      }}
    >
      <p
        className="mb-2 text-xs font-bold uppercase tracking-wider"
        style={{
          color: "var(--color-brand-accent-red)",
          fontFamily: "var(--font-mono)",
        }}
      >
        ✗ {title}
      </p>
      <div className="text-sm leading-relaxed [&_ul]:space-y-1 [&_ul]:pl-4 [&_li]:list-disc">
        {children}
      </div>
    </div>
  );
}
