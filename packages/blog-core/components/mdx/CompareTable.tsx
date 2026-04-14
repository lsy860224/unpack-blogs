import type { ReactNode } from "react";

export interface CompareTableColumn {
  key: string;
  label: string;
  /** "win" 값을 갖는 행은 Accent Green, "lose"는 Accent Red로 강조 */
  highlight?: boolean;
}

export interface CompareTableRow {
  label: string;
  values: Record<string, ReactNode>;
  /** 어느 컬럼이 win/lose인지 명시 (옵션) */
  verdict?: Record<string, "win" | "lose" | "tie" | undefined>;
}

export interface CompareTableProps {
  columns: CompareTableColumn[];
  rows: CompareTableRow[];
  caption?: string;
}

export function CompareTable({ columns, rows, caption }: CompareTableProps) {
  return (
    <div className="my-8 overflow-x-auto not-prose">
      {caption && (
        <p className="mb-2 text-xs uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
          {caption}
        </p>
      )}
      <table className="w-full border-collapse text-sm">
        <thead>
          <tr className="border-b-2 border-[var(--color-brand-primary)]">
            <th className="py-2 px-3 text-left text-xs font-semibold uppercase tracking-wider text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]">
              {" "}
            </th>
            {columns.map((c) => (
              <th
                key={c.key}
                className="py-2 px-3 text-left font-semibold text-[var(--color-brand-primary)]"
              >
                {c.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr
              key={row.label}
              className="border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)]"
            >
              <th
                scope="row"
                className="py-2 px-3 text-left text-xs font-semibold uppercase tracking-wider text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
              >
                {row.label}
              </th>
              {columns.map((c) => {
                const v = row.verdict?.[c.key];
                const color =
                  v === "win"
                    ? "var(--color-brand-accent-green)"
                    : v === "lose"
                    ? "var(--color-brand-accent-red)"
                    : undefined;
                return (
                  <td
                    key={c.key}
                    className="py-2 px-3 tabular-nums"
                    style={color ? { color, fontWeight: 600 } : undefined}
                  >
                    {row.values[c.key] ?? "—"}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
