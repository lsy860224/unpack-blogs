export type Locale = "ko" | "en";

export const SUPPORTED_LOCALES: readonly Locale[] = ["ko", "en"] as const;
export const DEFAULT_LOCALE: Locale = "ko";

export interface BlogCoreMessages {
  readingTimeLabel: string;
  readingTimeUnit: string;
  tableOfContents: string;
  relatedPosts: string;
  comments: string;
}

const MESSAGES: Record<Locale, BlogCoreMessages> = {
  ko: {
    readingTimeLabel: "읽는 시간",
    readingTimeUnit: "분",
    tableOfContents: "목차",
    relatedPosts: "관련 글",
    comments: "댓글",
  },
  en: {
    readingTimeLabel: "Reading time",
    readingTimeUnit: "min",
    tableOfContents: "Table of Contents",
    relatedPosts: "Related Posts",
    comments: "Comments",
  },
};

export function getBlogCoreMessages(locale?: string): BlogCoreMessages {
  if (!locale) return MESSAGES[DEFAULT_LOCALE];
  const normalized = locale.toLowerCase().slice(0, 2) as Locale;
  return MESSAGES[normalized] ?? MESSAGES[DEFAULT_LOCALE];
}

export function toOgLocale(locale?: string): string {
  const normalized = (locale ?? DEFAULT_LOCALE).toLowerCase().slice(0, 2);
  if (normalized === "en") return "en_US";
  return "ko_KR";
}

export function toBcp47(locale?: string): string {
  const normalized = (locale ?? DEFAULT_LOCALE).toLowerCase().slice(0, 2);
  if (normalized === "en") return "en-US";
  return "ko-KR";
}
