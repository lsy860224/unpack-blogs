/**
 * Date utilities for post frontmatter.
 *
 * Supports two frontmatter `date` formats:
 *   - `"YYYY-MM-DD"` (legacy, assumed Asia/Seoul midnight)
 *   - `"YYYY-MM-DD HH:mm"` or ISO 8601 (preferred, with or without timezone)
 *
 * When no timezone is given, Asia/Seoul (+09:00) is assumed.
 */

const KST_OFFSET = "+09:00";

export function parsePostDate(input: string): Date {
  const trimmed = input.trim();
  // Pure date → KST midnight
  if (/^\d{4}-\d{2}-\d{2}$/.test(trimmed)) {
    return new Date(`${trimmed}T00:00:00${KST_OFFSET}`);
  }
  // Allow "YYYY-MM-DD HH:mm[:ss]" → convert space to T
  const iso = trimmed.includes("T") ? trimmed : trimmed.replace(" ", "T");
  const hasTz = /[+-]\d{2}:?\d{2}$|Z$/.test(iso);
  return new Date(hasTz ? iso : `${iso}${KST_OFFSET}`);
}

export function hasTimeComponent(input: string): boolean {
  return !/^\d{4}-\d{2}-\d{2}$/.test(input.trim());
}

export interface FormatPostDateOptions {
  /** Force time inclusion. Default: auto — show time only when the source has time. */
  includeTime?: boolean;
}

const PART_FORMATTER = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Seoul",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  hour12: false,
});

function formatParts(date: Date) {
  const parts = PART_FORMATTER.formatToParts(date);
  const get = (type: string) => parts.find((p) => p.type === type)?.value ?? "";
  return {
    year: get("year"),
    month: get("month"),
    day: get("day"),
    hour: get("hour"),
    minute: get("minute"),
  };
}

/**
 * Render a post date in `YYYY-MM-DD HH:mm` (KST) form.
 * If the source has no time component and `includeTime` is not forced,
 * returns just `YYYY-MM-DD`.
 */
export function formatPostDate(input: string, opts: FormatPostDateOptions = {}): string {
  const date = parsePostDate(input);
  const withTime = opts.includeTime ?? hasTimeComponent(input);
  const { year, month, day, hour, minute } = formatParts(date);
  const base = `${year}-${month}-${day}`;
  return withTime ? `${base} ${hour}:${minute}` : base;
}

/** Short `MM-DD HH:mm` form for compact UIs (e.g. timeline pins). */
export function formatPostDateShort(input: string, opts: FormatPostDateOptions = {}): string {
  const date = parsePostDate(input);
  const withTime = opts.includeTime ?? hasTimeComponent(input);
  const { month, day, hour, minute } = formatParts(date);
  const base = `${month}-${day}`;
  return withTime ? `${base} ${hour}:${minute}` : base;
}

/** ISO 8601 datetime for machine-readable attributes (`<time dateTime>`, JSON-LD). */
export function toIsoDatetime(input: string): string {
  return parsePostDate(input).toISOString();
}
